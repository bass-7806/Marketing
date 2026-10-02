# BWELL CREATIVE SYSTEM — DECISION LOG + REDLINE

Date: 2026-10-02 | Prepared for: Bass
Scope: ทำให้ทุก AI และ designer ใช้กฎชุดเดียวกัน เพื่อแก้ปัญหางานดีไซน์ไม่ต่อเนื่อง
ไฟล์ใน repo นี้: `BWELL_CI_QUICK_SPEC.md` + `BWELL_SOCIAL_CREATIVE_MASTER_PROMPT_v2.txt`
ไฟล์บน Drive: ยังไม่ได้แก้ — Bass แก้ตาม redline ส่วนที่ 3

---

## 1. DECISION LOG (Bass ตัดสิน 2026-10-02)

| # | หัวข้อ | Decision |
|---|---|---|
| Q1 | Brand Blue | `#0D99DB` |
| Q2 | Font | แยกตามหมวด: Electronics = DB Helvethaica X / Ergo + Sports = Kanit / Beauty EN = Poppins, TH = Kanit |
| Q3 | Gradient | Blue: `#0D99DB` → `#005D9D` แนวตั้ง 180° · Gray: `#D3D3D4` → `#A8AAAD` แนวตั้ง 180° |
| Q4 | Logo size | แนวนอนกว้าง 28.5% W · แนวตั้ง/จัตุรัสสูง 11.4% H · margin ขวา 5.9% บน 2.85% |
| Q5 | Sub-brand logo | Ergo = เก้าอี้ + เบาะ · Beauty = Hair Styling · Bwell = ที่เหลือ |
| Q6 | ราคาบน artwork | ได้ทุก channel เมื่อ verify จาก bwell.co.th + URL + เวลาตรวจ |
| Q7 | QC | Dual 10/10 (Bwell CI QC แบบถ่วงน้ำหนัก §12 + Beauty QC §23.10) |
| Q8 | Positioning | ใช้คู่กัน: Brand = Total wellness for everyday life · Category Air/Water/Clean = Home Environment Wellness |
| Q9 | Master Prompt v1.0 | Rewrite เป็น v2.0 และเลิกใช้ v1.0 |
| Q10 | ส่งมอบ | Repo + redline (ไม่แก้ไฟล์ Drive) |

## 2. ADDITIONAL DECISIONS (Bass ตัดสิน 2026-10-02 รอบ 2)

| # | หัวข้อ | Decision |
|---|---|---|
| O1 | Type scale | Standard: Headline 7.5% W Bold/Black (≤ 2 บรรทัด) · Sub 4.4% W Medium · Body/CTA 3.3% W Regular/Medium · Line-height ไทย 1.3 |
| O2 | Safe area 9:16 | Conservative ค่าเดียวทุก platform: บน 250px · ล่าง 450px · ขวา 140px · ซ้าย 60px |
| O3 | Logo margin base | ขวา 5.9% ของความกว้าง · บน 2.85% ของความสูง; 9:16 ให้ safe area ชนะ margin |
| O4 | Claim source | Approved manual/spec → bwell.co.th exact-model page · Product Intelligence = context เท่านั้น · ขัดกัน = ถาม Bass |
| O5 | ทิศ gradient | ตามที่ Bass ล็อก: บน `#0D99DB` → ล่าง `#005D9D` (`linear-gradient(180deg, ...)`) |

ไม่มี open item เหลือในระดับ spec

## 3. REDLINE — สิ่งที่ Bass ต้องแก้ในไฟล์ Drive / ไฟล์อื่น

### 3.1 Bwell CI 10/10 Production Standard (Source of Truth)

| Section | ข้อความเดิม (สรุป) | แก้เป็น |
|---|---|---|
| หัวเอกสาร "CI COLOR OVERRIDE 2026-09-27" | `#008AD0` และ `#005D9D` DEPRECATED | `#008AD0` DEPRECATED · `#005D9D` ใช้ได้เฉพาะปลาย Blue Gradient (`#0D99DB` → `#005D9D` 180°) ห้ามใช้เป็น Brand Blue เดี่ยวหรือสีตัวอักษร |
| §23.5 Color Lock | Navy → `#0D99DB` 180° เมื่อ brief ระบุ; ไม่มี hex navy | แทนด้วย 2 gradient ที่อนุมัติ: Blue `#0D99DB` → `#005D9D` 180° และ Gray `#D3D3D4` → `#A8AAAD` 180° ห้ามสร้าง gradient อื่น |
| §6 Logo Lock | บอกแค่ TOP-RIGHT | เพิ่ม: ขนาด 28.5% W (แนวนอน) / 11.4% H (แนวตั้ง-จัตุรัส), margin ขวา 5.9% บน 2.85%, Logo family Ergo / Beauty / Bwell ตามหมวด |
| §12 vs §23.10 | QC สองระบบ ไม่บอกว่าใช้อันไหน | เพิ่มประโยค: "§12 = Bwell CI QC scorecard ภายใต้ Dual 10/10 ใน §23.10; QC_PASS = CI 10 + Beauty 10" |
| §23.8 Badge / §9 Claim | ไม่ระบุเรื่องราคาบน artwork | เพิ่ม: "ราคา/โปรใส่บน artwork ได้ทุก channel เมื่อ verify จาก bwell.co.th exact-model page + URL + เวลาตรวจ" |
| §21 Claim Authority | Manual → Product Intelligence → bwell.co.th | Approved manual/spec → bwell.co.th exact-model page; Product Intelligence = context เท่านั้น; ขัดกัน = ถาม Bass |
| §23.4 Typography | ไม่มี type scale | เพิ่ม: Headline 7.5% W · Sub 4.4% W · Body/CTA 3.3% W · Line-height ไทย 1.3 · Headline ≤ 2 บรรทัด |
| §23.12 Final Gate | "safe area verified" ไม่มีค่า | เพิ่ม: 9:16 safe area บน 250 / ล่าง 450 / ขวา 140 / ซ้าย 60 px |
| §6 Logo margin | — | ระบุฐาน: ขวา 5.9% ของ W, บน 2.85% ของ H; 9:16 ให้ safe area ชนะ |
| เลข section | มี "21)" สองหัวข้อ | เปลี่ยน /bwell-composite7 เป็น 21A หรือเลื่อนเลข |
| §19 อ้าง Source Index | "2026-09-16" | ใช้ชื่อปัจจุบัน "Bwell Social Creative SOP & Source Index" |
| Router §22 | ใช้ /perspective-composite, /safe-placement | เพิ่ม: "ทุกคำสั่ง composite = /bwell-composite7; /safe-placement คือ variant ของ composite7" |
| §16 + §22 คำสั่งที่ไม่มีนิยาม (16 ตัว) | /drawingpainting /marketplaceinfo /productad /retaildisplay /inuse /demo /howto /productuse /packshot /ugcvideo /product-angle-lock /scene-first /perspective-composite /native-product-integration /safe-placement /qcperspective | เพิ่ม pointer: "นิยามอยู่ใน BWELL_IMAGE_COMMAND_LIBRARY.md Part C" (หลัง Bass approve) |
| Section ใหม่ | — | เพิ่ม pointer: "Quick Spec 1 หน้า = BWELL_CI_QUICK_SPEC.md (ค่าตัวเลขทั้งหมด)" |

### 3.2 Bwell Brand DNA 2026

| จุด | แก้เป็น |
|---|---|
| Legacy colors / Cheat sheet "Legacy Blue" | `#008AD0` deprecated · `#005D9D` = Gradient Navy endpoint เท่านั้น |
| Gradient rule | ใช้ 2 gradient ตาม Quick Spec |
| Positioning | เพิ่มบรรทัด Category umbrella: Home Environment Wellness (Air / Water / Clean Home) |
| Logo System | เพิ่ม Logo family Ergo / Beauty / Bwell |
| Shopee/Lazada Banner template | ใช้ได้ (ราคาบน artwork อนุญาตแล้ว) แต่ตัด emoji ออกจากข้อความบน artwork |
| Tone by Platform — TikTok | คง "3 วิแรก" (ตรงกับ v2.0) |

### 3.3 Bwell Product Intelligence 2026

| จุด | แก้เป็น |
|---|---|
| ข้อห้าม "ห้ามใส่ราคาใน artwork — ใช้ใน caption เท่านั้น" | ลบออก แทนด้วย "ราคาบน artwork ได้ทุก channel เมื่อ verify จาก bwell.co.th + URL + เวลาตรวจ" |
| ข้อความ "Dyson alternative" ใน USP / Pain point | เพิ่มหมายเหตุ: internal positioning เท่านั้น ห้ามใช้ใน content |

### 3.4 Bwell Command Menu Cross-AI

| จุด | แก้เป็น |
|---|---|
| §1 ตารางติดตั้ง — ไฟล์ Knowledge | แทน `BWELL SOCIAL CREATIVE MASTER PROMPT.txt` ด้วย `BWELL_SOCIAL_CREATIVE_MASTER_PROMPT_v2.txt` + `BWELL_CI_QUICK_SPEC.md` |
| §2 System Prompt | แทนทั้งบล็อกด้วย Master Prompt v2.0 (ไม่มี system prompt สองชุด) |
| §2 ข้อ 6 Typography | เพิ่ม gradient 2 แบบ |
| §4 Angle → Pipeline | เพิ่มหมายเหตุ: Creative Type เป็นตัวกำหนด layout family; pipeline เป็นแค่ทางผลิต ผลลัพธ์ต้องผ่าน Quick Spec เท่ากันทุก pipeline |
| QC Output | เปลี่ยนเป็น Dual 10/10 ตาม v2.0 §11 |

### 3.5 BWELL SOCIAL CREATIVE MASTER PROMPT v1.0 (.txt)

| Action |
|---|
| ย้ายไป `99_Archive` และเปลี่ยนชื่อเป็น `DEPRECATED_...v1.0.txt` |
| ลบออกจาก Knowledge ของ ChatGPT Custom GPT / Gemini Gem / Grok Project ทุกตัว แล้วแนบ v2.0 + Quick Spec แทน |

### 3.6 User preferences ของ Bass (Claude / ChatGPT profile)

| เดิม | แก้เป็น |
|---|---|
| Brand color: #005D9D (primary navy) | Brand Blue #0D99DB · Gradient #0D99DB → #005D9D (180°) |
| Fonts: DB Helvethaica X (TH,EN), Poppins (EN), Kanit (TH) | Fonts ตามหมวด: Electronics = DB Helvethaica X · Ergo/Sports = Kanit · Beauty EN = Poppins / TH = Kanit |
| Positioning: Home Environment Wellness | Brand: Total wellness for everyday life · Category Air/Water/Clean: Home Environment Wellness |

## 4. ROLL-OUT CHECKLIST

| # | งาน | Owner |
|---|---|---|
| 1 | ตัดสิน O1–O5 — DONE 2026-10-02 | Bass |
| 2 | แก้ CI, Brand DNA, Product Intelligence, Command Menu ตามส่วนที่ 3 | Bass |
| 2a | Review + approve `BWELL_IMAGE_COMMAND_LIBRARY.md` (Part C นิยาม 16 คำสั่ง, Part F รายการ BLOCKED) | Bass |
| 2b | แก้ `Bwell_Prompt_Library.xlsx`: Base Prompt ห้ามส่งโลโก้เข้า image model → เปลี่ยนเป็น scene-only + composite7 | Bass |
| 2c | ย้าย `_TMP_BWELL_CI_SYNC_COMMAND` (Command Menu ฉบับเก่าที่กฎขัดกัน) ไป 99_Archive | Bass |
| 3 | อัปโหลด v2.0 + Quick Spec + Image Command Library ขึ้น Drive (01_RULES) และวาง Library Part A เป็น Custom Instruction ในทุก AI | Bass |
| 4 | เปลี่ยน Knowledge ใน ChatGPT / Gemini / Grok / Claude Project | Bass |
| 5 | แก้ user preferences ทุก AI | Bass |
| 6 | Test: สั่ง `/bwell-create AP-P4019US + /creativeads + /problemsolution + Facebook + Awareness + 4:5` ใน AI ทุกตัว แล้วเทียบ font / สี / โลโก้ / QC ว่าตรงกัน | Bass + Claude |
