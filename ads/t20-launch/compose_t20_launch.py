#!/usr/bin/env python3
"""Compose Bwell Robot Ultra T20 New Launch online ads (hero, no price).

Inputs (AI scenes, no text): hero_1x1.png, hero_4x5.png, hero_9x16.png, hero_16x9.png
Outputs (JPG):
  T20_Launch_Feed_1x1.jpg        2048x2048  FB/IG feed, marketplace square
  T20_Launch_Feed_4x5.jpg        1638x2048  FB/IG feed portrait
  T20_Launch_Story_9x16.jpg      1152x2048  Story / Reels / TikTok
  T20_Launch_Web_16x9.jpg        2048x1152  bwell.co.th hero, FB cover
  T20_Launch_Marketplace_2x1.jpg 2048x1024  Shopee / Lazada shop banner (confirm platform spec)

Usage: python3 compose_t20_launch.py <scenes_dir> <fonts_dir> <out_dir>
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

NAVY = (0, 93, 157)       # #005D9D
DEEP = (4, 22, 44)
WHITE = (255, 255, 255)
SOFT = (200, 222, 240)

COPY = {
    "tag": "NEW LAUNCH",
    "product": "Bwell Robot Ultra T20",
    "headline": "บ้านสะอาด โดยไม่ต้องลงมือ",
    "sub": "All-In-One Station ดูด ถู ล้าง อบแห้ง จบในเครื่องเดียว",
    "cta": "ดูรายละเอียดเพิ่มเติม",
    "url": "www.bwell.co.th",
}

FORMATS = [
    # name, scene, size, layout
    ("T20_Launch_Feed_1x1", "hero_1x1.png", (2048, 2048), "top"),
    ("T20_Launch_Feed_4x5", "hero_4x5.png", (1638, 2048), "top"),
    ("T20_Launch_Story_9x16", "hero_9x16.png", (1152, 2048), "story"),
    ("T20_Launch_Web_16x9", "hero_16x9.png", (2048, 1152), "left"),
    ("T20_Launch_Marketplace_2x1", "hero_16x9.png", (2048, 1024), "left"),
]


def font(fdir, name, size):
    return ImageFont.truetype(os.path.join(fdir, name), size)


def cover(img, size):
    """Scale to fill, crop centre (bias right for wide banners keeps product in frame)."""
    tw, th = size
    s = max(tw / img.width, th / img.height)
    im = img.resize((round(img.width * s), round(img.height * s)), Image.LANCZOS)
    x = (im.width - tw) // 2
    y = (im.height - th) // 2
    return im.crop((x, y, x + tw, y + th))


def vscrim(img, y0, y1, alpha, top_dark=True):
    w = img.width
    h = y1 - y0
    grad = Image.linear_gradient("L").resize((w, h))
    if top_dark:
        grad = grad.point(lambda v: int(alpha * (1 - v / 255)))
    else:
        grad = grad.point(lambda v: int(alpha * v / 255))
    layer = Image.new("RGBA", (w, h), DEEP + (0,))
    layer.putalpha(grad)
    img.alpha_composite(layer, (0, y0))


def hscrim(img, x1, alpha):
    h = img.height
    grad = Image.linear_gradient("L").rotate(90, expand=True).resize((x1, h))
    grad = grad.point(lambda v: int(alpha * (1 - v / 255) ** 0.8))
    layer = Image.new("RGBA", (x1, h), DEEP + (0,))
    layer.putalpha(grad)
    img.alpha_composite(layer, (0, 0))


def pill(d, xy, text, f, fill, fg, outline=None, anchor_center=False, pad=(40, 0), h=None):
    tw = d.textlength(text, font=f)
    h = h or int(f.size * 1.5)
    w = int(tw + pad[0] * 2)
    x, y = xy
    if anchor_center:
        x = x - w // 2
    d.rounded_rectangle((x, y, x + w, y + h), radius=h // 2, fill=fill, outline=outline, width=3)
    d.text((x + w / 2, y + h / 2 + f.size * 0.06), text, font=f, fill=fg, anchor="mm")
    return x, y, w, h


def fit(d, text, fdir, name, size, max_w):
    while size > 20:
        f = font(fdir, name, size)
        if d.textlength(text, font=f) <= max_w:
            return f
        size -= 4
    return font(fdir, name, size)


def compose(scene, size, layout, fdir):
    img = cover(Image.open(scene).convert("RGBA"), size).convert("RGBA")
    W, H = size
    u = min(W, H) / 1000  # scale unit
    if layout == "story":
        u *= 1.3
    d = ImageDraw.Draw(img)

    if layout in ("top", "story"):
        vscrim(img, 0, int(H * (0.48 if layout == "top" else 0.42)), 190)
        if layout == "story":
            vscrim(img, int(H * 0.72), H, 200, top_dark=False)
        d = ImageDraw.Draw(img)
        cx = W // 2
        max_w = W - int(120 * u)
        y = int((70 if layout == "top" else 150) * u)
        f_tag = font(fdir, "DBHX-Bold.ttf", int(34 * u))
        _, _, _, h = pill(d, (cx, y), COPY["tag"], f_tag, NAVY, WHITE, outline=WHITE, anchor_center=True)
        y += h + int(26 * u)
        f_prod = fit(d, COPY["product"], fdir, "DBHX-Med.ttf", int(52 * u), max_w)
        d.text((cx, y), COPY["product"], font=f_prod, fill=SOFT, anchor="ma")
        y += int(f_prod.size * 1.15)
        f_head = fit(d, COPY["headline"], fdir, "DBHX-Bold.ttf", int(104 * u), max_w)
        d.text((cx, y), COPY["headline"], font=f_head, fill=WHITE, anchor="ma")
        y += int(f_head.size * 1.12)
        f_sub = fit(d, COPY["sub"], fdir, "DBHX-Reg.ttf", int(46 * u), max_w)
        d.text((cx, y), COPY["sub"], font=f_sub, fill=SOFT, anchor="ma")
        f_cta = font(fdir, "DBHX-Bold.ttf", int(38 * u))
        f_url = font(fdir, "DBHX-Med.ttf", int(28 * u))
        if layout == "story":
            cy = int(H * 0.80)
        else:
            cy = H - int(150 * u)
        _, _, _, h = pill(d, (cx, cy), COPY["cta"], f_cta, WHITE, NAVY, anchor_center=True, pad=(int(48 * u), 0))
        d.text((cx, cy + h + int(16 * u)), COPY["url"], font=f_url, fill=SOFT, anchor="ma")
    else:
        hscrim(img, int(W * 0.62), 235)
        d = ImageDraw.Draw(img)
        x = int(W * 0.06)
        max_w = int(W * 0.46)
        uh = H / 1000
        y = int(H * 0.16)
        f_tag = font(fdir, "DBHX-Bold.ttf", int(46 * uh))
        _, _, _, h = pill(d, (x, y), COPY["tag"], f_tag, NAVY, WHITE, outline=WHITE)
        y += h + int(34 * uh)
        f_prod = fit(d, COPY["product"], fdir, "DBHX-Med.ttf", int(64 * uh), max_w)
        d.text((x, y), COPY["product"], font=f_prod, fill=SOFT)
        y += int(f_prod.size * 1.2)
        f_head = fit(d, COPY["headline"], fdir, "DBHX-Bold.ttf", int(130 * uh), max_w)
        d.text((x, y), COPY["headline"], font=f_head, fill=WHITE)
        y += int(f_head.size * 1.15)
        f_sub = fit(d, COPY["sub"], fdir, "DBHX-Reg.ttf", int(54 * uh), max_w)
        d.text((x, y), COPY["sub"], font=f_sub, fill=SOFT)
        y += int(f_sub.size * 1.3) + int(50 * uh)
        f_cta = font(fdir, "DBHX-Bold.ttf", int(46 * uh))
        _, _, w, h = pill(d, (x, y), COPY["cta"], f_cta, WHITE, NAVY, pad=(int(56 * uh), 0))
        f_url = font(fdir, "DBHX-Med.ttf", int(38 * uh))
        d.text((x + w + int(36 * uh), y + h / 2), COPY["url"], font=f_url, fill=SOFT, anchor="lm")
    return img.convert("RGB")


def main():
    scenes, fdir, out = sys.argv[1:4]
    os.makedirs(out, exist_ok=True)
    for name, scene, size, layout in FORMATS:
        compose(os.path.join(scenes, scene), size, layout, fdir).save(
            os.path.join(out, name + ".jpg"), quality=92)
        print("ok", name)


if __name__ == "__main__":
    main()
