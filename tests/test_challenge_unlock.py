"""Menu-only mod checks, optionally against the user's original x86 routine."""
from pathlib import Path
import ctypes,hashlib,json,os,struct,unittest

ROOT=Path(__file__).resolve().parents[1]
FACTS=json.loads((ROOT/'config/revisions'/os.environ.get('JSRF_TEST_REVISION','ntsc-u')/'challenge-unlock.json').read_text())
OWNER,MAIN,MODES,SOURCE=0x400000,0x401000,0x402000,0x408000
LISTS=(0x403000,0x404000,0x405000,0x406000)
COUNTS=(13,13,6,7)
SPANS=[(MAIN+0x58,4),(MODES,64),*((p,n*16) for p,n in zip(LISTS,COUNTS))]
def put(ram,at,*values):struct.pack_into('<'+'I'*len(values),ram,at,*values)
def views(ram):return [bytes(ram[at:at+n]) for at,n in SPANS]


@unittest.skipUnless(os.environ.get('JSRF_CHALLENGE_FIXTURE'),'Build the portable native mod fixture first')
class ChallengeUnlockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.library=ctypes.CDLL(os.environ['JSRF_CHALLENGE_FIXTURE'])
        cls.library.jsrf_challenge_fixture.argtypes=[ctypes.c_void_p,ctypes.c_uint,ctypes.c_uint,ctypes.c_uint]
        cls.library.jsrf_challenge_error.restype=ctypes.c_char_p

    def seed(self,original=None):
        ram=bytearray(0x410000)
        if original:
            base=struct.unpack_from('<I',original,0x104)[0]
            table=struct.unpack_from('<I',original,0x120)[0]-base
            for i in range(struct.unpack_from('<I',original,0x11c)[0]):
                flags,va,virtual,offset,size=struct.unpack_from('<5I',original,table+i*56)
                ram[va:va+size]=original[offset:offset+size]
        else:
            put(ram,FACTS['area_ids'],*(0x10000+i for i in range(14)))
            put(ram,FACTS['zone_map'],*range(100))
            zones=[10+i%10 for i in range(256)]
            put(ram,FACTS['soul_zones'],*zones)
        put(ram,FACTS['actor_manager'],0x300000)
        put(ram,0x300000+0x98+FACTS['menu_actor_id']*4,OWNER)
        put(ram,OWNER,FACTS['menu_vtable'])
        put(ram,OWNER+0xb4,MAIN);put(ram,OWNER+0xcc,MODES);put(ram,OWNER+0xf8,SOURCE)
        for at,pointer in zip(FACTS['menu_list_pointers'],LISTS):put(ram,OWNER+at,pointer)
        for mode,(offset,count) in enumerate(zip(FACTS['source_list_offsets'],COUNTS)):
            for row in range(count):put(ram,SOURCE+offset+row*16,(row+mode)%14,100+row,200+row)
        put(ram,FACTS['chapter'],3)
        put(ram,FACTS['collected_souls'],*([0]*8))
        return ram

    def apply(self,ram,enabled=1,reset=1):
        view=(ctypes.c_ubyte*len(ram)).from_buffer(ram)
        result=self.library.jsrf_challenge_fixture(view,len(ram),enabled,reset)
        if result<0:raise ValueError(self.library.jsrf_challenge_error().decode())
        return result

    def test_default_on_contract_preserves_soul_and_story_bytes(self):
        ram=self.seed();before=bytes(ram)
        self.assertEqual(self.apply(ram),6)
        self.assertEqual(struct.unpack_from('<I',ram,MAIN+0x58)[0],0)
        for at,size in SPANS:ram[at:at+size]=before[at:at+size]
        self.assertEqual(bytes(ram),before)

    def test_missing_one_soul_stays_locked_and_completed_area_unlocks(self):
        ram=self.seed()
        words=[0xffffffff]*8
        put(ram,FACTS['collected_souls'],*words)
        self.apply(ram)
        self.assertEqual(struct.unpack_from('<I',ram,MAIN+0x58)[0],1)
        self.assertEqual(struct.unpack_from('<I',ram,LISTS[0]+8)[0],1)
        words[0]&=~1;put(ram,FACTS['collected_souls'],*words)
        self.apply(ram,reset=0)
        self.assertEqual(struct.unpack_from('<I',ram,LISTS[0]+8)[0],0)
        self.assertEqual(struct.unpack_from('<I',ram,LISTS[0]+16+8)[0],1)

    def test_disabled_and_original_postgame_are_untouched(self):
        ram=self.seed();before=bytes(ram)
        self.assertEqual(self.apply(ram,enabled=0),0);self.assertEqual(bytes(ram),before)
        put(ram,FACTS['chapter'],9);before=bytes(ram)
        self.assertEqual(self.apply(ram),0);self.assertEqual(bytes(ram),before)

    def test_cached_menu_and_recreated_menu(self):
        ram=self.seed();put(ram,FACTS['collected_souls'],*([0xffffffff]*8))
        self.assertEqual(self.apply(ram),6);self.assertEqual(self.apply(ram,reset=0),0)
        put(ram,MAIN+0x58,0)
        self.assertEqual(self.apply(ram,reset=0),6)

    def test_rejects_aliased_destination_before_any_write(self):
        ram=self.seed();put(ram,OWNER+0xd4,OWNER)
        before=bytes(ram)
        with self.assertRaisesRegex(ValueError,'aliased'):self.apply(ram)
        self.assertEqual(bytes(ram),before)

    @unittest.skipUnless(os.environ.get('JSRF_ORIGINAL_XBE'),'Original image is private')
    def test_original_postgame_x86_matches_mod_before_story_completion(self):
        from unicorn import Uc,UC_ARCH_X86,UC_MODE_32
        from unicorn.x86_const import UC_X86_REG_ESP,UC_X86_REG_ECX,UC_X86_REG_EIP
        original=Path(os.environ['JSRF_ORIGINAL_XBE']).read_bytes()
        self.assertEqual(hashlib.sha256(original).hexdigest(),FACTS['xbe_sha256'])
        base=struct.unpack_from('<I',original,0x104)[0]
        table=struct.unpack_from('<I',original,0x120)[0]-base
        for proof in FACTS['functions']+FACTS['tables']:
            for i in range(struct.unpack_from('<I',original,0x11c)[0]):
                _,va,_,offset,size=struct.unpack_from('<5I',original,table+i*56)
                if va<=proof['address']<va+size:
                    start=offset+proof['address']-va
                    self.assertEqual(hashlib.sha256(original[start:start+proof['bytes']]).hexdigest(),proof['sha256']);break
            else:self.fail('Original proof outside source image')
        for label,words in [('none',[0]*8),('one_missing',[0xfffffffe]+[0xffffffff]*7),
                            ('alternating',[0x55555555]*8),('all',[0xffffffff]*8)]:
            with self.subTest(label=label):
                ram=self.seed(original);put(ram,FACTS['collected_souls'],*words)
                reference=bytearray(ram);put(reference,FACTS['chapter'],9)
                uc=Uc(UC_ARCH_X86,UC_MODE_32);uc.mem_map(0,0x800000);uc.mem_write(0,bytes(reference))
                uc.mem_write(0x700000,struct.pack('<I',0x700100))
                uc.reg_write(UC_X86_REG_ESP,0x700000);uc.reg_write(UC_X86_REG_ECX,OWNER)
                uc.emu_start(0x756e0,0x700100,count=200000)
                self.assertEqual(uc.reg_read(UC_X86_REG_EIP),0x700100,'Original routine did not return within the bound')
                expected=[bytes(uc.mem_read(at,size)) for at,size in SPANS]
                self.apply(ram)
                self.assertEqual(views(ram),expected)
                self.assertEqual(struct.unpack_from('<I',ram,FACTS['chapter'])[0],3)


if __name__=='__main__':unittest.main()
