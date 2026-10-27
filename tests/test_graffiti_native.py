import hashlib,hmac,struct,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import graffiti_native as g

class GraffitiTests(unittest.TestCase):
    def test_saved_gallery_uses_signed_native_and_valid_hd(self):
        pixels=bytes((7,23,241,255))*128*128;key=bytes(range(16))
        save=g.encode(pixels,0,1,key)
        hd=g.high_resolution(pixels,128,128,0,'contain',2,save)
        class Store:
            data={'save.dat':save,'SaveMeta.xbx':'\ufeffName=GRAFFITI002\r\n'.encode('utf-16le'),'xboxllr-hd.bin':hd}
            def read(self,name,file,limit):return self.data.get(file) if name==g.directory(1) else None
        store=Store();design=g.saved_design(store,1,key)
        self.assertEqual(design['rgba'],pixels);self.assertTrue(design['deletable']);self.assertEqual(design['density'],2)
        full=g.saved_design(store,1,key,full=True);self.assertEqual((full['width'],full['height']),(256,256));self.assertEqual(full['rgba'],hd[88:])
        self.assertIsNone(g.saved_design(store,0,key))
        self.assertIsNone(g.saved_design(store,1,bytes(16))['rgba'])
        store.data['xboxllr-hd.bin']=hd[:-1]+bytes((hd[-1]^1,))
        self.assertEqual(g.saved_design(store,1,key,full=True)['rgba'],pixels)
        store.data['SaveMeta.xbx']='Name=GRAFFITI001\r\n'.encode('utf-16')
        self.assertFalse(g.saved_design(store,1,key)['deletable'])
    def test_high_resolution_native_fallback_and_editor_invalidation(self):
        # High-frequency detail exists in the companion, independently of the
        # native payload and its signed editable/display raster layers.
        source=bytes((7,23,241,255))*512*512
        native=g.encode(g.fit(source,512,512,0),0,1,bytes(16))
        hd=g.high_resolution(source,512,512,0,'contain',4,native)
        self.assertEqual(struct.unpack_from('<4I',hd,8),(0,4,512,512))
        self.assertEqual(hd[88:],source)
        class Store:
            def read(self,name,file,limit):
                if name!=g.directory(1):return None
                return {'save.dat':native,'xboxllr-hd.bin':hd}.get(file)
        entries=list(g.texture_replacements(Store()))
        self.assertEqual(len(entries),5) # editable atlas, RGB565/BC2 full and tile
        self.assertEqual(entries[0]['rgba'],source)
        self.assertEqual((entries[0]['width'],entries[0]['hd_width']),(128,512))
        native=native[:-1]+bytes((native[-1]^1,))
        self.assertEqual(list(g.texture_replacements(Store())),[])
        with self.assertRaises(ValueError):g.fit(source,512,512,0,density=8)
    def test_native_payloads_signatures_and_transparency(self):
        for size in range(5):
            _,w,h,backing,tw=g.dimensions(size)
            pixel=bytes((255,0,0,255));rgba=pixel*(w*h//2)+bytes(w*h*2)
            key=bytes(range(16));save=g.encode(rgba,size,7,key)
            self.assertEqual(save[:16],bytes((size,35,0,0))+b'JSRF'+bytes(8))
            self.assertEqual(save[16:36],hmac.digest(key,save[:16],'sha1'))
            sizes=[tw*64,backing*2,backing*4,backing,720,16];at=156;blocks=[]
            for i,length in enumerate(sizes):
                data=save[at:at+length];blocks.append(data);at+=length
                self.assertEqual(save[36+i*20:56+i*20],hmac.digest(key,data,'sha1'))
            self.assertEqual(at,len(save))
            self.assertEqual(blocks[1][:2],b'\0\xf8')
            self.assertEqual(blocks[1][w*h:w*h+2],b'\x18\xc6')
            self.assertEqual(blocks[2][:4],b'\0\0\xff\xff')
            self.assertEqual(blocks[3][:8],b'\xff'*8)
            self.assertEqual(blocks[3][w*h//2:w*h//2+8],bytes(8))
            self.assertTrue(all(struct.unpack_from('<i',blocks[4],i*48)[0]==-1 for i in range(15)))

    def test_original_name_hash_and_occupied_directory(self):
        self.assertEqual(g.directory(0),'85BE4CFBC301')
        self.assertEqual(g.directory(1),'85BE4CFBC302')
        self.assertEqual(g.directory(9),'85BE4CFCC300')
        class Existing:
            def names(self):return ['85be4cfbc303','unrelated']
            def read(self,*args):return None
        self.assertEqual(g.occupied_slots(Existing()),{2})

    def test_alpha_resample_and_fit(self):
        # Fully transparent blue must not make a dark/blue edge in red art.
        result=g.resize(bytes((255,0,0,255,0,0,255,0)),2,1,1,1)
        self.assertEqual(result,bytes((255,0,0,128)))
        source=bytes((10,20,30,255))*8
        contained=g.fit(source,4,2,0,'contain')
        self.assertEqual(contained[:4],bytes(4));self.assertEqual(contained[(64*128+64)*4:(64*128+64)*4+4],bytes((10,20,30,255)))
        for args in [(source,0,2,0),(source,4,2,8)]:
            with self.assertRaises(ValueError):g.fit(*args)
        with self.assertRaises(ValueError):g.encode(bytes(128*128*4),0,28,bytes(16))

if __name__=='__main__':unittest.main()
