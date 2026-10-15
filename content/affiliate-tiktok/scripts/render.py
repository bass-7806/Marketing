# Composite locked layers over AI background video -> raw RGB frames to stdout
# usage: python3 render.py bg.mp4 layers_dir | ffmpeg -f rawvideo ...
import sys, subprocess, math, numpy as np
from PIL import Image
BG, LD = sys.argv[1], sys.argv[2]
W,H,FPS,N=1080,1920,30,300
L={k:Image.open(f'{LD}/{k}.png').convert('RGBA') for k in
   ['logo','head1','head2','head3','card','foot','disc','brackets','cta','scanline']}
def cl(x): return max(0.,min(1.,x))
def eo(x): x=cl(x); return 1-(1-x)**3
def back(x):
    x=cl(x); c1=1.70158; c3=c1+1; return 1+c3*(x-1)**3+c1*(x-1)**2
def alpha(im,a):
    if a>=0.999: return im
    r=im.copy(); r.putalpha(r.getchannel('A').point(lambda v:int(v*a))); return r
def put(c,im,x,y,a=1.):
    if a<=0.003: return
    c.alpha_composite(alpha(im,a),(int(round(x)),int(round(y))))
p=subprocess.Popen(['ffmpeg','-v','error','-i',BG,'-vf',f'fps={FPS},scale={W}:{H}:flags=lanczos',
   '-frames:v',str(N),'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
last=None
for f in range(N):
    t=f/FPS
    buf=p.stdout.read(W*H*3)
    if len(buf)==W*H*3: last=buf
    c=Image.frombuffer('RGB',(W,H),last,'raw','RGB',0,1).convert('RGBA')
    put(c,L['card'],0,200)                                   # QR card locked from frame 0
    k=eo((t-0.0)/0.5);  put(c,L['logo'],390,250-30*(1-k),k)
    k=eo((t-0.25)/0.5)
    if k>0:
        s=1.12-0.12*k; im=L['head1']; w,h=im.size
        im2=im.resize((int(w*s),int(h*s)),Image.LANCZOS)
        put(c,im2,228+w/2-im2.size[0]/2,305+h/2-im2.size[1]/2,k)
    k=eo((t-0.6)/0.5);  put(c,L['head2'],165-70*(1-k),400,k)
    k=eo((t-1.0)/0.5);  put(c,L['head3'],300,476+24*(1-k),k)
    k=eo((t-1.6)/0.4)
    if k>0:
        pulse=0.6+0.4*(0.5+0.5*math.cos(2*math.pi*(t-1.6)/1.0))
        put(c,L['brackets'],285,554,k*pulse)
    if 1.8<=t<5.8:                                           # scan sweep, gone before the clean hold
        u=(t-1.8)/2.0; u=u-int(u); y=650+(975-650)*(0.5-0.5*math.cos(2*math.pi*u))
        put(c,L['scanline'],334,y-30,0.85*cl((t-1.8)/0.3)*cl((5.8-t)/0.3))
    k=eo((t-1.7)/0.5);  put(c,L['foot'],170,1290+30*(1-k),k)
    k=(t-2.2)/0.6
    if k>0:
        y=1395+140*(1-back(k)); bob=4*math.sin(2*math.pi*(t-2.8)/1.2) if t>2.8 else 0
        im=L['cta']
        if t>2.8:
            s=1+0.035*max(0,math.sin(2*math.pi*(t-2.8)/1.2))
            im=im.resize((int(im.size[0]*s),int(im.size[1]*s)),Image.LANCZOS)
        put(c,im,144+396-im.size[0]/2,y+bob-(im.size[1]-132)/2,cl(k*2))
    k=eo((t-2.4)/0.5);  put(c,L['disc'],305,1495,k)
    sys.stdout.buffer.write(c.convert('RGB').tobytes())
