# Bwell x TikTok Affiliate: TikTok motion graphic v1

- Output: 1080x1920, 30fps, 10.0s, H.264 + AAC (music). Not scheduled.
- Video: https://d2ol7oe51mr4n9.cloudfront.net/user_3Dy6Z3ucZX6ucLB5u9pTBF68wRy/a20a2273-338d-40f4-8b68-4251f9e144ed.mp4

## Pipeline
| Step | Tool | Note |
|---|---|---|
| Plate | scripts/layers.py | Removes text from the poster (inpaint); keys text layers to RGBA |
| 9:16 | scripts/canvas916.py | Original at y=200; mirrored extension top/bottom (Magnific expand rejected: garbled text) |
| BG motion | Magnific Seedance Pro 2.5, 10s, 9:16, 1080p | Ribbons/confetti/sparkles only, locked camera; 7,900 credits |
| Music | Magnific ElevenLabs Music v2, 12s instrumental | 240 credits |
| Composite | scripts/render.py + ffmpeg (Higgsfield sandbox) | QR card locked from frame 0; text entrances 0-2.6s; CTA bounce + pulse |

## QC
- QR card region vs original poster: mean abs diff 1.15/255 at t=7s (pixel-locked).
- Scan line runs 1.8-5.8s only; QR is clean from 5.8s to 10s.
- OpenCV QRCodeDetector cannot decode the source poster either (stylized modules + LINE logo), so the scan test must be done on a phone.
