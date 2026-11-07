# Bwell AP-P4019US: "Flight" product video v1

- Output: 1080x1920, 30fps, 10.0s, H.264 + AAC (cinematic music + thruster SFX), no on-screen text
- Video: https://d2ol7oe51mr4n9.cloudfront.net/user_3Dy6Z3ucZX6ucLB5u9pTBF68wRy/2247a5b8-9aa7-4002-84da-a1637f1f4c65.mp4
- Packshot source: bwell.co.th/product/ap-p4019us/ (AP-P4019US_02-scaled.webp)

| Step | Tool | Credits |
|---|---|---|
| Scene: salt flat at golden hour (replace background) | Magnific | 50 |
| Expand to 9:16 | Magnific | 50 |
| Video 10s 1080p, start frame = scene | Magnific Seedance Pro 2.5 | 7,900 |
| Music 11s instrumental | Magnific ElevenLabs Music v2 | 220 |
| Mix + scale 1080x1920 | ffmpeg (Higgsfield sandbox) | 0 |

Storyboard: 0-2s thrusters ignite on a glowing blue ring / 2-5s liftoff with vapour trail / 5-8s flying through clouds / 8-10s hero hover above the clouds.
Note: the Seedance source is 606x1080 (preview), upscaled to 1080x1920.

## Kickflip v1 (reference: Tesla X post "Do a kickflip!", 2026-10-16)
- Video: https://d2ol7oe51mr4n9.cloudfront.net/user_3Dy6Z3ucZX6ucLB5u9pTBF68wRy/bd2080e2-e902-4ba2-ae3a-3c162449ac0d.mp4
- Reference used only for direction (night stage, red LED bars, floodlights, smoke, thrusters, mid-air kickflip). Tesla footage was NOT fed into the AI; no Tesla car/logo/name in output.
- Timeline: 0-2s thrusters ignite in smoke / 2-4s lift-off and hover / 4-7s 360-degree kickflip mid-air / 7-10s soft landing, hero push-in
- Credits: night-stage background 50 + 9:16 expand 50 + Seedance 10s 1080p 7,900 = 8,000 (music reused from Flight v1)

## Loop Reel v1 (reference: Facebook reel, flying car loop over city boulevard, 2026-10-18)
- Video: https://d2ol7oe51mr4n9.cloudfront.net/user_3Dy6Z3ucZX6ucLB5u9pTBF68wRy/63180ece-fe93-4668-a79c-09b383487583.mp4
- Spec: 1080x1920, 9:16, 10s, H.264 + AAC (native SFX + cinematic music bed, no text)
- Reference used only for direction (handheld POV, wet European boulevard, bus, vertical blast-off, sky loop with ring vapor trail). Reference footage was NOT fed into the AI; no Tesla car/logo/name in output.
- Timeline: 0-3s product on wet autumn boulevard, bus passes / 3-5s thrusters ignite, vapor plume, blasts up / 5-9s full loop in overcast sky, ring vapor trail / 9-10s disappears, ring hangs in sky
- Credits: background replace 50 + 9:16 expand 50 + Seedance 10s 1080p 7,900 = 8,000 (music reused from Flight v1)

## Loop Reel v2 — CI blue #0D99DB + Bwell logo end card (2026-10-18)
- Video: https://d2ol7oe51mr4n9.cloudfront.net/user_3Dy6Z3ucZX6ucLB5u9pTBF68wRy/d5f0f8d8-86f3-445a-803b-4708a3fcc601.mp4
- Spec: 1080x1920, 9:16, 13s (10s flight + 3s logo end card), H.264 + AAC
- Timeline: 0-3s boulevard + bus / 3-5s blue jet + blue smoke blast-off / 5-9s blue smoke ring loop / 9-10s product holds inside ring / 10-13s blue smoke condenses into Bwell logo inside the ring
- Color: AI smoke came out teal; graded cyan/green hues +26 deg toward #0D99DB in post
- Logo: official wordmark from bwell.co.th header (logoBwell_pantone), recolored to #0D99DB, composited in post (not AI-drawn)
- Audio: native SFX + Flight v1 music time-stretched to 13s + whoosh at 9.8s + soft chime at 11s
- Credits: Seedance 10s 1080p 7,900 (start frame reused from v1)
