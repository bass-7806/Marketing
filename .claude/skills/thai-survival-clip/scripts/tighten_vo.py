# Shorten pauses in the VO, speed it up, and remap the character alignment to the new timeline.
# usage: tighten_vo.py vo_raw.mp3 vo_alignment.json out.wav out_alignment.json --cap 0.3 --twist-at 89.6 --twist-cap 0.6 --tempo 1.12
import sys, json, re, subprocess, argparse
p = argparse.ArgumentParser(); p.add_argument("src"); p.add_argument("align"); p.add_argument("out"); p.add_argument("out_align")
p.add_argument("--cap", type=float, default=0.3); p.add_argument("--twist-at", type=float, default=1e9)
p.add_argument("--twist-cap", type=float, default=0.6); p.add_argument("--tempo", type=float, default=1.0)
a = p.parse_args()
log = subprocess.run(["ffmpeg","-i",a.src,"-af","silencedetect=n=-35dB:d=0.25","-f","null","-"],capture_output=True,text=True).stderr
st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]; en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
dur = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",a.src],capture_output=True,text=True).stdout)
# keep-ranges: cut the middle of each long silence down to the cap
keep, t = [], 0.0
for s, e in zip(st, en):
    cap = a.twist_cap if s >= a.twist_at else a.cap
    if e - s > cap:
        keep.append((t, s + cap/2)); t = e - cap/2
keep.append((t, dur))
def remap(x):  # source time -> output time (before tempo)
    out = 0.0
    for s, e in keep:
        if x <= s: return out
        if x <= e: return out + (x - s)
        out += e - s
    return out
fc = "".join(f"[0:a]atrim={s:.3f}:{e:.3f},asetpts=PTS-STARTPTS[s{i}];" for i, (s, e) in enumerate(keep))
fc += "".join(f"[s{i}]" for i in range(len(keep))) + f"concat=n={len(keep)}:v=0:a=1,atempo={a.tempo}[o]"
subprocess.run(["ffmpeg","-v","error","-y","-i",a.src,"-filter_complex",fc,"-map","[o]","-ar","48000","-ac","2",a.out],check=True)
al = json.load(open(a.align))
al["character_start_times_seconds"] = [remap(x)/a.tempo for x in al["character_start_times_seconds"]]
al["character_end_times_seconds"] = [remap(x)/a.tempo for x in al["character_end_times_seconds"]]
json.dump(al, open(a.out_align,"w"), ensure_ascii=False)
print("out duration", round(remap(dur)/a.tempo, 2))
