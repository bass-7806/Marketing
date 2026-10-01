# Bwell Robot Ultra T20 — PDP Image Set

Layout reference: L6C PDP set (Drive folder `1zFJE3_rOnZxoGANFW0JRIO0EOUSWAHPB`, 6 x 3000x3000).
Spec source: `T20_Ultra_Product_Profile.md` (Drive).

## Deliverables

| File | Size | Channel |
|---|---|---|
| `web/T20_PDP_0N_*.jpg` | 2048x2048 | bwell.co.th PDP |
| `mkp/T20_PDP_0N_*.jpg` | 1000x1000 | Shopee / Lazada / TikTok Shop |

Download (zip, 12 files): https://d2ol7oe51mr4n9.cloudfront.net/user_3Dy6Z3ucZX6ucLB5u9pTBF68wRy/638f85ad-7360-4143-806a-2317fd1f6016.zip
Contact sheet: https://d2ol7oe51mr4n9.cloudfront.net/user_3Dy6Z3ucZX6ucLB5u9pTBF68wRy/fb72f8d1-11f6-4b1c-9b6e-95e053c3c697.jpg

## Slide map (L6C -> T20)

| # | L6C reference | T20 slide | Headline | Spec on image |
|---|---|---|---|---|
| 1 | Hero living room + station | Hero | หุ่นยนต์ดูดฝุ่นถูพื้น All-in-One | Auto-Empty / Auto-Fill / Auto-Clean Mop / Auto-Dry |
| 2 | Mapping + no-go zone | LiDAR | LiDAR สร้างแผนที่บ้านอัจฉริยะ | LiDAR (LDS) / No-Go Zones / Zone-based Routing |
| 3 | "5000Pa" particles | Battery | ทำงานต่อเนื่องนานกว่า 200 นาที* | 5,200 mAh / Resume After Charge / ชาร์จ < 7 ชม. |
| 4 | In-the-box | 4-in-1 Station | 4-in-1 Station จบทุกงานหลังทำความสะอาด | ถุงฝุ่น 2.8 L / น้ำสะอาด 5.0 L / น้ำเสีย 4.2 L / Auto-Dry |
| 5 | App multi-room map | Smart Life App | สั่งงานได้ทุกที่ผ่านแอป | Room Selection / Scheduling / OTA Update |
| 6 | Carpet detection | Auto Carpet Lift | เจอพรม ยกผ้าถูอัตโนมัติ | Ultrasonic / Cliff / Wall Sensor |

## Claim control

- Suction (Pa) and noise (dB): marked UNVERIFIED in the profile, not used. Slide 3 swaps L6C "5000Pa" for battery runtime.
- ">200 นาที" is Quiet Mode per Bwell manual; footnote is on slide 3.
- Slide 4 replaces L6C "in-the-box" because T20 box contents are not in the profile.

## Pipeline

1. Scenes: Higgsfield `gpt_image_2_5` (high, 2K, 1:1) with T20 packshot/robot/mop references, no text.
2. Copy overlay: `compose_t20_pdp.py` with DB Helvethaica X (Bold/Med/Reg; fonts not committed, licensed).

```
python3 compose_t20_pdp.py <scenes_dir with s1..s6.png> <fonts_dir> <out_dir>
```

Font files expected: `DBHX-Bold.ttf`, `DBHX-Med.ttf`, `DBHX-Reg.ttf`. Requires Pillow with raqm (Thai shaping).
