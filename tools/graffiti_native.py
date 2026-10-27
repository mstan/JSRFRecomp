"""Authored JSRF native graffiti codec. No original artwork or signing keys.

Format derived from original 12CCB0/12D6C0/12DFC0/12E240 (USA).
All seven signatures use the selected console's title key, flags=0.
The game stores five size classes, 28 HDD slots, linear RGB565 previews,
BGRA editable pixels, and a BC2 display texture. M has unused backing padding.
"""
import hashlib
import hmac
import math
import re
import struct

SIZES = (("SS",128,128,16384,32), ("S",128,128,16384,32),
         ("M",384,256,131072,48), ("L",512,256,131072,64),
         ("XL",1024,256,262144,128))
KEY_COLOR = 0xc618


def dimensions(size):
    if type(size) is not int or not 0 <= size < len(SIZES):
        raise ValueError("Choose a graffiti size from SS through XL")
    return SIZES[size]


def _weights(source, target):
    # Exact area coverage for shrinking, bilinear for enlarging. Working in
    # premultiplied alpha avoids black fringes around transparent PNG edges.
    if target < source:
        scale = source / target
        return [[(j, max(0, min((i+1)*scale, j+1)-max(i*scale,j))/scale)
                 for j in range(int(i*scale), min(source, math.ceil((i+1)*scale)))]
                for i in range(target)]
    out = []
    for i in range(target):
        x = max(0, min(source-1, (i+.5)*source/target-.5)); lo = int(x)
        out.append([(lo, 1-(x-lo)), (min(lo+1,source-1), x-lo)])
    return out


def resize(rgba, width, height, out_width, out_height):
    if type(width) is not int or type(height) is not int or not 1 <= width <= 8192 or not 1 <= height <= 8192 or width*height > 16777216 or len(rgba) != width*height*4:
        raise ValueError("Image must contain at most 16 million pixels (8192 per side)")
    if (width,height) == (out_width,out_height):
        return bytes(rgba)
    wx, wy = _weights(width,out_width), _weights(height,out_height)
    # Only retain horizontally resampled rows still needed by this output row.
    cache = {}; result = bytearray(out_width*out_height*4)
    for y, weights in enumerate(wy):
        needed = {sy for sy,_ in weights}
        cache = {sy: row for sy,row in cache.items() if sy in needed}
        for sy in needed-cache.keys():
            row = []
            for weights_x in wx:
                channels = [0.,0.,0.,0.]
                for sx, weight in weights_x:
                    at = (sy*width+sx)*4; alpha = rgba[at+3]
                    for c in range(3): channels[c] += rgba[at+c]*alpha*weight
                    channels[3] += alpha*weight
                row.append(channels)
            cache[sy] = row
        for x in range(out_width):
            channels = [sum(cache[sy][x][c]*weight for sy,weight in weights) for c in range(4)]
            at = (y*out_width+x)*4; alpha = channels[3]
            for c in range(3): result[at+c] = min(255,max(0,round(channels[c]/alpha))) if alpha else 0
            result[at+3] = min(255,max(0,round(alpha)))
    return bytes(result)


def fit(rgba, width, height, size, mode="contain", density=1):
    if type(width) is not int or type(height) is not int or not 1<=width<=8192 or not 1<=height<=8192 or width*height>16777216 or len(rgba)!=width*height*4:
        raise ValueError("Invalid image dimensions or pixel data")
    _, w,h,_,_ = dimensions(size)
    if density not in (1,2,4):raise ValueError("Choose native, 2x or 4x detail")
    w*=density;h*=density
    if mode not in ("contain","crop","stretch"): raise ValueError("Unknown image fit")
    if mode == "stretch": return resize(rgba,width,height,w,h)
    scale = (min if mode == "contain" else max)(w/width,h/height)
    rw,rh = max(1,round(width*scale)),max(1,round(height*scale))
    # Crop source first for extreme panoramas; intermediate stays bounded.
    if mode == "crop":
        cw,ch = min(width,max(1,round(w/scale))),min(height,max(1,round(h/scale)))
        left,top=(width-cw)//2,(height-ch)//2
        rgba = b"".join(rgba[((top+y)*width+left)*4:((top+y)*width+left+cw)*4] for y in range(ch))
        return resize(rgba,cw,ch,w,h)
    pixels=resize(rgba,width,height,rw,rh); out=bytearray(w*h*4)
    left,top=(w-rw)//2,(h-rh)//2
    for y in range(rh):out[((top+y)*w+left)*4:((top+y)*w+left+rw)*4]=pixels[y*rw*4:(y+1)*rw*4]
    return bytes(out)


def _rgb565(pixel):
    r,g,b,a=pixel
    if a < 128:return KEY_COLOR
    value=((r>>3)<<11)|((g>>2)<<5)|(b>>3)
    return value if value != KEY_COLOR else value^1


def _rgb(value):
    return ((value>>11)*255//31, ((value>>5)&63)*255//63, (value&31)*255//31)


def bc2(rgb565, width, height):
    """Portable BC2 encoder; independent 4x4 blocks, explicit 4-bit alpha.

    Choose endpoints along the block's principal color axis, then select the
    nearest of the four RGB565 interpolants. Encoding happens only on import.
    """
    out=bytearray()
    for y in range(0,height,4):
        for x in range(0,width,4):
            values=[rgb565[(y+dy)*width+x+dx] for dy in range(4) for dx in range(4)]
            pixels=[_rgb(v) for v in values if v != KEY_COLOR]
            alpha=sum((15 if v != KEY_COLOR else 0)<<(4*i) for i,v in enumerate(values))
            if pixels:
                # Farthest pair gives a stable color axis, including blocks
                # whose extrema do not lie on a luminance ordering.
                lo,hi=max(((a,b) for a in pixels for b in pixels),key=lambda pair:sum((pair[0][c]-pair[1][c])**2 for c in range(3)))
                c0,c1=_rgb565((*hi,255)),_rgb565((*lo,255))
            else:c0,c1=0,1
            a,b=_rgb(c0),_rgb(c1)
            palette=(a,b,tuple((2*a[c]+b[c])//3 for c in range(3)),tuple((a[c]+2*b[c])//3 for c in range(3)))
            indices=0
            for i,value in enumerate(values):
                color=_rgb(value)
                index=min(range(4),key=lambda j:sum((color[c]-palette[j][c])**2 for c in range(3))) if value!=KEY_COLOR else 0
                indices|=index<<(2*i)
            out.extend(struct.pack("<QHHI",alpha,c0,c1,indices))
    return bytes(out)


def encode(rgba, size, slot, title_key):
    _,w,h,backing,thumb_width=dimensions(size)
    if type(slot) is not int or not 0 <= slot < 28:raise ValueError("All 28 HDD graffiti slots are in use")
    if len(title_key)!=16 or len(rgba)!=w*h*4:raise ValueError("Invalid graffiti pixels or signing identity")
    pixels=[_rgb565(rgba[i:i+4]) for i in range(0,len(rgba),4)]
    thumb=resize(rgba,w,h,thumb_width,32)
    small=struct.pack("<"+"H"*(len(thumb)//4),*(_rgb565(thumb[i:i+4]) for i in range(0,len(thumb),4)))
    full=struct.pack("<"+"H"*len(pixels),*pixels)+bytes((backing-w*h)*2)
    editable=bytearray(rgba)
    editable[0::4],editable[2::4]=rgba[2::4],rgba[0::4]
    editable.extend(bytes((backing-w*h)*4))
    display=bc2(pixels,w,h)+bytes(backing-w*h)
    # Fifteen unused editor objects. Original constructor puts them on a 3x5
    # grid, with object ID -1; imports contain only the painted raster layer.
    objects=b"".join(struct.pack("<iii9f",-1,0,0,(col-1)*.8,2.2-row*.8,10.,0.,0.,0.,.7,.7,.7)
                     for row in range(5) for col in range(3))
    blocks=(small,full,bytes(editable),display,objects,struct.pack("<4I",0,0,0,3))
    header=bytes((size,28+slot,0,0))+b"JSRF"+bytes(8)
    sign=lambda value:hmac.digest(title_key,value,"sha1")
    return header+sign(header)+b"".join(map(sign,blocks))+b"".join(blocks)


def files(rgba,size,slot,title_key,thumbnail):
    """thumbnail is read from the owner's verified original game assets."""
    if len(thumbnail)!=4096:raise ValueError("Original graffiti slot thumbnail is unavailable")
    name=f"GRAFFITI{slot+1:03}"
    return {"save.dat":encode(rgba,size,slot,title_key),
            "SaveMeta.xbx":("\ufeffName="+name+"\r\n").encode("utf-16le"),
            "SaveImage.xbx":bytes(thumbnail)}


def high_resolution(pixels,width,height,size,mode,density,native_save):
    """Companion in the same native save directory; the game ignores this file.

    The entire native save digest invalidates it after an original editor save.
    Its own pixels are hashed so damaged companions fall back to native art.
    """
    if density==1:return None
    rgba=fit(pixels,width,height,size,mode,density)
    _,w,h,_,_=dimensions(size);w*=density;h*=density
    return (b'JSRFHD1\0'+struct.pack('<4I',size,density,w,h)+
            hashlib.sha256(native_save).digest()+hashlib.sha256(rgba).digest()+rgba)


def saved_design(store,slot,title_key,full=False):
    """Read the actual selected native save, never a generated placeholder."""
    if type(slot) is not int or not 0<=slot<28:raise ValueError('Invalid graffiti slot')
    name=directory(slot);save=store.read(name,'save.dat',2*1024*1024)
    if save is None:return None
    result=dict(slot=slot,sha=hashlib.sha256(save).hexdigest(),size=0,density=1,width=0,height=0,rgba=None,deletable=False)
    try:
        size=save[0];_,w,h,backing,tw=dimensions(size)
        if save[:16]!=bytes((size,28+slot,0,0))+b'JSRF'+bytes(8):return result
        meta=store.read(name,'SaveMeta.xbx',8192)
        try:identified=meta is not None and re.search(r'(?:^|\n)Name=GRAFFITI'+f'{slot+1:03}'+r'(?:\r?\n|$)',meta.decode('utf-16')) is not None
        except UnicodeError:identified=False
        result['deletable']=identified
        lengths=(tw*64,backing*2,backing*4,backing,720,16)
        if len(save)!=156+sum(lengths) or not hmac.compare_digest(save[16:36],hmac.digest(title_key,save[:16],'sha1')):return result
        at=156;blocks=[]
        for i,n in enumerate(lengths):
            block=save[at:at+n];at+=n
            if not hmac.compare_digest(save[36+i*20:56+i*20],hmac.digest(title_key,block,'sha1')):return result
            blocks.append(block)
        pixels=bytearray(blocks[2][:w*h*4]);pixels[0::4],pixels[2::4]=pixels[2::4],pixels[0::4]
        result.update(size=size,width=w,height=h,rgba=bytes(pixels))
        hd=store.read(name,'xboxllr-hd.bin',88+16*1024*1024)
        if hd is not None and len(hd)>=88 and hd[:8]==b'JSRFHD1\0' and hd[24:56]==hashlib.sha256(save).digest():
            hs,density,hw,hh=struct.unpack_from('<4I',hd,8)
            if hs==size and density in (2,4) and (hw,hh)==(w*density,h*density) and len(hd)==88+hw*hh*4 and hashlib.sha256(hd[88:]).digest()==hd[56:88]:
                result['density']=density
                if full:result.update(width=hw,height=hh,rgba=hd[88:])
        return result
    except (OSError,ValueError,IndexError,struct.error):return result


def texture_replacements(store):
    """Yield content-bound BC2 replacements, including the game's 128px tiles.

    No addresses, title code, or guessed renderer resource IDs enter the host.
    Only untouched imported saves qualify. Slot reuse and native editor changes
    automatically discard their old high-resolution attachment.
    """
    for slot in range(28):
        name=directory(slot)
        try:
            hd=store.read(name,'xboxllr-hd.bin',88+16*1024*1024)
            if hd is None:continue
            if len(hd)<88 or hd[:8]!=b'JSRFHD1\0':continue
            size,density,hw,hh=struct.unpack_from('<4I',hd,8)
            _,w,h,backing,tw=dimensions(size)
            if density not in (2,4) or (hw,hh)!=(w*density,h*density):continue
            rgba=hd[88:]
            if len(rgba)!=hw*hh*4 or hashlib.sha256(rgba).digest()!=hd[56:88]:continue
            save=store.read(name,'save.dat',2*1024*1024)
            if save is None or hashlib.sha256(save).digest()!=hd[24:56]:continue
            if save[:2]!=bytes((size,28+slot)):continue
            full=save[156+tw*64:156+tw*64+backing*2]
            at=156+tw*64+backing*6;bc=save[at:at+backing]
            if len(bc)!=backing:continue
            # Original display textures are cutouts. Keep that alpha contract
            # while retaining all source RGB detail in the companion.
            pixels=bytearray(rgba);pixels[3::4]=bytes(255 if a>=128 else 0 for a in pixels[3::4])
            editable=save[156+tw*64+backing*2:156+tw*64+backing*2+w*h*4]
            yield dict(format=0x12,width=w,height=h,source=editable,hd_width=hw,hd_height=hh,rgba=bytes(pixels))
            def region(x,y,rw,rh,fmt):
                if fmt==0xe:source=b''.join(bc[((y//4+row)*(w//4)+x//4)*16:((y//4+row)*(w//4)+(x+rw)//4)*16] for row in range(rh//4))
                else:source=b''.join(full[((y+row)*w+x)*2:((y+row)*w+x+rw)*2] for row in range(rh))
                high=b''.join(pixels[((y*density+row)*hw+x*density)*4:((y*density+row)*hw+(x+rw)*density)*4] for row in range(rh*density))
                return dict(format=fmt,width=rw,height=rh,source=source,hd_width=rw*density,hd_height=rh*density,rgba=high)
            yield region(0,0,w,h,0x11)
            if not (w&(w-1)):yield region(0,0,w,h,0xe)
            for y in range(0,h,128):
                for x in range(0,w,128):
                    yield region(x,y,128,128,0xe)
                    yield region(x,y,128,128,0x11)
        except (OSError,ValueError,struct.error):
            continue


THUMBNAILS=("SaveImageSS.xbx","SaveImage_S.xbx","SaveImage_M.xbx","SaveImage_L.xbx","SaveImageXL.xbx")

def thumbnail_path(size):
    dimensions(size)
    return 'Media/Mark/'+THUMBNAILS[size]


def directory(slot):
    """Original XAPI 146C6C polynomial hash of the UTF-16 save name."""
    if type(slot) is not int or not 0<=slot<28:raise ValueError('Invalid graffiti slot')
    value=0
    for unit in f'GRAFFITI{slot+1:03}':value=(value*65536+ord(unit))%0xffffffffffc5
    return f'{value:012X}'


def occupied_slots(store):
    names=store.names();folded={name.casefold() for name in names}
    # Never reuse a canonical directory whose metadata is missing/corrupt.
    used={slot for slot in range(28) if directory(slot).casefold() in folded}
    for name in names:
        meta=store.read(name,'SaveMeta.xbx',8192)
        if meta is None:continue
        try:text=meta.decode('utf-16')
        except UnicodeError:continue
        match=re.search(r'(?:^|\n)Name=GRAFFITI(\d{3})(?:\r?\n|$)',text)
        if match:
            number=int(match[1])
            if 1<=number<=28:used.add(number-1)
            else:raise ValueError('Unrecognized existing graffiti slot number')
    return used
