# ตัวอย่างผลลัพธ์: `/brief` + `/prompt` สำหรับ W3-B Robot vacuum

ไฟล์นี้แสดงว่า prompt pack ควรได้ผลลัพธ์หน้าตาแบบไหน ผมเขียนตาม output spec ของ `/brief` และ `/prompt` ใน `bwell-chatgpt-graphic-prompts.md` ทีมใช้เทียบกับผลจาก ChatGPT ได้ ช่องที่ยังไม่มีข้อมูลยังเป็น `[ ]`

**Input ที่ใช้**

```
/brief
Campaign: Bwell Home Check-up Q4 2026
Calendar slot: W3-B
Objective / Funnel: Awareness / TOFU
Platform: TikTok cover + Reels cover
Product / Model: Robot vacuum (L6C / L0 / Y1 รอ product team เลือกรุ่นในคลิป)
Target persona: Family Protector
Key message: ฝุ่นที่มองไม่เห็นใต้เตียง ให้หุ่นยนต์ดูดฝุ่นช่วยดูแลทุกวัน
Headline / copy บนภาพ: ใต้เตียงคุณหน้าตาแบบนี้ไหม
CTA: เช็คบ้าน 1 นาทีที่ LINE Bwell
Offer: ไม่มี
Assets ที่มี: รูปสินค้า, logo
Deadline: 13 ต.ค. 2026
Approver: [ ]
```

---

## Output: Graphic Brief

### 1. Summary

| Item | Detail |
|---|---|
| Campaign / Slot | Bwell Home Check-up Q4 2026 / W3-B |
| Objective / Funnel | Awareness / TOFU |
| Platform | TikTok cover, Reels cover (9:16) |
| Product | Robot vacuum [รุ่นที่ใช้ในคลิป] |
| Deadline | 13 ต.ค. 2026 (โพส 14 ต.ค. เลี่ยงวันที่ 13 ต.ค.) |
| Approver | [ ] |

### 2. Key message

ฝุ่นที่มองไม่เห็นใต้เตียง ให้หุ่นยนต์ดูดฝุ่นช่วยดูแลทุกวัน

Support point: มุมที่ไม้กวาดเข้าไม่ถึง เช่น ใต้เตียงและใต้โซฟา (ไม่ใส่ spec หรือตัวเลขจนกว่า product team จะยืนยัน)

### 3. On-image copy

| Level | Copy |
|---|---|
| Headline | ใต้เตียงคุณหน้าตาแบบนี้ไหม |
| Sub-headline | ฝุ่นที่มองไม่เห็น ก็ยังอยู่ในห้องนอน |
| CTA | เช็คบ้าน 1 นาทีที่ LINE Bwell |

Headline ทางเลือก (ถ้าอยากทดสอบ A/B):
1. ใต้เตียงคุณหน้าตาแบบนี้ไหม
2. ฝุ่นใต้เตียงที่ไม่มีใครเคยเห็น
3. มุมนี้ไม้กวาดเข้าไม่ถึง

### 4. Visual direction

| Item | Direction |
|---|---|
| Scene | ห้องนอนคอนโดหรือบ้าน มุมกล้องต่ำระดับพื้น มองเข้าใต้เตียง |
| Mood | สะอาด สว่าง premium แต่เห็นความจริงของฝุ่นใต้เตียง |
| Product placement | หุ่นยนต์ดูดฝุ่นกำลังเข้าใต้เตียง ใช้รูปสินค้าจริงเท่านั้น |
| Background treatment | Photo + Navy band ด้านล่างสำหรับ CTA (ตามกฎ text บน photo) |

### 5. Layout (9:16, 1080x1920)

| Zone | ตำแหน่ง | เนื้อหา |
|---|---|---|
| Headline | บนสุด ใต้ safe zone ของ UI platform | Headline สีขาวบน Gradient A overlay บางๆ |
| Visual | กลางจอ | ภาพใต้เตียง + หุ่นยนต์ดูดฝุ่น |
| Sub-headline | ใต้ visual | สีขาว |
| CTA + logo | Navy band ด้านล่าง เหนือ UI ของ platform | CTA สีขาว + logo Bwell สีขาว |

### 6. CI notes

| Element | Spec |
|---|---|
| Headline | DB Helvethaica X Bold / Black, สีขาว |
| Sub / CTA | Kanit, สีขาว |
| Overlay | Gradient A 180deg #0d99db > #005D9D |
| CTA band | Navy #005D9D |
| Logo | Bwell white logo บนพื้น navy, clear space 1x icon |

### 7. Deliverables

| Platform | Size | Ratio | File | Qty |
|---|---|---|---|---|
| TikTok cover | 1080x1920 | 9:16 | PNG / JPG | 1 |
| Reels cover | 1080x1920 | 9:16 | PNG / JPG | 1 |
| Grid crop สำหรับ IG profile | ตรวจว่าตรงกลาง 1080x1350 อ่านได้ | 4:5 | - | - |

ขนาดทั้งหมดต้องยืนยันกับ spec ปัจจุบันของ platform ก่อนส่ง

### 8. Do / Don't

| Do | Don't |
|---|---|
| ใช้รูปสินค้าจริงและ logo จริง | ให้ AI วาดหุ่นยนต์ดูดฝุ่นหรือ logo |
| ภาพฝุ่นดูเป็นธรรมชาติ | ทำให้ห้องดูสกปรกจนน่ารังเกียจ |
| ข้อความสั้น อ่านจบใน 2 วินาที | ใส่ spec หรือตัวเลขที่ยังไม่ยืนยัน |
| | อ้างผลต่อภูมิแพ้หรือสุขภาพ |

### 9. Open questions

- รุ่นที่ใช้ในคลิป: L6C, L0 หรือ Y1
- Approver
- จะใช้ภาพ cover จากคลิปจริง หรือถ่ายภาพนิ่งแยก

---

## Output: AI Image Prompt (`/prompt`)

**Input**

```
/prompt
ใช้กับ: W3-B TikTok / Reels cover
ห้อง / ฉาก: ห้องนอนคอนโด มองเข้าใต้เตียง
เวลา / แสง: เช้า แดดอ่อนจากหน้าต่าง
ฤดู / บรรยากาศ: ปลายฝน
คน: ไม่มี
พื้นที่ว่างสำหรับ: สินค้า ใต้เตียงด้านซ้าย / headline ด้านบน
Ratio: 9:16
```

**Prompt (wide)**

```
Low-angle photo at floor level looking under a bed in a modern Bangkok condominium bedroom, soft morning daylight from a window after rain, light gray wooden floor, white bed frame and white linen, a thin natural layer of dust and a few dust bunnies visible under the bed, clean and calm premium interior, cool colour grading with soft blue, navy, white and light gray tones, shallow depth of field, empty clear floor space under the left side of the bed reserved for a product to be added later, empty upper third of the frame for a headline, realistic photography, vertical 9:16. No logos, no brand names, no text, no appliances in the empty area.
```

**Prompt (closer)**

```
Close-up floor-level photo of the gap under a white bed in a bright modern condo bedroom, gentle morning light, fine dust visible on a light gray wooden floor, soft blue and white colour grading, realistic, minimal and clean, empty floor area on the left for a product to be added later, empty top area for text, vertical 9:16. No logos, no brand names, no text, no appliances in the empty area.
```

**Avoid:** logo หรือตัวหนังสือในภาพ, เครื่องใช้ไฟฟ้าที่หน้าตาเหมือนสินค้าคู่แข่ง, ห้องรก, สีจัดเกินจริง, ลำแสงเฉียงสีน้ำเงิน, มือหรือเท้าที่ผิดรูป

**วางสินค้าและ logo:** วางรูปหุ่นยนต์ดูดฝุ่นจริงที่ช่องว่างใต้เตียงด้านซ้าย ปรับเงาให้ตรงกับแสงจากหน้าต่าง วาง logo สีขาวบน Navy band ด้านล่างใน Figma / Photoshop ห้ามแก้ logo ด้วย AI
