# Seat the real BSL-01 packshot (lying on its back) onto a surface in a plate
import cv2,numpy as np,sys
from PIL import Image
def place(src,dst,tip,L,ang,squash=0.8,blur=0.7,warm=1.0,shade=(1.08,0.90),refl=0.18):
    f=cv2.imread(src).astype(np.float32)/255; Hh,Ww=f.shape[:2]
    p=Image.open('bsl01_hq.png').convert('RGBA'); p=p.crop((0,0,p.width,1505)).convert('RGBa')
    s=L/1505; p=p.resize((round(p.width*s*squash),L),Image.LANCZOS).rotate(90-ang,resample=Image.BICUBIC,expand=True).convert('RGBA')
    P=np.array(p).astype(np.float32)/255; rgb=P[...,:3][...,::-1].copy(); a=P[...,3]
    ys,xs=np.where(a>0.5); ox=tip[0]-xs.min(); oy=tip[1]-int(np.median(ys[xs<xs.min()+8]))
    rgb=rgb*np.array([0.86,0.97,1.06],np.float32)**warm; rgb=0.90*rgb+0.045
    rgb=rgb*np.linspace(shade[0],shade[1],rgb.shape[1],dtype=np.float32)[None,:,None]
    A=np.zeros((Hh,Ww),np.float32); C=np.zeros_like(f); ph,pw=a.shape
    y0,x0=max(oy,0),max(ox,0); y1,x1=min(oy+ph,Hh),min(ox+pw,Ww)
    A[y0:y1,x0:x1]=a[y0-oy:y1-oy,x0-ox:x1-ox]; C[y0:y1,x0:x1]=rgb[y0-oy:y1-oy,x0-ox:x1-ox]
    solid=cv2.morphologyEx((A>0.5).astype(np.uint8)*255,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
    solid=cv2.morphologyEx(solid,cv2.MORPH_OPEN,np.ones((7,7),np.uint8))
    R=np.zeros_like(f); ra=np.zeros((Hh,Ww),np.float32)
    for x in np.where(solid.any(0))[0]:
        c=np.where(solid[:,x]>0)[0]; yb=c.max(); Lr=min(50,yb-c.min()); d=np.arange(1,Lr); d=d[yb+d<Hh]
        R[yb+d,x]=C[yb-d,x]; ra[yb+d,x]=A[yb-d,x]*refl*(1-d/Lr)**1.6
    R=cv2.GaussianBlur(R,(0,0),2.5); ra=cv2.GaussianBlur(ra,(0,0),2.5)[...,None]; f=f*(1-ra)+R*ra
    sh=np.zeros((Hh,Ww),np.float32)
    for dy,dx,b,op in ((3,3,3,0.85),(10,9,12,0.45),(24,20,32,0.28)):
        s_=cv2.warpAffine(solid,np.float32([[1,0,dx],[0,1,dy]]),(Ww,Hh)).astype(np.float32)/255
        sh=np.maximum(sh,cv2.GaussianBlur(s_,(0,0),b)*op)
    f=f*(1-sh[...,None]*0.85)
    # depth of field: defocus product + its shadow to match the surface
    if blur>0:
        C=cv2.GaussianBlur(C*A[...,None],(0,0),blur); A2=cv2.GaussianBlur(A,(0,0),blur); C=C/np.maximum(A2,1e-4)[...,None]; A=A2
    out=f*(1-A[...,None])+C*A[...,None]
    cv2.imwrite(dst,np.clip(out*255,0,255).astype(np.uint8))
if __name__=='__main__':
    place('c1.png','c1r.png',tip=(560,1712),L=500,ang=10,squash=0.78,blur=3.0,warm=1.6,shade=(1.0,0.82))
    place('c3.png','c3r.png',tip=(520,1680),L=520,ang=8,squash=0.78,blur=1.6,warm=1.6,shade=(1.0,0.84))
