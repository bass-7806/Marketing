# Halloween Festival Reel: CF-8428 (v2, DRAFT)

- Final: https://d2ol7oe51mr4n9.cloudfront.net/user_3Dy6Z3ucZX6ucLB5u9pTBF68wRy/4b945ba2-46c8-4d93-9c98-88e95076af3f.mp4 (md5 f7e3830ccba0defe47ffc283a1588fd5)
- 720x1280 (9:16), 10.04s, 24fps, original audio kept (no VO)
- Source: Gemini-generated video (refs/orig.mp4) - QC failed: wrong purifier, Christmas trees, garbled Thai end card, AI-drawn logo

| Shot | Time | Fix |
|---|---|---|
| 1 Pumpkin + title | 0-3s | Regenerated without tree/text; title "Happy Halloween Festival" DB Helvethaica X Bold (text/title.png) |
| 2 Woman presents purifier | 3-6s | Purifier replaced with CF-8428 (packshot CF8428.webp) |
| 3 Purifier close-up | 6-8.4s | CF-8428 from packshot, tree removed |
| 4 Woman + pumpkin + end card | 8.4-10s | Tree removed, AI text removed; end card "Happy Halloween Festival / จาก Bwell" + official logo (text/endcard.png) |

Pipeline: gpt_image_2_5 keyframe edit -> seedance_2_0 720p i2v (no audio) -> ffmpeg concat + overlays + original audio.
