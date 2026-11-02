# Flood village EP1 — shot list. Times come from the narration alignment (see captions.json).
# Run:  python3 <skill>/scripts/build.py shots.py <video_dir> <captions.json>
from framework import *

# ---------------- shots ----------------
# 1 — flooded village at night, cat in the upstairs window
svg = sky(980) + treeline(900) + house(-60, 1180, 330, 420, roof_h=120, color="#6f6656") + house(800, 1170, 340, 400, roof_h=110, color="#6f6656")
svg += house(270, 1240, 540, 620, roof_h=170, lit={(0, 0)})
svg += cat(400, 820, 0.55, face="right", tail_id="s01-tail")  # sits in the lit upstairs window
svg += water(1010, wid="s01-wv") + f'<ellipse cx="820" cy="1150" rx="70" ry="10" fill="{C["moon"]}" opacity=".35"/>'
svg += '<g id="s01-debris"><rect x="120" y="1260" width="90" height="16" rx="6" fill="#b23b3b"/><rect x="130" y="1220" width="12" height="44" fill="#b23b3b"/><rect x="190" y="1220" width="12" height="44" fill="#b23b3b"/></g>'
svg += rain("s01-rain")
js = js_scroll("#s01-wv", dx=-180, period=4.5, dur=7.5) + js_scroll("#s01-rain", dy=1920, period=1.6, dur=7.5)
js += 'tl.fromTo("#s01-debris",{x:0},{x:260,duration:D,ease:"none"},0);\n'
js += 'tl.fromTo("#s01-tail",{rotation:0},{rotation:-14,transformOrigin:"100% 100%",duration:.9,ease:"sine.inOut",yoyo:true,repeat:7},0);\n'
scene("s01", 0.0, 7.5, svg, js=js, origin="40% 42%", push=1.16)

# 2 — legs in moving water, 15 cm card
svg = f'<rect x="0" y="0" width="1080" height="1100" fill="#3a3a44"/><rect x="0" y="0" width="1080" height="1100" fill="url(#g-sky)" opacity=".6"/>'
svg += f'<g id="s02-legs"><rect x="430" y="700" width="90" height="760" rx="30" fill="{C["pants"]}"/><rect x="560" y="700" width="90" height="760" rx="30" fill="{C["pants"]}"/></g>'
svg += water(1180, wid="s02-wv", lines=8)
svg += '<g id="s02-flow">' + "".join(f'<path d="M{x} {y} l50 22 l-50 22" fill="none" stroke="#cfe0e8" stroke-width="7" stroke-linecap="round" opacity=".55"/>' for x in range(-200, 1300, 230) for y in (1260, 1420, 1580)) + '</g>'
svg += f'<g><rect x="150" y="1060" width="56" height="300" fill="#e8d9a8"/>' + "".join(f'<rect x="150" y="{1060+i*30}" width="{28 if i%5 else 46}" height="5" fill="#3a352e"/>' for i in range(10)) + f'<rect x="140" y="1176" width="80" height="8" fill="{C["red"]}"/></g>'
overlay = f'<div class="card" id="s02-card"><div class="t">น้ำไหลสูงแค่</div><div class="n" id="s02-n">15<small>ซม.</small></div><div class="t">ก็พัดผู้ใหญ่ล้มได้</div>{danger_bar(4)}</div>'
js = js_scroll("#s02-wv", dx=-180, period=1.4, dur=6.1) + js_scroll("#s02-flow", dx=230, period=0.9, dur=6.1)
js += js_card("#s02-card", 2.3, "#s02-n", 15)
js += 'tl.fromTo("#s02-legs",{rotation:0},{rotation:-5,transformOrigin:"50% 100%",duration:.5,ease:"power2.inOut",yoyo:true,repeat:5},3.6);\n'
scene("s02", 7.5, 6.1, svg, overlay, js, origin="50% 70%")

# 3 — dark water close-up, something passes under
svg = f'<rect x="0" y="0" width="1080" height="1920" fill="{C["water2"]}"/>' + water(0, h=1920, wid="s03-wv", lines=14)
svg += f'<g id="s03-shadow" opacity="0"><ellipse cx="0" cy="980" rx="420" ry="70" fill="#060b0e"/><ellipse cx="-330" cy="990" rx="160" ry="34" fill="#060b0e"/></g>'
svg += "".join(ripple(560, 960, 160, 46, f"s03-r{i}", width=5) for i in range(3))
js = js_scroll("#s03-wv", dx=-180, period=3.0, dur=2.8)
js += 'tl.fromTo("#s03-shadow",{x:-500,opacity:0},{x:1500,opacity:.85,duration:2.6,ease:"none"},0.1);\n' + js_ripples(["s03-r0", "s03-r1", "s03-r2"], 0.9)
scene("s03", 13.6, 2.8, svg, js=js, push=1.04)

# 4 — upstairs: you and Somo, stairs swallowed by water
svg = f'<rect x="0" y="0" width="1080" height="1180" fill="{C["wall"]}"/><rect x="0" y="1180" width="1080" height="740" fill="{C["floor"]}"/>'
svg += f'<rect x="120" y="260" width="300" height="380" fill="{C["sky1"]}"/><circle cx="330" cy="360" r="40" fill="{C["moon"]}"/>' + f'<rect x="262" y="260" width="10" height="380" fill="{C["wall_dk"]}"/><rect x="110" y="250" width="320" height="400" fill="none" stroke="{C["wall_dk"]}" stroke-width="20"/>'
svg += "".join(f'<rect x="0" y="{1180+i*90}" width="1080" height="4" fill="{C["floor_dk"]}"/>' for i in range(9))
svg += f'<path d="M640 1300 h400 v620 h-400 z" fill="{C["shadow"]}"/>' + "".join(f'<rect x="{660+i*20}" y="{1320+i*70}" width="360" height="22" fill="{C["floor_dk"]}"/>' for i in range(3))
svg += f'<clipPath id="s04-clip"><rect x="640" y="1300" width="400" height="620"/></clipPath><g clip-path="url(#s04-clip)">{water(1520, h=400, wid="s04-wv", lines=3)}</g>'
svg += flashlight_floor(560, 1650, -170)
svg += person_sitting(260, 1580, 1.25) + cat(560, 1600, 0.9, face="right", tail_id="s04-tail")
js = js_scroll("#s04-wv", dx=-180, period=4, dur=4.5) + 'tl.fromTo("#s04-tail",{rotation:0},{rotation:-16,transformOrigin:"100% 100%",duration:.7,ease:"sine.inOut",yoyo:true,repeat:5},0);\n'
scene("s04", 16.4, 4.5, svg, js=js, origin="45% 70%")

# 5 — the bathroom door, Somo sits facing away from it (the planted clue)
svg = f'<rect x="0" y="0" width="1080" height="1920" fill="{C["wall_dk"]}"/><rect x="0" y="1300" width="1080" height="620" fill="{C["floor"]}"/>'
svg += door(350, 420, 380, 880, gap_id="s05-gap")
svg += cat(250, 1700, 1.1, face="left", tail_id="s05-tail")
svg += f'<rect x="0" y="0" width="1080" height="1920" fill="#000" opacity=".18"/>'
js = 'tl.fromTo("#s05-gap",{scaleX:1,x:0},{scaleX:2.2,x:-20,duration:2.4,ease:"sine.inOut"},0.4);\n' + 'tl.fromTo("#s05-tail",{rotation:0},{rotation:-10,transformOrigin:"100% 100%",duration:.8,ease:"sine.inOut",yoyo:true,repeat:3},0);\n'
scene("s05", 20.9, 3.1, svg, js=js, origin="50% 45%")

# 6 — breaker panel, a hand pulls the main switch, the house goes dark
svg = f'<rect x="0" y="0" width="1080" height="1920" fill="{C["wall"]}"/>'
svg += f'<rect x="270" y="760" width="540" height="520" rx="18" fill="#c9c6bc"/><rect x="300" y="790" width="480" height="460" rx="10" fill="#4a4e57"/>'
svg += "".join(f'<rect x="{330+i*80}" y="1020" width="56" height="180" rx="8" fill="#e8e6e0"/><rect x="{344+i*80}" y="1040" width="28" height="60" rx="4" fill="#55595f"/>' for i in range(5))
svg += f'<rect x="460" y="830" width="160" height="150" rx="10" fill="#e8e6e0"/><g id="s06-lever"><rect x="510" y="840" width="60" height="70" rx="8" fill="{C["red"]}"/></g>'
svg += f'<g id="s06-hand"><path d="M1100 870 L640 870 Q600 870 600 900 Q600 930 640 930 L1100 960 Z" fill="{C["skin"]}"/><rect x="900" y="840" width="200" height="140" fill="{C["shirt"]}"/></g>'
svg += f'<rect x="460" y="1560" width="120" height="90" rx="12" fill="#e8e6e0"/><circle cx="500" cy="1605" r="9" fill="#555"/><circle cx="540" cy="1605" r="9" fill="#555"/>'
svg += water(1720, h=200, wid="s06-wv", lines=2)
svg += f'<rect id="s06-dark" x="0" y="0" width="1080" height="1920" fill="#05070d" opacity="0"/>'
overlay = f'<div class="card" id="s06-card"><div class="t">ไฟแค่</div><div class="n" id="s06-n">0.1<small>แอมป์</small></div><div class="t">ผ่านหัวใจ = อันตรายถึงชีวิต</div>{danger_bar(5)}</div>'
js = 'tl.fromTo("#s06-hand",{x:300},{x:0,duration:.5,ease:"power3.out"},0.05);\n'
js += 'tl.fromTo("#s06-lever",{y:0},{y:70,duration:.18,ease:"power4.in"},0.8);\n'
js += 'tl.fromTo("#s06-dark",{opacity:0},{opacity:.55,duration:.12,ease:"none"},1.0);\n'
js += js_scroll("#s06-wv", dx=-180, period=4, dur=6.2) + js_card("#s06-card", 2.9)
scene("s06", 24.0, 6.2, svg, overlay, js, origin="50% 45%")

# 7 — 20:00, Somo's ears swing toward the stairs
svg = f'<rect x="0" y="0" width="1080" height="1920" fill="#3b3a44"/><circle cx="540" cy="1000" r="560" fill="url(#g-warm)" opacity=".35"/>'
svg += cat(520, 1720, 3.0, face="right", tail_id="s07-tail", ear_id="s07-ears", eye_id="s07-eyes")
overlay = '<div class="chip" id="s07-clock">🕗 20:00 น.</div>'
js = 'tl.fromTo("#s07-clock",{y:-20,opacity:0},{y:0,opacity:1,duration:.35,ease:"power3.out"},0.1);\n'
js += 'tl.fromTo("#s07-ears",{rotation:0},{rotation:22,transformOrigin:"50% 100%",duration:.35,ease:"back.out(2)"},1.75);\n'
js += 'tl.fromTo("#s07-eyes",{x:0},{x:9,duration:.25,ease:"power2.out"},1.95);\n'
scene("s07", 30.2, 4.6, svg, overlay, js, origin="50% 40%", push=1.08)

# 8 — the stairs into the water: rings with no wind; a foot pulls back
svg = f'<rect x="0" y="0" width="1080" height="1920" fill="{C["wall_dk"]}"/>'
svg += "".join(f'<rect x="{60+i*90}" y="{380+i*120}" width="900" height="34" fill="{C["floor"]}"/><rect x="{60+i*90}" y="{414+i*120}" width="900" height="86" fill="{C["floor_dk"]}"/>' for i in range(7))
svg += water(1150, wid="s08-wv", lines=6)
svg += "".join(ripple(600, 1320, 200, 50, f"s08-r{i}", color="#7fa0ad", width=6) for i in range(3))
svg += f'<g id="s08-foot"><rect x="160" y="900" width="70" height="300" rx="28" fill="{C["pants"]}"/><ellipse cx="200" cy="1210" rx="50" ry="26" fill="{C["skin"]}"/></g>'
js = js_scroll("#s08-wv", dx=-180, period=4, dur=6.7) + js_ripples(["s08-r0", "s08-r1", "s08-r2"], 1.25, gap=.5, life=1.8)
js += 'tl.fromTo("#s08-foot",{y:-420},{y:0,duration:.6,ease:"power2.out"},3.9);\n'
js += 'tl.to("#s08-foot",{y:-520,duration:.25,ease:"power4.in"},5.2);\n'
scene("s08", 34.8, 6.7, svg, js=js, origin="55% 65%")

# 9 — 2011: nearly 100 crocodiles escaped farms around Ayutthaya
svg = sky(800, moon=(860, 230)) + treeline(760, seed=9) + water(820, wid="s09-wv", lines=9) + croc(-400, 1250, 1.3, "s09-croc")
overlay = f'<div class="card" id="s09-card"><div class="t">น้ำท่วมใหญ่ ปี 2554</div><div class="n"><span id="s09-n">100</span><small>ตัว</small></div><div class="t">จระเข้หลุดจากฟาร์ม รอบอยุธยา</div>{danger_bar(4)}</div>'
js = js_scroll("#s09-wv", dx=-180, period=3.5, dur=5.1) + 'tl.fromTo("#s09-croc",{x:-400},{x:1200,duration:5.1,ease:"none"},0);\n' + js_card("#s09-card", 0.6, "#s09-n", 100)
scene("s09", 41.5, 5.1, svg, overlay, js, origin="50% 65%")

# 10 — phone: dial 1784, battery 20 %
svg = f'<rect x="0" y="0" width="1080" height="1920" fill="#2a2a33"/><circle cx="540" cy="1000" r="520" fill="url(#g-warm)" opacity=".25"/>'
svg += f'<path d="M300 1900 L360 1150 Q370 1100 420 1100 L520 1100 L480 1900 Z" fill="{C["skin"]}"/>'
svg += f'<rect x="330" y="560" width="420" height="860" rx="56" fill="#16181d"/><rect x="352" y="590" width="376" height="800" rx="40" fill="#0f1a24"/>'
svg += f'<path d="M700 1180 Q760 1180 760 1240 L760 1420 L660 1420 Z" fill="{C["skin"]}"/>'
overlay = """<div id="s10-ui" style="position:absolute;left:352px;top:590px;width:376px;height:800px;font-family:'TH';color:#e9eef2;text-align:center">
 <div style="position:absolute;right:26px;top:22px;font-size:30px;font-weight:700;color:#e0574f">▮ 20%</div>
 <div style="position:absolute;left:0;right:0;top:150px;font-size:34px;font-weight:500;opacity:.75">สายด่วน ปภ.</div>
 <div id="s10-num" style="position:absolute;left:0;right:0;top:210px;font-size:110px;font-weight:700;letter-spacing:4px"><span id="s10-d0" style="opacity:0">1</span><span id="s10-d1" style="opacity:0">7</span><span id="s10-d2" style="opacity:0">8</span><span id="s10-d3" style="opacity:0">4</span></div>
 <div id="s10-calling" style="position:absolute;left:0;right:0;top:380px;font-size:36px;font-weight:500;opacity:0">กำลังโทร…</div>
 <div style="position:absolute;left:50%;top:600px;width:130px;height:130px;margin-left:-65px;border-radius:50%;background:#1f7a3a;font-size:64px;line-height:130px">✆</div>
</div>"""
js = "".join(f'tl.fromTo("#s10-d{i}",{{opacity:0,y:20}},{{opacity:1,y:0,duration:.12,ease:"power2.out"}},{0.15+i*0.28:.2f});\n' for i in range(4))
js += 'tl.fromTo("#s10-calling",{opacity:0},{opacity:1,duration:.3},1.5);\n'
scene("s10", 46.6, 4.3, svg, overlay, js, origin="50% 50%", push=1.05)

# 11 — the dark room, one candle: "everything right… except one thing"
svg = f'<rect x="0" y="0" width="1080" height="1920" fill="#16141a"/><rect x="0" y="1300" width="1080" height="620" fill="#221b16"/>'
svg += candle(540, 1420, "s11-flame") + cat(300, 1500, 0.95, face="right")
svg += f'<rect x="0" y="0" width="1080" height="1920" fill="#000" opacity=".25"/>'
js = 'tl.fromTo("#s11-flame",{scaleY:1,scaleX:1},{scaleY:1.15,scaleX:.9,transformOrigin:"50% 100%",duration:.23,ease:"sine.inOut",yoyo:true,repeat:12},0);\n'
scene("s11", 50.9, 3.0, svg, js=js, origin="50% 70%", push=1.10)

# 12 — cross-section: the upstairs toilet pipe runs down into the same flood water
svg = f'<rect x="0" y="0" width="1080" height="1920" fill="#e9e3d6"/>'
svg += f'<polygon points="120,360 540,190 960,360" fill="{C["roof"]}"/><rect x="160" y="360" width="760" height="900" fill="#d6cdbb" stroke="#5b5346" stroke-width="10"/>'
svg += f'<rect x="160" y="700" width="760" height="18" fill="#5b5346"/>'
svg += f'<rect x="0" y="800" width="1080" height="1120" fill="#3d6e8a" opacity=".85"/>'
svg += f'<path d="M0 800 q45 -14 90 0 t90 0 t90 0 t90 0 t90 0 t90 0 t90 0 t90 0 t90 0 t90 0 t90 0 t90 0" fill="none" stroke="#9fc3d4" stroke-width="5"/>'
svg += f'<rect x="680" y="420" width="12" height="280" fill="#5b5346"/>'
svg += toilet_front(800, 700, 0.62) + cat(330, 695, 0.55, face="right") + person_sitting(470, 695, 0.5)
svg += f'<path id="s12-pipe" d="M800 650 L800 760 L1010 760 L1010 1010 L70 1010" fill="none" stroke="{C["red"]}" stroke-width="22" stroke-linejoin="round" stroke-dasharray="1700" stroke-dashoffset="1700"/>'
svg += f'<g font-family="TH" font-weight="700" font-size="46" fill="#2e2a24"><text x="200" y="440">ชั้นสอง</text></g><g font-family="TH" font-weight="700" font-size="46" fill="#ffffff"><text x="200" y="900">ชั้นล่าง (จมน้ำ)</text><text id="s12-lab" x="80" y="1080" opacity="0">ท่อน้ำทิ้ง → น้ำท่วมทั้งหมู่บ้าน</text></g>'
js = 'tl.fromTo("#s12-pipe",{attr:{"stroke-dashoffset":1700}},{attr:{"stroke-dashoffset":0},duration:2.2,ease:"power2.inOut"},0.4);\n' + 'tl.fromTo("#s12-lab",{opacity:0},{opacity:1,duration:.3},2.4);\n'
scene("s12", 53.9, 4.7, svg, js=js, origin="50% 40%", push=1.04)

# 13 — Somo stares at the bathroom door, fur up
svg = f'<rect x="0" y="0" width="1080" height="1920" fill="{C["wall_dk"]}"/><rect x="0" y="1300" width="1080" height="620" fill="{C["floor"]}"/>'
svg += door(620, 420, 380, 880, gap_id="s13-gap", sign=True)
svg += f'<g id="s13-cat">{cat(330, 1720, 1.35, face="right", tail_id="s13-tail")}</g>'
svg += f'<rect x="0" y="0" width="1080" height="1920" fill="#000" opacity=".28"/>'
js = 'tl.fromTo("#s13-cat",{scale:1},{scale:1.07,transformOrigin:"50% 100%",duration:.25,ease:"back.out(3)"},2.1);\n' + 'tl.fromTo("#s13-tail",{rotation:0},{rotation:28,transformOrigin:"100% 100%",duration:.25,ease:"power3.out"},2.1);\n'
scene("s13", 58.6, 4.1, svg, js=js, origin="70% 45%", push=1.10)

# 14 — inside the toilet: the water ripples; hard cut to black
svg = f'<rect x="0" y="0" width="1080" height="1920" fill="#cfd3d4"/><rect x="0" y="1290" width="1080" height="630" fill="#9ea6a8"/>'
svg += toilet_front(540, 1330, 1.9)
svg += "".join(ripple(540, 889, 60, 15, f"s14-r{i}", color="#9fc3d4", width=4) for i in range(3))
svg += f'<rect x="0" y="0" width="1080" height="1920" fill="#000" opacity=".22"/><rect id="s14-black" x="0" y="0" width="1080" height="1920" fill="#000" opacity="0"/>'
js = js_ripples(["s14-r0", "s14-r1", "s14-r2"], 1.85, gap=.35, life=1.2, scale=3.2) + 'tl.set("#s14-black",{opacity:1},3.15);\n'
scene("s14", 62.7, 3.3, svg, js=js, origin="50% 46%", push=1.12)

# 15 — next episode card
svg = f'<rect x="0" y="0" width="1080" height="1920" fill="{C["water2"]}"/>' + water(0, h=1920, wid="s15-wv", lines=12)
overlay = """<div id="s15-txt" style="position:absolute;left:0;right:0;top:700px;text-align:center;font-family:'TH';color:#f2ece0;opacity:0">
 <div style="font-size:48px;font-weight:500;opacity:.8">ตอนต่อไป</div>
 <div style="font-size:96px;font-weight:700;line-height:1.3;margin-top:16px">มีอะไรอยู่<br>ในชักโครก?</div>
</div>"""
js = js_scroll("#s15-wv", dx=-180, period=4, dur=2.5) + 'tl.fromTo("#s15-txt",{opacity:0,y:30},{opacity:1,y:0,duration:.5,ease:"power3.out"},0.2);\n'
scene("s15", 66.0, 2.5, svg, overlay, js, push=1.03)


build(68.5)
