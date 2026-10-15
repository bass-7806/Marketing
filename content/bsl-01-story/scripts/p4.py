# Frame 4: replace pasted product with the real BSL-01 packshot and seat it on the table
import cv2,numpy as np
from PIL import Image
im=cv2.imread('c4.png'); hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV); H,S=hsv[...,0].astype(int),hsv[...,1].astype(int)
raw=np.zeros(im.shape[:2],np.uint8); raw[1500:1770,85:1080]=(~((H>=5)&(H<=28)&(S>95)))[1500:1770,85:1080]*255
raw=cv2.morphologyEx(raw,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
n,l,st,_=cv2.connectedComponentsWithStats(raw); k=1+np.argmax(st[1:,4]); raw=np.where(l==k,255,0).astype(np.uint8)
hole=cv2.dilate(cv2.morphologyEx(raw,cv2.MORPH_CLOSE,np.ones((15,15),np.uint8)),np.ones((9,9),np.uint8)); V=hsv[...,2].astype(int); dk=np.zeros_like(hole); dk[1490:1758,85:460]=((V<95)|(S<60))[1490:1758,85:460]*255
hole=cv2.bitwise_or(hole,cv2.dilate(dk,np.ones((7,7),np.uint8))); hole[:,905:]=0
plate=cv2.inpaint(im,hole,15,cv2.INPAINT_TELEA)
# wood grain is horizontal: smooth inpaint along x only, then add grain noise so it is not smeary
sm=cv2.GaussianBlur(plate,(61,1),0); hm=cv2.GaussianBlur(hole,(0,0),4).astype(np.float32)[...,None]/255
plate=(plate*(1-hm)+sm*hm).astype(np.uint8)
# product from packshot (front view laid flat; perspective squash across the width)
p=Image.open('bsl01_hq.png').convert('RGBA'); p=p.crop((0,0,p.width,1505)).convert('RGBa')
L=830; s=L/1505; p=p.resize((round(p.width*s*0.80),L),Image.LANCZOS).rotate(83,resample=Image.BICUBIC,expand=True).convert('RGBA')
P=np.array(p).astype(np.float32)/255; rgb=P[...,:3][...,::-1].copy(); a=P[...,3]
ys,xs=np.where(a>0.5); ox,oy=92-xs.min(), 1600-int(np.median(ys[xs<xs.min()+8]))
# warm ambient grade, softer contrast, lamp light from the left, slight lens softness
rgb=rgb*np.array([0.86,0.97,1.06],np.float32); rgb=0.90*rgb+0.045
rgb=rgb*np.linspace(1.08,0.90,rgb.shape[1],dtype=np.float32)[None,:,None]
rgb=cv2.GaussianBlur(rgb,(0,0),0.7)
f=plate.astype(np.float32)/255; Hh,Ww=f.shape[:2]
A=np.zeros((Hh,Ww),np.float32); C=np.zeros_like(f)
ph,pw=a.shape; A[oy:oy+ph,ox:ox+pw]=a[:Hh-oy,:Ww-ox][:ph,:pw]; C[oy:oy+ph,ox:ox+pw]=rgb[:Hh-oy,:Ww-ox][:ph,:pw]
solid=(cv2.morphologyEx((A>0.5).astype(np.uint8)*255,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8)))
solid=cv2.morphologyEx(solid,cv2.MORPH_OPEN,np.ones((7,7),np.uint8))
# reflection on lacquered wood
refl=np.zeros_like(f); ra=np.zeros((Hh,Ww),np.float32)
for x in np.where(solid.any(0))[0]:
    c=np.where(solid[:,x]>0)[0]; yb=c.max(); Lr=min(60,yb-c.min())
    d=np.arange(1,Lr); d=d[yb+d<Hh]
    refl[yb+d,x]=C[yb-d,x]; ra[yb+d,x]=A[yb-d,x]*0.20*(1-d/Lr)**1.6
refl=cv2.GaussianBlur(refl,(0,0),2.5); ra=cv2.GaussianBlur(ra,(0,0),2.5)[...,None]
f=f*(1-ra)+refl*ra
# contact shadow: occlusion + soft falloff (light from upper left)
sh=np.zeros((Hh,Ww),np.float32)
for dy,dx,b,op in ((3,3,3,0.85),(12,10,14,0.45),(28,22,38,0.28)):
    s_=cv2.warpAffine(solid,np.float32([[1,0,dx],[0,1,dy]]),(Ww,Hh)).astype(np.float32)/255
    sh=np.maximum(sh,cv2.GaussianBlur(s_,(0,0),b)*op)
f=f*(1-sh[...,None]*0.85)
A3=A[...,None]; out=f*(1-A3)+C*A3
cv2.imwrite('c4r.png',np.clip(out*255,0,255).astype(np.uint8))
