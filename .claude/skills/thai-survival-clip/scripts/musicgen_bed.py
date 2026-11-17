# Local MusicGen: one ~28s seed from a mood prompt, crossfade-looped to the target length.
# usage: musicgen_bed.py "<prompt>" <target_seconds> <out.wav> [seed]
import sys, numpy as np, soundfile as sf, torch
from transformers import AutoProcessor, MusicgenForConditionalGeneration
prompt, target, out = sys.argv[1], float(sys.argv[2]), sys.argv[3]
torch.manual_seed(int(sys.argv[4]) if len(sys.argv) > 4 else 7)
dev = "mps" if torch.backends.mps.is_available() else "cpu"
proc = AutoProcessor.from_pretrained("facebook/musicgen-small")
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small", torch_dtype=torch.float16 if dev=="mps" else torch.float32, low_cpu_mem_usage=True).to(dev)
print("model loaded on", dev, flush=True)
inp = proc(text=[prompt], padding=True, return_tensors="pt").to(dev)
audio = model.generate(**inp, do_sample=True, guidance_scale=3.5, max_new_tokens=int(27.5 * 50))
sr = model.config.audio_encoder.sampling_rate
seed = audio[0, 0].float().cpu().numpy()
xf = int(3.0 * sr); n = int(target * sr); outbuf = seed.copy()
while len(outbuf) < n:
    ramp = np.linspace(0, 1, xf)
    outbuf = np.concatenate([outbuf[:-xf], outbuf[-xf:] * (1 - ramp) + seed[:xf] * ramp, seed[xf:]])
outbuf = outbuf[:n]
fade = int(2.5 * sr); outbuf[-fade:] *= np.linspace(1, 0, fade); outbuf[:int(0.5*sr)] *= np.linspace(0, 1, int(0.5*sr))
outbuf = outbuf / (np.abs(outbuf).max() + 1e-9) * 0.89
sf.write(out, outbuf, sr); print("wrote", out, len(outbuf) / sr, "s on", dev)
