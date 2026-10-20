# BW2-P08 / Air Purifier: Storyboard Video (FB / IG)

- Final: `20-10-Bwell_BW2-P08_AirPurifier_36s_4x5.mp4`. Hosted at https://d2ol7oe51mr4n9.cloudfront.net/user_3Dy6Z3ucZX6ucLB5u9pTBF68wRy/2d2eed20-ddf3-4bdf-928b-22b37a55772e.mp4
- Spec: 1080x1350 (4:5), 30fps, 36.0s, H.264 + AAC 48kHz. Audio is -14.5 LUFS with a -1.5 dBTP peak. md5 d36612bbdd7af54ed4daa13eea69ef94
- Per Bass (2026-10-20):
  - AI video on every shot.
  - On-screen text only, no VO.
  - No disclaimer and no AI label.
- Product refs (Google Drive, used for keyframes and QC):
  - `G9.png` packshot (2000x2000).
  - `01_STYLEPROOF-REAL_AP-P4019US_Photoreal_2026-07-30.jpg`.
  - Copies are in `refs/`.
- Pipeline:
  1. Keyframes: GPT Image 2.5 at 3:4, using the storyboard crop and the packshot as references.
  2. Shots: Seedance 2.0 image-to-video, 1080p, no audio.
  3. Edit: center-crop to 4:5, 0.25s dissolves.
  4. Overlays: Kanit / Poppins text plus the official bwell.co.th logo (white), composited in post rather than drawn by AI.
- Music: ElevenLabs Music v2 via Magnific, instrumental ambient piano, 37s, trimmed with a 2.5s fade-out.

| # | Time | Camera | On-screen text |
|---|---|---|---|
| 01 | 0-5s | Wide / slow push-in | รู้จักเครื่องฟอกอากาศ Bwell / สองรูปแบบ ใกล้ชีวิตคุณ |
| 02 | 5-12s | Medium / lateral slide | AP-P4019US / เครื่องฟอกอากาศสำหรับห้อง |
| 03 | 12-18s | Macro push-in (display shows icons only, no numbers) | เห็นรายละเอียด / ก่อนเลือกใช้งาน |
| 04 | 18-25s | Front hero push-in | G9 / เครื่องฟอกอากาศพกพา / รถยนต์ |
| 05 | 25-31s | Split screen, both sides | พื้นที่ต่างกัน / เลือกประเภทให้เหมาะ |
| 06 | 31-36s | Hero hold (slowed 1.2x) | Bwell logo + คุณอยากรู้จักรูปแบบไหนต่อ? |

Cost:

| Item | Credits |
|---|---|
| Higgsfield keyframes | 6 x 0.25 |
| Higgsfield Seedance 1080p | 2 x 5s, 2 x 6s, 2 x 7s |
| Magnific music | 740 |
