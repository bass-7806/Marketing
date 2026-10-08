from PIL import Image, ImageDraw, ImageFont, ImageFilter
A='/home/user/Marketing/content/baw-02-multi-styler/assets/'
W,H=1080,1920
def F(n,s): return ImageFont.truetype(A+n,s)
logo=Image.open(A+'bwell_beauty_logo_blue.png').convert('RGBA'); _a=logo.split()[3]; logo=Image.new('RGBA',logo.size,(0x0D,0x99,0xDB,255)); logo.putalpha(_a)  # CI Primary Blue #0D99DB
lw=300; logo=logo.resize((lw,round(logo.height*lw/logo.width)),Image.LANCZOS)
segs=[(None,'เลือกหัวให้ตรงลุค','7 in 1 Multi Styler'),
      (None,'แปรงกลม','เพิ่มวอลลุ่ม จัดปลายผมให้โค้ง'),
      (None,'แกนม้วน','ลุคลอนสวยเป็นธรรมชาติ'),
      ('BAW-02','BLDC Multi Hair Styler',None)]
WHITE=(255,255,255,255); GRAY=(222,222,222,255)
for i,(k,h,s) in enumerate(segs,1):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    for y in range(1050,H):
        a=int(165*((y-1050)/(H-1050))**1.3); d.line([(0,y),(W,y)],fill=(0,0,0,a))
    txt=Image.new('RGBA',(W,H),(0,0,0,0)); t=ImageDraw.Draw(txt)
    hs=88
    while F('Kanit-Bold.ttf',hs).getlength(h)>940: hs-=2
    lines=[]
    if k: lines.append((k,F('Kanit-Regular.ttf',42),GRAY,18))
    lines.append((h,F('Kanit-Bold.ttf',hs),WHITE,10))
    if s: lines.append((s,F('Kanit-Regular.ttf',50),GRAY,0))
    hts=[]; 
    for tx,f,c,g in lines:
        b=t.textbbox((0,0),tx,font=f); hts.append(b[3]-b[1])
    total=sum(hts)+sum(l[3] for l in lines)
    y=1560-total
    for (tx,f,c,g),hh in zip(lines,hts):
        b=t.textbbox((0,0),tx,font=f); x=(W-(b[2]-b[0]))//2-b[0]
        t.text((x,y-b[1]),tx,font=f,fill=c); y+=hh+g
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); sh.putalpha(txt.split()[3].point(lambda v:int(v*0.45)))
    sh=sh.filter(ImageFilter.GaussianBlur(6))
    im=Image.alpha_composite(im,sh); im=Image.alpha_composite(im,txt)
    im.paste(logo,((W-lw)//2,130),logo)
    im.save(f'ov{i}.png')
print('done')
