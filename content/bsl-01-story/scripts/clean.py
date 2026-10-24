import cv2, numpy as np, sys
D=sys.argv[1]
boxes={1:[(55,180,380,370),(55,1760,540,1845)],2:[(615,180,940,340),(55,1760,440,1845)],3:[(55,180,530,370),(55,1770,535,1845)],4:[(55,180,340,365)]}
logo={1:(60,55,300,165),2:(45,45,255,145),3:(60,55,300,165),4:(60,55,300,165)}
for i in (1,2,3,4):
    im=cv2.imread(f'{D}/f{i}.png'); hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    m=np.zeros(im.shape[:2],np.uint8)
    for x0,y0,x1,y1 in boxes[i]:
        sub=im[y0:y1,x0:x1].astype(int); g=sub.mean(2); s=hsv[y0:y1,x0:x1,1]
        mm=((g>170)&(s<70)).astype(np.uint8)*255; m[y0:y1,x0:x1]|=mm
    x0,y0,x1,y1=logo[i]; s=hsv[y0:y1,x0:x1]; mm=((s[...,0]>90)&(s[...,0]<120)&(s[...,1]>80)).astype(np.uint8)*255; m[y0:y1,x0:x1]|=mm
    m=cv2.dilate(m,np.ones((7,7),np.uint8),iterations=2)
    out=cv2.inpaint(im,m,9,cv2.INPAINT_TELEA)
    cv2.imwrite(f'{D}/c{i}.png',out); cv2.imwrite(f'{D}/m{i}.png',m)
    ys,xs=np.where(m[0:200]>0); print(i,'logo mask bbox',xs.min(),ys.min(),xs.max(),ys.max())
