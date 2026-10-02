# BWELL CI QUICK SPEC — 1 PAGE

Version: 1.0 | Effective: 2026-10-02 | Owner: Bass (Marketing Manager)
Parent: Bwell CI 10/10 Production Standard — Source of Truth (Drive ID `1-DwL2dLmHwjMzU_qmx1t5qOKrvhvFJP1K3CK1BQGMeA`)
Use: แนบไฟล์นี้คู่กับ `BWELL_SOCIAL_CREATIVE_MASTER_PROMPT_v2.txt` ในทุก AI (Claude / ChatGPT / Gemini / Grok / Codex) และทุก designer — ห้ามใช้ Master Prompt v1.0

Priority เมื่อขัดกัน: คำสั่งล่าสุดของ Bass ในงานนั้น > Quick Spec นี้ (ค่าที่ Bass ล็อก 2026-10-02) > CI Source of Truth > SOP / Source Index > เอกสารอื่น

---

## 1. COLOR

| Token | Hex | ใช้กับ | ห้าม |
|---|---|---|---|
| Brand Blue | `#0D99DB` | พื้นหลัง, shape, line, panel, icon, accent | ห้ามใช้เป็นสีตัวอักษร |
| Brand Gray | `#A8AAAD` | border, divider, secondary surface, supporting text | — |
| White | `#FFFFFF` | Headline (บังคับ), supporting text, พื้นหลัง | — |
| Gradient Navy | `#005D9D` | ปลาย Blue Gradient เท่านั้น | ห้ามใช้เป็น Brand Blue เดี่ยว / พื้นสีเดี่ยว / ตัวอักษร |
| Gradient Light Gray | `#D3D3D4` | ต้น Gray Gradient เท่านั้น | ห้ามใช้นอก gradient |
| `#008AD0` | — | — | DEPRECATED ห้ามใช้ |

### Approved gradients (มีแค่ 2 แบบ)

| ชื่อ | CSS | ทิศทาง |
|---|---|---|
| Blue Gradient | `linear-gradient(180deg, #0D99DB 0%, #005D9D 100%)` | แนวตั้ง 180° — บน `#0D99DB` → ล่าง `#005D9D` |
| Gray Gradient | `linear-gradient(180deg, #D3D3D4 0%, #A8AAAD 100%)` | แนวตั้ง 180° — บน `#D3D3D4` → ล่าง `#A8AAAD` |

- ห้ามสร้าง gradient อื่น ห้ามเปลี่ยนทิศ ห้าม sample สีจากงานเก่า
- Gray Gradient เป็นพื้นสว่าง: headline สีขาวต้องใช้ soft diffuse shadow หรือ neutral scrim เพื่อให้อ่านออก

## 2. TEXT COLOR LOCK

| Element | สีที่อนุญาต |
|---|---|
| Headline | `#FFFFFF` เท่านั้น |
| Subheadline / body / CTA / label / badge text | `#FFFFFF`, `#333333`, `#667085`, `#A8AAAD`, `#E5E7EB`, `#F5F7F9` |
| ถ้าอ่านไม่ชัด | soft diffuse drop shadow หรือ neutral scrim/safe field |
| ห้าม | ตัวอักษรสีฟ้า/น้ำเงิน/สีอื่น, outline, glow, hard shadow |

## 3. TYPOGRAPHY (ตามหมวดสินค้า)

| หมวด | ภาษา | Font | Weights ที่อนุมัติ |
|---|---|---|---|
| Electronics (Air, Water, Dehumidifier, Robot/Vacuum, Portable AC, Water Heater, Filters) | TH + EN | DB Helvethaica X | Regular, Medium, Bold, Black |
| Ergonomics (เก้าอี้, เบาะ/หมอน) | TH + EN | Kanit | Regular, Medium, Bold |
| Sports (Foam Roller, Yoga Mat) | TH + EN | Kanit | Regular, Medium, Bold |
| Beauty (Hair Styling) | EN | Poppins | Regular, SemiBold, Bold |
| Beauty (Hair Styling) | TH | Kanit | Regular, Medium, Bold |

- ใช้เฉพาะไฟล์ใน Drive `04_Fonts` ห้าม fallback เป็น Arial/Helvetica/generic sans ห้าม stretch/condense/skew
- ห้ามใช้ Poppins กับข้อความไทย
- ข้อความไทยบน final artwork ต้องวางด้วย layout tool (Canva/Figma/PIL) — ตัวอักษรที่ image model สร้างไม่นับเป็น final

| Type scale (% ของความกว้าง canvas) | Size | ที่ 1080px | Weight |
|---|---|---|---|
| Headline | 7.5% W | ≈81px | Bold / Black (Kanit, Poppins: Bold) |
| Subheadline | 4.4% W | ≈48px | Medium (Poppins: SemiBold) |
| Body / CTA / label | 3.3% W | ≈36px | Regular / Medium |
| Line-height ไทย | 1.3 | — | — |
| Headline สูงสุด | 2 บรรทัด | — | — |

## 4. LOGO

| หัวข้อ | Spec |
|---|---|
| Source | ไฟล์ official ใน Drive `03_Logos` เท่านั้น — ห้าม generate / retype / redraw / recolor / stretch / shadow / outline / glow |
| Logo family | Ergo logo = เก้าอี้ + เบาะ/หมอน · Beauty logo = Hair Styling · Bwell logo = หมวดอื่นทั้งหมด (รวม Sports) |
| Variant | พื้นสว่าง = Blue/Gray official · พื้นเข้ม = White/reversed official |
| Position | TOP-RIGHT เสมอ (เปลี่ยนได้เฉพาะคำสั่ง Bass ของงานนั้น) |
| Size — แนวนอน | กว้าง 28.5% ของความกว้าง canvas |
| Size — แนวตั้ง / จัตุรัส | สูง 11.4% ของความสูง canvas |
| Margin | ขวา 5.9% ของความกว้าง · บน 2.85% ของความสูง (1080×1080 = ขวา 64px บน 31px · 1080×1350 = ขวา 64px บน 38px · 1080×1920 = ขวา 64px บน 55px) |
| 9:16 | วางโลโก้ใต้ safe area บน (y ≥ 250px) ขวา 140px — safe area ชนะ margin |
| Minimum | Digital 80px · Print 20mm |
| ขั้นตอน | วางโลโก้หลังสร้างฉากเสมอ ห้ามส่งโลโก้เข้า image model |

## 5. PRODUCT DEPICTION

| Rule | Spec |
|---|---|
| วิธีหลัก | `/bwell-composite7` — วาง official packshot ลงฉากที่ไม่มีสินค้า |
| 7 layers | 1 Perspective & Scale · 2 Contact & Weight Shadow · 3 Lighting · 4 Color/White-Balance · 5 Occlusion · 6 Reflection/Bounce/Edge · 7 Camera & Texture |
| AI redraw / เปลี่ยนมุม | ทำได้โดยไม่ต้องขออนุมัติก่อน แต่ต้องแจ้ง Bass ทุกครั้ง (SKU, ไฟล์ต้นทาง, จุดที่เปลี่ยน) และบันทึก `AI_REDRAW / ANGLE_CHANGED` |
| ห้าม | เปลี่ยน shape, สี, ปุ่ม, display, sensor, vent, port, accessory, สร้าง variant ใหม่ |
| Scene prompt | ต้องมี `no product, no appliance, no brand, no text, no logos, no watermark` |

## 6. CLAIM / PRICE

| หัวข้อ | Rule |
|---|---|
| Claim / spec | ลำดับแหล่ง: Approved manual/spec ของ SKU → หน้า bwell.co.th ของรุ่นนั้น · Product Intelligence = context เท่านั้น · สองแหล่งขัดกัน = ถาม Bass · ไม่ verify = ตัดออก |
| ราคา / โปร | ใส่บน artwork ได้ทุก channel เมื่อ verify จากหน้า bwell.co.th ของรุ่นนั้น + บันทึก URL + วันเวลาตรวจ |
| Banned | "ป้องกัน COVID", "รักษาโรคภูมิแพ้", "ป้องกันโรค", ชื่อคู่แข่ง, fear-based copy |

## 7. OUTPUT SIZE

| Platform | Ratio | Pixel |
|---|---|---|
| Facebook | 1:1 / 4:5 | 1080×1080 / 1080×1350 |
| Instagram Feed | 4:5 | 1080×1350 |
| IG Story / Reel, TikTok, YouTube Shorts | 9:16 | 1080×1920 |
| Threads | 4:5 | 1080×1350 |
| X | 16:9 | 1600×900 |
| Safe area 9:16 (TikTok / Reel / Story / Shorts) | — | ห้ามวาง text, logo, product สำคัญใน: บน 250px · ล่าง 450px · ขวา 140px · ซ้าย 60px |

## 8. QC — DUAL 10/10 (ระบบเดียว)

**A. Bwell CI QC = 10.0/10**

| ข้อ | คะแนน |
|---|---|
| Official Source & SKU verification | 1.5 |
| Product geometry & proportion | 2.0 |
| SKU-specific details / controls / components | 1.5 |
| Official logo & Bwell CI (สี, ฟอนต์, ตำแหน่งโลโก้) | 1.5 |
| Scene / scale / lighting / realism (composite7 ผ่านครบ) | 1.0 |
| Composition / hierarchy | 1.0 |
| Copy / claims / specs / price | 1.0 |
| Ratio / technical output | 0.5 |

**B. Beauty QC = 10.0/10** — ต้องไม่มีจุดบกพร่องในทั้ง 5 ด้าน: (1) Visual impact & premium finish (2) Composition, balance, hierarchy, spacing (3) Lighting, color harmony, realism (4) Product integration, scale, perspective, shadow (5) Typography craft, Thai typesetting, platform fit

QC_PASS = CI 10/10 **และ** Beauty 10/10 **และ** ไม่มี Critical Fail → ส่ง BASS_REVIEW
QC_PASS ไม่ใช่การอนุมัติโพสต์ — ต้องมี Bass approve exact version ก่อนทุกครั้ง

**Critical Fail (ข้อเดียว = FAIL):** ผิด SKU/variant · geometry ผิด · ฟีเจอร์ที่แต่งขึ้น · โลโก้ AI/ถูกแก้/ไม่อยู่ top-right · ฟอนต์ผิดหมวด · Headline ไม่ใช่ `#FFFFFF` · ตัวอักษรสี · ใช้สีนอก palette/gradient นอก spec · claim/ราคาไม่ verify · redraw ไม่แจ้ง · ไม่ได้ Bass approve exact version
