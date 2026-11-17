# Turn a caption plan + ElevenLabs character alignment into timed caption groups.
# usage: caption_groups.py <audio/vo_alignment.json> <captions_plan.json> <audio/captions.json>
# captions_plan.json: [["<spoken text exactly as in vo_text>", "<display text, | = line break>", 0|1 highlight], ...]
# Groups are matched in order, so every phrase of the narration must appear once, in sequence.
import json, sys
a = json.load(open(sys.argv[1])); plan = json.load(open(sys.argv[2]))
chars = a["characters"]; S = a["character_start_times_seconds"]; E = a["character_end_times_seconds"]
text = "".join(chars); pos = 0; out = []
for spoken, disp, hl in plan:
    i = text.find(spoken, pos)
    if i < 0:
        sys.exit(f"not found after position {pos}: {spoken!r} — check the spelling matches vo_text.txt exactly")
    j = i + len(spoken.rstrip(".")) - 1
    out.append({"text": disp, "start": round(S[i], 3), "end": round(E[j], 3), "hl": int(hl)})
    pos = j + 1
for k, g in enumerate(out):
    g["in"] = round(max(0.15, g["start"] - 0.08), 3)
    nxt = out[k + 1]["start"] - 0.1 if k + 1 < len(out) else g["end"] + 0.8
    g["out"] = round(min(max(g["end"] + 0.35, g["in"] + 0.9), nxt), 3)
json.dump(out, open(sys.argv[3], "w"), ensure_ascii=False, indent=1)
for g in out:
    print(f'{g["in"]:6.2f}-{g["out"]:6.2f} {"*" if g["hl"] else " "} {g["text"]}')
