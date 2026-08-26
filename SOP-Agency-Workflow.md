# SOP: Agency-Style Marketing Workflow

**ทีมการตลาด Bwell — วาง Claude เป็น Workflow Coordinator ตรงกลาง แล้วให้เครื่องมือแต่ละตัวรับช่วงงานในสิ่งที่ตัวเองถนัด**

| | |
|---|---|
| **เวอร์ชัน** | 1.0 |
| **วันที่บังคับใช้** | สิงหาคม 2026 |
| **ผู้ดูแลเอกสาร** | Marketing Team Lead |
| **รอบทบทวน** | ทุกไตรมาส |

---

## 1. วัตถุประสงค์

SOP ฉบับนี้กำหนดขั้นตอนมาตรฐานให้ทีมการตลาดทำงานแบบ Agency ครบวงจร ตั้งแต่รับ Brief จนถึงส่ง Report โดยเปลี่ยนจากการทำงานแบบ

> ใช้ AI ช่วยทำงานทีละอย่าง → Copy ข้อมูลย้ายเครื่องมือเอง → Context หายระหว่างทาง

ไปเป็น

> **วาง Claude ไว้กลาง Workflow ถือ Context ของแคมเปญตั้งแต่ต้นจนจบ แล้วเชื่อมเครื่องมือแต่ละตัวเข้ามารับช่วงงานผ่าน Connector และ MCP**

ผลลัพธ์ที่ต้องการ:

- งาน 6–7 ก้อนที่เคยแยกกัน กลายเป็น **End-to-End Workflow เดียว**
- ลดเวลา Copy ข้อมูล / ย้าย Context / ส่งงานต่อระหว่างเครื่องมือ
- ทุกแคมเปญมี Context กลาง (Goal, Target Audience, Key Message) ที่ทุก Stage อ้างอิงชุดเดียวกัน
- คนยังเป็นผู้ตัดสินใจในจุดสำคัญเสมอ (Budget, การเผยแพร่, การเปิด Ads)

**ขอบเขต**: ใช้กับงาน Campaign ทุกประเภท — Product Launch, Seasonal, Double Digit, Always-on Content

---

## 2. Operating Model: Claude คือ "ตัวประสาน Workflow" ไม่ใช่เครื่องมือที่ 6

หลักคิดสำคัญ — Claude ไม่ได้มาแทน 5 เครื่องมือ แต่ทำหน้าที่เหมือน **Marketing Coordinator** ของ Agency:

| หน้าที่ของ Claude | รายละเอียด |
|---|---|
| ถือ Context กลาง | Goal, Target Audience, Key Message, Budget Frame ของแคมเปญ — อ้างอิงชุดเดียวตลอดทุก Stage |
| แตกโจทย์ | รับ Brief แล้วแตกเป็นงานย่อยของแต่ละตำแหน่ง / แต่ละเครื่องมือ |
| เตรียมงานส่งต่อ | Creative Brief, Ad Copy, Caption, Audience Hypothesis — พร้อมส่งให้เครื่องมือปลายทางทันที |
| สั่งงานเครื่องมือ | ผ่าน Connector / MCP — Generate ภาพ, ดึงข้อมูล Analytics ได้จากแชทเดียว |
| สรุปผลกลับ | อ่าน Pattern จากตัวเลข แล้วร่าง Executive Summary: เกิดอะไรขึ้น → เพราะอะไร → รอบต่อไปควรทำอะไร |

**กติกาเหล็ก 3 ข้อ**

1. **Context อยู่ที่ Claude ที่เดียว** — ทุกแคมเปญเริ่มด้วย Campaign Context Doc (ดูภาคผนวก A) แล้วทุก Stage ทำงานต่อจากแชท/Project เดียวกัน ห้ามเปิดแชทใหม่กลางแคมเปญโดยไม่พก Context ไปด้วย
2. **เครื่องมือทำสิ่งที่ตัวเองถนัด** — ไม่ใช้ Claude ทำภาพ ไม่ใช้ Higgsfield คิดกลยุทธ์ ไม่ใช้ Hootsuite วิเคราะห์ Conversion
3. **Human Approval Gate ข้ามไม่ได้** — จุดที่กระทบเงินหรือกระทบสาธารณะ (ดูข้อ 6) ต้องมีคนตรวจและกดยืนยันเองเสมอ

---

## 3. Tool Stack และหน้าที่ในแต่ละช่วง

```
Brief → Content → Creative → Publishing → Ads → Analytics → Report
  │        │         │           │          │        │         │
  └─ Claude ┴─ Claude ┴ Higgsfield ┴ Hootsuite ┴ Meta Ads ┴─ GA4 ──┴ Looker Studio + Claude
                    (Claude เป็นจุดเชื่อมตรงกลางตลอดสาย)
```

| # | เครื่องมือ | ถนัดอะไร | รับช่วงตอนไหน | เชื่อมกับ Claude อย่างไร |
|---|---|---|---|---|
| 0 | **Claude** | ถือ Context, คิดกลยุทธ์, เขียน Copy, แตกงาน, สรุป Insight | ทุก Stage | — (ศูนย์กลาง) |
| 1 | **Higgsfield** | Generate ภาพนิ่ง + วิดีโอสำหรับ Creative | Production หลังได้ Concept | **MCP โดยตรง** — Generate จากในแชทเดิมได้เลย |
| 2 | **Hootsuite** | รวม Social Account, วาง Content Calendar, Schedule Post | หลัง Content + Creative เสร็จ | Connector / Copy จาก Handoff Package |
| 3 | **Meta Ads** | สร้างและบริหาร Paid Campaign บน Facebook / Instagram | ต่อยอด Content ที่ Perform ดี | Claude เตรียม Ad Copy, Creative Angle, Audience Hypothesis, A/B Plan — คนเปิด Campaign เอง |
| 4 | **GA4** | ติดตามพฤติกรรมหลังคลิก — Page View, ปุ่ม, สมัคร, Conversion | ตลอดช่วงแคมเปญรัน | Connector ดึงตัวเลข หรือ Export กลับมาให้ Claude อ่าน |
| 5 | **Looker Studio** (Data Studio) | รวมข้อมูลหลายแหล่งเป็น Dashboard หน้าเดียว | ปลายแคมเปญ + Report ประจำเดือน | Claude อ่านตัวเลขจาก Dashboard แล้วร่าง Executive Summary |

> **หมายเหตุ**: Google เปลี่ยนชื่อ Data Studio เป็น **Looker Studio** แล้ว — ใน SOP นี้ใช้ชื่อ Looker Studio แต่หมายถึงเครื่องมือเดียวกัน

**ทำไม GA4 ถึงสำคัญกว่า Like/Click**: ยอด Like หรือ Click บอกได้แค่ Content Performance แต่ GA4 บอกต่อว่า Traffic ที่ได้มา **สร้างผลลัพธ์ทางธุรกิจจริงหรือเปล่า** — นี่คือจุดที่ Marketing เชื่อมจาก Content Performance → Business Outcome

---

## 4. Roles & RACI

Mapping ตำแหน่งในทีม (ตามโครงสร้าง Bwell Marketing Team 10 ตำแหน่ง) เข้ากับแต่ละ Stage:

| Stage | Accountable (A) | Responsible (R) | Consulted (C) | Claude ช่วยอะไร |
|---|---|---|---|---|
| 1. Brief Intake | Marketing Strategist | Marketing Strategist | ทุกตำแหน่งที่เกี่ยว | แตก Brief, ตั้งคำถามที่ข้อมูลขาด |
| 2. Strategy & Content | Marketing Strategist | Content Marketing Manager | Creative Director | Campaign Concept, Content Plan, Caption |
| 3. Creative Production | Creative Director | Graphic Designer / Video Content Creator | Content Marketing Manager | Creative Brief + Prompt สำหรับ Higgsfield |
| 4. Publishing | Content Marketing Manager | Content Marketing Manager | — | Copy สุดท้าย + ตารางโพสต์พร้อมวาง |
| 5. Paid Ads | Performance Marketing Specialist | Performance Marketing Specialist | Marketing Strategist | Ad Copy, Audience Hypothesis, A/B Plan |
| 6. Measurement | Marketing Data Analyst | Marketing Data Analyst | Performance Specialist | อ่าน Pattern, ตรวจ Anomaly |
| 7. Report & Retro | Marketing Strategist | Marketing Data Analyst | ทุกตำแหน่ง | Executive Summary + Next Experiment |

> ทีมเล็กที่คนเดียวถือหลายหมวก: ใช้ตารางนี้เป็น "หมวกที่ต้องสลับใส่" — SOP ยังใช้ได้เหมือนเดิม เพราะ Claude ช่วยรับบทตำแหน่งที่ขาดผ่าน Skill `bwell-marketing-team`

---

## 5. Workflow หลัก 7 Stage

### Stage 1 — Brief Intake (รับ Brief และแตกโจทย์)

| | |
|---|---|
| **Owner** | Marketing Strategist |
| **Input** | Brief จากลูกค้า / ผู้บริหาร (ประโยคเดียวก็ได้ เช่น "เดือนหน้าเปิดตัวเมนูใหม่ อยากเพิ่มยอดจอง") |
| **Tool** | Claude |
| **Output** | Campaign Context Doc (ภาคผนวก A) ที่อนุมัติแล้ว |
| **SLA** | 1 วันทำการ |

**ขั้นตอน**

1. รับ Brief แล้ววางลงแชท Claude ของแคมเปญ (เปิดแชท/Project ใหม่ 1 แคมเปญ = 1 แชท)
2. ให้ Claude แตก Brief เป็น: **Goal (วัดได้) → Target Audience → Key Message → Campaign Idea → Content Plan → งานย่อยต่อตำแหน่ง**
3. ถ้าข้อมูลไม่พอ ให้ Claude ลิสต์คำถามกลับไปหาเจ้าของ Brief ก่อน — ห้ามเดา Budget, Timeline, KPI
4. Strategist ตรวจ + ปรับ แล้ว **บันทึกเป็น Campaign Context Doc** — เอกสารนี้คือ Single Source of Truth ของทุก Stage ถัดไป

**Definition of Done**: Context Doc มีครบ Goal / Audience / Key Message / KPI / Budget Frame / Timeline และ Strategist อนุมัติแล้ว

---

### Stage 2 — Strategy & Content (คิด Concept และ Content Plan)

| | |
|---|---|
| **Owner** | Content Marketing Manager |
| **Input** | Campaign Context Doc |
| **Tool** | Claude |
| **Output** | Content Calendar + Caption ทุกโพสต์ + Creative Brief |
| **SLA** | 1–2 วันทำการ |

**ขั้นตอน**

1. ในแชทเดิม ให้ Claude เสนอ Campaign Concept 2–3 ทาง พร้อมเหตุผล → ทีมเลือก 1
2. ให้ Claude ร่าง Content Calendar (วันที่ / Platform / Content Pillar / Format / หัวข้อ / CTA)
3. ให้ Claude เขียน Caption รายโพสต์ตาม Brand Voice (อ้างอิง Skill `bwell-content-copy` / `bwell-brand-guidelines-2026`)
4. ให้ Claude แปลง Concept เป็น **Creative Brief** สำหรับส่งต่อ Stage 3 — ระบุ Mood & Tone, Key Visual, Deliverables ครบ

**Definition of Done**: Content Manager ตรวจ Caption ทุกชิ้น + Creative Director อนุมัติ Creative Brief

---

### Stage 3 — Creative Production (ทำภาพ/วิดีโอด้วย Higgsfield)

| | |
|---|---|
| **Owner** | Creative Director |
| **Input** | Creative Brief จาก Stage 2 |
| **Tool** | Higgsfield (ผ่าน MCP ในแชทเดิม) |
| **Output** | ภาพนิ่ง / วิดีโอ ครบตาม Deliverables ทั้ง Organic และ Ads |
| **SLA** | 2–3 วันทำการ (รวมรอบแก้) |

**ขั้นตอน**

1. ให้ Claude แปลง Creative Brief เป็น Generation Prompt รายชิ้น (ระบุ Ratio ต่อ Platform: 1:1, 4:5, 9:16)
2. สั่ง Generate ผ่าน Higgsfield MCP **จากในแชทเดิม** — ไม่ต้อง Copy Prompt ย้ายเครื่องมือ
3. Creative Director คัดเลือก → สั่งแก้เป็นรอบ (Iterate ใน Context เดิม Claude จำ Feedback ก่อนหน้าได้)
4. ทำชุด Creative สำหรับ Ads แยกจาก Organic (เผื่อ A/B Test อย่างน้อย 2 Variant ต่อ Ad Set)
5. เก็บไฟล์ Final เข้าโฟลเดอร์กลางตาม Naming Convention (ข้อ 7)

**Definition of Done**: Creative ครบทุก Deliverable, ผ่านการตรวจ Brand (โลโก้/สี/ฟอนต์ถูกต้อง), มี Variant สำหรับ A/B

**⚠️ หมายเหตุค่าใช้จ่าย**: การ Generate ผ่าน MCP ใช้ Credit ของบัญชี Higgsfield — Creative Director คุมจำนวนรอบ Generate ให้อยู่ในงบ

---

### Stage 4 — Publishing (วางตารางโพสต์ด้วย Hootsuite)

| | |
|---|---|
| **Owner** | Content Marketing Manager |
| **Input** | Caption (Stage 2) + Creative (Stage 3) |
| **Tool** | Hootsuite |
| **Output** | โพสต์ Schedule ครบทุกช่องทางตาม Content Calendar |
| **SLA** | 0.5–1 วันทำการ |

**ขั้นตอน**

1. ให้ Claude ประกอบ **Publishing Package**: ตาราง วันที่-เวลา / Platform / Caption Final / ชื่อไฟล์ Creative / Link + UTM (ข้อ 7)
2. นำ Package เข้า Hootsuite — วาง Content Calendar และ Schedule Post ทุกช่องทาง
3. ตรวจ Preview ทุกโพสต์ (ตัวสะกด, ภาพถูกชิ้น, Link ถูก, เวลาถูก Timezone)
4. **🚦 Approval Gate**: Content Manager กดยืนยัน Schedule เอง — Claude เตรียมให้ได้ทุกอย่างแต่ไม่กดเผยแพร่แทน

**Definition of Done**: ทุกโพสต์อยู่ในสถานะ Scheduled และผ่านการตรวจ Preview แล้ว

---

### Stage 5 — Paid Ads (ต่อยอดเป็น Paid Media ด้วย Meta Ads)

| | |
|---|---|
| **Owner** | Performance Marketing Specialist |
| **Input** | Content ที่ Organic Engagement ดี + Creative Variants + Context Doc |
| **Tool** | Meta Ads Manager |
| **Output** | Campaign เปิดรันตาม Media Plan |
| **SLA** | 1 วันทำการหลังเลือก Content |

**ขั้นตอน**

1. หลังโพสต์รัน 2–3 วัน ให้ Claude ช่วยคัด Content ที่ Engagement ดีที่สุดมาต่อยอดเป็น Ads
2. ให้ Claude เตรียม **Ads Package**: Objective ที่แนะนำ, Ad Copy (Primary Text / Headline / Description), Creative Angle, Audience Hypothesis 2–3 ชุด, แผน A/B Testing, Budget Split แนะนำ
3. Performance Specialist ตั้ง Campaign ใน Meta Ads Manager ตาม Package
4. **🚦 Approval Gate**: **Budget, Targeting และการกดเปิด Campaign จริง — คนตรวจสอบและกดยืนยันเองเสมอ** ห้ามให้ระบบอัตโนมัติใดๆ เปิด Ads แทน
5. ติดตั้ง UTM ทุก Ad ตามมาตรฐานข้อ 7 เพื่อให้ GA4 อ่านผลได้

**Definition of Done**: Campaign Live, UTM ครบ, บันทึก Setup (Audience/Budget/Variant) กลับเข้าแชทแคมเปญเพื่อให้ Claude ถือ Context ต่อ

---

### Stage 6 — Measurement (วัดผลด้วย GA4)

| | |
|---|---|
| **Owner** | Marketing Data Analyst |
| **Input** | Traffic จาก Organic + Ads ที่ติด UTM |
| **Tool** | GA4 (+ Meta Ads Report) |
| **Output** | ข้อมูล Performance รายสัปดาห์กลับเข้าแชทแคมเปญ |
| **Cadence** | ทุกสัปดาห์ระหว่างแคมเปญรัน |

**ขั้นตอน**

1. ก่อนแคมเปญเริ่ม: ตรวจว่า GA4 Track Event สำคัญครบ (เปิดหน้า Product, กดปุ่มจอง/สมัคร, Conversion ตามเป้า)
2. ระหว่างรัน: ดึงตัวเลข GA4 + Meta Ads กลับมาให้ Claude ในแชทแคมเปญ (ผ่าน Connector หรือ Export CSV — ใช้ Skill `ai-analytic-ga4` / `meta-ads-analyzer` ช่วยวิเคราะห์ได้)
3. ให้ Claude อ่าน Pattern: Campaign ไหนทำผลงานดี, Creative ไหนเริ่มตก (Fatigue), Metric ไหนเปลี่ยนผิดปกติ
4. ถ้าพบปัญหา → Claude เสนอ Optimization → **คนตัดสินใจปรับใน Meta Ads เอง** (ย้อนใช้ Gate ข้อ 5)

**Definition of Done**: มีบันทึกผลรายสัปดาห์ในแชทแคมเปญ + Action ที่ตัดสินใจไปแล้วถูกจดไว้

---

### Stage 7 — Report & Retro (รวมข้อมูลใน Looker Studio แล้วให้ Claude สรุป)

| | |
|---|---|
| **Owner** | Marketing Data Analyst (Report) + Marketing Strategist (Retro) |
| **Input** | ข้อมูลครบแคมเปญจาก GA4, Meta Ads, Social |
| **Tool** | Looker Studio + Claude |
| **Output** | Dashboard + Executive Summary + Next Experiment List |
| **SLA** | ภายใน 3 วันทำการหลังจบแคมเปญ |

**ขั้นตอน**

1. รวมข้อมูลทุกแหล่งเข้า Looker Studio Dashboard (KPI หลักหน้าเดียว: Spend, Reach, CTR, CPC, Conversion, CPA/ROAS)
2. นำตัวเลข/Insight จาก Dashboard กลับมาให้ Claude ในแชทแคมเปญ
3. ให้ Claude ร่าง **Executive Summary** ตามโครง: **เกิดอะไรขึ้น → เพราะอะไร → รอบต่อไปควรทำอะไร**
4. **คนตรวจสอบตัวเลขและความถูกต้องอีกครั้งก่อนส่ง** — Claude ร่าง คนรับรอง
5. ทำ Retro 30 นาที: อะไรเวิร์ก / อะไรไม่เวิร์ก / รอบหน้าทดลองอะไร → บันทึกเป็น Learning เปิดแคมเปญหน้า

**Definition of Done**: Report ส่งผู้บริหาร/ลูกค้าแล้ว + Next Experiment List ถูกบันทึกเข้า Backlog

---

## 6. Human Approval Gates (จุดที่ต้องมีคนกดยืนยันเสมอ)

| Gate | Stage | ผู้อนุมัติ | เหตุผล |
|---|---|---|---|
| อนุมัติ Campaign Context Doc | 1 | Marketing Strategist | ทุก Stage อ้างอิงเอกสารนี้ ผิดตั้งแต่ต้น = ผิดทั้งสาย |
| อนุมัติ Creative Final | 3 | Creative Director | Brand Integrity |
| กดยืนยัน Schedule โพสต์ | 4 | Content Marketing Manager | เผยแพร่สู่สาธารณะ ย้อนกลับยาก |
| **เปิด Ads Campaign / ตั้ง Budget / ปรับ Targeting** | 5 | Performance Marketing Specialist | **กระทบเงินจริงโดยตรง** |
| รับรอง Report ก่อนส่ง | 7 | Data Analyst + Strategist | ตัวเลขต้องตรวจสอบได้ |

หลักการ: **Claude เตรียม → คนตรวจ → คนกด** — จุดไหนกระทบเงินหรือกระทบสาธารณะ ห้าม Automate ข้าม

---

## 7. Naming Convention & UTM Standard

Context ที่ส่งต่อได้ดี เริ่มจากตั้งชื่อให้เครื่องอ่านออกและคนเข้าใจตรงกัน

**Campaign Naming** (ใช้ทั้งใน Meta Ads, ไฟล์ Creative, Looker Studio):

```
{ปีเดือน}_{แบรนด์/สินค้า}_{แคมเปญ}_{Objective}
ตัวอย่าง: 2609_BWELL-CF8608_NewMenuLaunch_CONV
```

**ไฟล์ Creative**:

```
{Campaign}_{Platform}_{Format}_{Ratio}_{Variant}
ตัวอย่าง: 2609_NewMenuLaunch_IG_Reel_9x16_A.mp4
```

**UTM มาตรฐาน** (ทุก Link ที่ออกจาก Social และ Ads ต้องติด — ใช้ Skill `utm-campaign-planner` ช่วย Generate):

| Parameter | ค่าที่ใช้ | ตัวอย่าง |
|---|---|---|
| `utm_source` | platform ตัวเล็ก | `facebook`, `instagram`, `hootsuite` |
| `utm_medium` | `social` (organic) / `paidsocial` (ads) | `paidsocial` |
| `utm_campaign` | Campaign Name ตาม Convention | `2609_newmenulaunch` |
| `utm_content` | ระบุ Creative/Variant | `reel_9x16_a` |

> UTM ไม่ Standard = Data แตกใน GA4 = Stage 6–7 อ่านผลไม่ได้ — ถือเป็นข้อบังคับ ไม่ใช่ทางเลือก

---

## 8. ตัวอย่างการรันจริง: Campaign ร้านอาหาร 1 งาน

**Brief จากลูกค้า**: "เดือนหน้าจะเปิดตัวเมนูใหม่ อยากเพิ่มยอดจอง"

| Stage | สิ่งที่เกิดขึ้น |
|---|---|
| 1. Brief | Claude แตก Brief → Target: คนทำงานย่านใกล้ร้าน + คู่เดท / Goal: ยอดจองผ่านเว็บ +30% / Key Message: เมนูใหม่ Limited / Content Plan 12 โพสต์ 3 สัปดาห์ → Strategist อนุมัติ Context Doc |
| 2. Content | Claude เสนอ Concept 3 ทาง → เลือก "เปิดครัวโชว์จานแรก" → ได้ Calendar + Caption + Creative Brief |
| 3. Creative | ส่ง Brief ให้ Higgsfield ผ่าน MCP ในแชทเดิม → ได้ภาพเมนู Hero 4:5 + วิดีโอ Teaser 9:16 อย่างละ 2 Variant |
| 4. Publishing | Claude ประกอบ Publishing Package → วาง Schedule ใน Hootsuite → Content Manager ตรวจ Preview แล้วกดยืนยัน |
| 5. Ads | โพสต์ Teaser Engagement ดีสุด → Claude เตรียม Ads Package (Objective: Conversion — การจอง, Audience 3 ชุด, A/B Creative) → Specialist ตรวจ Budget แล้วกดเปิดเอง |
| 6. Measurement | GA4 ดูว่าคนเข้าเว็บ → เปิดหน้าเมนู → กดจอง เพิ่มขึ้นไหม / Claude ชี้ว่า Audience "คู่เดท" CPA ต่ำกว่าครึ่งหนึ่ง → ทีมโยก Budget |
| 7. Report | รวมข้อมูลใน Looker Studio → Claude สรุป: จองเพิ่ม +38%, Creative วิดีโอชนะภาพนิ่ง, รอบหน้าทดลอง Retarget คนที่เปิดหน้าเมนูแต่ไม่จอง |

งานที่เคยเป็น 6–7 ก้อนแยกกัน จบใน Workflow เดียว โดย Context ไม่หายระหว่างทาง

---

## 9. Adoption Roadmap — ไม่ต้องต่อครบทุกตัวตั้งแต่วันแรก

อย่าเริ่มด้วยคำถามว่า "ต้องต่อ Tool อะไรให้ครบ?" ให้เริ่มจาก **"งานซ้ำอะไรที่กินเวลาเรามากที่สุด?"**

| Pain Point ที่เจอ | เริ่มที่ | Phase |
|---|---|---|
| ติดคอขวดทำ Creative | Claude + Higgsfield (Stage 1–3) | 1 |
| โพสต์หลายช่องทางไม่ทัน | เพิ่ม Hootsuite (Stage 4) | 2 |
| เริ่มจริงจังกับ Paid Media | เพิ่ม Meta Ads + GA4 (Stage 5–6) | 3 |
| ต้องทำ Report ซ้ำทุกเดือน | เพิ่ม Looker Studio (Stage 7) | 4 |

วิธีขยาย: เริ่มจาก **1 Workflow ที่ทำซ้ำบ่อย → ทำให้ไหลลื่น → วัดเวลาที่ประหยัดได้ → แล้วค่อยต่อระบบเพิ่ม**

สิ่งที่ทำให้นักการตลาดหนึ่งคนทำงานได้เหมือนมีทีม ไม่ใช่การมี AI หรือ Tool เยอะที่สุด แต่คือการรู้ว่า **งานไหนควรให้ใครทำ และ Context จะถูกส่งต่อไปยังขั้นถัดไปอย่างไร**

---

## 10. ค่าใช้จ่ายและข้อจำกัดที่ต้องรู้

| รายการ | เงื่อนไข |
|---|---|
| Claude Free | ใช้ Custom Connector ได้ แต่จำกัด 1 Custom Connector — ทีมที่ต่อหลายเครื่องมือควรใช้ Paid Plan |
| Higgsfield MCP | ต้องมี Subscription ที่รองรับ และการ Generate ผ่าน MCP ใช้ Credit ของบัญชี |
| Hootsuite | มีช่วง Trial ก่อนเข้า Paid Plan |
| Meta Ads | ไม่มีค่าสมาชิก Ads Manager — จ่ายตาม Media Budget |
| GA4 Standard | ไม่มีค่า License |
| Looker Studio | เวอร์ชันทั่วไปไม่มีค่า License |
| **การเชื่อมระบบ** | ต้นทุนแฝงที่แท้จริง — บาง Automation ต้องพึ่ง API, MCP Server, Automation Platform หรือ Developer เพิ่ม |

> ต้นทุนไม่ได้ขึ้นกับว่ามี Tool กี่ตัว แต่ขึ้นกับว่าเราต้องการ Automation **"ลึกแค่ไหน"** — เริ่มตื้น (Claude ถือ Context + คนกดปุ่ม) แล้วค่อยลึกขึ้นเมื่อคุ้ม

---

## ภาคผนวก A — Campaign Context Doc (แบบฟอร์มรับ Brief)

ทุกแคมเปญต้องกรอกครบก่อนออกจาก Stage 1:

```
📋 Campaign Context Doc — [ชื่อแคมเปญ]

1. Background     : [ที่มาของโจทย์ / Brief ต้นฉบับ]
2. Goal (วัดได้)   : [เช่น ยอดจองผ่านเว็บ +30% ภายใน 30 วัน]
3. KPI            : [Primary + Secondary เช่น Bookings, CPA, CTR]
4. Target Audience: [Demographics / Interest / Behavior / Pain Point]
5. Key Message    : [1 ประโยคที่ทุก Content ต้องสื่อ]
6. Budget Frame   : [Media Budget / Production Budget / Credit Generate]
7. Timeline       : [เริ่ม–จบ + Milestone สำคัญ]
8. Channels       : [FB / IG / TikTok / เว็บไซต์ / อื่นๆ]
9. Do's & Don'ts  : [ข้อบังคับแบรนด์ / ข้อห้าม / Compliance]
10. อนุมัติโดย     : [ชื่อ + วันที่]
```

---

## ภาคผนวก B — Prompt Templates ต่อ Stage

**Stage 1 — แตก Brief**

```
นี่คือ Brief ที่ได้รับ: "[วาง Brief]"
ช่วยแตกเป็น Campaign Context Doc ตามแบบฟอร์มของทีม
ข้อไหนข้อมูลไม่พอ ให้ลิสต์คำถามที่ต้องถามเจ้าของ Brief กลับมา ห้ามเดาเอง
```

**Stage 2 — Content Plan**

```
จาก Campaign Context Doc ข้างต้น:
1) เสนอ Campaign Concept 3 ทาง พร้อมข้อดี-ข้อเสีย
2) เมื่อเลือกแล้ว ร่าง Content Calendar [X] โพสต์ ใน [Y] สัปดาห์
   ระบุ วันที่ / Platform / Pillar / Format / หัวข้อ / CTA
3) เขียน Caption ทุกโพสต์ตาม Brand Voice ของ Bwell
4) สรุปเป็น Creative Brief สำหรับส่งทีม Production
```

**Stage 3 — Generation Prompt**

```
จาก Creative Brief นี้ ช่วยเขียน Prompt สำหรับ Generate ภาพ/วิดีโอใน Higgsfield
แยกรายชิ้นตาม Deliverables ระบุ Ratio ต่อ Platform (1:1 / 4:5 / 9:16)
แล้ว Generate ผ่าน MCP ทีละชิ้น เริ่มจาก Hero Image ก่อน
```

**Stage 5 — Ads Package**

```
โพสต์นี้ Organic Performance ดีที่สุด: [แปะข้อมูลโพสต์]
ช่วยเตรียม Ads Package สำหรับ Meta Ads:
- Objective ที่เหมาะกับ Goal ใน Context Doc
- Ad Copy: Primary Text 3 แบบ / Headline 3 แบบ / Description
- Audience Hypothesis 3 ชุด พร้อมเหตุผล
- แผน A/B Testing และ Budget Split แนะนำ
(ฉันจะตรวจและตั้ง Campaign ใน Ads Manager เอง)
```

**Stage 7 — Executive Summary**

```
นี่คือตัวเลขสรุปแคมเปญจาก Looker Studio: [แปะข้อมูล/ตาราง]
ช่วยวิเคราะห์:
1) เกิดอะไรขึ้น — เทียบกับ KPI ใน Context Doc
2) เพราะอะไร — Pattern ไหนอธิบายผลลัพธ์ได้
3) รอบต่อไปควรทำอะไร — เรียง Next Experiment ตาม Impact
ร่างเป็น Executive Summary ไม่เกิน 1 หน้า ฉันจะตรวจตัวเลขก่อนส่งจริง
```

---

## ภาคผนวก C — Pre-Flight Checklist ก่อนแคมเปญ Live

- [ ] Campaign Context Doc อนุมัติแล้ว
- [ ] Caption ทุกโพสต์ผ่านการตรวจ Brand Voice
- [ ] Creative ครบทุก Ratio + มี Variant สำหรับ A/B
- [ ] ทุกโพสต์ Scheduled ใน Hootsuite และตรวจ Preview แล้ว
- [ ] GA4 Track Event สำคัญครบ (ทดสอบยิง Event จริงแล้ว)
- [ ] UTM ติดครบทุก Link ตามมาตรฐานข้อ 7
- [ ] Ads Campaign ตั้งค่าแล้วแต่ **ยังไม่กดเปิด** จนกว่า Specialist ยืนยัน Budget/Targeting
- [ ] Looker Studio Dashboard เตรียม Data Source เชื่อมแล้ว
- [ ] นัด Retro หลังจบแคมเปญลงปฏิทินแล้ว
