import cv2,numpy as np
im=cv2.imread('b1.jpg').astype(np.float32); mn=im.min(2)
near=(mn>238).astype(np.uint8)
ff=near.copy(); h,w=ff.shape; mask=np.zeros((h+2,w+2),np.uint8)
for pt in ((0,0),(w-1,0),(0,h-1),(w-1,h-1)): cv2.floodFill(ff,mask,pt,2)
bg=(ff==2)
soft=np.clip((250-mn)/45,0,1)
a=np.where(bg,soft,1.0).astype(np.float32)
# within bg band, unpremultiply against white to kill the fringe
a3=np.maximum(a,1e-3)[...,None]; col=np.clip((im-(1-a3)*255)/a3,0,255)
col=np.where(a3>0.02,col,0)
ys,xs=np.where(a>0.1); x0,x1,y0,y1=xs.min(),xs.max(),ys.min(),ys.max(); print(x0,y0,x1,y1)
out=np.dstack([col,a*255]).astype(np.uint8)[y0:y1+1,x0:x1+1]
cv2.imwrite('bsl01_hq.png',out)
