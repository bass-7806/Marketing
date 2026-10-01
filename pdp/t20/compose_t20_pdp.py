#!/usr/bin/env python3
"""Compose Bwell Robot Ultra T20 PDP images (layout reference: L6C PDP set).

Takes the 6 clean AI scenes (s1..s6.png, 2048x2048, no text) and lays headline,
sub-copy and spec chips on top in DB Helvethaica X.

Outputs per slide:
  out/web/T20_PDP_0N.jpg   2048x2048  (bwell.co.th PDP)
  out/mkp/T20_PDP_0N.jpg   1000x1000  (Shopee / Lazada / TikTok Shop)

Spec source: T20_Ultra_Product_Profile.md (Drive). Suction (Pa) and noise (dB)
are marked UNVERIFIED in the profile and are intentionally not used.

Usage: python3 compose_t20_pdp.py <scenes_dir> <fonts_dir> <out_dir>
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

NAVY = (0, 93, 157)        # #005D9D Bwell primary
INK = (22, 32, 44)
WHITE = (255, 255, 255)
SIZE = 2048
MARGIN = 120

SLIDES = [
    {
        "key": "01_hero",
        "eyebrow": "Bwell Robot Ultra T20",
        "headline": "หุ่นยนต์ดูดฝุ่นถูพื้น All-in-One",
        "sub": "ไม่ต้องทำเองอีกต่อไป Station ดูแลให้ครบ 4 ขั้นตอนอัตโนมัติ",
        "chips": ["Auto-Empty", "Auto-Fill", "Auto-Clean Mop", "Auto-Dry"],
        "layout": "top", "theme": "light",
    },
    {
        "key": "02_lidar",
        "eyebrow": "LiDAR Navigation",
        "headline": "LiDAR สร้างแผนที่บ้านอัจฉริยะ",
        "sub": "วางแผนเส้นทางเป็นระเบียบ กำหนด No-Go Zone กันมุมที่ไม่ต้องการได้",
        "chips": ["LiDAR (LDS)", "No-Go Zones", "Zone-based Routing"],
        "layout": "top", "theme": "light",
    },
    {
        "key": "03_battery",
        "eyebrow": "Long-lasting Battery",
        "headline": "ทำงานต่อเนื่องนานกว่า 200 นาที*",
        "sub": "แบตเตอรี่ Lithium-ion 5,200 mAh แบตหมดกลับไปชาร์จแล้วทำงานต่อจากจุดเดิม",
        "chips": ["5,200 mAh", "Resume After Charge", "ชาร์จ < 7 ชม."],
        "footnote": "*Quiet Mode อ้างอิงคู่มือ Bwell",
        "layout": "top", "theme": "light",
    },
    {
        "key": "04_station",
        "eyebrow": "All-In-One Station",
        "headline": "4-in-1 Station\nจบทุกงานหลังทำความสะอาด",
        "sub": None,
        "specs": [
            ("ถุงเก็บฝุ่น 2.8 L", "ดูดฝุ่นออกจากหุ่นยนต์อัตโนมัติ"),
            ("ถังน้ำสะอาด 5.0 L", "เติมน้ำให้หุ่นยนต์อัตโนมัติ"),
            ("ถังน้ำเสีย 4.2 L", "ล้างผ้าถูด้วยแปรงหมุนอัตโนมัติ"),
            ("Auto-Dry", "เป่าลมอบแห้งผ้าถู ลดกลิ่นอับ"),
        ],
        "layout": "left", "theme": "light",
    },
    {
        "key": "05_app",
        "eyebrow": "Smart Life App",
        "headline": "สั่งงานได้ทุกที่ผ่านแอป",
        "sub": "ดูแผนที่ เลือกห้อง ตั้งเวลา ปรับแรงดูดและปริมาณน้ำ",
        "chips": ["Room Selection", "Scheduling", "OTA Update"],
        "layout": "top", "theme": "dark",
    },
    {
        "key": "06_carpet",
        "eyebrow": "Auto Carpet Lift",
        "headline": "เจอพรม ยกผ้าถูอัตโนมัติ",
        "sub": "ตรวจจับพรมด้วยเซ็นเซอร์ พรมไม่เปียก พร้อมเซ็นเซอร์กันตกและกันชน",
        "chips": ["Ultrasonic Sensor", "Cliff Sensors", "Wall Sensor"],
        "layout": "top", "theme": "light",
    },
]


def fonts(fdir):
    f = lambda name, s: ImageFont.truetype(os.path.join(fdir, name), s)
    return {
        "eyebrow": f("DBHX-Med.ttf", 64),
        "headline": f("DBHX-Bold.ttf", 150),
        "sub": f("DBHX-Med.ttf", 76),
        "chip": f("DBHX-Med.ttf", 58),
        "spec_t": f("DBHX-Bold.ttf", 86),
        "spec_d": f("DBHX-Reg.ttf", 64),
        "foot": f("DBHX-Reg.ttf", 44),
        "tag": f("DBHX-Med.ttf", 52),
    }


def scrim(img, box, color, max_alpha, direction):
    """Soft gradient panel so copy stays legible over the photo."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    grad = Image.new("L", (w, h))
    px = grad.load()
    for i in range(w if direction == "x" else h):
        t = 1 - i / (w if direction == "x" else h)
        a = int(max_alpha * min(1.0, t * 1.35) ** 1.4)
        if direction == "x":
            for y in range(h):
                px[i, y] = a
        else:
            for x in range(w):
                px[x, i] = a
    layer = Image.new("RGBA", (w, h), color + (0,))
    layer.putalpha(grad)
    img.alpha_composite(layer, (x0, y0))


def wrap(draw, text, font, width):
    lines = []
    for para in text.split("\n"):
        cur = ""
        for word in para.split(" "):
            test = (cur + " " + word).strip()
            if draw.textlength(test, font=font) <= width or not cur:
                cur = test
            else:
                lines.append(cur)
                cur = word
        lines.append(cur)
    return lines


def chips(draw, items, F, x, y, fg, bg, border, max_w):
    pad_x, h, gap = 34, 92, 20
    cx, cy = x, y
    for it in items:
        w = int(draw.textlength(it, font=F["chip"])) + pad_x * 2
        if cx + w > x + max_w:
            cx, cy = x, cy + h + gap
        draw.rounded_rectangle((cx, cy, cx + w, cy + h), radius=h // 2, fill=bg, outline=border, width=3)
        draw.text((cx + w / 2, cy + h / 2 + 4), it, font=F["chip"], fill=fg, anchor="mm")
        cx += w + gap
    return cy + h


def compose(slide, scene, F):
    img = Image.open(scene).convert("RGBA").resize((SIZE, SIZE), Image.LANCZOS)
    dark = slide["theme"] == "dark"
    head_c = WHITE if dark else NAVY
    body_c = WHITE if dark else INK
    panel = (18, 40, 70) if dark else (255, 255, 255)

    if slide["layout"] == "top":
        scrim(img, (0, 0, SIZE, 900), panel, 205 if dark else 215, "y")
        text_w = SIZE - MARGIN * 2
        x = MARGIN
    else:
        scrim(img, (0, 0, 1180, SIZE), panel, 235, "x")
        text_w = 900
        x = MARGIN

    d = ImageDraw.Draw(img)
    y = 110
    d.text((x, y), slide["eyebrow"].upper(), font=F["eyebrow"], fill=head_c)
    d.rectangle((x, y + 84, x + 96, y + 92), fill=head_c)
    y += 130

    for line in wrap(d, slide["headline"], F["headline"], text_w):
        d.text((x, y), line, font=F["headline"], fill=head_c)
        y += 158
    y += 12

    if slide.get("sub"):
        for line in wrap(d, slide["sub"], F["sub"], text_w):
            d.text((x, y), line, font=F["sub"], fill=body_c)
            y += 92
        y += 26

    if slide.get("chips"):
        fg, bg, br = WHITE, NAVY, (WHITE if dark else NAVY)
        chips(d, slide["chips"], F, x, y, fg, bg, br, text_w)

    if slide.get("specs"):
        y += 40
        for title, desc in slide["specs"]:
            d.rectangle((x, y + 14, x + 12, y + 150), fill=NAVY)
            d.text((x + 44, y), title, font=F["spec_t"], fill=NAVY)
            d.text((x + 44, y + 96), desc, font=F["spec_d"], fill=INK)
            y += 210

    if slide.get("footnote"):
        d.text((MARGIN, SIZE - 90), slide["footnote"], font=F["foot"],
               fill=(255, 255, 255, 235) if dark else (40, 40, 40, 235))

    return img.convert("RGB")


def main():
    scenes, fdir, out = sys.argv[1:4]
    F = fonts(fdir)
    os.makedirs(os.path.join(out, "web"), exist_ok=True)
    os.makedirs(os.path.join(out, "mkp"), exist_ok=True)
    for i, s in enumerate(SLIDES, 1):
        im = compose(s, os.path.join(scenes, f"s{i}.png"), F)
        name = f"T20_PDP_{s['key']}.jpg"
        im.save(os.path.join(out, "web", name), quality=92)
        im.resize((1000, 1000), Image.LANCZOS).save(os.path.join(out, "mkp", name), quality=90)
        print("ok", name)


if __name__ == "__main__":
    main()
