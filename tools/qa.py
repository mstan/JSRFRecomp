"""Private JSRF gameplay QA controls; independent of the base recompile.

Teleport and mission handover bypass prerequisites and never certify completion.
Only the private process/state identified by --run can be modified.
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
        def objects(self):
            values={self.facts['camera_vtable']:'camera',**{v:'flow' for v in self.facts.get('flow_vtables',[self.facts['flow_vtable']])}}
            found=self.find_values(values)
            cameras=[];flows=[]
            for at in found['camera']:
                try:
                    player=self.u32(at+self.facts['camera_target']);mode=self.u32(at+self.facts['camera_mode'])
                    if not self.valid(player,0x1000) or mode>20:continue
                    position=struct.unpack('<3f',self.read(player+self.facts['player_position'],12))
                    if all(math.isfinite(x) and abs(x)<1000000 for x in position):cameras.append({'object':at,'player':player,'mode':mode,'position':position})
                except OSError:pass
            for at in found['flow']:
                try:
                    mission=self.u32(at+self.facts['flow_mission']);state=self.u32(at+self.facts['flow_state'])
                    if state<119 and mission>>16<100:flows.append({'object':at,'mission':mission,'state':state})
                except OSError:pass
            return {'pid':self.pid,'camera':cameras,'flow':flows,'raw_flow_candidates':found['flow']}
        def teleport(self,camera,position):
            if len(position)!=3 or not all(math.isfinite(x) and abs(x)<1000000 for x in position):raise ValueError('teleport coordinates')
            with self.frozen():
                if self.u32(camera['object'])!=self.facts['camera_vtable'] or self.u32(camera['object']+self.facts['camera_target'])!=camera['player']:raise ValueError('camera owner changed')
                at=camera['player']+self.facts['player_position']
                old=struct.unpack('<3f',self.read(at,12));self.write(at,struct.pack('<3f',*position))
            self.record({'operation':'teleport','player':camera['player'],'before':old,'after':position,'bypass':True})
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
            self.record({'operation':'mission-handover','before':old,'requested':mission,'bypass':True,'completion_claimed':False,'event_completion_bypassed':state==19})
    return TitleQa(run,facts,write)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run',type=Path,required=True)
    parser.add_argument('--development-framework',type=Path)
    commands=parser.add_subparsers(dest='command',required=True)
    commands.add_parser('status')
    teleport=commands.add_parser('teleport');teleport.add_argument('position',nargs=3,type=float)
    mission=commands.add_parser('mission');mission.add_argument('id',type=lambda s:int(s,0));mission.add_argument('--cancel-event',action='store_true')
    args=parser.parse_args();p=open_qa(args.run,args.development_framework,args.command!='status')
    try:
        state=p.objects()
        if args.command=='teleport':
            if len(state['camera'])!=1:raise ValueError('ambiguous camera owner')
            p.teleport(state['camera'][0],args.position)
        elif args.command=='mission':
            active=[f for f in state['flow'] if f['state'] in ((15,19) if args.cancel_event else (15,))]
            if len(active)!=1:raise ValueError('ambiguous active flow')
            p.mission(active[0],args.id,args.cancel_event)
        print(json.dumps(state,indent=2))
    finally:p.close()
    return 0

if __name__=='__main__':raise SystemExit(main())
