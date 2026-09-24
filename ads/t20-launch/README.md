# Bwell Robot Ultra T20 — New Launch Online Ads (Hero, no price)

Download (zip, 5 files): https://d2ol7oe51mr4n9.cloudfront.net/user_3Dy6Z3ucZX6ucLB5u9pTBF68wRy/e15c03c4-13ce-4c82-be39-f173cc18c562.zip
Contact sheet: https://d2ol7oe51mr4n9.cloudfront.net/user_3Dy6Z3ucZX6ucLB5u9pTBF68wRy/69f89095-3933-4541-9049-214a6f6551d4.jpg

| File | Size | Placement |
|---|---|---|
| T20_Launch_Feed_1x1.jpg | 2048x2048 | FB/IG Feed, marketplace square |
| T20_Launch_Feed_4x5.jpg | 1638x2048 | FB/IG Feed portrait |
| T20_Launch_Story_9x16.jpg | 1152x2048 | Story / Reels / TikTok (copy kept out of top/bottom UI zones) |
| T20_Launch_Web_16x9.jpg | 2048x1152 | bwell.co.th hero, FB cover |
| T20_Launch_Marketplace_2x1.jpg | 2048x1024 | Shopee / Lazada shop banner — confirm current platform spec before upload |

## Copy

| Element | Text |
|---|---|
| Tag | NEW LAUNCH |
| Product | Bwell Robot Ultra T20 |
| Headline | บ้านสะอาด โดยไม่ต้องลงมือ |
| Sub | All-In-One Station ดูด ถู ล้าง อบแห้ง จบในเครื่องเดียว |
| CTA | ดูรายละเอียดเพิ่มเติม |
| URL | www.bwell.co.th |

No price / promo / launch date on image (per brief). No Pa / dB claims (unverified in product profile).

## Pipeline

1. Scenes: Higgsfield `gpt_image_2_5` (high, 2K) at native 1:1, 4:5, 9:16, 16:9, referencing T20 station + robot packshots. Dark studio, #005D9D navy light.
2. Copy overlay: `compose_t20_launch.py` (DB Helvethaica X Bold/Med/Reg, same font files as `pdp/t20`).

```
python3 compose_t20_launch.py <scenes_dir: hero_1x1/4x5/9x16/16x9.png> <fonts_dir> <out_dir>
```
