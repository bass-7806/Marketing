# Bwell G8 Jet Reel — QC fix v3 (2026-10-19)
Source: `19-10-Bwell_G8_Jet_SFX_Preview_1080canvas.mp4` (Drive) · Output: `19-10-Bwell_G8_Jet_v3_1080x1920.mp4` (7.3 MB, in this folder)

## Fixes
| # | Issue (QC) | Fix |
|---|---|---|
| 1 | Audio 7–10s near-silent (-60 to -67 dB), whole clip -20.5 LUFS | Added music bed (A minor pad → C major at 8.0s reveal, riser 6.6–8.0s, sub impact + chime at title "Bwell G8"), kept original SFX; loudness -15.2 LUFS, true peak -1.4 dBFS |
| 2 | Disclaimer "ภาพคอนเซปต์จินตนาการ" ~17px at y≈1480 (inside TikTok/Reels caption zone) | v2: moved under logo · v3 (Bass 2026-10-19): disclaimer removed entirely — old text inpainted out per frame (OpenCV), no new text |

## Unchanged
Video content, logo, headline, product, 1080×1920 30fps 10s.

## Notes
- Music is synthesized in-house (no third-party/licensed track) — replace with a library track if preferred.
- 8.5–10s: faint inpaint trace at former disclaimer spot on the console edge; not visible at phone size.
