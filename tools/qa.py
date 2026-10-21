"""Private JSRF gameplay QA controls; independent of the base recompile.

Teleport and mission handover bypass prerequisites and never certify completion.
Only the private process/state identified by --run can be modified.
Handovers leave persistent story progression unchanged; save/reload and mission
chain checks require a consistent chapter/area setup in addition to scene entry.
"""
from pathlib import Path
import argparse,json,math,struct,sys


def open_qa(run,framework=None,write=False):
    root=Path(__file__).resolve().parents[1]
    framework=Path(framework) if framework else root/'xboxllr'
    sys.path.insert(0,str(framework/'tools'))
    from native_qa_memory import NativeQaMemory
    facts=json.loads((root/'config/revisions/ntsc-u/gameplay-qa.json').read_text())
    class TitleQa(NativeQaMemory):
        def enemy_groups(self):
            """Inspect live encounter groups; definitions alone do not prove spawns."""
            layout=self.facts['enemy_groups'];manager=self.u32(layout['manager']);result=[]
            if not self.valid(manager,4+layout['buckets']*4):return result
            seen=set()
            for kind in range(layout['buckets']):
                node=self.u32(manager+4+kind*4)
                while node:
                    if node in seen or len(seen)>=1024 or not self.valid(node,8):raise ValueError('unstable enemy registry')
                    seen.add(node);at=self.u32(node)
                    if not self.valid(at,layout['flags']+4) or self.u32(at)!=layout['vtable'] or self.u32(at+layout['kind'])!=kind:
                        raise ValueError('unqualified enemy group owner')
                    remaining=self.u32(at+layout['remaining'])
                    if remaining>10000:raise ValueError('unqualified enemy group count')
                    result.append({'object':at,'type':kind,'remaining':remaining,'flags':self.u32(at+layout['flags'])})
                    node=self.u32(node+4)
            return result
        def force_encounter_end(self):
            """Cheat the original defeated predicate; never a combat correctness pass."""
            changed=[];layout=self.facts['enemy_groups']
            with self.frozen():
                for group in self.enemy_groups():
                    if group['remaining'] and not group['flags']&layout['defeated_mask']:
                        self.write(group['object']+layout['flags'],struct.pack('<I',group['flags']|layout['defeated_mask']))
                        changed.append(group)
            self.record({'operation':'force-encounter-end','groups':changed,'bypass':True,
                'original_defeat_condition_bypassed':True,'combat_pass_claimed':False})
            return changed
        def tags(self):
            """Read original per-piece reference positions, not completion overrides."""
            layout=self.facts['graffiti'];result=[];seen=set()
            for bucket,at in enumerate(struct.unpack('<256I',self.read(layout['registry'],1024))):
                while at:
                    if at in seen or len(seen)>=1024:raise ValueError('unstable graffiti registry')
                    seen.add(at);id=self.u32(at+layout['id']);parts=self.u32(at+layout['parts'])
                    if id&255!=bucket or parts not in (1,3,6,10):raise ValueError('unqualified graffiti layout')
                    base=self.u32(at+layout['piece_array']);stride=layout['piece_stride']
                    if not self.valid(base,parts*stride):raise ValueError('invalid graffiti piece extent')
                    positions=[];centers=[]
                    for i in range(parts):
                        piece=self.read(base+i*stride,stride)
                        positions.append(struct.unpack_from('<3f',piece,layout['piece_position']))
                        points=[struct.unpack_from('<3f',piece,j*12) for j in range(6)]
                        normals=[struct.unpack_from('<3f',piece,layout['region_normals']+j*12) for j in range(6)]
                        if not all(math.isfinite(v) and abs(v)<1000000 for point in points+normals for v in point):raise ValueError('invalid graffiti region')
                        center=tuple(sum(point[axis] for point in points)/6 for axis in range(3))
                        inside=all(sum((center[axis]-point[axis])*normal[axis] for axis in range(3))<=.01 for point,normal in zip(points,normals))
                        centers.append(center if inside else None)
                    if not all(math.isfinite(v) and abs(v)<1000000 for point in positions for v in point):raise ValueError('invalid graffiti reference position')
                    result.append({'object':at,'id':id,'parts':parts,
                        'unpainted':self.u32(at+layout['unpainted']),
                        'designs':self.u32(at+layout['designs']),
                        'back_designs':self.u32(at+layout['back_designs']),
                        'piece_positions':positions,'piece_region_centers':centers})
                    at=self.u32(at+layout['next'])
            return sorted(result,key=lambda tag:tag['id'])
        def objects(self):
            values={self.facts['camera_vtable']:'camera',**{v:'flow' for v in self.facts.get('flow_vtables',[self.facts['flow_vtable']])}}
            found=self.find_values(values)
            cameras=[];flows=[]
            for at in found['camera']:
                try:
                    player=self.u32(at+self.facts['camera_target']);mode=self.u32(at+self.facts['camera_mode'])
                    if not self.valid(player,0x1000) or mode>20:continue
                    position=struct.unpack('<3f',self.read(player+self.facts['player_position'],12))
                    if all(math.isfinite(x) and abs(x)<1000000 for x in position):
                        cameras.append({'object':at,'player':player,'mode':mode,'position':position,
                            'health':self.u32(player+self.facts['player_health']),
                            'health_capacity':self.u32(player+self.facts['player_health_capacity']),
                            'spray_cans':self.u32(player+self.facts['player_spray_cans']),
                            'spray_capacity':self.u32(player+self.facts['player_spray_capacity'])})
                except OSError:pass
            for at in found['flow']:
                try:
                    mission=self.u32(at+self.facts['flow_mission']);state=self.u32(at+self.facts['flow_state'])
                    if state<119 and mission>>16<100:flows.append({'object':at,'mission':mission,'state':state})
                except OSError:pass
            return {'pid':self.pid,'camera':cameras,'flow':flows,'raw_flow_candidates':found['flow']}
        def teleport(self,camera,position,sweep=False):
            if len(position)!=3 or not all(math.isfinite(x) and abs(x)<1000000 for x in position):raise ValueError('teleport coordinates')
            with self.frozen():
                if self.u32(camera['object'])!=self.facts['camera_vtable'] or self.u32(camera['object']+self.facts['camera_target'])!=camera['player']:raise ValueError('camera owner changed')
                at=camera['player']+self.facts['player_position']
                old=struct.unpack('<3f',self.read(at,12));data=struct.pack('<3f',*position)
                if not sweep:
                    if self.facts['player_previous_position']!=self.facts['player_position']+12:raise ValueError('requires adjacent original motion samples')
                    data+=data
                self.write(at,data)
            self.record({'operation':'teleport','player':camera['player'],'before':old,'after':position,
                'motion_history_synchronized':not sweep,'bypass':True})
        def mission(self,flow,mission,allow_event=False):
            if mission<0 or mission>>16>99 or mission&0xffff>999:raise ValueError('mission range')
            with self.frozen():
                at=flow['object']
                state=self.u32(at+self.facts['flow_state'])
                if self.u32(at)!=self.facts['flow_vtable'] or state not in ((15,19) if allow_event else (15,)):raise ValueError('requires stable original gameplay flow or explicit event cancellation')
                start=self.facts['flow_next_chapter'];end=self.facts['flow_state']+4
                old=self.u32(at+self.facts['flow_mission']);block=bytearray(self.read(at+start,end-start))
                struct.pack_into('<I',block,0,mission>>16)
                struct.pack_into('<I',block,self.facts['flow_next_number']-start,mission&0xffff)
                struct.pack_into('<I',block,self.facts['flow_state']-start,self.facts['handover_state'])
                self.write(at+start,bytes(block))
            self.record({'operation':'mission-handover','before':old,'requested':mission,'bypass':True,'completion_claimed':False,'event_completion_bypassed':state==19,'persistent_story_updated':False,'save_context_consistency_claimed':False})
        def cans(self,camera,count):
            if type(count) is not int or count<0:raise ValueError('can count must be a nonnegative integer')
            with self.frozen():
                owner=camera['object'];player=camera['player']
                if self.u32(owner)!=self.facts['camera_vtable'] or self.u32(owner+self.facts['camera_target'])!=player:
                    raise ValueError('camera owner changed')
                if self.u32(owner+self.facts['camera_mode']) not in self.facts.get('resource_camera_modes',[3,5]):raise ValueError('requires a supported live-player camera')
                capacity=self.u32(player+self.facts['player_spray_capacity'])
                at=player+self.facts['player_spray_cans'];before=self.u32(at)
                if not 0<capacity<=999 or before>capacity or count>capacity:raise ValueError('can count exceeds current original capacity')
                self.write(at,struct.pack('<I',count))
            self.record({'operation':'spray-can-refill','player':player,'before':before,'after':count,
                'capacity':capacity,'bypass':True,'pickup_claimed':False,'completion_claimed':False})
        def health(self,camera,count):
            if type(count) is not int or count<1:raise ValueError('health must be a positive integer')
            with self.frozen():
                owner=camera['object'];player=camera['player']
                if self.u32(owner)!=self.facts['camera_vtable'] or self.u32(owner+self.facts['camera_target'])!=player:
                    raise ValueError('camera owner changed')
                if self.u32(owner+self.facts['camera_mode']) not in self.facts.get('resource_camera_modes',[3,5]):raise ValueError('requires a supported live-player camera')
                capacity=self.u32(player+self.facts['player_health_capacity'])
                at=player+self.facts['player_health'];before=self.u32(at)
                if not 0<capacity<=999 or before>capacity or count>capacity:raise ValueError('health exceeds current original capacity')
                self.write(at,struct.pack('<I',count))
            self.record({'operation':'health-refill','player':player,'before':before,'after':count,
                'capacity':capacity,'bypass':True,'damage_or_pickup_claimed':False,'completion_claimed':False})
    return TitleQa(run,facts,write)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run',type=Path,required=True)
    parser.add_argument('--development-framework',type=Path)
    commands=parser.add_subparsers(dest='command',required=True)
    commands.add_parser('status')
    commands.add_parser('tags',help='Read original per-piece graffiti positions and paint state')
    commands.add_parser('enemy-groups',help='Read currently registered encounter groups')
    commands.add_parser('force-encounter-end',help='Cheat the defeated condition to reach the original end sequence; does not pass combat')
    teleport=commands.add_parser('teleport');teleport.add_argument('position',nargs=3,type=float)
    teleport.add_argument('--sweep',action='store_true',help='Retain the previous motion sample for intentional crossing checks')
    mission=commands.add_parser('mission');mission.add_argument('id',type=lambda s:int(s,0));mission.add_argument('--cancel-event',action='store_true')
    cans=commands.add_parser('cans');cans.add_argument('count',type=int)
    health=commands.add_parser('health');health.add_argument('count',type=int)
    args=parser.parse_args();p=open_qa(args.run,args.development_framework,args.command not in ('status','tags','enemy-groups'))
    try:
        if args.command in ('enemy-groups','force-encounter-end'):
            print(json.dumps(p.enemy_groups() if args.command=='enemy-groups' else p.force_encounter_end(),indent=2))
            return 0
        if args.command=='tags':
            print(json.dumps(p.tags(),indent=2))
            return 0
        state=p.objects()
        if args.command=='teleport':
            if len(state['camera'])!=1:raise ValueError('ambiguous camera owner')
            p.teleport(state['camera'][0],args.position,args.sweep)
        elif args.command=='mission':
            active=[f for f in state['flow'] if f['state'] in ((15,19) if args.cancel_event else (15,))]
            if len(active)!=1:raise ValueError('ambiguous active flow')
            p.mission(active[0],args.id,args.cancel_event)
        elif args.command=='cans':
            if len(state['camera'])!=1:raise ValueError('ambiguous camera owner')
            p.cans(state['camera'][0],args.count)
        elif args.command=='health':
            if len(state['camera'])!=1:raise ValueError('ambiguous camera owner')
            p.health(state['camera'][0],args.count)
        print(json.dumps(p.objects() if args.command!='status' else state,indent=2))
    finally:p.close()
    return 0

if __name__=='__main__':raise SystemExit(main())
