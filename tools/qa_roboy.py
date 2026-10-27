"""Reach Roboy from a copied endgame save using original controller menus.

Private USA standalone QA only. Position-only travel to Roboy bypasses walking;
it does not open a menu, set a result, or modify persistent owner progress.
Every checkpoint keeps a screenshot and the native input recorder remains on.
Use --from-checkpoint to resume steering instead of replaying a failed prefix.
"""
import argparse,base64,json,sys,time
from pathlib import Path
from qa import open_qa


def navigate(run,port,start='title',slot=2):
    root=Path(__file__).resolve().parents[1]
    sys.path.insert(0,str(root/'xboxllr/tools'))
    from native_debug import request,gamepad,save_png
    deadline=time.monotonic()+45
    while True:
        try:
            if request(port,'status',timeout=2)['frames']>1:break
        except (OSError,ValueError):pass
        if time.monotonic()>=deadline:raise TimeoutError('Native debug renderer did not become ready')
        time.sleep(.5)
    q=open_qa(run,revision='usa-standalone',write=True)
    out=Path(run)/'roboy-route';out.mkdir(exist_ok=True)
    stages=['title','load','character','garage','roboy','graffiti']
    def press(button='',ms=120,wait=.35,**axes):
        request(port,'set_input '+gamepad(button,**axes).hex()+' '+str(ms))
        time.sleep(ms/1000+wait)
    def checkpoint(name):
        shot=save_png(request(port,'screenshot'),out/(name+'.png'))
        q.record(dict(operation='roboy-route-checkpoint',checkpoint=name,screenshot=str(out/(name+'.png')),frame=shot.get('frame')))
        print(name,flush=True)
    def wait_for(getter,seconds):
        until=time.monotonic()+seconds
        while time.monotonic()<until:
            q.ensure_alive();result=getter()
            if result:return result
            time.sleep(.5)
        checkpoint('timeout');raise TimeoutError('Route checkpoint not reached; observe timeout.png and resume steering')
    def orange_menu():
        try:shot=request(port,'screenshot')
        except ValueError as error:
            if str(error)=='no presented frame within 3 seconds':return False
            raise
        rgba=base64.b64decode(shot['data'],validate=True)
        width,height=shot['width'],shot['height']
        samples=[rgba[(y*width+x)*4:(y*width+x)*4+3]
                 for y in range(height//10,height//3,max(1,height//40))
                 for x in range(width//4,3*width//4,max(1,width//40))]
        return sum(p[0]>150 and p[1]>80 and p[2]<50 for p in samples)>len(samples)*.65
    def size_menu():
        # The camera still eases after the scene first presents. Wait for the
        # original Back prompt and selected green SS control before steering.
        try:shot=request(port,'screenshot')
        except ValueError as error:
            if str(error)=='no presented frame within 3 seconds':return False
            raise
        rgba=base64.b64decode(shot['data'],validate=True);width,height=shot['width'],shot['height']
        def count(box,predicate):
            x0,y0,x1,y1=box;hits=0
            for y in range(int(y0*height),int(y1*height),max(1,height//180)):
                for x in range(int(x0*width),int(x1*width),max(1,width//320)):
                    hits+=bool(predicate(*rgba[(y*width+x)*4:(y*width+x)*4+3]))
            return hits
        return (count((.075,.86,.12,.93),lambda r,g,b:g>110 and g>r*1.3 and g>b*1.2)>8 and
                count((.10,.34,.15,.43),lambda r,g,b:r>100 and r>g*2 and r>b*2)>5)
    def finish_roboy_dialogue():
        if orange_menu():return True
        press('a',wait=1)
        return False
    try:
        if stages.index(start)<=0:
            # Source-bound title state table: 3=Start prompt, 4=main menu,
            # 6=attract. One Start leaves attract; the next opens the menu.
            if q.facts['xbe_sha256']!='fd19055756719893c466302809b433b785ecf5732df0441286f3f605f0f3ef9c':
                raise ValueError('Title menu layout requires the qualified USA image')
            title=wait_for(lambda:next(iter(q.find_values({0x1ccef8:'title'})['title']),0),45)
            for _ in range(8):
                phase=q.u32(title+0x44)
                if phase==4:break
                press('start',wait=.7)
            if q.u32(title+0x44)!=4:raise ValueError('Main menu did not open; observe and resume')
            for _ in range(3):
                selected=q.u32(title+0x54)
                if selected==1:break
                press(ly=-32767 if selected==0 else 32767)
            if q.u32(title+0x54)!=1:raise ValueError('Load Game was not selected')
            checkpoint('title-load-selected');press('a',wait=4)
        if stages.index(start)<=1:
            checkpoint('load-slots')
            for _ in range(slot-1):press(ly=-32767)
            press('a',wait=.6);press(lx=-32767);press('a',wait=12)
            checkpoint('character-select')
        if stages.index(start)<=2:
            def select_character():
                cameras=q.objects()['camera']
                ready=next((c for c in cameras if c['mode']==3),None)
                if not ready:press('a',wait=1)
                return ready
            wait_for(select_character,45)
            checkpoint('garage-loaded')
        if stages.index(start)<=3:
            camera=wait_for(lambda:next((c for c in q.objects()['camera'] if c['mode']==3),None),20)
            # mssn0900.bin character19 transform translation is
            # (58.912605,34.495224,182.638138); approach from the platform.
            q.teleport(camera,(69,34.5,183))
            press('rt',ms=200,wait=1)
            wait_for(finish_roboy_dialogue,25)
            checkpoint('roboy-garage-menu')
        if stages.index(start)<=4:
            wait_for(finish_roboy_dialogue,25)
            # Roboy Garage: System, Character, Practice, Graffiti, Music,
            # Test Run. D-pad is the original menu input here.
            for _ in range(3):press('right')
            press('a',wait=3);wait_for(orange_menu,20);checkpoint('graffiti-options')
        if stages.index(start)<=5:
            press('a',wait=2);wait_for(size_menu,30);checkpoint('graffiti-size-preview')
        request(port,'clear_input')
        return dict(checkpoint='graffiti-size-preview',position_travel_bypassed=True,menu_pass_claimed=False)
    finally:
        try:request(port,'clear_input')
        finally:q.close()


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run',type=Path,required=True)
    parser.add_argument('--port',type=int,required=True)
    parser.add_argument('--slot',type=int,choices=[1,2,3],default=2)
    parser.add_argument('--from-checkpoint',choices=['title','load','character','garage','roboy','graffiti'],default='title')
    args=parser.parse_args()
    print(json.dumps(navigate(args.run,args.port,args.from_checkpoint,args.slot)))
