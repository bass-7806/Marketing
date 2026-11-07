# Thai narration with ElevenLabs + per-character timestamps (used for captions and shot timing).
# usage: tts_elevenlabs.py <vo_text.txt> <out_dir> [--voice JBFqnCBsd6RMkjVDRZzb] [--model eleven_v3] [--stability 0.0] [--speed 1.0] [--env-file PATH]
# Key: $ELEVENLABS_API_KEY, else ELEVENLABS_API_KEY=... from --env-file. The key is never printed.
# Writes out_dir/vo_raw.mp3, vo_alignment.json, vo.wav (48 kHz stereo) and prints the duration.
import sys, os, json, base64, argparse, subprocess, urllib.request
p = argparse.ArgumentParser()
p.add_argument("text"); p.add_argument("out")
p.add_argument("--voice", default="JBFqnCBsd6RMkjVDRZzb")   # George (premade, works on the free plan)
p.add_argument("--model", default="eleven_v3")
p.add_argument("--stability", type=float, default=0.0)      # v3: 0.0 = Creative, most expressive
p.add_argument("--speed", type=float, default=1.0)
p.add_argument("--env-file", default=None)
a = p.parse_args()
key = os.environ.get("ELEVENLABS_API_KEY")
if not key and a.env_file:
    for line in open(os.path.expanduser(a.env_file)):
        if line.startswith("ELEVENLABS_API_KEY="):
            key = line.split("=", 1)[1].strip().strip('"').strip("'")
if not key:
    sys.exit("No ELEVENLABS_API_KEY: set the env var or pass --env-file")
os.makedirs(a.out, exist_ok=True)
body = {"text": open(a.text).read().strip(), "model_id": a.model,
        "voice_settings": {"stability": a.stability, "speed": a.speed}}
req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{a.voice}/with-timestamps?output_format=mp3_44100_128",
                             data=json.dumps(body).encode(), headers={"xi-api-key": key, "Content-Type": "application/json"})
try:
    d = json.load(urllib.request.urlopen(req, timeout=300))
except urllib.error.HTTPError as e:
    msg = e.read()[:400].decode("utf-8", "replace")
    hint = ""
    if "text_to_speech" in msg: hint = "\n→ The key lacks the Text to Speech permission: enable it in ElevenLabs → Developers → API Keys."
    if "paid_plan_required" in msg or "free_users_not_allowed" in msg: hint = "\n→ Library voices need a paid plan via the API; use a premade voice (e.g. George) or upgrade."
    sys.exit(f"ElevenLabs error {e.code}: {msg}{hint}")
open(f"{a.out}/vo_raw.mp3", "wb").write(base64.b64decode(d["audio_base64"]))
json.dump(d["alignment"], open(f"{a.out}/vo_alignment.json", "w"), ensure_ascii=False)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{a.out}/vo_raw.mp3", "-ar", "48000", "-ac", "2", f"{a.out}/vo.wav"], check=True)
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{a.out}/vo.wav"], capture_output=True, text=True).stdout)
print(f"ok — narration {dur:.1f}s, {len(body['text'])} characters billed")
