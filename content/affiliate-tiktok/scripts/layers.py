# Split poster into clean plate (no text) + locked text layers (RGBA)
import cv2, numpy as np
from PIL import Image
D='/home/user/Marketing/content/affiliate-tiktok/'
im=cv2.imread(D+'src/poster_4x5.jpg'); H,W=im.shape[:2]
mn=im.min(axis=2).astype(np.float32)
BOX={'logo':(390,50,690,105),'head1':(228,105,862,200),'head2':(165,200,905,272),'head3':(300,276,762,380),
     'foot':(170,1090,890,1210),'disc':(305,1290,780,1330)}
plate_mask=np.zeros((H,W),np.uint8)
for k,(x0,y0,x1,y1) in BOX.items():
    sub=im[y0:y1,x0:x1]; m=mn[y0:y1,x0:x1]
    thr=120 if k!='disc' else 110
    a=np.clip((m-thr)/70.,0,1)
    if k=='logo':  # keep TikTok red/cyan accents too
        hsv=cv2.cvtColor(sub,cv2.COLOR_BGR2HSV)
        a=np.maximum(a,np.clip((hsv[...,2].astype(np.float32)-170)/50.,0,1)*(hsv[...,1]>90))
    a=cv2.GaussianBlur(a,(0,0),0.6)
    rgba=np.dstack([cv2.cvtColor(sub,cv2.COLOR_BGR2RGB),(a*255).astype(np.uint8)])
    Image.fromarray(rgba).save(D+f'layers/{k}.png')
    bm=(cv2.dilate((a>0.08).astype(np.uint8),np.ones((9,9),np.uint8))*255)
    plate_mask[y0:y1,x0:x1]=np.maximum(plate_mask[y0:y1,x0:x1],bm)
plate=cv2.inpaint(im,plate_mask,9,cv2.INPAINT_TELEA)
bl=cv2.GaussianBlur(plate,(0,0),6); mm=cv2.GaussianBlur(plate_mask,(0,0),5)[...,None]/255.
plate=(plate*(1-mm)+bl*mm).astype(np.uint8)
cv2.imwrite(D+'src/plate_4x5.jpg',plate,[cv2.IMWRITE_JPEG_QUALITY,95])
# center lock: QR card + podium + products (soft ellipse-ish region)
lock=np.zeros((H,W),np.float32)
cv2.rectangle(lock,(322,382),(772,968),1,-1)
cv2.ellipse(lock,(537,985),(340,62),0,0,360,1,-1)
lock=cv2.GaussianBlur(lock,(0,0),5)
Image.fromarray(np.dstack([cv2.cvtColor(im,cv2.COLOR_BGR2RGB),(lock*255).astype(np.uint8)])).save(D+'layers/card.png')
