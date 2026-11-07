# CTA pill, scan brackets, scan line overlays (1080-wide canvas coords)
from PIL import Image, ImageDraw, ImageFont, ImageFilter
F='/home/user/Marketing/content/baw-02-multi-styler/assets/Kanit-Bold.ttf'
RG=(242,190,160,255); WH=(255,255,255,255)
# CTA pill
f=ImageFont.truetype(F,44); t='แคปหน้าจอ แล้วสแกน QR สมัครเลย'
w=int(f.getlength(t))+96; h=92
im=Image.new('RGBA',(w+40,h+40),(0,0,0,0)); d=ImageDraw.Draw(im)
sh=Image.new('RGBA',im.size,(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle((20,26,20+w,26+h),h//2,fill=(0,0,0,140))
im=Image.alpha_composite(im,sh.filter(ImageFilter.GaussianBlur(8))); d=ImageDraw.Draw(im)
d.rounded_rectangle((20,20,20+w,20+h),h//2,fill=(236,170,140,255))
d.rounded_rectangle((24,24,16+w,16+h),h//2-4,outline=(255,232,215,255),width=3)
d.text((20+w/2,20+h/2-2),t,font=f,fill=(70,22,20,255),anchor='mm')
im.save('layers/cta.png')
# Scan brackets around white QR card (card x345-752, y402-820 in poster -> +200 y)
x0,y0,x1,y1=325,594,772,1040; L=70; T=10
br=Image.new('RGBA',(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(br)
for (cx,cy,sx,sy) in [(x0,y0,1,1),(x1,y0,-1,1),(x0,y1,1,-1),(x1,y1,-1,-1)]:
    d.line([(cx,cy+sy*L),(cx,cy),(cx+sx*L,cy)],fill=WH,width=T,joint='curve')
g=br.filter(ImageFilter.GaussianBlur(10)); br=Image.alpha_composite(Image.alpha_composite(Image.new('RGBA',br.size),g),br)
br.crop((x0-40,y0-40,x1+40,y1+40)).save('layers/brackets.png')
# Scan line (glow bar, spans QR modules width x372-716)
sl=Image.new('RGBA',(420,60),(0,0,0,0)); d=ImageDraw.Draw(sl)
d.rounded_rectangle((10,26,410,34),4,fill=(255,120,90,230))
sl=Image.alpha_composite(sl.filter(ImageFilter.GaussianBlur(9)),sl); sl.save('layers/scanline.png')
print(w+40,h+40)
