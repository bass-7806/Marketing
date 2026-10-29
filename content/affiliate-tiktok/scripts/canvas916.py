# Build 1080x1920 plate: original at y=TOP, mirrored extensions top/bottom, feathered seams
import numpy as np, cv2
TOP=200
p=cv2.imread('src/plate_4x5.jpg').astype(np.float32); H=p.shape[0]
c=np.zeros((1920,1080,3),np.float32)
c[TOP:TOP+H]=p
top=p[:TOP][::-1]; c[:TOP]=top
nb=1920-TOP-H; bot=p[H-nb:][::-1]; c[TOP+H:]=bot
# soften seams: blur bands and darken extremes a touch
for y in (TOP,TOP+H):
    band=c[y-40:y+40].copy(); bl=cv2.GaussianBlur(band,(0,0),12)
    w=(1-np.abs(np.linspace(-1,1,80)))[:,None,None]; c[y-40:y+40]=band*(1-w)+bl*w
g=np.ones(1920,np.float32); g[:TOP]=np.linspace(0.75,1,TOP); g[TOP+H:]=np.linspace(1,0.8,nb)
c*=g[:,None,None]
cv2.imwrite('src/plate_9x16.jpg',np.clip(c,0,255).astype(np.uint8),[cv2.IMWRITE_JPEG_QUALITY,95])
cv2.imwrite('/tmp/claude-0/-home-user-Marketing/86b9e76c-cba4-5a6b-8751-62d8a417c735/scratchpad/p916.jpg',cv2.resize(np.clip(c,0,255).astype(np.uint8),(405,720)))
