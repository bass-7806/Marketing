# Reusable flat-vector drawing parts for the survival-clip style (1080x1920 canvas).
# Every function returns an SVG string. Randomness is seeded so every build is identical.
import random

C = dict(
    sky1="#141a33", sky2="#2b3157", moon="#efe6c8", star="#c9cbe0",
    water="#1f3440", water2="#16262f", wave="#4b6b78", murk="#2c3d38",
    wall="#8f8778", wall_dk="#6f675b", floor="#5e4632", floor_dk="#4a3727", shadow="#3d342b",
    house="#7d735f", house_dk="#5f5748", roof="#5a2e2a", roof_dk="#45221f", win="#2a2f45", win_lit="#f2c46b",
    tree="#121a2a", red="#c9353a", warm="#f2c46b",
    cat="#e08a3c", cat_dk="#b8652a", cat_lt="#f3d3a6", cat_ear="#f3b38a", cat_eye="#d9e36a",
    skin="#e7c09b", hair="#222222", shirt="#3b5a7a", pants="#2b3b52",
)

def defs_common():
    return f'''<defs>
  <linearGradient id="g-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{C['sky1']}"/><stop offset="1" stop-color="{C['sky2']}"/></linearGradient>
  <linearGradient id="g-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{C['water']}"/><stop offset="1" stop-color="{C['water2']}"/></linearGradient>
  <radialGradient id="g-moon"><stop offset=".55" stop-color="{C['moon']}" stop-opacity=".55"/><stop offset="1" stop-color="{C['moon']}" stop-opacity="0"/></radialGradient>
  <radialGradient id="g-warm"><stop offset="0" stop-color="{C['warm']}" stop-opacity=".55"/><stop offset="1" stop-color="{C['warm']}" stop-opacity="0"/></radialGradient>
</defs>'''

def sky(h=1000, moon=(820, 260), stars=18, seed=1):
    r = random.Random(seed)
    s = f'<rect x="0" y="0" width="1080" height="{h}" fill="url(#g-sky)"/>'
    for _ in range(stars):
        s += f'<circle cx="{r.randint(20,1060)}" cy="{r.randint(20,int(h*.55))}" r="{r.choice([1.5,2,2.5])}" fill="{C["star"]}" opacity="{r.uniform(.3,.8):.2f}"/>'
    if moon:
        mx, my = moon
        s += f'<circle cx="{mx}" cy="{my}" r="150" fill="url(#g-moon)"/><circle cx="{mx}" cy="{my}" r="62" fill="{C["moon"]}"/>'
    return s

def treeline(y, seed=2):
    r = random.Random(seed); s = f'<rect x="0" y="{y}" width="1080" height="60" fill="{C["tree"]}"/>'
    x = -20
    while x < 1100:
        w = r.randint(50, 110); hh = r.randint(40, 120)
        s += f'<ellipse cx="{x+w/2}" cy="{y+5}" rx="{w/2}" ry="{hh/2}" fill="{C["tree"]}"/>'
        if r.random() < .25:  # palm
            s += f'<rect x="{x+w/2-3}" y="{y-hh-40}" width="6" height="{hh+40}" fill="{C["tree"]}"/><ellipse cx="{x+w/2}" cy="{y-hh-40}" rx="34" ry="12" fill="{C["tree"]}"/>'
        x += w - 20
    return s

def water(y, h=None, wid="wv", lines=6, seed=3):
    """Flood water from y down. Wave highlight group id=<wid> is wider than the frame so it can scroll."""
    h = h or 1920 - y
    r = random.Random(seed)
    s = f'<rect x="0" y="{y}" width="1080" height="{h}" fill="url(#g-water)"/>'
    s += f'<g id="{wid}">'
    for i in range(lines):
        yy = y + 30 + i * (h - 40) / max(lines, 1)
        for k in range(-2, 9):
            x = k * 180 + r.randint(0, 60)
            s += f'<path d="M{x} {yy:.0f} q22 -9 44 0 t44 0" fill="none" stroke="{C["wave"]}" stroke-width="{4 - i*0.3:.1f}" stroke-linecap="round" opacity="{.55 - i*.05:.2f}"/>'
    s += '</g>'
    s += f'<rect x="0" y="{y-3}" width="1080" height="6" fill="{C["wave"]}" opacity=".6"/>'
    return s

def rain(wid="rain", n=70, seed=4, opacity=.35):
    """Two stacked copies (0..1920 and -1920..0) so the group can scroll down by 1920 seamlessly."""
    r = random.Random(seed); drops = ""
    for _ in range(n):
        x = r.randint(0, 1080); y = r.randint(0, 1920); l = r.randint(30, 60)
        drops += f'<line x1="{x}" y1="{y}" x2="{x-8}" y2="{y+l}" stroke="#aab4d4" stroke-width="2.5" stroke-linecap="round"/>'
    return f'<g id="{wid}" opacity="{opacity}"><g>{drops}</g><g transform="translate(0 -1920)">{drops}</g></g>'

def house(x, base, w, h, roof_h=150, floors=2, lit=(), seed=5, color=None):
    """A two-storey Thai row-house. base = y of ground (usually hidden under water)."""
    col = color or C["house"]; top = base - h
    s = f'<rect x="{x}" y="{top}" width="{w}" height="{h}" fill="{col}"/>'
    s += f'<rect x="{x+w*0.62}" y="{top}" width="{w*0.38}" height="{h}" fill="{C["house_dk"]}" opacity=".35"/>'
    s += f'<polygon points="{x-20},{top} {x+w/2},{top-roof_h} {x+w+20},{top}" fill="{C["roof"]}"/>'
    s += f'<polygon points="{x+w/2},{top-roof_h} {x+w+20},{top} {x+w/2},{top}" fill="{C["roof_dk"]}" opacity=".5"/>'
    fh = h / floors
    for f in range(floors):
        for i in range(2):
            wx = x + w * (0.16 + i * 0.46); wy = top + f * fh + fh * 0.22; ww = w * 0.26; wh = fh * 0.5
            fill = C["win_lit"] if (f, i) in lit else C["win"]
            s += f'<rect x="{wx:.0f}" y="{wy:.0f}" width="{ww:.0f}" height="{wh:.0f}" fill="{fill}"/>'
            s += f'<rect x="{wx+ww/2-2:.0f}" y="{wy:.0f}" width="4" height="{wh:.0f}" fill="{C["house_dk"]}"/>'
        s += f'<rect x="{x}" y="{top + (f+1)*fh - 6:.0f}" width="{w}" height="10" fill="{C["house_dk"]}"/>'
    return s

def cat(x, y, s=1.0, face="right", tail_id=None, ear_id=None, eye_id=None, puff=False):
    """Sitting orange cat. (x,y) = bottom centre. face: right | left | back."""
    flip = -1 if face == "left" else 1
    t_id = f' id="{tail_id}"' if tail_id else ""
    e_id = f' id="{ear_id}"' if ear_id else ""
    y_id = f' id="{eye_id}"' if eye_id else ""
    fur = 1.12 if puff else 1.0
    g = f'<g transform="translate({x} {y}) scale({s*flip} {s})">'
    g += f'<g{t_id}><path d="M-40 -20 C-120 -20 -130 -90 -95 -150" fill="none" stroke="{C["cat"]}" stroke-width="{20*fur:.0f}" stroke-linecap="round"/>'
    g += f'<path d="M-112 -100 l18 -6 M-118 -70 l20 -2" stroke="{C["cat_dk"]}" stroke-width="6" stroke-linecap="round"/></g>'
    g += f'<ellipse cx="0" cy="-75" rx="{58*fur:.0f}" ry="{76*fur:.0f}" fill="{C["cat"]}"/>'
    g += f'<path d="M-50 -110 q14 6 22 -6 M-56 -78 q16 6 26 -6 M-52 -46 q14 6 24 -6" fill="none" stroke="{C["cat_dk"]}" stroke-width="7" stroke-linecap="round"/>'
    if face != "back":
        g += f'<ellipse cx="30" cy="-82" rx="26" ry="46" fill="{C["cat_lt"]}"/>'
    g += f'<rect x="10" y="-36" width="18" height="36" rx="8" fill="{C["cat"]}"/><rect x="36" y="-36" width="18" height="36" rx="8" fill="{C["cat"]}"/>'
    hx = 32 if face != "back" else 4
    g += f'<g{e_id}>'
    g += f'<polygon points="{hx-36},-176 {hx-28},-236 {hx-2},-196" fill="{C["cat"]}"/><polygon points="{hx-30},-186 {hx-26},-222 {hx-10},-198" fill="{C["cat_ear"]}"/>'
    g += f'<polygon points="{hx+36},-176 {hx+28},-236 {hx+2},-196" fill="{C["cat"]}"/><polygon points="{hx+30},-186 {hx+26},-222 {hx+10},-198" fill="{C["cat_ear"]}"/></g>'
    g += f'<circle cx="{hx}" cy="-160" r="{48*fur:.0f}" fill="{C["cat"]}"/>'
    g += f'<path d="M{hx-14} -206 l4 18 M{hx} -208 l0 18 M{hx+14} -206 l-4 18" stroke="{C["cat_dk"]}" stroke-width="5" stroke-linecap="round"/>'
    if face != "back":
        g += f'<g{y_id}><ellipse cx="{hx-17}" cy="-162" rx="9" ry="11" fill="{C["cat_eye"]}"/><ellipse cx="{hx+17}" cy="-162" rx="9" ry="11" fill="{C["cat_eye"]}"/>'
        g += f'<ellipse cx="{hx-15}" cy="-162" rx="3.5" ry="9" fill="#111"/><ellipse cx="{hx+19}" cy="-162" rx="3.5" ry="9" fill="#111"/></g>'
        g += f'<path d="M{hx-5} -146 l5 6 l5 -6 z" fill="#d9776f"/>'
        g += f'<path d="M{hx-30} -144 l-26 -4 M{hx-30} -138 l-26 4 M{hx+30} -144 l26 -4 M{hx+30} -138 l26 4" stroke="#f5ead8" stroke-width="2" opacity=".7"/>'
    return g + '</g>'

def person_sitting(x, y, s=1.0, face="right"):
    """Person sitting on the floor hugging their knees. (x,y)=floor contact."""
    flip = -1 if face == "left" else 1
    g = f'<g transform="translate({x} {y}) scale({s*flip} {s})">'
    g += f'<ellipse cx="0" cy="0" rx="120" ry="14" fill="#000" opacity=".25"/>'
    g += f'<rect x="-70" y="-210" width="90" height="200" rx="40" fill="{C["shirt"]}"/>'
    g += f'<path d="M-40 -20 L70 -20 L70 -150 L30 -150 Z" fill="{C["pants"]}"/>'
    g += f'<rect x="58" y="-150" width="30" height="150" rx="12" fill="{C["pants"]}"/>'
    g += f'<path d="M-10 -170 Q60 -170 80 -120" fill="none" stroke="{C["shirt"]}" stroke-width="28" stroke-linecap="round"/>'
    g += f'<circle cx="82" cy="-118" r="14" fill="{C["skin"]}"/>'
    g += f'<circle cx="-20" cy="-262" r="56" fill="{C["skin"]}"/>'
    g += f'<path d="M-78 -270 Q-70 -330 -20 -322 Q40 -330 40 -268 Q20 -300 -20 -296 Q-60 -300 -78 -270 Z" fill="{C["hair"]}"/>'
    g += f'<circle cx="2" cy="-262" r="5" fill="#222"/><circle cx="22" cy="-262" r="5" fill="#222"/>'
    g += f'<path d="M6 -236 q8 -3 14 0" stroke="#8a5a44" stroke-width="3" fill="none" stroke-linecap="round"/>'
    return g + '</g>'

def door(x, y, w, h, gap_id=None, sign=True):
    """Bathroom door, slightly ajar: a dark gap on its right edge."""
    gid = f' id="{gap_id}"' if gap_id else ""
    s = f'<rect x="{x-24}" y="{y-24}" width="{w+48}" height="{h+24}" fill="{C["shadow"]}"/>'
    s += f'<rect{gid} x="{x+w-18}" y="{y}" width="18" height="{h}" fill="#05070b"/>'
    s += f'<rect x="{x}" y="{y}" width="{w-18}" height="{h}" fill="#a98f6c"/>'
    s += f'<rect x="{x+30}" y="{y+40}" width="{w-78}" height="{h*0.38:.0f}" fill="#9a8160"/><rect x="{x+30}" y="{y+h*0.5:.0f}" width="{w-78}" height="{h*0.4:.0f}" fill="#9a8160"/>'
    s += f'<circle cx="{x+w-48}" cy="{y+h*0.52:.0f}" r="11" fill="#d8c08a"/>'
    if sign:
        sx, sy = x + w/2 - 9 - 45, y + 70
        s += f'<rect x="{sx}" y="{sy}" width="90" height="90" rx="10" fill="#e9e2d2"/>'
        s += f'<circle cx="{sx+45}" cy="{sy+28}" r="10" fill="#4a5a70"/><path d="M{sx+30} {sy+42} h30 l-6 34 h-18 z" fill="#4a5a70"/>'
    return s

def toilet_front(x, y, s=1.0):
    """Toilet seen from the front at a slight top angle; bowl water ellipse id=toilet-water."""
    g = f'<g transform="translate({x} {y}) scale({s})">'
    g += f'<rect x="-150" y="-430" width="300" height="190" rx="18" fill="#e6e3dc"/><rect x="-150" y="-260" width="300" height="20" fill="#cfcac0"/>'
    g += f'<path d="M-200 -240 h400 q0 170 -120 220 l20 120 h-200 l20 -120 q-120 -50 -120 -220 z" fill="#efece6"/>'
    g += f'<ellipse cx="0" cy="-240" rx="200" ry="60" fill="#d9d4ca"/><ellipse cx="0" cy="-238" rx="160" ry="44" fill="#c8c2b6"/>'
    g += f'<ellipse id="toilet-water" cx="0" cy="-232" rx="128" ry="32" fill="#1c2b33"/>'
    return g + '</g>'

def ripple(cx, cy, rx, ry, rid, color=None, width=4):
    return f'<ellipse id="{rid}" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{color or C["wave"]}" stroke-width="{width}" opacity="0"/>'

def croc(x, y, s=1.0, cid="croc"):
    """Crocodile seen from the side, mostly under water: dark body + eyes/snout bumps."""
    g = f'<g id="{cid}" transform="translate({x} {y}) scale({s})">'
    g += f'<path d="M-260 30 Q-120 70 60 40 L210 20 Q240 15 230 40 L60 70 Q-120 110 -300 80 Q-380 70 -440 110 Q-360 40 -260 30 Z" fill="#0d1a1c" opacity=".75"/>'
    g += f'<ellipse cx="120" cy="2" rx="22" ry="12" fill="#2f3b2c"/><ellipse cx="212" cy="8" rx="14" ry="8" fill="#2f3b2c"/>'
    g += f'<circle cx="124" cy="-2" r="4" fill="#e8c35a"/>'
    return g + '</g>'

def flashlight_floor(x, y, angle=-15):
    g = f'<g transform="translate({x} {y}) rotate({angle})"><polygon points="40,0 600,-160 600,160" fill="url(#g-warm)" opacity=".7"/>'
    g += f'<rect x="-60" y="-16" width="100" height="32" rx="8" fill="#30343c"/><rect x="30" y="-22" width="22" height="44" rx="6" fill="#444a55"/></g>'
    return g

def candle(x, y, fid="flame"):
    g = f'<circle cx="{x}" cy="{y-90}" r="260" fill="url(#g-warm)" opacity=".8"/>'
    g += f'<rect x="{x-16}" y="{y-80}" width="32" height="80" rx="4" fill="#efe6d0"/>'
    g += f'<ellipse id="{fid}" cx="{x}" cy="{y-100}" rx="10" ry="22" fill="#ffd27a"/>'
    return g
