"""Inventory owned mission content for QA; emits metadata, never game bytes.

The original flow reads four command arrays at mission+0x174 through +0x18c,
with adjacent counts and 0x54-byte command records. On disc the
relocated runtime pointers are file offsets. Scene keys are grouped facts;
they are not automatically names or proof that an area works.
"""
from pathlib import Path
import argparse,collections,hashlib,json,struct


def enemy_sets(data,label):
    """Block3 defines enemies; block5 groups definition indices for A2/A4/D.

    Placement records are source data, not a count of live spawned actors.
    Keep that distinction visible when planning combat coverage.
    """
    def extent(at,count,stride):
        if count>10000 or (count and (at<0x19c or at+count*stride>len(data))):
            raise ValueError('invalid enemy extent: '+label)
    at,count=struct.unpack_from('<2I',data,0x34+3*8);extent(at,count,20)
    definitions=[]
    for index in range(count):
        kind,_,_,placements,_=struct.unpack_from('<5I',data,at+index*20)
        definitions.append({'index':index,'type':kind,'placement_records':placements})
    at,count=struct.unpack_from('<2I',data,0x34+5*8);extent(at,count,8)
    groups=[]
    for index in range(count):
        members,size=struct.unpack_from('<2I',data,at+index*8);extent(members,size,4)
        indices=list(struct.unpack_from('<'+str(size)+'I',data,members)) if size else []
        if any(i>=len(definitions) for i in indices):
            raise ValueError('invalid enemy definition index: '+label)
        groups.append({'index':index,'definitions':indices})
    return definitions,groups


def inventory(media):
    folder=Path(media)/'Media'/'Mission'
    rows=[]
    for path in sorted(folder.glob('mssn[0-9][0-9][0-9][0-9].bin')):
        data=path.read_bytes();partner=path.with_suffix('.dat')
        if len(data)<0x19c or not partner.is_file():raise ValueError('incomplete mission pair: '+path.name)
        digits=path.stem[4:];chapter,number=int(digits[:2]),int(digits[2:])
        # Filename formatting aliases numbers modulo 100. In particular,
        # mssn0196 is reached as 0x100c4 (196), not the naive number 96.
        # Retain candidates as candidates until original flow proves the ID.
        row={'file':path.stem,'filename_id_candidate':(chapter<<16)|number,
             'scene_key':struct.unpack_from('<I',data)[0],
             'bin_sha256':hashlib.sha256(data).hexdigest(),
             'dat_sha256':hashlib.sha256(partner.read_bytes()).hexdigest()}
        definitions,groups=enemy_sets(data,path.name)
        row['enemy_definitions']=definitions;row['enemy_group_sets']=groups
        for name,offset in [('setup',0x174),('triggers',0x17c),
                            ('nonblocking',0x184),('blocking',0x18c)]:
            at,count=struct.unpack_from('<2I',data,offset)
            if count>10000 or (count and (at<0x19c or at+count*0x54>len(data))):
                raise ValueError('invalid command extent: '+path.name+' '+name)
            ops=collections.Counter(struct.unpack_from('<I',data,at+i*0x54+0x10)[0] for i in range(count))
            row[name]={'count':count,'operations':dict(sorted(ops.items()))}
        rows.append(row)
    if not rows:raise ValueError('no mission content found')
    groups=collections.defaultdict(list)
    for row in rows:groups[row['scene_key']].append(row['file'])
    return {'schema':'jsrf.qa-content-inventory.v2','scope':'content metadata; behavior, spawn counts and area names unverified',
            'mission_pairs':len(rows),'scene_keys':len(groups),
            'groups':[{'scene_key':key,'files':files} for key,files in sorted(groups.items())],
            'missions':rows}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--media-root',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.resolve().drive.upper()=='C:':raise ValueError('keep generated QA output off C:')
    result=inventory(args.media_root)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('schema','mission_pairs','scene_keys')}))
    return 0


if __name__=='__main__':raise SystemExit(main())
