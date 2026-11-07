# Generic HyperFrames writer for 9:16 survival clips: one sub-composition per shot, captions, grain/vignette, index.html.
# An episode's shots.py calls scene(...) for every shot, then build(TOTAL). Run it through build.py, never directly.
import json, math, sys, os, subprocess
from lib_draw import *

OUT = None
CAPS = None

def init(out, caps):
    global OUT, CAPS
    OUT, CAPS = out, caps
    os.makedirs(f"{OUT}/compositions", exist_ok=True)

FONT = """@font-face{font-family:"TH";src:local("Sukhumvit Set Bold"),local("SukhumvitSet-Bold"),url("assets/fonts/Kanit-Bold.ttf");font-weight:700}
@font-face{font-family:"TH";src:local("Sukhumvit Set Medium"),local("SukhumvitSet-Medium"),url("assets/fonts/Kanit-Medium.ttf");font-weight:500}"""

CARD_CSS = """
.card{position:absolute;left:90px;right:90px;top:230px;background:#f2ece0;border-radius:24px;padding:34px 44px 38px;
  border-left:14px solid #c9353a;box-shadow:0 22px 48px rgba(0,0,0,.5);font-family:"TH";color:#3a352e;opacity:0}
.card .t{font-size:42px;font-weight:500;line-height:1.35}
.card .n{font-size:150px;font-weight:700;color:#c9353a;line-height:1.05}
.card .n small{font-size:64px;margin-left:12px;color:#3a352e}
.card .bar{display:flex;gap:10px;margin-top:18px}.card .bar i{flex:1;height:14px;border-radius:7px;background:#d6d0c4}
.chip{position:absolute;left:70px;top:200px;background:rgba(12,14,24,.82);color:#f2ece0;border-radius:40px;padding:14px 30px;
  font-family:"TH";font-weight:700;font-size:46px;opacity:0}
"""

SHOTS = []  # (id, start, dur)

def scene(sid, start, dur, svg, overlay="", js="", css="", origin="50% 50%", push=1.06):
    SHOTS.append((sid, start, dur))
    html = f"""<template>
<style>
{FONT}
#root{{position:absolute;inset:0;overflow:hidden;background:{C['sky1']}}}
#{sid}-cam{{position:absolute;inset:0;transform-origin:{origin}}}
#{sid}-cam svg{{position:absolute;inset:0;width:1080px;height:1920px}}
{CARD_CSS}
{css}
</style>
<div id="root" data-composition-id="{sid}" data-width="1080" data-height="1920" data-layout-allow-overlap>
  <div id="{sid}-cam" data-layout-ignore><svg viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">{defs_common()}{svg}</svg></div>
  {overlay}
</div>
<script>
(function(){{
const tl = gsap.timeline({{paused:true}});
const D = {dur};
tl.fromTo("#{sid}-cam",{{scale:1}},{{scale:{push},duration:D,ease:"sine.inOut"}},0);
{js}
window.__timelines["{sid}"] = tl;
}})();
</script>
</template>"""
    open(f"{OUT}/compositions/{sid}.html", "w").write(html)

def js_scroll(sel, dx=0, dy=0, period=1.0, dur=10):
    n = max(1, math.ceil(dur / period))
    return f'tl.fromTo("{sel}",{{x:0,y:0}},{{x:{dx},y:{dy},duration:{period},ease:"none",repeat:{n-1}}},0);\n'

def js_ripples(ids, t0, gap=0.45, life=1.5, scale=1.8):
    s = ""
    for k, rid in enumerate(ids):
        t = t0 + k * gap
        s += f'tl.fromTo("#{rid}",{{scale:.2,opacity:.9,transformOrigin:"50% 50%"}},{{scale:{scale},opacity:0,transformOrigin:"50% 50%",duration:{life},ease:"power1.out"}},{t:.2f});\n'
    return s

def js_card(sel, t, num_sel=None, to=None, fmt="int"):
    s = f'tl.fromTo("{sel}",{{y:40,opacity:0}},{{y:0,opacity:1,duration:.4,ease:"power3.out"}},{t:.2f});\n'
    if num_sel:
        s += f'(function(){{const o={{v:0}};const el=document.querySelector("{num_sel}");tl.fromTo(o,{{v:0}},{{v:{to},duration:.6,ease:"power2.out",onUpdate:()=>{{el.firstChild.nodeValue={ "Math.round(o.v)" if fmt=="int" else "o.v.toFixed(1)" };}}}},{t+0.1:.2f});}})();\n'
    return s

def danger_bar(level=4):
    cols = ["#6fbf73", "#c9c23a", "#e0a33a", "#c9353a", "#8e1f24"]
    return '<div class="bar">' + "".join(f'<i style="background:{cols[i]}"></i>' if i < level else "<i></i>" for i in range(5)) + "</div>"

def build(TOTAL):

    # ---------------- captions ----------------
    caps = json.load(open(CAPS))
    groups, cjs = "", ""
    for k, g in enumerate(caps):
        txt = g["text"].replace("|", "<br>")
        inner = f'<span class="hl">{txt}</span>' if g["hl"] else txt
        groups += f'<div class="cap" id="cap-{k}">{inner}</div>\n'
        cjs += f'tl.fromTo("#cap-{k}",{{opacity:0,scale:.96}},{{opacity:1,scale:1,duration:.12,ease:"power2.out"}},{g["in"]});\n'
        cjs += f'tl.to("#cap-{k}",{{opacity:0,duration:.1,ease:"power2.in"}},{g["out"]-0.1:.3f});\ntl.set("#cap-{k}",{{opacity:0,visibility:"hidden"}},{g["out"]});\n'
    open(f"{OUT}/compositions/captions.html", "w").write(f"""<template>
    <style>
    {FONT}
    #root{{position:absolute;inset:0;pointer-events:none}}
    .cap{{position:absolute;left:0;right:0;top:1130px;text-align:center;font-family:"TH";font-weight:700;font-size:68px;line-height:1.35;color:#fff;
      text-shadow:0 0 18px rgba(0,0,0,.95),0 3px 6px rgba(0,0,0,.9);opacity:0;overflow:visible;padding:0 60px}}
    .cap .hl{{background:{C['red']};padding:6px 26px 10px;border-radius:12px;text-shadow:none;box-decoration-break:clone;-webkit-box-decoration-break:clone}}
    </style>
    <div id="root" data-composition-id="captions" data-width="1080" data-height="1920" data-layout-allow-overlap>
    {groups}</div>
    <script>
    (function(){{
    const tl = gsap.timeline({{paused:true}});
    {cjs}
    window.__timelines["captions"] = tl;
    }})();
    </script>
    </template>""")

    # ---------------- film grain + vignette ----------------
    open(f"{OUT}/compositions/fx.html", "w").write(f"""<template>
    <style>
    #root{{position:absolute;inset:0;pointer-events:none}}
    #fx-grain{{position:absolute;inset:-200px;opacity:.16;mix-blend-mode:overlay;
     background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E")}}
    #fx-vig{{position:absolute;inset:0;background:radial-gradient(ellipse 75% 60% at 50% 46%,rgba(0,0,0,0) 50%,rgba(0,0,0,.55) 100%)}}
    </style>
    <div id="root" data-composition-id="fx" data-width="1080" data-height="1920" data-layout-ignore>
      <div id="fx-grain"></div><div id="fx-vig"></div>
    </div>
    <script>
    (function(){{
    const tl = gsap.timeline({{paused:true}});
    tl.fromTo("#fx-grain",{{x:0,y:0}},{{x:-180,y:-120,duration:{TOTAL},ease:"steps({int(TOTAL*12)})"}},0);
    window.__timelines["fx"] = tl;
    }})();
    </script>
    </template>""")

    # ---------------- index.html ----------------
    hosts = ""
    for sid, st, du in SHOTS:
        hosts += f'      <div id="{sid}" data-composition-id="{sid}" data-composition-src="compositions/{sid}.html" data-start="{st}" data-duration="{du}" data-track-index="1" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index:1"></div>\n'
    AUDIO = json.load(open(f"{OUT}/audio_cues.json")) if os.path.exists(f"{OUT}/audio_cues.json") else []
    auds = ""
    for a in AUDIO:
        extra = "".join(f" data-{k}='{v}'" for k, v in a.get("attrs", {}).items())
        import subprocess
        dur = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"{OUT}/{a['src']}"],capture_output=True,text=True).stdout)
        dur = round(min(dur, TOTAL - a["start"]), 3)
        auds += f'      <audio id="{a["id"]}" class="clip" src="{a["src"]}" data-start="{a["start"]}" data-duration="{dur}" data-track-index="{a.get("track", 5)}" data-volume="{a.get("volume", 1)}"{extra}></audio>\n'
    open(f"{OUT}/index.html", "w").write(f"""<!doctype html>
    <html lang="th" data-resolution="portrait">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=1080, height=1920" />
        <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
        <style>
          * {{ margin: 0; padding: 0; box-sizing: border-box; }}
          html, body {{ margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: #000; }}
          #root {{ position: relative; width: 100%; height: 100%; }}
        </style>
      </head>
      <body>
        <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
    {hosts}      <div id="fx" data-composition-id="fx" data-composition-src="compositions/fx.html" data-start="0" data-duration="{TOTAL}" data-track-index="2" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index:5"></div>
          <div id="captions" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{TOTAL}" data-track-index="3" data-track-kind="captions" data-width="1080" data-height="1920" style="z-index:10"></div>
    {auds}    </div>
        <script>
          const tl = gsap.timeline({{ paused: true }});
          window.__timelines["main"] = tl;
        </script>
      </body>
    </html>
    """)
    print("built", len(SHOTS), "shots, total", TOTAL, "s")
