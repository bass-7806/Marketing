import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
D='/tmp/claude-0/-home-user-Marketing/86b9e76c-cba4-5a6b-8751-62d8a417c735/scratchpad/qc4'
A='/home/user/Marketing/content/baw-02-multi-styler/assets/'
FB=ImageFont.truetype(A+'Kanit-Bold.ttf',58); FR=ImageFont.truetype(A+'Kanit-Regular.ttf',39)
# logo recolor to CI #0D99DB
lg=Image.open(A+'bwell_beauty_logo_blue.png').convert('RGBA'); al=lg.split()[3]
lg=Image.new('RGBA',lg.size,(0x0D,0x99,0xDB,255)); lg.putalpha(al)
LW=205; lg=lg.resize((LW,round(lg.height*LW/lg.width)),Image.LANCZOS)
TX={1:(["เลิกงานแล้ว","แต่มีนัดต่อ?"],"แวะเตรียมตัวหน้ากระจกสักครู่"),
    2:(["เตรียมอุปกรณ์","ให้พร้อม"],"เลือกใช้ตามคู่มือของรุ่น"),
    3:(["เช็กความเรียบร้อย","หน้ากระจก"],"เก็บรายละเอียดก่อนออกไปต่อ"),
    4:(["พร้อมแล้ว","ไปต่อกัน"],None)}
def text(im,x,ytop,s,f):
    d=ImageDraw.Draw(im); b=f.getbbox(s); d.text((x-b[0],ytop-b[1]),s,font=f,fill=(255,255,255))
def overlay(im,i,logo_y,head_y,bot_y):
    im.alpha_composite(lg,(77,logo_y))
    h,b=TX[i]
    for k,s in enumerate(h): text(im,65,head_y+94*k,s,FB)
    if b: text(im,65,bot_y,b,FR)
    return im
def product(bg,H,x_off,y):
    p=Image.open(f'{D}/bsl01_cut.png').convert('RGBA'); arr=np.array(p)
    for yy in range(1506,arr.shape[0]):
        arr[yy,:,:3]=np.where(arr[yy,:,3:]>0,[42,42,44],arr[yy,:,:3]); arr[yy,:,3]=(arr[yy,:,3]*max(0,1-(yy-1506)/90)).astype(np.uint8)
    p=Image.fromarray(arr)
    r,g,b,a=p.split(); r=r.point(lambda v:min(255,int(v*1.04))); b=b.point(lambda v:int(v*0.93)); p=Image.merge('RGBA',(r,g,b,a))
    p=p.resize((round(p.width*H/p.height),H),Image.LANCZOS).rotate(-10,resample=Image.BICUBIC,expand=True)
    x=(bg.width-p.width)//2+x_off
    sh=Image.new('RGBA',p.size,(0,0,0,0)); sh.putalpha(p.split()[3].point(lambda v:int(v*0.5))); sh=sh.filter(ImageFilter.GaussianBlur(28))
    bg.alpha_composite(sh,(x+35,y+40)); bg.alpha_composite(p,(x,y)); return bg
def finish(im,seed):
    # photographic finish so the scene reads as a camera photo: softer saturation, highlight roll-off, vignette, luma grain
    a=np.asarray(im.convert('RGB')).astype(np.float32)/255; h,w=a.shape[:2]
    g=a.mean(2,keepdims=True); a=g+(a-g)*0.90
    a=np.where(a>0.75,0.75+(a-0.75)*0.7,a); a=0.015+a*0.985
    yy,xx=np.mgrid[0:h,0:w]; r=np.hypot((xx-w/2)/(w/2),(yy-h/2)/(h/2)); a=a*(1-0.10*np.clip(r-0.55,0,1)[...,None]**1.5)
    n=np.random.default_rng(seed).normal(0,1,(h,w)).astype(np.float32); n=(n+np.roll(n,1,0)*0.35+np.roll(n,1,1)*0.35)/1.3
    a=a+n[...,None]*0.016
    return Image.fromarray(np.clip(a*255,0,255).astype(np.uint8)).convert('RGBA')
out={}
for i in (1,2,3,4):
    # 9:16
    if i==2: base=product(Image.open(f'{D}/bg2.png').convert('RGBA'),1300,110,380)
    else: base=Image.open(f'{D}/'+('c4r.png' if i==4 else f'c{i}.png')).convert('RGBA')
    out[(i,'916')]=overlay(finish(base,i),i,70,199,1782)
    # 4:5
    if i==2:
        bg=Image.open(f'{D}/bg2.png').convert('RGBA').crop((0,330,1080,1680))
        b45=product(bg,960,190,300)
    elif i==4:
        src=Image.open(f'{D}/c4r.png').convert('RGBA').crop((0,140,1080,1840)); sc=1350/1700
        fg=src.resize((round(1080*sc),1350),Image.LANCZOS)
        b45=src.resize((1080,1350)).filter(ImageFilter.GaussianBlur(30)); m=Image.new('L',fg.size,255); import numpy as _n; ma=_n.array(m).astype(float); ma[:,:120]*=_n.linspace(0,1,120)[None,:]; fg.putalpha(Image.fromarray(ma.astype('uint8'))); b45.alpha_composite(fg,(1080-fg.width,0))
    else:
        y0={1:150,3:60}[i]; b45=Image.open(f'{D}/c{i}.png').convert('RGBA').crop((0,y0,1080,y0+1350))
    out[(i,'45')]=overlay(finish(b45,10+i),i,60,150,1262)
import os; os.makedirs(f'{D}/out',exist_ok=True)
for (i,k),im in out.items(): im.convert('RGB').save(f'{D}/out/BSL-01_set_{i}_{"9x16" if k=="916" else "4x5"}.png')
ims=[out[(i,'916')].convert('RGB').resize((270,480)) for i in (1,2,3,4)]
s=Image.new('RGB',(1080,480)); [s.paste(im,(n*270,0)) for n,im in enumerate(ims)]; s.save(f'{D}/sheet916.jpg',quality=88)
ims=[out[(i,'45')].convert('RGB').resize((270,338)) for i in (1,2,3,4)]
s=Image.new('RGB',(1080,338)); [s.paste(im,(n*270,0)) for n,im in enumerate(ims)]; s.save(f'{D}/sheet45.jpg',quality=88)
