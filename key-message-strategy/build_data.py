# -*- coding: utf-8 -*-
"""
Bwell Key Message Strategy — single source data.
Generates data.json (for HTML playbook) and sku_matrix.csv / channel_rules.csv (for Google Sheet).

Sources (checked 2026-11-02):
- Bwell Product Master — Consolidated Review 2026-09-29 (Products / Prices / Product_Facts)
- Bwell สรุปผู้บริหาร 111 SKU (3 ต.ค. 2026) — stock (WICE 8 ก.ย. 2026), price conflicts, claim ban
- Bwell_Brand_Guidelines_2026.md + Bwell Project Knowledge — personality, pillars, persona, channel tone
- bwell.co.th homepage (fetched 2026-11-02) — website claims (supporting only)
"""
import json, csv, os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- BRAND
BRAND = {
    "essence_th": "สุขภาพดีในทุกมิติของชีวิต",
    "essence_en": "Total Wellness for Everyday Life",
    "corporate_tagline": "We Deliver The Top Brand Experiences. / เรามอบประสบการณ์แบรนด์ที่ดีที่สุดให้แก่คุณ",
    "brand_line_options": [
        {"th": "สุขภาพดี เริ่มที่บ้าน", "en": "Wellness Starts at Home", "note": "แนะนำ: ครอบคลุมทั้ง Home Environment และ Personal Wellness (ใช้ที่บ้าน/ที่ทำงาน)"},
        {"th": "บ้านที่ดูแลสุขภาพคุณ", "en": "A Home That Cares for You", "note": "เน้น Warm & Caring เหมาะกับ Family Protector"},
        {"th": "อากาศ น้ำ บ้าน และตัวคุณ ดูแลครบในแบรนด์เดียว", "en": "Air. Water. Home. You.", "note": "เน้น Ecosystem ใช้เป็น Sub-line ได้"},
    ],
    "umbrellas": [
        {"id": "home", "name": "Home Environment Wellness", "th": "สิ่งแวดล้อมในบ้านที่ดีต่อสุขภาพ",
         "promise": "อากาศ น้ำ และพื้นบ้านที่สะอาด ให้ทุกคนในบ้านใช้ชีวิตได้อย่างสบายใจ",
         "pillars": ["air", "water", "clean"]},
        {"id": "personal", "name": "Personal Wellness", "th": "สุขภาพและความมั่นใจของตัวคุณ",
         "promise": "ดูแลร่างกายและความมั่นใจของคุณ ทั้งเวลานั่งทำงาน เวลาเดินทาง และเวลาแต่งตัว",
         "pillars": ["body"]},
    ],
    "personality": [
        ["Trustworthy", "พูดตรง อิงข้อมูลที่ตรวจแล้ว ไม่ overclaim"],
        ["Warm & Caring", "เข้าใจความกังวลของคนในบ้าน พูดเหมือนเพื่อนที่เชี่ยวชาญ"],
        ["Empowering", "ให้ความรู้และช่วยเลือกรุ่น ไม่กดดันให้ซื้อ"],
        ["Modern & Premium", "ดูดี ทันสมัย และเข้าถึงได้"],
    ],
    "rtb": [
        ["ตั้งแต่ปี 2011", "อยู่ในตลาดสุขภาพในบ้านของไทยมาตั้งแต่ 2011 (ใช้คำว่า \"ตั้งแต่ปี 2011\" แทน \"13+ ปี\" ที่ไม่อัปเดต)"],
        ["ดูแลหลังการขายในไทย", "Showroom Crystal Design Center ชั้น 1 โซน K1, บริการหลังการขายและรับประกันในไทย, ไส้กรอง/อะไหล่หาซื้อได้"],
        ["ครบในแบรนด์เดียว", "Air · Water · Clean Home · Body ใช้แบรนด์เดียวทั้งบ้าน"],
        ["Buy-to-Own", "จ่ายครั้งเดียว เป็นเจ้าของทันที ไม่ผูกสัญญารายเดือน (ใช้กับเครื่องกรองน้ำเทียบโมเดลเช่ารายเดือน)"],
        ["Value for Premium", "คุณภาพระดับ premium ในราคาที่เข้าถึงได้กว่าแบรนด์ global (ห้ามระบุชื่อคู่แข่งในเชิงลบ)"],
    ],
    "message_pillars": [
        ["Health & Wellness", "ลงทุนกับสุขภาพคุณและครอบครัว เริ่มจากอากาศ น้ำ และบ้าน"],
        ["Science-backed Quality", "ใช้สเปก/มาตรฐาน/ผลทดสอบที่ผ่าน Product_Facts แล้วเท่านั้น"],
        ["Value for Money", "คุ้มค่า ใช้ได้นาน ดูแลหลังการขายได้"],
        ["Lifestyle Fit", "ออกแบบให้เข้ากับบ้านและชีวิตคนเมืองไทย"],
    ],
    "personas": [
        {"id": "P1", "name": "Urban Pro", "age": "28–38", "pain": "PM2.5, น้ำดื่ม, Office syndrome, ไม่มีเวลาทำความสะอาด", "channel": "IG · Facebook · Shopee · Lazada"},
        {"id": "P2", "name": "Family Protector", "age": "30–42", "pain": "อากาศ/น้ำที่ปลอดภัยสำหรับลูกและผู้สูงอายุ, บ้านสะอาด, ภูมิแพ้", "channel": "Facebook · LINE OA · Shopee"},
        {"id": "P3", "name": "Wellness Enthusiast", "age": "25–35", "pain": "อยากได้ของที่ช่วยเรื่องสุขภาพ ความสวย และ self-care", "channel": "TikTok · IG Reels · YouTube"},
    ],
}

# ---------------------------------------------------------------- CLAIM GOVERNANCE
CLAIM_RULES = {
    "status_legend": [
        ["CLAIM-READY", "ใช้ได้เฉพาะ job ที่ระบุใน Product_Facts (production_eligibility)", "ok"],
        ["BRAND-CONFIRMED", "Bass ยืนยันเป็นสเปกแบรนด์ ต้องผูก job + asset ก่อนใช้", "ok"],
        ["VERIFIED-SOURCE", "ตรวจข้อความจากหน้าเว็บตรงรุ่นแล้ว แต่ยัง BLOCKED_SKU_MAPPING ห้ามใช้จนกว่าจะผูก SKU/asset ของงาน", "warn"],
        ["UNVERIFIED", "ยังไม่มีหลักฐานตรงรุ่น เติมค่าห้ามใช้ ต้องส่ง Product Owner ตรวจ", "risk"],
        ["CONFLICT", "แหล่งข้อมูลขัดกัน ห้ามใช้จนกว่าจะตัดสิน", "risk"],
        ["BANNED", "ห้ามใช้จนกว่าจะมีผลแล็บ / legal อนุมัติ", "risk"],
        ["EXEC-DIRECTED", "Key message ที่ผู้บริหารสั่ง (5 พ.ย.) ใช้เป็นแกนสื่อสารได้ แต่ต้องแนบหลักฐาน (ใบรับรอง/สเปก) ก่อนขึ้นแอดและ Marketplace", "info"],
    ],
    "banned": [
        ["CADR / ตร.ม. / 99.9% / 99.97%", "สั่งงดตามสรุปผู้บริหาร 3 ต.ค. 2026 จนกว่าจะมีผลแล็บ แม้ CF-8428 จะมีค่า CADR ในหน้าเว็บ"],
        ["\"กรองอนุภาคเล็กกว่า PM2.5 ได้ 800 เท่า\"", "พบบนหน้าแรก bwell.co.th ไม่มีหลักฐานใน Master → ให้ทีมเว็บถอดหรือแนบผลทดสอบ"],
        ["\"กรองเค็มได้ 100%\" / \"การันตี 100%\"", "พบบนเว็บ ไม่มีหลักฐาน และขัด Words to Avoid"],
        ["\"รับรองโดยแพทย์/โรงพยาบาลชั้นนำ\"", "พบบนเว็บ ไม่มีรายชื่อหน่วยงานหรือเอกสาร"],
        ["\"วิจัยด้านการฟอกอากาศมากว่า 20 ปี\"", "ขัดกับ \"ก่อตั้ง 2011\" ใช้ \"ตั้งแต่ปี 2011\" แทน"],
        ["\"ฆ่าเชื้อ/ไวรัส X%\" , \"รักษา/บรรเทาอาการ\"", "เป็น health/medical claim ต้องมีผลแล็บและผ่าน legal (ชื่อเทคโนโลยี Virus Killer Triple Action ใช้ได้ แต่ห้ามระบุผลเป็นตัวเลขหรือรับรองผลการรักษา)"],
        ["\"Hot Air\" สำหรับ Ultra T20", "Product_Facts: UNVERIFIED ใช้ \"เป่าม็อบแห้งอัตโนมัติ\" แทน"],
        ["\"ดีที่สุด\" / \"เหนือกว่าทุกแบรนด์\" / \"อันดับ 1\"", "Overclaim ตาม Brand Guideline"],
        ["\"ขาเหล็ก\" (เก้าอี้)", "ขัดหน้าเว็บทุกรุ่น (ขา Aluminum) ใช้ \"ขาอะลูมิเนียม\" — ตรวจ 19 พ.ย. 2026"],
        ["\"เครื่องได้ NSF\" / \"มี NSF มาตรฐานอเมริกา\" (สื่อว่าทั้งเครื่อง)", "NSF รับรองเฉพาะไส้กรอง/กระบอกกรอง NSF/ANSI 42 ใช้ \"ไส้กรองและกระบอกกรองผ่านการรับรองตามมาตรฐาน NSF/ANSI 42 (สหรัฐอเมริกา)\""],
        ["\"ระบบความปลอดภัย 10 จุด\" (น้ำอุ่น)", "ไม่มีรายการ 10 จุด ใช้ \"5 ระบบความปลอดภัย\" และระบุชื่อครบ"],
        ["\"ดูดขอบมุมได้ชิดที่สุด\" (T20)", "Superlative ไม่มีผลเทียบ ใช้ \"ดูดชิดขอบผนังและมุมห้อง\""],
        ["\"น้ำดื่ม\" กับ BW-BB20PP", "เป็นเครื่องกรองน้ำใช้"],
        ["\"ป้องกันการบาดเจ็บ\" (เสื่อ)", "ไม่มีผลทดสอบ ใช้ \"ช่วยรองรับแรงกระแทก\""],
    ],
    "words_avoid": "ยิ่งไปกว่านั้น · อย่างแท้จริง · อย่างมีนัยสำคัญ · อย่างครบวงจร · ในยุคปัจจุบัน · ในโลกที่เปลี่ยนแปลง · ไม่อาจปฏิเสธได้ว่า · พิสูจน์แล้วว่า",
    "naming": [
        "เขียน \"Bwell\" เสมอ (ไม่ใช่ bwell / BWELL) ใส่ชื่อ + โลโก้ให้เห็นชัด โดยเฉพาะหมวด Ergo/Sport เพราะชื่อ \"Bewell\" แย่งผลค้นหา",
        "สรรพนามใช้ \"คุณ\" เท่านั้น",
        "ศัพท์เทคนิคเป็นภาษาอังกฤษ: HEPA, UV-C, PM2.5, BLDC, RO, UF, ELSD, LDS",
        "ราคาทุกตัวเลขต้องเช็กจากหน้า bwell.co.th ตรงรุ่น พร้อม URL และเวลาตรวจ ราคาในเอกสารนี้เป็น snapshot วันที่ 26 ก.ย. 2026",
    ],
}

# ---------------------------------------------------------------- CI (visual)
CI = [
    ["Brand Blue", "#0D99DB", "สีหลักปัจจุบัน (CI override 27 ก.ย. 2026) ใช้กับพื้นหลัง/graphic/panel ห้ามใช้เป็นสีตัวอักษรใน artwork"],
    ["Legacy Blue", "#005D9D / #008AD0", "Historical only ห้ามใช้ในงานใหม่ (ใน Profile ยังเขียน #005D9D ควรอัปเดต)"],
    ["Brand Gray", "#A8AAAD", "ข้อความรอง เส้นขอบ"],
    ["Headline on artwork", "#FFFFFF", "Headline ใช้สีขาวเท่านั้น ถ้าอ่านยากให้ใช้ soft shadow หรือ scrim"],
    ["Font: Electronics", "DB Helvethaica X", "Air / Water / Clean Home / Water Heater / Portable AC"],
    ["Font: Ergonomics & Sport", "Kanit", "เก้าอี้ หมอน เบาะ Foam Roller เสื่อ + โลโก้ Bwell Ergo"],
    ["Font: Beauty", "Poppins (EN) / Kanit (TH)", "Hair Styling + โลโก้ Bwell Beauty"],
    ["Logo", "TOP_LEFT", "Social 1080×1080 safe zone 54 px จากซ้ายและบน ใช้ไฟล์ official เท่านั้น"],
]

# ---------------------------------------------------------------- CHANNEL RULES (global)
CHANNELS = [
    {"id": "fb", "name": "Facebook Page", "funnel": "TOFU · MOFU", "objective": "Awareness, Education, Retargeting",
     "layer": "Pillar + Category message", "tone": "Informative + Inspirational, storytelling, Thai-EN mix",
     "structure": "Hook 1 บรรทัด → Pain → Benefit → RTB (feature/spec ที่ผ่านแล้ว) → CTA",
     "length": "Primary text 3–5 บรรทัดก่อน \"ดูเพิ่มเติม\" · Headline โฆษณา ≤ 40 ตัวอักษร",
     "cta": "ดูรุ่นที่เหมาะกับห้องคุณ / ทักแชท / ช้อปที่ Shopee-Lazada",
     "kpi": "ROAS ≥ 3× · CTR ≥ 1.5% · Frequency ≤ 3.5 · VTR ≥ 30%",
     "example": "\"ฝุ่นกลับมาแล้ว ห้องนอนลูกพร้อมหรือยัง\" → เลือกเครื่องฟอกอากาศตามขนาดห้อง"},
    {"id": "ig", "name": "Instagram", "funnel": "TOFU · MOFU", "objective": "Brand look & feel, Lifestyle",
     "layer": "Category message + SKU headline", "tone": "Visual-first, Modern & Premium",
     "structure": "ภาพ lifestyle ในบ้านจริง → Caption บรรทัดแรกคือ benefit → 3 bullet → CTA",
     "length": "บรรทัดแรก ≤ 125 ตัวอักษร (ก่อน fold) · Hashtag 3–5 ตัว",
     "cta": "ลิงก์ใน Bio / แตะสินค้า", "kpi": "Engagement rate, Saves, Profile visits",
     "example": "\"มุมทำงานที่หลังไม่ล้าตอนบ่าย\" + Bwell Ergo chair"},
    {"id": "tt", "name": "TikTok / Reels / Shorts", "funnel": "TOFU · MOFU", "objective": "Reach, Education (how-to / myth-busting ชนะ unboxing)",
     "layer": "SKU hook + Category pain", "tone": "Fun, relatable, ภาษาง่าย แต่ไม่ลดภาพลักษณ์แบรนด์",
     "structure": "Hook 0–3 วิ → Problem → Demo → Proof (spec ที่ผ่านแล้ว) → CTA",
     "length": "15–30 วิ (TOFU) · 45–60 วิ (how-to/MOFU) · ชื่อ Bwell + โลโก้ภายใน 3 วิแรก",
     "cta": "กดตะกร้า / ดูรุ่นในโปรไฟล์", "kpi": "Views ≥ 10K/คลิป · VTR ≥ 25% · Follower growth รายสัปดาห์",
     "example": "\"ใช้โหมด Dry ของแอร์แทนเครื่องลดความชื้นได้ไหม?\""},
    {"id": "line", "name": "LINE OA", "funnel": "BOFU · Retention", "objective": "CRM, Follow-up, Filter reminder, Offer",
     "layer": "SKU + Offer + After-sales", "tone": "Personal, conversational",
     "structure": "ทักทาย → เหตุผลที่ส่ง (ครบรอบเปลี่ยนไส้กรอง/โปร) → Offer + เงื่อนไข/วันหมดเขต → ปุ่มเดียว",
     "length": "ข้อความ ≤ 3 บรรทัด + Rich message 1 ภาพ · แยก record LINE OA จากช่องทางอื่นทุกแคมเปญ",
     "cta": "สั่งไส้กรอง / รับโค้ด / นัดดูสินค้าที่ Showroom", "kpi": "Open ≥ 25% · Click ≥ 5% · Block ≤ 5%",
     "example": "\"ครบ [X] เดือนแล้ว ถึงเวลาเปลี่ยนไส้กรอง [รุ่น] ของคุณ\""},
    {"id": "mp", "name": "Marketplace (Shopee / Lazada / TikTok Shop)", "funnel": "BOFU", "objective": "Conversion, Search ranking",
     "layer": "SKU (title + bullets + banner)", "tone": "Benefit-driven, keyword-rich, ชัดเจน",
     "structure": "Title = Bwell + คำค้นหมวด (TH) + รุ่น + จุดเด่นหลัก + Use case · Bullet 5 ข้อ: Benefit → Feature → Spec → For whom → After-sales",
     "length": "Title ≤ 100 ตัวอักษร (มาตรฐานภายในให้ใช้ได้ทุก platform) · Bullet ข้อละ ≤ 1 บรรทัด",
     "cta": "เพิ่มลงตะกร้า / ใช้โค้ดร้าน", "kpi": "CVR ≥ 3% · Review ≥ 4.7★ · Response ≥ 95%",
     "example": "Bwell เครื่องลดความชื้น BDH-30A ระบบคอมเพรสเซอร์ ลดความชื้นในห้อง กันเชื้อรา"},
    {"id": "web", "name": "Website PDP / SEO", "funnel": "MOFU · BOFU", "objective": "Education, Trust, Organic",
     "layer": "Category + SKU + spec table", "tone": "Educational, trustworthy",
     "structure": "H1 = ชื่อสินค้า + benefit · Overview 3 benefit · Tech Specs (จาก Product_Facts เท่านั้น) · FAQ · Compare รุ่น",
     "length": "Meta title ≤ 60 ตัวอักษร · Meta description ≤ 155", "cta": "ซื้อเลย / เปรียบเทียบรุ่น / ทัก LINE",
     "kpi": "Bounce ≤ 60% · Session ≥ 2 นาที · CVR ≥ 1.5%",
     "example": "แก้หน้าว่างก่อนยิงแอด: AP-8119US, AICSN-H3-Y03D, RO-500, T12, BDH-26, BDH-53"},
    {"id": "posm", "name": "POSM (Central / HomePro / Power Buy / Robinson)", "funnel": "BOFU (in-store)", "objective": "Stop shopper, ช่วย PC ปิดการขาย",
     "layer": "SKU headline + 3 icon claims", "tone": "สั้น อ่านได้ใน 3 วินาทีจากระยะ 2 เมตร",
     "structure": "Headline (benefit) → Sub-headline (ทำไมต้องรุ่นนี้) → 3 icon claims → ราคา/โปร (ถ้าอนุมัติ) → QR LINE OA/เว็บ",
     "length": "Headline ≤ 18 ตัวอักษร · Sub ≤ 40 · Icon claim ข้อละ ≤ 12 ตัวอักษร",
     "cta": "สแกน QR ดูรีวิว/รุ่นเปรียบเทียบ · สอบถาม PC", "kpi": "Sell-through ≥ 80%/เดือน · Revenue vs Target ≥ 100%",
     "example": "Headline \"ห้องแห้ง ผ้าแห้ง\" · Icons: คอมเพรสเซอร์ | โหมดตากผ้า | ตัดน้ำเต็มอัตโนมัติ [ตรวจรายรุ่น]"},
    {"id": "kol", "name": "KOL / Affiliate", "funnel": "TOFU · MOFU", "objective": "Trust, Real-home demo",
     "layer": "Category pain + SKU must-say", "tone": "เล่าจากการใช้จริงในบ้าน ไม่อ่านสคริปต์",
     "structure": "Must-say 3 ข้อ · Don't-say (Banned list) · Demo scene 1 ฉาก · ชื่อ Bwell + โลโก้ภายใน 3 วิแรก",
     "length": "ตาม brief แต่ละ platform", "cta": "ลิงก์ Affiliate / โค้ดเฉพาะ KOL",
     "kpi": "CPV, Engagement, Affiliate GMV, ROAS ต่อ KOL",
     "example": "ห้ามพูดตัวเลขสเปกที่ยังไม่ CLAIM-READY แม้ KOL จะเห็นในหน้าเว็บ"},
    {"id": "video", "name": "Clip Video (Brand / Product)", "funnel": "TOFU → BOFU", "objective": "Explain product, Build preference",
     "layer": "Pillar → SKU", "tone": "Warm, premium, ชัดเจน",
     "structure": "15s: Hook-Benefit-Product-CTA · 30s: Hook-Pain-Solution-Demo-CTA · 60s how-to: Myth-Fact-Demo-เลือกรุ่น-CTA",
     "length": "Super/คำบนจอ ≤ 7 คำต่อช็อต · End card: Logo + Brand line + CTA",
     "cta": "ช้อปที่ Shopee-Lazada / bwell.co.th", "kpi": "VTR, CPV, Brand lift",
     "example": "ซีรีส์ How-to รายหมวด (อนุมัติแล้วในสรุปผู้บริหาร): ELSD, ความเชื่อเรื่องน้ำ RO, UV-C, ค่าไฟแอร์เคลื่อนที่"},
    {"id": "pc", "name": "PC / Sales Script (Offline)", "funnel": "BOFU", "objective": "ปิดการขายหน้าร้าน",
     "layer": "Category RTB + SKU positioning", "tone": "Empowering ช่วยเลือก ไม่กดดัน",
     "structure": "ถาม 2 ข้อ (ขนาดห้อง/ปัญหา, คนในบ้าน) → แนะนำ 1 รุ่น + 1 รุ่นทางเลือก → After-sales → Close",
     "length": "Pitch ≤ 30 วินาทีต่อรุ่น", "cta": "ซื้อวันนี้ + ลงทะเบียน LINE OA รับการแจ้งเตือนไส้กรอง",
     "kpi": "Conversion ต่อ PC, Attach rate ไส้กรอง/อุปกรณ์เสริม", "example": "\"ห้องของคุณประมาณกี่ตารางเมตรครับ\" (ถามลูกค้าได้ แต่ห้ามเคลมพื้นที่รองรับจนกว่าจะผ่าน)"},
]

HEADLINE_RULES = [
    ["Headline", "พูด benefit ที่ลูกค้าได้ ไม่ใช่ชื่อ feature · ไม่มีตัวเลขสเปกที่ยังไม่ CLAIM-READY · ≤ 18 ตัวอักษร (POSM) / ≤ 40 (Digital)", "\"ห้องแห้ง ผ้าแห้ง\""],
    ["Sub-headline", "บอกว่าทำไมต้องรุ่นนี้ = Feature หลัก + For whom · ≤ 40 ตัวอักษร (POSM) / ≤ 90 (Digital)", "\"เครื่องลดความชื้นระบบคอมเพรสเซอร์ สำหรับห้องนอนและห้องนั่งเล่น\""],
    ["Body / Bullet", "Benefit → Feature → Spec slot [fact_id] → After-sales", "ระบบกรองหลายชั้น · ไส้กรองหาซื้อได้ที่ Bwell"],
    ["CTA", "คำกริยาเดียว ชัดว่ากดแล้วไปไหน", "\"เลือกรุ่นที่เหมาะกับห้องคุณ\""],
    ["Spec slot", "เขียนเป็น [ชื่อสเปก: ค่า · fact_id · สถานะ] ใน brief เท่านั้น ห้ามส่งขึ้นงานจริงจนสถานะเป็น CLAIM-READY", "[ความจุลดความชื้น: 30 L/วัน · BDH30A_DEHUMIDIFY_CAPACITY · VERIFIED-SOURCE]"],
]

FUNNEL = [
    ["TOFU", "ปัญหาและความรู้", "Pillar / Category pain", "Facebook, TikTok, KOL, Brand video", "Reach, VTR, CPV"],
    ["MOFU", "ทำไมต้อง Bwell / เลือกรุ่นไหน", "Category RTB + Compare รุ่น", "IG, Website, How-to clip, KOL review, Retargeting", "CTR, Session, Add-to-cart"],
    ["BOFU", "ทำไมต้องซื้อตอนนี้", "SKU headline + Offer (ราคา/โปรที่อนุมัติ)", "Marketplace, LINE OA, POSM, PC", "CVR, ROAS, Sell-through"],
    ["Retention", "ใช้ให้คุ้ม ดูแลต่อเนื่อง", "After-sales, ไส้กรอง, Trade-up", "LINE OA, CRM, Email", "Repeat rate, Filter attach"],
]

# ---------------------------------------------------------------- PILLARS & CATEGORIES
def S(label, value, status, fact=""):
    return {"label": label, "value": value, "status": status, "fact": fact}

PILLARS = [
    {"id": "air", "umbrella": "home", "name": "AIR", "th": "อากาศดีในบ้าน",
     "message": "อากาศในบ้านที่ทุกคนหายใจได้อย่างสบายใจ ทั้งเรื่องฝุ่น ความชื้น และความร้อน",
     "categories": [
        {"id": "ap", "name": "เครื่องฟอกอากาศ (ในบ้าน)", "font": "DB Helvethaica X",
         "key_message": "อากาศสะอาดในห้องที่ครอบครัวใช้เวลามากที่สุด",
         "pain": "ฝุ่น PM2.5 ช่วง พ.ย.–เม.ย., ลูกเล็ก/ผู้สูงอายุ/คนเป็นภูมิแพ้ในบ้าน, กังวลเชื้อโรคในอากาศ",
         "benefit": "ห้องนอนและห้องนั่งเล่นที่อากาศสะอาดขึ้น นอนหลับสบายขึ้น อุ่นใจเรื่องคนในบ้าน",
         "rtb": ["ระบบกรองหลายชั้น (เช่น Pre-filter / HEPA / Carbon) [จำนวนขั้นตอนตรงรุ่น: SPEC]",
                 "เทคโนโลยี Virus Killer Triple Action ของ Bwell [ยืนยันรุ่นที่มี + ห้ามระบุ % จนมีผลแล็บ]",
                 "ไส้กรองแท้และบริการหลังการขายในไทย", "Bwell อยู่ในตลาดเครื่องฟอกอากาศไทยตั้งแต่ปี 2011"],
         "persona": "P2 Family Protector (หลัก) · P1 Urban Pro",
         "competitor": "Xiaomi / Dreame / Philips: \"ไม่ใช่แค่สเปก แต่เป็นแบรนด์สุขภาพที่ดูแลคุณหลังการขายในไทย\"",
         "funnel": {"TOFU": "รู้ทันฝุ่น: ค่าฝุ่นสูงแล้วในบ้านปลอดภัยแค่ไหน", "MOFU": "วิธีเลือกเครื่องฟอกอากาศตามห้องและคนในบ้าน", "BOFU": "รุ่นแนะนำต่อห้อง + โปร/บันเดิลไส้กรอง"},
         "season": "Peak: พ.ย.–เม.ย. (ฝุ่น) · เริ่มดันตอนนี้ (พ.ย.)",
         "dont": "CADR, ตร.ม., 99.9%, 99.97%, 800 เท่า, รับรองโดยแพทย์"},
        {"id": "car", "name": "เครื่องฟอกอากาศในรถยนต์", "font": "DB Helvethaica X",
         "key_message": "อากาศที่ดีขึ้นในรถ ทุกการเดินทางของครอบครัว",
         "pain": "รถติดนาน ฝุ่นและกลิ่นในห้องโดยสาร, พาลูกเล็กเดินทาง",
         "benefit": "ห้องโดยสารที่อากาศดีขึ้น ติดตั้งง่าย ใช้ได้ทุกวัน",
         "rtb": ["ใช้ไฟจากรถ [พอร์ต USB/ที่จุดบุหรี่ตรงรุ่น: SPEC]", "ตั้งเวลาปิดได้ (G9) [VERIFIED-SOURCE]", "ไส้กรองเปลี่ยนได้ หาซื้อได้ที่ Bwell"],
         "persona": "P1 Urban Pro · P2 Family Protector",
         "competitor": "เทียบเครื่องฟอกในรถทั่วไป: เน้นแบรนด์สุขภาพ + ไส้กรองหาซื้อได้",
         "funnel": {"TOFU": "อากาศในรถตอนรถติด", "MOFU": "G8 vs G9 ต่างกันอย่างไร", "BOFU": "ของขวัญ/บันเดิลกับเครื่องในบ้าน (ระบายสต็อก G9)"},
         "season": "ตลอดปี · ช่วงเดินทางเทศกาล (ธ.ค., เม.ย.)",
         "dont": "ห้ามเคลม ionizer ใน G9 (ข้อมูลขัดกัน)"},
        {"id": "dh", "name": "เครื่องลดความชื้น", "font": "DB Helvethaica X",
         "key_message": "ลดความชื้นในห้อง ลดโอกาสเกิดเชื้อราและกลิ่นอับ",
         "pain": "ฝนตก/หลังน้ำลด บ้านอับชื้น ผ้าไม่แห้ง เชื้อราขึ้นผนัง-ตู้เสื้อผ้า",
         "benefit": "ห้องแห้งสบาย ผ้าแห้งในบ้าน ลดกลิ่นอับ",
         "rtb": ["ระบบคอมเพรสเซอร์ [ยืนยันรายรุ่น]", "โหมดตากผ้า / โหมดนอน / เซนเซอร์ความชื้น [ยืนยันรายรุ่น]",
                 "ความจุลดความชื้นต่อวันตรงรุ่น [SPEC]"],
         "persona": "P2 Family Protector · P1 Urban Pro (คอนโด)",
         "competitor": "Xiaomi ขึ้นราคาหลังจบโปร ก.ย. → BDH-12A ได้เปรียบราคา · Philips DE5305 ราคาต่ำกว่า BDH-53A ต้องสู้ด้วย value/บริการ",
         "funnel": {"TOFU": "ความชื้นกับ PM2.5 (คลิป Short เดิม 1.3M views)", "MOFU": "\"ใช้โหมด Dry ของแอร์แทนได้ไหม\" + วิธีเลือกความจุ", "BOFU": "BDH-30A / BDH-53A + โปร"},
         "season": "Peak: มิ.ย.–พ.ย. (ฝน/หลังน้ำลด) · ตอนนี้ปลายฝน",
         "dont": "ห้ามดัน BDH-26 / BDH-53 (ราคาเท่ารุ่น A แย่งยอดกันเอง)"},
        {"id": "ac", "name": "แอร์เคลื่อนที่", "font": "DB Helvethaica X",
         "key_message": "ความเย็นในห้องที่ติดแอร์ไม่ได้ ย้ายไปห้องไหนก็ได้",
         "pain": "คอนโด/บ้านเช่าติดแอร์ไม่ได้, ห้องร้อนเฉพาะจุด, หน้าร้อน",
         "benefit": "เย็นทันทีโดยไม่ต้องเจาะผนังติดตั้ง ย้ายห้องได้",
         "rtb": ["ขนาดความเย็นตรงรุ่น [BTU: SPEC]", "โหมดนอน / ล็อกป้องกันเด็ก [ยืนยันรายรุ่น]", "ล้อเลื่อนย้ายห้องได้ [ยืนยันรายรุ่น]"],
         "persona": "P1 Urban Pro (คอนโด/บ้านเช่า)",
         "competitor": "เทียบแอร์ติดผนัง: ไม่ต้องติดตั้ง ไม่ต้องขออนุญาตเจ้าของห้อง",
         "funnel": {"TOFU": "ห้องร้อนแต่ติดแอร์ไม่ได้", "MOFU": "ค่าไฟแอร์เคลื่อนที่จริงเท่าไร (content gap)", "BOFU": "BPAC-12B (ห้องใหญ่) / BPAC-09B"},
         "season": "Peak: มี.ค.–พ.ค. · เริ่มปูความรู้ ก.พ.",
         "dont": "ห้ามใช้ข้อมูล BPAC-09 / BPAC-12 (DO_NOT_USE) กับรุ่น B"},
     ]},
    {"id": "water", "umbrella": "home", "name": "WATER", "th": "น้ำสะอาดและปลอดภัย",
     "message": "น้ำที่ทั้งบ้านดื่มและใช้ได้อย่างมั่นใจ ตั้งแต่น้ำดื่มถึงน้ำอาบ",
     "categories": [
        {"id": "wp", "name": "เครื่องกรองน้ำดื่ม", "font": "DB Helvethaica X",
         "key_message": "น้ำดื่มสะอาดจากก๊อกในบ้าน จ่ายครั้งเดียว เป็นเจ้าของทันที",
         "pain": "ซื้อน้ำขวดทุกสัปดาห์, ไม่มั่นใจน้ำประปา, ไม่อยากผูกสัญญาเช่ารายเดือน",
         "benefit": "มีน้ำดื่มสะอาดในบ้านตลอด ลดการซื้อน้ำขวด ไม่มีค่าเช่ารายเดือน",
         "rtb": ["เลือกระบบได้ตามน้ำในบ้าน: RO / UV / UF", "Buy-to-own ไม่ผูกสัญญา", "ไส้กรองแท้หาซื้อได้ + แจ้งเตือนเปลี่ยนผ่าน LINE OA",
                 "ระดับการกรองตรงรุ่น [ไมครอน/ขั้นตอน: SPEC]"],
         "persona": "P2 Family Protector · P1 Urban Pro",
         "competitor": "Coway (subscription): \"ลงทุนครั้งเดียว ไม่ใช่จ่ายรายเดือนตลอดไป\"",
         "funnel": {"TOFU": "ความเชื่อเรื่องน้ำ RO (content gap)", "MOFU": "RO vs UV vs UF เลือกแบบไหนให้เหมาะกับบ้าน", "BOFU": "รุ่นแนะนำ + ราคาเท่ากันทุกช่องทาง"},
         "season": "ตลอดปี · หน้าน้ำเค็ม/น้ำประปามีกลิ่น (ก.พ.–เม.ย.)",
         "dont": "\"กรองเค็ม 100%\", ราคาที่ Power Buy ไม่ตรงเว็บ (รอปรับก่อนยิงแอด)"},
        {"id": "wh", "name": "เครื่องกรองน้ำใช้ (ทั้งบ้าน)", "font": "DB Helvethaica X",
         "key_message": "กรองน้ำใช้ตั้งแต่ต้นทาง ก่อนเข้าทุกก๊อกในบ้าน",
         "pain": "ตะกอน/สนิมในน้ำประปา, เครื่องใช้ไฟฟ้าและสุขภัณฑ์เป็นคราบ",
         "benefit": "น้ำใช้ทั้งบ้านสะอาดขึ้น ช่วยดูแลเครื่องทำน้ำอุ่นและสุขภัณฑ์",
         "rtb": ["กระบอกกรองขนาด 20 นิ้ว (จากชื่อรุ่น)", "ไส้ PP / Carbon block เปลี่ยนได้ [ยืนยันไส้ตรงรุ่น]"],
         "persona": "P2 Family Protector (บ้านเดี่ยว/ทาวน์โฮม)",
         "competitor": "ขายเป็นชุด Water ทั้งบ้าน: กรองน้ำใช้ + เครื่องทำน้ำอุ่น + กรองน้ำดื่ม",
         "funnel": {"TOFU": "น้ำประปาก่อนเข้าบ้านเป็นอย่างไร", "MOFU": "กรองน้ำใช้ต่างจากกรองน้ำดื่มอย่างไร", "BOFU": "Bundle กับเครื่องทำน้ำอุ่น"},
         "season": "บ้านใหม่/รีโนเวท",
         "dont": "ห้ามสื่อว่าดื่มได้ (เป็นเครื่องกรองน้ำใช้)"},
        {"id": "heat", "name": "เครื่องทำน้ำอุ่น / น้ำร้อน", "font": "DB Helvethaica X",
         "key_message": "อาบน้ำอุ่นสบาย พร้อมระบบป้องกันไฟรั่วที่ทำให้คุณอุ่นใจ",
         "pain": "กลัวไฟรั่วในห้องน้ำ, น้ำอุ่นไม่สม่ำเสมอ, ผู้สูงอายุ/เด็กในบ้าน",
         "benefit": "อาบน้ำอุ่นได้ทุกวันอย่างอุ่นใจ",
         "rtb": ["ระบบตัดไฟรั่ว ELSD [ค่าตัดไฟ/เวลาตัดตรงรุ่น: VERIFIED-SOURCE เฉพาะบางรุ่น]",
                 "มาตรฐานกันน้ำ IP25 [VERIFIED-SOURCE เฉพาะบางรุ่น]", "เลือกกำลังวัตต์ตามจำนวนจุดใช้/ห้องน้ำ"],
         "persona": "P2 Family Protector",
         "competitor": "Stiebel AQX 35/45 ราคาชน LUKA → สู้ด้วยความปลอดภัย + บริการในไทย",
         "funnel": {"TOFU": "ELSD คืออะไร ทำไมต้องมี (content gap)", "MOFU": "เลือกกี่วัตต์ดี", "BOFU": "LUKA (หลัก) · FELIX/ELKA/Konrad ผ่าน bundle"},
         "season": "หน้าหนาว (พ.ย.–ก.พ.) · ตอนนี้เริ่มได้",
         "dont": "ราคาห้างต่ำกว่าเว็บมาก (LUKA ที่ Power Buy) ต้องตัดสินนโยบายราคาก่อน"},
     ]},
    {"id": "clean", "umbrella": "home", "name": "CLEAN HOME", "th": "บ้านสะอาด ไม่เหนื่อย",
     "message": "พื้นบ้านสะอาดโดยใช้เวลาและแรงน้อยลง เพื่อให้คุณมีเวลาให้คนที่รัก",
     "categories": [
        {"id": "robot", "name": "หุ่นยนต์ดูดฝุ่น", "font": "DB Helvethaica X",
         "key_message": "บ้านสะอาดทุกวัน โดยที่คุณแทบไม่ต้องลงมือ",
         "pain": "ทำงานทั้งวัน ไม่มีเวลาดูดฝุ่น-ถูพื้น, มีสัตว์เลี้ยง/เด็กเล็ก",
         "benefit": "คืนเวลาให้คุณ บ้านสะอาดสม่ำเสมอ",
         "rtb": ["ระบบนำทางทำแผนที่บ้าน [LDS/Gyro ตรงรุ่น]", "สั่งงานผ่านแอป [ยืนยันรายรุ่น]",
                 "Ultra T20: แท่น All-in-One ซักม็อบ-เป่าแห้ง-เติมน้ำ-เก็บฝุ่นอัตโนมัติ [CLAIM-READY เฉพาะ job]"],
         "persona": "P1 Urban Pro · P2 Family Protector",
         "competitor": "Dreame / Xiaomi / Dyson รุ่นใหม่อยู่ที่ ฿33k–53k · Bwell อยู่ช่วง ฿8k–18k → \"ครบฟังก์ชันที่ใช้จริง ในราคาที่เข้าถึงได้\"",
         "funnel": {"TOFU": "ถ้าไม่ต้องถูพื้นเองอีกเลย จะเอาเวลาไปทำอะไร", "MOFU": "Y1 / L0 / L6C / T20 ต่างกันอย่างไร", "BOFU": "T20 (Hero) + KOL review"},
         "season": "ตลอดปี · 11.11 / 12.12 / ของขวัญปีใหม่",
         "dont": "\"Hot Air\" สำหรับ T20, แรงดูดของรุ่นอื่นที่ยังไม่ยืนยัน"},
        {"id": "vac", "name": "เครื่องดูดฝุ่นไร้สาย", "font": "DB Helvethaica X",
         "key_message": "ดูดฝุ่นสะอาดถึงฝุ่นละเอียด สำหรับบ้านที่มีคนเป็นภูมิแพ้",
         "pain": "ไรฝุ่น/ขนสัตว์ทำให้แพ้, เครื่องมีสายใช้ยาก",
         "benefit": "ทำความสะอาดได้ทุกมุมโดยไม่ต้องลากสาย ลดฝุ่นที่ทำให้แพ้",
         "rtb": ["ไร้สาย หยิบใช้ได้ทันที", "ระบบกรองหลายชั้น [ขั้นตอน/ระดับไมครอนตรงรุ่น: SPEC]", "Flomo Lite: ดูดและถูพื้นในเครื่องเดียว (จากชื่อสินค้า)"],
         "persona": "P2 Family Protector (บ้านมีภูมิแพ้/สัตว์เลี้ยง)",
         "competitor": "Dyson WashG1 / V12 จัดโปรใกล้ช่วงราคา T12 Allergy Plus → เน้นภูมิแพ้ + value + บริการ",
         "funnel": {"TOFU": "ไรฝุ่นในที่นอน/โซฟา", "MOFU": "T12 Allergy Plus vs Pro", "BOFU": "Flomo Lite (ระบายสต็อก) / T12 Plus"},
         "season": "ตลอดปี · ช่วงฝุ่น/ทำความสะอาดปีใหม่",
         "dont": "125,000 รอบ / 0.3 ไมครอน / 99.9% (ยังไม่ผ่าน Product_Facts) · หน้า T12 ยังว่าง"},
     ]},
    {"id": "body", "umbrella": "personal", "name": "BODY", "th": "สุขภาพและความมั่นใจของตัวคุณ",
     "message": "ดูแลร่างกายและความมั่นใจของคุณ ทั้งเวลานั่งทำงาน เดินทาง ออกกำลังกาย และแต่งตัว",
     "categories": [
        {"id": "chair", "name": "เก้าอี้เพื่อสุขภาพ (Bwell Ergo)", "font": "Kanit",
         "key_message": "นั่งทำงานได้นานขึ้น โดยที่หลังและคอไม่ล้า",
         "pain": "Work from home/ออฟฟิศ นั่งนาน ปวดหลัง-คอ-บ่า (Office syndrome)",
         "benefit": "ท่านั่งที่ถูกต้อง สบายขึ้นตลอดวันทำงาน",
         "rtb": ["ออกแบบตามหลัก Ergonomic ปรับได้หลายจุด [จุดปรับตรงรุ่น: SPEC]", "อ้างอิงมาตรฐาน BIFMA [ยืนยันเอกสารรายรุ่น]",
                 "รับประกัน [ปี: SPEC — อยู่ใน migration backlog]", "ลองนั่งได้ที่ Showroom CDC"],
         "persona": "P1 Urban Pro",
         "competitor": "Bewell (ชื่อคล้าย): ต้องใส่ชื่อ \"Bwell Ergo\" + โลโก้ชัดเจนทุกชิ้นงาน",
         "funnel": {"TOFU": "สัญญาณว่าเก้าอี้คุณกำลังทำร้ายหลัง", "MOFU": "เลือกเก้าอี้ตามงบและสรีระ (5 รุ่น)", "BOFU": "ลองนั่งที่ Showroom + โปร/ผ่อน"},
         "season": "Mother's Day (พ.ค.) · Back to work (ม.ค.) · 11.11/12.12",
         "dont": "\"รักษา/ลดอาการออฟฟิศซินโดรม\" (medical claim) · ขนาด/น้ำหนักรับได้ (ยังไม่มีข้อมูล)"},
        {"id": "cush", "name": "หมอนและเบาะเพื่อสุขภาพ", "font": "Kanit",
         "key_message": "ปรับท่านั่งให้สบายขึ้น ทั้งที่โต๊ะทำงานและในรถ",
         "pain": "นั่งนาน ขับรถนาน เดินทางไกล เมื่อยหลัง-คอ",
         "benefit": "อัปเกรดเก้าอี้/เบาะรถที่มีอยู่ให้นั่งสบายขึ้นในราคาไม่สูง",
         "rtb": ["รูปทรงรองรับสรีระ [วัสดุตรงรุ่น: SPEC]", "ใช้ร่วมกับเก้าอี้เดิมหรือเบาะรถได้"],
         "persona": "P1 Urban Pro · ของขวัญ",
         "competitor": "ราคาต่ำเป็น entry สู่แบรนด์ Bwell Ergo",
         "funnel": {"TOFU": "ท่านั่งขับรถที่ถูกต้อง", "MOFU": "เลือกหมอน/เบาะตามจุดที่เมื่อย", "BOFU": "Set โต๊ะทำงาน / Set รถยนต์ / Add-on กับเก้าอี้"},
         "season": "ของขวัญ ปีใหม่ · เดินทางเทศกาล",
         "dont": "medical claim"},
        {"id": "sport", "name": "อุปกรณ์ออกกำลังกาย", "font": "Kanit",
         "key_message": "เริ่มดูแลร่างกายที่บ้านได้ทุกวัน",
         "pain": "ไม่มีเวลาไปยิม, กล้ามเนื้อตึงหลังนั่งทำงาน/ออกกำลังกาย",
         "benefit": "ยืดเหยียด คลายกล้ามเนื้อ และออกกำลังกายได้เองที่บ้าน",
         "rtb": ["Move: วัสดุ High Density NBR, 183 × 61 × 1.2 ซม. [VERIFIED-SOURCE]", "Matrix Foam Roller 2 ขนาด (13\" / 24\")"],
         "persona": "P3 Wellness Enthusiast",
         "competitor": "Bewell แย่งผลค้นหาหมวดฟิตเนส → ใส่ Bwell + โลโก้ชัด",
         "funnel": {"TOFU": "5 ท่าคลายหลังหลังเลิกงาน", "MOFU": "Foam roller ใช้อย่างไร", "BOFU": "Set Move + Matrix / Add-on กับเก้าอี้"},
         "season": "ปีใหม่ (New year resolution, ม.ค.)",
         "dont": "medical claim"},
        {"id": "beauty", "name": "อุปกรณ์จัดแต่งทรงผม (Bwell Beauty)", "font": "Poppins (EN) / Kanit (TH)",
         "key_message": "ผมสวยทรงที่ใช่ ทำเองได้ที่บ้านทุกวัน",
         "pain": "ไม่มีเวลาไปร้าน, กลัวผมเสียจากความร้อน, เครื่องหนักใช้ยาก",
         "benefit": "จัดทรงได้เองเร็วขึ้น เครื่องเบา ใช้ง่าย",
         "rtb": ["มอเตอร์ BLDC ในรุ่นไดร์/สไตล์เลอร์ (จากชื่อสินค้า)", "รุ่นดิจิทัล [ช่วงอุณหภูมิ/ระดับตรงรุ่น: SPEC]",
                 "น้ำหนักเครื่อง BDR-02 / BDR-03 / BDR-04 [VERIFIED-SOURCE]", "ขนาดแกนตรงรุ่นระบุในชื่อสินค้า (มม.)"],
         "persona": "P3 Wellness Enthusiast · ของขวัญ (Mother's Day)",
         "competitor": "Panasonic EH-HV70 ขึ้นราคา +36% → BDR-02 ดูคุ้มขึ้น · Dyson (premium) → \"ผลลัพธ์ทรงสวยในราคาที่เข้าถึงได้\"",
         "funnel": {"TOFU": "ลอนสวยใน 10 นาที (how-to)", "MOFU": "เลือกขนาดแกน 28 / 32 / 40 มม. ตามความยาวผม", "BOFU": "BDR-02 / BAW-02 + ของขวัญ"},
         "season": "Mother's Day (พ.ค.) · 11.11 / 12.12 · วาเลนไทน์",
         "dont": "\"ปกป้องผมจากความร้อน\" แบบไม่มีหลักฐาน · น้ำหนักกล่อง BDR-03 (CONFLICT)"},
     ]},
]

# ---------------------------------------------------------------- SKU MATRIX
# fields: cat, sku, name, price (website snapshot 26 Sep 2026), role, push, persona,
#         headline, sub, hook, mp, icons, kol, specs[list], note
P = "PUSH"; M = "MAINTAIN"; C = "PUSH VIA BUNDLE (สต็อกสูง)"; L = "HOLD ADS (สต็อกต่ำ)"; F = "FIX PAGE FIRST"; X = "DO NOT PUSH (legacy)"

SKUS = [
 # ---- AIR PURIFIER
 dict(cat="ap", sku="AP-P4019US", name="เครื่องฟอกอากาศกำจัดไวรัส รุ่น AP-P4019US", price="32,990", role="Flagship", push=M, persona="P2",
      headline="อากาศสะอาดสำหรับพื้นที่ใหญ่ของทั้งบ้าน", sub="เรือธงเครื่องฟอกอากาศ Bwell สำหรับห้องนั่งเล่นและพื้นที่รวมของครอบครัว",
      hook="ห้องนั่งเล่นคือที่ที่ทุกคนในบ้านอยู่นานที่สุด อากาศตรงนั้นเป็นอย่างไร",
      mp="Bwell เครื่องฟอกอากาศ AP-P4019US รุ่นเรือธง ห้องใหญ่ ระบบกรองหลายชั้น", icons="รุ่นเรือธง | กรองหลายชั้น | ดูแลในไทย",
      kol="รุ่นเรือธงของ Bwell · เหมาะกับพื้นที่รวมของครอบครัว · มีบริการหลังการขายและไส้กรองในไทย",
      specs=[S("พื้นที่รองรับ", "", "BANNED"), S("ระบบกรอง/เทคโนโลยีฆ่าเชื้อ", "", "UNVERIFIED")], note="Halo product ใช้ยกภาพแบรนด์ ไม่ต้องยิงแอดหนัก"),
 dict(cat="ap", sku="AP-H3029US", name="เครื่องฟอกอากาศกำจัดไวรัส รุ่น AP-H3029US", price="25,990", role="Premium", push=P, persona="P2",
      headline="อากาศสะอาดในห้องนอนของคนที่คุณรัก", sub="เครื่องฟอกอากาศระดับ premium สำหรับบ้านที่มีเด็ก ผู้สูงอายุ หรือคนเป็นภูมิแพ้",
      hook="ลูกนอนในห้องนี้ 8–10 ชั่วโมงทุกคืน",
      mp="Bwell เครื่องฟอกอากาศ AP-H3029US ห้องนอน บ้านมีเด็ก ผู้สูงอายุ ภูมิแพ้", icons="ห้องนอนลูก | กรองหลายชั้น | ไส้กรองแท้",
      kol="เหมาะกับห้องนอนเด็กและผู้สูงอายุ · ระบบกรองหลายชั้น · ไส้กรองแท้หาซื้อได้ที่ Bwell",
      specs=[S("HEPA grade + UV", "", "UNVERIFIED"), S("พื้นที่รองรับ", "", "BANNED")], note=""),
 dict(cat="ap", sku="CF-8428", name="เครื่องฟอกอากาศกำจัดไวรัส รุ่น CF-8428 (Compact Series)", price="17,990", role="Core", push=C, persona="P1",
      headline="เครื่องฟอกอากาศดีไซน์กะทัดรัด เข้ากับทุกมุมบ้าน", sub="Compact Series สำหรับห้องนอนและคอนโดที่พื้นที่จำกัด",
      hook="ห้องเล็กแค่ไหน ก็มีอากาศดีได้",
      mp="Bwell เครื่องฟอกอากาศ CF-8428 Compact ห้องนอน คอนโด ดีไซน์กะทัดรัด", icons="ดีไซน์กะทัดรัด | ห้องนอน/คอนโด | ดูแลในไทย",
      kol="ดีไซน์กะทัดรัด วางได้ทุกมุม · เหมาะกับคอนโดและห้องนอน · ไส้กรองหาซื้อได้",
      specs=[S("กำลังไฟ", "55 W", "VERIFIED-SOURCE", "CF8428_POWER"), S("CADR Pollen/Dust/Smoke", "192/160/153 CFM", "BANNED", "CF8428_CADR_*"),
             S("ไม่ก่อให้เกิดโอโซน", "", "UNVERIFIED")], note="สต็อก ~943 เครื่อง (~32 เดือน) ระบายผ่าน bundle ไส้กรอง/ของแถม"),
 dict(cat="ap", sku="AP-8119US", name="เครื่องฟอกอากาศกำจัดไวรัส รุ่น AP-8119US", price="11,990", role="Core", push=F + " → " + C, persona="P2",
      headline="อุ่นใจเรื่องอากาศในห้องที่ลูกใช้เวลามากที่สุด", sub="เครื่องฟอกอากาศกลุ่ม Virus Fighter สำหรับห้องนอนและห้องทำงาน",
      hook="ช่วงหวัดและฝุ่นมาพร้อมกัน ห้องลูกพร้อมหรือยัง",
      mp="Bwell เครื่องฟอกอากาศ AP-8119US ห้องนอน ห้องทำงาน กรองหลายชั้น", icons="ห้องนอน/ทำงาน | กรองหลายชั้น | ไส้กรองแท้",
      kol="เหมาะกับห้องนอนและห้องทำงาน · ระบบกรองหลายชั้น · มีไส้กรองเปลี่ยนที่ Bwell",
      specs=[S("UV-C + HEPA", "", "UNVERIFIED"), S("พื้นที่รองรับ", "", "BANNED")], note="สต็อกค้างมูลค่าสูงสุด (~1,160 เครื่อง) แต่หน้าเว็บว่าง → แก้หน้าเป็นอันดับ 1"),
 dict(cat="ap", sku="CF-8005", name="เครื่องฟอกอากาศกำจัดไวรัส รุ่น CF-8005", price="6,990", role="Entry", push=C, persona="P1",
      headline="เริ่มต้นดูแลอากาศในห้อง ในงบที่เข้าถึงได้", sub="เครื่องฟอกอากาศรุ่นเริ่มต้นสำหรับห้องนอนส่วนตัว",
      hook="เครื่องฟอกอากาศเครื่องแรก ควรเลือกอย่างไร",
      mp="Bwell เครื่องฟอกอากาศ CF-8005 ห้องนอน รุ่นเริ่มต้น ไส้กรองเปลี่ยนได้", icons="รุ่นเริ่มต้น | ห้องนอน | ไส้กรองแท้",
      kol="รุ่นเริ่มต้นราคาเข้าถึงได้ · เหมาะห้องนอนส่วนตัว · ไส้กรองหาซื้อได้",
      specs=[S("ระบบ UV", "", "UNVERIFIED")], note="สต็อก ~1,073 เครื่อง → bundle / ของขวัญ / trade-up"),
 dict(cat="ap", sku="AP-H2219S", name="เครื่องฟอกอากาศ PM2.5 รุ่น AP-H2219S", price="[ตรวจหน้าเว็บ]", role="Core (PM2.5)", push=L, persona="P1",
      headline="รับมือฝุ่น PM2.5 ในห้องนอนของคุณ", sub="เครื่องฟอกอากาศกลุ่ม PM2.5 สำหรับห้องนอนและคอนโด",
      hook="ค่าฝุ่นนอกบ้านสีแดง ในห้องคุณเป็นสีอะไร",
      mp="Bwell เครื่องฟอกอากาศ PM2.5 AP-H2219S ห้องนอน คอนโด ไส้กรองเปลี่ยนได้", icons="กลุ่ม PM2.5 | ห้องนอน | ไส้กรองแท้",
      kol="ออกแบบมาสำหรับช่วงฝุ่น PM2.5 · เหมาะห้องนอน/คอนโด · มีไส้กรองเปลี่ยน",
      specs=[S("HEPA grade", "", "UNVERIFIED")], note="ราคาได้เปรียบ Xiaomi 4 Pro หลังขึ้นราคา แต่สต็อกเหลือ ~36 และไส้กรองเหลือ 1 ชิ้น → restock ก่อนยิงแอด"),
 dict(cat="ap", sku="AP-M1536S", name="เครื่องฟอกอากาศ PM2.5 รุ่น AP-M1536S", price="[ตรวจหน้าเว็บ]", role="Entry (PM2.5)", push=L, persona="P1",
      headline="อากาศดีขึ้นในห้องเล็กของคุณ", sub="เครื่องฟอกอากาศ PM2.5 ขนาดเล็กสำหรับห้องส่วนตัว",
      hook="ห้องเล็ก งบไม่มาก แต่อยากหายใจสบาย",
      mp="Bwell เครื่องฟอกอากาศ PM2.5 AP-M1536S ห้องเล็ก ห้องนอน", icons="กลุ่ม PM2.5 | ห้องเล็ก | ไส้กรองแท้",
      kol="ขนาดเล็กสำหรับห้องส่วนตัว · ช่วงฝุ่นใช้ได้ทุกวัน · ไส้กรองหาซื้อได้",
      specs=[], note="สต็อกเหลือ ~6 เครื่อง"),
 # ---- CAR
 dict(cat="car", sku="G9", name="เครื่องฟอกอากาศในรถยนต์ รุ่น G9", price="4,990", role="Core (Car)", push=C, persona="P1",
      headline="อากาศดีขึ้นทุกครั้งที่ขึ้นรถ", sub="เครื่องฟอกอากาศในรถ ตั้งเวลาปิดได้ สำหรับคนที่อยู่บนถนนทุกวัน",
      hook="วันละ 2 ชั่วโมงในรถติด คุณหายใจอะไรอยู่",
      mp="Bwell เครื่องฟอกอากาศในรถยนต์ G9 ตั้งเวลาปิดได้ ไส้กรองเปลี่ยนได้", icons="สำหรับรถยนต์ | ตั้งเวลาปิด | ไส้กรองแท้",
      kol="ใช้ในรถทุกวัน · ตั้งเวลาปิดได้ · มีไส้กรองเปลี่ยน",
      specs=[S("ตั้งเวลาปิด", "2 / 4 ชม.", "VERIFIED-SOURCE", "G9_TIMER"), S("Ionizer", "", "CONFLICT")], note="สต็อก ~595 (~18 เดือน) → ของขวัญ/บันเดิลกับเครื่องในบ้าน"),
 dict(cat="car", sku="G8", name="เครื่องฟอกอากาศรถยนต์ รุ่น G8", price="2,990", role="Entry (Car)", push=M, persona="P1",
      headline="เพื่อนร่วมทางที่ช่วยดูแลอากาศในรถ", sub="เครื่องฟอกอากาศในรถรุ่นเริ่มต้น ติดตั้งง่าย",
      hook="ของขวัญปีใหม่ให้คนที่ขับรถทุกวัน",
      mp="Bwell เครื่องฟอกอากาศรถยนต์ G8 ติดตั้งง่าย รุ่นเริ่มต้น", icons="สำหรับรถยนต์ | ติดตั้งง่าย | ไส้กรองแท้",
      kol="ติดตั้งง่าย · ราคาเริ่มต้น · ไส้กรองหาซื้อได้", specs=[], note="เหมาะเป็นของขวัญ/ของแถม"),
 # ---- DEHUMIDIFIER
 dict(cat="dh", sku="BDH-12A", name="เครื่องลดความชื้น Bwell รุ่น BDH-12A", price="7,990", role="Entry", push=P, persona="P1",
      headline="ลาก่อนกลิ่นอับในห้องนอน", sub="เครื่องลดความชื้นรุ่นเริ่มต้นสำหรับห้องนอนและคอนโด",
      hook="ตู้เสื้อผ้ามีกลิ่นอับ ทั้งที่ซักผ้าทุกวัน",
      mp="Bwell เครื่องลดความชื้น BDH-12A ห้องนอน คอนโด ลดกลิ่นอับ กันเชื้อรา", icons="ห้องนอน/คอนโด | ลดกลิ่นอับ | รุ่นเริ่มต้น",
      kol="เหมาะห้องนอนและคอนโด · ลดความชื้นและกลิ่นอับ · ราคาเริ่มต้น",
      specs=[S("ความจุลดความชื้น", "", "UNVERIFIED")], note="โอกาสราคา vs Xiaomi Smart Dehumidifier ที่ขึ้นราคา"),
 dict(cat="dh", sku="BDH-30A", name="เครื่องลดความชื้น Bwell รุ่น BDH-30A", price="15,990", role="Core (Hero)", push=P, persona="P2",
      headline="ห้องแห้ง ผ้าแห้ง ทั้งหน้าฝน", sub="เครื่องลดความชื้นระบบคอมเพรสเซอร์ สำหรับห้องนั่งเล่นและบ้านครอบครัว",
      hook="ฝนตกทั้งสัปดาห์ ผ้าในบ้านไม่แห้งสักตัว",
      mp="Bwell เครื่องลดความชื้น BDH-30A ห้องนั่งเล่น ตากผ้าในบ้าน กันเชื้อรา", icons="ห้องแห้ง | ผ้าแห้ง | ลดเชื้อรา",
      kol="ช่วยให้ผ้าแห้งในบ้านช่วงฝน · ลดความชื้นและกลิ่นอับ · เหมาะห้องนั่งเล่น",
      specs=[S("ความจุลดความชื้น", "30 L/วัน", "VERIFIED-SOURCE", "BDH30A_DEHUMIDIFY_CAPACITY"), S("พื้นที่ใช้งาน", "20–40 m²", "BANNED", "BDH30A_ROOM_AREA")],
      note="แทน BDH-26 (ราคาเท่ากัน) · ยอด ส.ค. 27 เครื่อง"),
 dict(cat="dh", sku="BDH-53A", name="เครื่องลดความชื้น Bwell รุ่น BDH-53A", price="19,990", role="Premium", push=P, persona="P2",
      headline="จัดการความชื้นทั้งพื้นที่ใหญ่ในบ้าน", sub="เครื่องลดความชื้นความจุสูง สำหรับบ้านเดี่ยว ห้องใต้ดิน และพื้นที่หลังน้ำลด",
      hook="หลังน้ำลด ผนังยังชื้น กลิ่นยังไม่หาย",
      mp="Bwell เครื่องลดความชื้น BDH-53A ความจุสูง บ้านเดี่ยว หลังน้ำท่วม", icons="ความจุสูง | พื้นที่ใหญ่ | หลังน้ำลด",
      kol="รองรับพื้นที่ใหญ่ · เหมาะหลังน้ำลดและหน้าฝน · ทำงานต่อเนื่องได้",
      specs=[S("ความจุลดความชื้น", "", "UNVERIFIED"), S("WiFi", "", "UNVERIFIED")], note="แทน BDH-53 · คู่แข่ง Philips DE5305 ราคาต่ำกว่า"),
 dict(cat="dh", sku="BDH-26", name="เครื่องลดความชื้น Bwell รุ่น BDH-26", price="15,990", role="Legacy", push=X, persona="—",
      headline="(ใช้ข้อความของ BDH-30A)", sub="", hook="", mp="Bwell เครื่องลดความชื้น BDH-26", icons="", kol="",
      specs=[S("ความจุลดความชื้น", "26 L/วัน", "VERIFIED-SOURCE", "BDH26_DEHUMIDIFY_CAPACITY"), S("กำลังไฟ", "", "CONFLICT")],
      note="ราคาเท่า BDH-30A แต่ความจุน้อยกว่า → ลดราคาหรือเลิกขาย · หน้าเว็บว่าง"),
 dict(cat="dh", sku="BDH-53", name="เครื่องลดความชื้น Bwell รุ่น BDH-53", price="19,990", role="Legacy", push=X, persona="—",
      headline="(ใช้ข้อความของ BDH-53A)", sub="", hook="", mp="Bwell เครื่องลดความชื้น BDH-53", icons="", kol="", specs=[],
      note="ราคาเท่า BDH-53A → ลดราคาหรือเลิกขาย · หน้าเว็บว่าง"),
 # ---- PORTABLE AC
 dict(cat="ac", sku="BPAC-12B", name="แอร์เคลื่อนที่ Bwell รุ่น BPAC-12B", price="15,990", role="Core (Hero)", push=P, persona="P1",
      headline="เย็นทั้งห้อง โดยไม่ต้องเจาะผนัง", sub="แอร์เคลื่อนที่สำหรับห้องที่ใหญ่ขึ้น ย้ายห้องได้ตามการใช้งาน",
      hook="คอนโดห้ามติดแอร์เพิ่ม แต่ห้องทำงานร้อนมาก",
      mp="Bwell แอร์เคลื่อนที่ BPAC-12B ไม่ต้องติดตั้ง คอนโด ห้องทำงาน ย้ายห้องได้", icons="ไม่ต้องติดตั้ง | ย้ายห้องได้ | โหมดนอน",
      kol="ไม่ต้องเจาะผนังติดตั้ง · ย้ายห้องได้ · เหมาะคอนโด/บ้านเช่า",
      specs=[S("ขนาดความเย็น", "", "UNVERIFIED")], note="ดันแทน BPAC-12 (DO_NOT_USE)"),
 dict(cat="ac", sku="BPAC-09B", name="แอร์เคลื่อนที่ Bwell รุ่น BPAC-09B", price="13,990", role="Entry", push=M, persona="P1",
      headline="ความเย็นที่ย้ายตามคุณได้", sub="แอร์เคลื่อนที่สำหรับห้องนอนและห้องทำงานขนาดเล็ก",
      hook="นอนห้องไหน ความเย็นตามไปห้องนั้น",
      mp="Bwell แอร์เคลื่อนที่ BPAC-09B ห้องนอน ไม่ต้องติดตั้ง ย้ายห้องได้", icons="ไม่ต้องติดตั้ง | ห้องนอน | โหมดนอน",
      kol="ไม่ต้องติดตั้ง · เหมาะห้องนอน · มีโหมดนอนไม่รบกวน", specs=[S("ขนาดความเย็น", "", "UNVERIFIED")], note=""),
 # ---- WATER PURIFIER (drinking)
 dict(cat="wp", sku="RO-500", name="เครื่องกรองน้ำ RO แบบไร้ถัง (RO-500)", price="11,990", role="Flagship", push=F, persona="P2",
      headline="น้ำดื่มระบบ RO ในครัวคุณ ไม่ต้องมีถังเก็บน้ำ", sub="เครื่องกรองน้ำ RO แบบไร้ถัง ประหยัดพื้นที่ใต้ซิงก์",
      hook="ยกน้ำขวดขึ้นคอนโดทุกสัปดาห์ เลิกได้แล้ว",
      mp="Bwell เครื่องกรองน้ำ RO-500 ระบบ RO ไร้ถัง ประหยัดพื้นที่ ไม่ผูกสัญญา", icons="ระบบ RO | ไร้ถัง | ไม่ผูกสัญญา",
      kol="ระบบ RO แบบไร้ถัง ประหยัดพื้นที่ · จ่ายครั้งเดียวไม่ผูกสัญญา · ไส้กรองหาซื้อได้",
      specs=[S("ระดับการกรอง (ไมครอน)", "", "UNVERIFIED"), S("WiFi / แอป", "", "UNVERIFIED")], note="มี artwork อนุมัติ V10 (Feed 4:5 ไม่ใส่ราคา) · หน้าเว็บว่าง · ยอดจริง ~40 เครื่อง/เดือน"),
 dict(cat="wp", sku="BW-D10RO5", name="เครื่องกรองน้ำ ระบบ RO รุ่น BW-D10RO5", price="8,690", role="Core (RO)", push=C, persona="P2",
      headline="น้ำดื่มสะอาดระบบ RO สำหรับทั้งครอบครัว", sub="เครื่องกรองน้ำระบบ RO ติดตั้งใต้ซิงก์ จ่ายครั้งเดียว เป็นเจ้าของทันที",
      hook="ค่าน้ำขวดทั้งปีของบ้านคุณ เท่าไร",
      mp="Bwell เครื่องกรองน้ำ ระบบ RO BW-D10RO5 น้ำดื่ม ครอบครัว ไม่ผูกสัญญา", icons="ระบบ RO | น้ำดื่มครอบครัว | ไม่ผูกสัญญา",
      kol="ระบบ RO · เหมาะครอบครัว · ไม่มีค่าเช่ารายเดือน", specs=[S("จำนวนขั้นตอน", "", "UNVERIFIED")],
      note="สต็อก ~255 (~153 เดือน) · ราคา Power Buy สูงกว่าเว็บ 38% → ปรับราคาก่อน"),
 dict(cat="wp", sku="AICSN-H3-Y03D", name="เครื่องกรองน้ำ รุ่น AICSN-H3-Y03D", price="6,990", role="Core", push=F + " → " + C, persona="P1",
      headline="น้ำดื่มสะอาดจากก๊อก ในครัวขนาดกะทัดรัด", sub="เครื่องกรองน้ำดื่มสำหรับคอนโดและครัวขนาดเล็ก",
      hook="ครัวคอนโดเล็ก ก็มีเครื่องกรองน้ำได้",
      mp="Bwell เครื่องกรองน้ำ AICSN-H3-Y03D น้ำดื่ม คอนโด ไส้กรองเปลี่ยนได้", icons="น้ำดื่ม | คอนโด | ไส้กรองแท้",
      kol="ขนาดกะทัดรัด · เหมาะคอนโด · ไส้กรองหาซื้อได้", specs=[S("ระบบกรอง", "", "UNVERIFIED")],
      note="หน้าเว็บว่าง · สต็อก ~165 · Power Buy ขายต่ำกว่าเว็บ 22%"),
 dict(cat="wp", sku="BW-D10UV5", name="เครื่องกรองน้ำระบบ UV รุ่น BW-D10UV5", price="6,290", role="Core (UV)", push=C, persona="P2",
      headline="น้ำดื่มผ่านระบบ UV ให้คุณมั่นใจขึ้น", sub="เครื่องกรองน้ำระบบ UV สำหรับบ้านที่ต้องการคงแร่ธาตุในน้ำ",
      hook="RO หรือ UV บ้านคุณเหมาะกับแบบไหน",
      mp="Bwell เครื่องกรองน้ำ ระบบ UV BW-D10UV5 น้ำดื่ม ไม่ผูกสัญญา", icons="ระบบ UV | น้ำดื่ม | ไม่ผูกสัญญา",
      kol="ระบบ UV · จ่ายครั้งเดียว · ไส้กรองหาซื้อได้", specs=[S("คงแร่ธาตุ", "", "UNVERIFIED")],
      note="สต็อก ~223 · Power Buy สูงกว่าเว็บ 16%"),
 dict(cat="wp", sku="BW-D10UF5", name="เครื่องกรองน้ำระบบ UF รุ่น BW-D10UF5", price="3,990", role="Entry (UF)", push=P, persona="P1",
      headline="เริ่มดื่มน้ำกรองที่บ้าน ในงบที่คุ้มค่า", sub="เครื่องกรองน้ำระบบ UF ติดตั้งง่าย ไม่ใช้ไฟฟ้า [ยืนยัน]",
      hook="เครื่องกรองน้ำเครื่องแรก งบไม่ถึง 4 พัน",
      mp="Bwell เครื่องกรองน้ำ ระบบ UF BW-D10UF5 น้ำดื่ม ติดตั้งง่าย คุ้มค่า", icons="ระบบ UF | ติดตั้งง่าย | คุ้มค่า",
      kol="ระบบ UF · ราคาคุ้มค่า · ติดตั้งง่าย", specs=[S("ไม่ใช้ไฟฟ้า", "", "UNVERIFIED")], note="Power Buy สูงกว่าเว็บ 33%"),
 dict(cat="wp", sku="BW-D103", name="เครื่องกรองน้ำ รุ่น BW-D103", price="2,490", role="Entry", push=P, persona="P1",
      headline="น้ำกรองสะอาด เริ่มต้นได้ง่าย", sub="เครื่องกรองน้ำรุ่นเริ่มต้นสำหรับครอบครัวเล็กและหอพัก",
      hook="งบหลักพัน ก็มีน้ำกรองดื่มที่บ้าน",
      mp="Bwell เครื่องกรองน้ำ BW-D103 รุ่นเริ่มต้น หอพัก ครอบครัวเล็ก", icons="รุ่นเริ่มต้น | ติดตั้งง่าย | ไส้กรองแท้",
      kol="รุ่นเริ่มต้น · ติดตั้งง่าย · ไส้กรองหาซื้อได้", specs=[S("ระบบกรอง", "", "UNVERIFIED")], note="Power Buy สูงกว่าเว็บ 40%"),
 # ---- WHOLE HOUSE
 dict(cat="wh", sku="BW-BB20CTO", name="เครื่องกรองน้ำใช้ขนาด 20 นิ้ว รุ่น BW-BB20CTO", price="5,790", role="Core", push=C, persona="P2",
      headline="กรองน้ำใช้ตั้งแต่ต้นทาง ก่อนเข้าทุกก๊อก", sub="เครื่องกรองน้ำใช้ 20 นิ้ว ลดตะกอนและกลิ่นสำหรับทั้งบ้าน [ยืนยันไส้]",
      hook="คราบเหลืองในอ่างล้างหน้า มาจากไหน",
      mp="Bwell เครื่องกรองน้ำใช้ 20 นิ้ว BW-BB20CTO กรองทั้งบ้าน ตะกอน กลิ่น", icons="กรองทั้งบ้าน | 20 นิ้ว | ไส้เปลี่ยนได้",
      kol="กรองน้ำใช้ทั้งบ้าน · ช่วยดูแลเครื่องทำน้ำอุ่นและสุขภัณฑ์ · ไส้เปลี่ยนได้", specs=[S("ชนิดไส้ (Carbon/PP)", "", "UNVERIFIED")],
      note="สต็อก ~246 · bundle กับเครื่องทำน้ำอุ่น"),
 dict(cat="wh", sku="BW-BB20PP", name="เครื่องกรองน้ำใช้ขนาด 20 นิ้ว รุ่น BW-BB20PP", price="5,190", role="Entry", push=M, persona="P2",
      headline="ดักตะกอนในน้ำใช้ ก่อนถึงห้องน้ำ", sub="เครื่องกรองน้ำใช้ 20 นิ้ว ไส้ PP สำหรับดักตะกอน",
      hook="น้ำประปามีตะกอน ทำอย่างไรดี",
      mp="Bwell เครื่องกรองน้ำใช้ 20 นิ้ว BW-BB20PP ดักตะกอน กรองทั้งบ้าน", icons="ดักตะกอน | 20 นิ้ว | ไส้เปลี่ยนได้",
      kol="ดักตะกอนน้ำใช้ · ติดตั้งก่อนเข้าบ้าน · ไส้เปลี่ยนได้", specs=[], note="นอกแคตตาล็อกโปรไฟล์ 3 ต.ค. · Power Buy สูงกว่าเว็บ 17%"),
]

# Water heaters — series template, per-wattage rows
HEATER = {
 "LUKA":   dict(role="Core (Hero)", headline="อาบน้ำอุ่นสบาย อุ่นใจทุกเช้า", sub="เครื่องทำน้ำอุ่น LUKA พร้อมระบบตัดไฟรั่ว ELSD สำหรับห้องน้ำทั่วไป",
                hook="ห้องน้ำคือห้องที่เสี่ยงไฟรั่วที่สุดในบ้าน", persona="P2"),
 "ELKA":   dict(role="Core", headline="น้ำอุ่นสม่ำเสมอ ปลอดภัยทุกครั้งที่อาบ", sub="เครื่องทำน้ำอุ่น ELKA ระบบตัดไฟรั่ว ELSD",
                hook="ELSD คืออะไร ทำไมเครื่องทำน้ำอุ่นต้องมี", persona="P2"),
 "FELIX":  dict(role="Core", headline="น้ำอุ่นที่ใช่ สำหรับทุกคนในบ้าน", sub="เครื่องทำน้ำอุ่น FELIX ระบบตัดไฟรั่ว ELSD",
                hook="เลือกเครื่องทำน้ำอุ่นกี่วัตต์ดี", persona="P2"),
 "Konrad": dict(role="Premium (น้ำร้อน)", headline="น้ำร้อนเต็มกำลัง สำหรับบ้านที่ต้องการมากกว่า", sub="เครื่องทำน้ำร้อน Konrad กำลังสูง ระบบตัดไฟรั่ว ELSD",
                hook="บ้านหลายคน อาบน้ำต่อกัน น้ำร้อนพอไหม", persona="P2"),
}
HEATER_ROWS = [
 ("LUKA-3500W", "LUKA", "3,500 W", "3,190", L, True, "สต็อก ~21 · Power Buy ขาย ฿2,100 (−34%) ยังไม่แก้"),
 ("LUKA-4500W", "LUKA", "4,500 W", "3,390", P, False, "ราคา LUKA 4500W ขัดกันระหว่างแหล่ง · Power Buy −32%"),
 ("ELKA-3500W", "ELKA", "3,500 W", "4,990", M, False, ""),
 ("ELKA-5500W", "ELKA", "5,500 W", "5,190", C, True, "สต็อก ~395 (~237 เดือน)"),
 ("FELIX-3500W", "FELIX", "3,500 W", "5,390", C, False, "FELIX รวม 1,227 เครื่อง ขาย 0–1.3/เดือน"),
 ("FELIX-4500W", "FELIX", "4,500 W", "5,890", C, True, ""),
 ("FELIX-5500W", "FELIX", "5,500 W", "6,190", C, False, ""),
 ("Konrad-6500W", "Konrad", "6,500 W", "7,390", C, False, "สต็อก ~303 (~182 เดือน)"),
 ("Konrad-8000W", "Konrad", "8,000 W", "7,790", M, True, "แรงดันน้ำ 0.3–6 bar [VERIFIED-SOURCE]"),
]
for sku, series, watt, price, push, elsd_ok, note in HEATER_ROWS:
    t = HEATER[series]
    st = "VERIFIED-SOURCE" if elsd_ok else "UNVERIFIED"
    fid = sku.replace("-", "").replace("W", "").upper()
    tag = "" if elsd_ok else " [ยืนยัน ELSD/IP25 ตรงรุ่นก่อนใช้]"
    SKUS.append(dict(cat="heat", sku=sku, name=f"Bwell เครื่องทำน้ำ{'ร้อน' if series=='Konrad' else 'อุ่น'} {series} {watt}", price=price, role=t["role"], push=push, persona=t["persona"],
        headline=t["headline"], sub=t["sub"] + tag, hook=t["hook"],
        mp=f"Bwell เครื่องทำน้ำ{'ร้อน' if series=='Konrad' else 'อุ่น'} {series} {watt} ระบบตัดไฟรั่ว ELSD กันน้ำ IP25" + tag,
        icons="ตัดไฟรั่ว ELSD | กันน้ำ IP25 | " + watt + tag,
        kol=f"ระบบตัดไฟรั่ว ELSD · กันน้ำ IP25 · {watt} เลือกตามการใช้งาน" + tag,
        specs=[S("ELSD ตัดไฟรั่ว", "15 mA / ≤ 0.01 วิ", st, fid + "_ELSD_*" if elsd_ok else ""), S("IP rating", "IP25", st, fid + "_IP" if elsd_ok else "")],
        note=note))

SKUS += [
 # ---- ROBOT
 dict(cat="robot", sku="Ultra T20", name="หุ่นยนต์ดูดฝุ่นทำความสะอาด Bwell Ultra T20 OmniBase (BST20)", price="17,990", role="Hero / Flagship", push=P, persona="P1",
      headline="ดูด ถู ซัก เป่าแห้ง จบในแท่นเดียว", sub="Bwell Ultra T20 OmniBase แท่น All-in-One ที่ดูแลตัวเองได้ เพื่อให้คุณไม่ต้องลงมือ",
      hook="ครั้งสุดท้ายที่คุณล้างม็อบเอง คือเมื่อไร",
      mp="Bwell หุ่นยนต์ดูดฝุ่นถูพื้น Ultra T20 OmniBase ซักม็อบ เป่าแห้ง เก็บฝุ่นอัตโนมัติ", icons="ซัก-เป่าม็อบเอง | เก็บฝุ่นอัตโนมัติ | นำทางเลเซอร์",
      kol="แท่นซักม็อบและเป่าแห้งอัตโนมัติ · เก็บฝุ่นและเติมน้ำเอง · ยกม็อบอัตโนมัติเมื่อเจอพรม",
      specs=[S("ดูดฝุ่น + ถูพื้น", "✓", "CLAIM-READY", "T20_VACUUM_MOP"), S("ซักม็อบอัตโนมัติ", "✓", "CLAIM-READY", "T20_AUTO_MOP_WASH"),
             S("เป่าม็อบแห้งอัตโนมัติ (ไม่ใช่ Hot Air)", "✓", "CLAIM-READY", "T20_AUTO_MOP_DRY"), S("เติมน้ำ / เก็บฝุ่นอัตโนมัติ", "✓", "CLAIM-READY", "T20_AUTO_WATER_REFILL / T20_AUTO_DUST_COLLECTION"),
             S("นำทางเลเซอร์ + Front Line Laser", "✓", "CLAIM-READY", "T20_LASER_NAVIGATION / T20_FRONT_LINE_LASER"), S("ตรวจจับพรม Ultrasonic + ยกม็อบ", "✓", "CLAIM-READY", "T20_ULTRASONIC_CARPET / T20_AUTO_MOP_LIFT"),
             S("แรงดูดสูงสุด", "22,000 Pa", "BRAND-CONFIRMED", "T20_MAX_SUCTION_PRESSURE"), S("Hot Air drying", "", "BANNED", "T20_HOT_AIR_PENDING")],
      note="CLAIM-READY ผูกกับ job LINE OA 5 ต.ค. งานใหม่ต้องผูก job + asset ใหม่ · มี KOL clip (PAT) แล้ว"),
 dict(cat="robot", sku="L6C", name="หุ่นยนต์ดูดฝุ่น Bwell รุ่น L6C", price="17,990", role="Premium", push=M, persona="P1",
      headline="หุ่นยนต์ทำความสะอาดที่ทิ้งฝุ่นได้เอง", sub="หุ่นยนต์ดูดฝุ่นนำทางด้วยเลเซอร์ พร้อมแท่นเก็บฝุ่น [ยืนยัน]",
      hook="ไม่ต้องเทถังฝุ่นทุกวันอีกต่อไป",
      mp="Bwell หุ่นยนต์ดูดฝุ่น L6C นำทางเลเซอร์ แท่นเก็บฝุ่น ควบคุมผ่านแอป", icons="นำทางเลเซอร์ | เก็บฝุ่นเอง | สั่งผ่านแอป",
      kol="นำทางด้วยเลเซอร์ · มีแท่นเก็บฝุ่น · สั่งงานผ่านแอป", specs=[S("LDS LiDAR", "", "UNVERIFIED"), S("Auto dirt disposal", "", "UNVERIFIED")],
      note="ราคาเท่า T20 → ให้ T20 เป็นตัวหลัก L6C ใช้เป็นทางเลือก"),
 dict(cat="robot", sku="L0", name="หุ่นยนต์ดูดฝุ่น Bwell รุ่น L0", price="11,990", role="Core", push=P, persona="P1",
      headline="วางแผนทำความสะอาดทั้งบ้านด้วยแผนที่อัจฉริยะ", sub="หุ่นยนต์ดูดฝุ่นที่ทำแผนที่บ้านและทำความสะอาดเป็นระบบ",
      hook="หุ่นยนต์ที่รู้ว่าห้องไหนยังไม่ได้ทำความสะอาด",
      mp="Bwell หุ่นยนต์ดูดฝุ่น L0 ทำแผนที่บ้าน ควบคุมผ่านแอป", icons="ทำแผนที่บ้าน | สั่งผ่านแอป | ราคาคุ้มค่า",
      kol="ทำแผนที่บ้าน · สั่งงานผ่านแอป · คุ้มค่าในช่วงราคากลาง",
      specs=[S("แรงดูดสูงสุด", "2,000 Pa", "VERIFIED-SOURCE", "L0_SUCTION"), S("กำลังไฟ", "28 W", "VERIFIED-SOURCE", "L0_POWER"), S("LDS LiDAR", "", "UNVERIFIED")],
      note="HomePro ขาย −20%"),
 dict(cat="robot", sku="Y1", name="หุ่นยนต์ดูดฝุ่น Bwell รุ่น Y1", price="7,990", role="Entry", push=P, persona="P1",
      headline="หุ่นยนต์ดูดฝุ่นตัวแรกของบ้านคุณ", sub="หุ่นยนต์ดูดฝุ่นรุ่นเริ่มต้น ใช้ง่าย สำหรับคอนโดและบ้านขนาดเล็ก",
      hook="งบไม่ถึงหมื่น ก็มีผู้ช่วยทำความสะอาดได้",
      mp="Bwell หุ่นยนต์ดูดฝุ่น Y1 รุ่นเริ่มต้น คอนโด ใช้งานง่าย", icons="รุ่นเริ่มต้น | คอนโด | ใช้ง่าย",
      kol="รุ่นเริ่มต้นใช้ง่าย · เหมาะคอนโด · ราคาเข้าถึงได้", specs=[S("Gyroscope navigation", "", "UNVERIFIED"), S("น้ำหนัก/เสียง", "", "CONFLICT")],
      note="HomePro ขาย −20%"),
 # ---- CORDLESS VACUUM
 dict(cat="vac", sku="T12 Allergy Pro", name="เครื่องดูดฝุ่นไร้สาย รุ่น T12 Allergy Pro", price="19,990", role="Flagship", push=L + " · " + F, persona="P2",
      headline="สะอาดถึงฝุ่นละเอียด สำหรับบ้านที่มีคนแพ้ง่าย", sub="เครื่องดูดฝุ่นไร้สายรุ่นท็อป ออกแบบสำหรับบ้านที่มีคนเป็นภูมิแพ้",
      hook="จามทุกเช้า อาจเป็นเพราะที่นอนของคุณ",
      mp="Bwell เครื่องดูดฝุ่นไร้สาย T12 Allergy Pro ภูมิแพ้ ไรฝุ่น ระบบกรองหลายชั้น", icons="สำหรับภูมิแพ้ | ไร้สาย | กรองหลายชั้น",
      kol="ออกแบบสำหรับบ้านที่มีคนภูมิแพ้ · ไร้สายใช้ง่าย · ระบบกรองหลายชั้น", specs=[S("รอบมอเตอร์ / 0.3 ไมครอน / 99.9%", "", "BANNED")],
      note="สต็อกเหลือ 1 · หน้าเว็บว่าง"),
 dict(cat="vac", sku="T12 Allergy Plus", name="เครื่องดูดฝุ่นไร้สาย รุ่น T12 Allergy Plus", price="16,990", role="Core (Hero)", push=F + " → " + P, persona="P2",
      headline="ลดฝุ่นที่ทำให้แพ้ ทุกมุมบ้าน", sub="เครื่องดูดฝุ่นไร้สายสำหรับบ้านที่มีคนเป็นภูมิแพ้และสัตว์เลี้ยง",
      hook="ขนแมวบนโซฟา ดูดหมดในรอบเดียวไหม",
      mp="Bwell เครื่องดูดฝุ่นไร้สาย T12 Allergy Plus ภูมิแพ้ ขนสัตว์ ไร้สาย", icons="สำหรับภูมิแพ้ | ขนสัตว์ | ไร้สาย",
      kol="เหมาะบ้านมีภูมิแพ้และสัตว์เลี้ยง · ไร้สาย · ระบบกรองหลายชั้น", specs=[S("ระบบกรอง (ขั้นตอน)", "", "UNVERIFIED")],
      note="HomePro ขาย −30% · Dyson โปรใกล้ช่วงราคา"),
 dict(cat="vac", sku="Flomo Lite", name="เครื่องดูดฝุ่นพร้อมถูพื้น Bwell รุ่น Flomo Lite", price="9,990", role="Core", push=C, persona="P1",
      headline="ดูดและถูพื้นในเครื่องเดียว", sub="เครื่องดูดฝุ่นพร้อมถูพื้น ประหยัดเวลาทำความสะอาดพื้นแข็ง",
      hook="ดูดเสร็จต้องถูต่อ ใช้เวลาสองเท่า",
      mp="Bwell เครื่องดูดฝุ่นพร้อมถูพื้น Flomo Lite ดูดและถูในเครื่องเดียว", icons="ดูด+ถู | ประหยัดเวลา | พื้นแข็ง",
      kol="ดูดและถูพื้นในเครื่องเดียว · ประหยัดเวลา · เหมาะพื้นกระเบื้อง/ลามิเนต", specs=[S("แรงดูด (8000/11000 Pa)", "", "UNVERIFIED")],
      note="สต็อก ~362 (~19 เดือน)"),
 dict(cat="vac", sku="201A", name="เครื่องดูดฝุ่นไร้สาย รุ่น 201A", price="6,990", role="Entry", push=M, persona="P1",
      headline="หยิบปุ๊บ ดูดได้ทันที", sub="เครื่องดูดฝุ่นไร้สายรุ่นเริ่มต้นสำหรับงานทำความสะอาดประจำวัน",
      hook="ฝุ่นนิดเดียว ไม่อยากลากเครื่องใหญ่",
      mp="Bwell เครื่องดูดฝุ่นไร้สาย 201A รุ่นเริ่มต้น น้ำหนักเบา ใช้ประจำวัน", icons="ไร้สาย | ใช้ประจำวัน | รุ่นเริ่มต้น",
      kol="ไร้สายหยิบใช้ง่าย · ทำความสะอาดประจำวัน · ราคาเริ่มต้น", specs=[], note=""),
]

# Chairs (price ladder from website; color variants)
CHAIRS = [
 ("Bjorn", "26,990 / 27,990", "Flagship", M, "เก้าอี้ Ergonomic รุ่นท็อปของ Bwell Ergo", "เก้าอี้ที่คุณจะอยากนั่งทั้งวัน", "สำหรับคนที่ทำงานหน้าจอวันละ 8 ชั่วโมงขึ้นไป"),
 ("Agnes", "20,990 / 21,990", "Premium", M, "เก้าอี้ Ergonomic ระดับ premium ปรับได้ละเอียด", "รองรับทุกช่วงของวันทำงาน", "สำหรับคนทำงานที่บ้านเต็มเวลา"),
 ("Greta", "13,990 / 14,990", "Core (Hero)", P, "เก้าอี้ Ergonomic ที่สมดุลระหว่างฟังก์ชันและงบ", "หลังสบายขึ้น ตั้งแต่เช้าจนเลิกงาน", "สำหรับ Work from home และออฟฟิศ"),
 ("Astrid", "9,990 / 10,990 (ขาว)", "Core", P, "เก้าอี้ Ergonomic ดีไซน์ทันสมัย มีสีขาว", "มุมทำงานสวย นั่งสบาย", "สำหรับโต๊ะทำงานที่บ้านที่อยากให้สวยด้วย"),
 ("Stella", "6,990 / 7,990", "Entry", P, "เก้าอี้ Ergonomic รุ่นเริ่มต้นของ Bwell Ergo", "เก้าอี้เพื่อสุขภาพตัวแรกของคุณ", "สำหรับนักศึกษาและคนเริ่มทำงาน"),
]
for model, price, role, push, sub, headline, forwho in CHAIRS:
    SKUS.append(dict(cat="chair", sku=f"{model} (Black/Grey{'/White' if model=='Astrid' else ''})", name=f"Bwell เก้าอี้ Ergonomic รุ่น {model}", price=price, role=role, push=push + " · " + F, persona="P1",
        headline=headline, sub=f"{sub} {forwho}",
        hook="ตอนบ่ายสาม หลังคุณยังโอเคอยู่ไหม" if model in ("Greta", "Stella", "Astrid") else "ลงทุนกับสิ่งที่คุณนั่งวันละ 8 ชั่วโมง",
        mp=f"Bwell Ergo เก้าอี้เพื่อสุขภาพ Ergonomic Chair รุ่น {model} ทำงานที่บ้าน ออฟฟิศ", icons="Bwell Ergo | ปรับได้หลายจุด | ลองนั่งที่ Showroom",
        kol=f"ใส่ชื่อ \"Bwell Ergo {model}\" + โลโก้ภายใน 3 วิ · เล่าการนั่งทำงานจริง · ชวนลองนั่งที่ Showroom",
        specs=[S("จุดปรับ / ขนาด / น้ำหนักรับได้", "", "UNVERIFIED"), S("BIFMA", "", "UNVERIFIED"), S("รับประกัน", "", "UNVERIFIED")],
        note="สีเทา/ขาวแพงกว่าสีดำ ฿1,000 · คำอธิบายสั้นบนหน้าเว็บเป็นข้อความเครื่องฟอกอากาศ (CMS bug) · Tier ตามราคาเว็บ (Guideline เดิมจัด Stella เป็น Premium ขัดกับราคา → Bass ยืนยัน)"))

CUSH = [
 ("Ergonomic-Chair-Lumbar-Cushion", "เบาะรองหลังเพื่อสุขภาพ", "690", P, "หลังส่วนล่างมีที่พิง ตลอดวันทำงาน", "หลังล่างไม่ล้า แม้นั่งนาน", "หลังเมื่อยทุกบ่าย ลองเพิ่มสิ่งนี้ที่เก้าอี้", ""),
 ("Ergonomic-Chair-Seat-Cushion", "เบาะรองนั่งเพื่อสุขภาพ", "690", L, "กระจายน้ำหนักขณะนั่ง สบายขึ้นทั้งวัน", "นั่งนานแค่ไหนก็สบายขึ้น", "เก้าอี้แข็งไป แก้ได้ในราคาไม่ถึงพัน", "สต็อกเหลือ ~9"),
 ("Ergonomic-Footrest", "ที่วางเท้าเพื่อสุขภาพ", "990", C, "ปรับระดับเท้าให้ท่านั่งสมดุล", "ท่านั่งดีขึ้น เริ่มที่เท้า", "เท้าลอยตอนนั่งทำงาน อาจทำให้หลังล้า", "สต็อก ~344 → bundle กับเก้าอี้"),
 ("Ergonomic-Car-Lumbar-Cushion", "เบาะรองหลังสำหรับรถยนต์", "690", P, "รองรับหลังระหว่างขับรถนาน", "ขับไกลแค่ไหน หลังก็สบายขึ้น", "ขับรถกลับบ้านต่างจังหวัด 5 ชั่วโมง", ""),
 ("Ergonomic-Car-Neck-Cushion", "หมอนรองคอสำหรับรถยนต์", "690", L, "รองรับคอระหว่างเดินทาง", "คอสบาย ทุกการเดินทาง", "พักสายตาบนรถ แต่ตื่นมาปวดคอ", "สต็อก ~29 วัน"),
 ("Ergonomic-Travel-Neck-Pillow", "หมอนรองคอเพื่อสุขภาพ (Travel)", "490", P, "หมอนรองคอสำหรับเครื่องบินและรถทัวร์", "เดินทางไกล คอไม่ล้า", "ไฟลต์ยาวครั้งหน้า อย่าลืมสิ่งนี้", "ขายดีกว่าหมอนรถ (68.7 vs 32.3/เดือน)"),
]
for sku, nm, price, push, sub, headline, hook, note in CUSH:
    SKUS.append(dict(cat="cush", sku=sku, name=f"Bwell {nm}", price=price, role="Accessory / Entry", push=push, persona="P1",
        headline=headline, sub=sub, hook=hook, mp=f"Bwell Ergo {nm} ปรับท่านั่ง ทำงาน เดินทาง", icons="Bwell Ergo | รองรับสรีระ | ใช้ได้ทุกวัน",
        kol="ใส่ชื่อ Bwell Ergo ให้ชัด · เล่าจุดที่เมื่อยและการใช้จริง · ห้ามพูดว่ารักษาอาการ", specs=[S("วัสดุ", "", "UNVERIFIED")], note=note))

SKUS += [
 dict(cat="sport", sku="Move", name="Bwell เสื่อโยคะ รุ่น Move", price="299", role="Entry", push=P, persona="P3",
      headline="พื้นที่ออกกำลังกายของคุณ กางได้ทุกที่", sub="เสื่อโยคะ Bwell Move วัสดุ NBR ความหนาแน่นสูง",
      hook="5 ท่ายืดหลังหลังเลิกงาน บนเสื่อผืนเดียว",
      mp="Bwell เสื่อโยคะ Move NBR หนา 1.2 ซม. ออกกำลังกายที่บ้าน", icons="NBR หนาแน่นสูง | 183×61 ซม. | พกพาง่าย",
      kol="เล่าการใช้จริงที่บ้าน · ใส่ชื่อ Bwell ให้ชัด", specs=[S("วัสดุ", "High Density NBR", "VERIFIED-SOURCE", "MOVE_MATERIAL"), S("ขนาด", "183 × 61 × 1.2 ซม.", "VERIFIED-SOURCE", "MOVE_DIMENSIONS"), S("น้ำหนัก", "0.96 kg", "VERIFIED-SOURCE", "MOVE_WEIGHT")],
      note="ยอดบัญชี 409/ชิ้น ต่างจาก ladder 265 → ยืนยันยอด"),
 dict(cat="sport", sku="Matrix-13inch", name="Foam Roller รุ่น Matrix 13 นิ้ว", price="490", role="Entry", push=P, persona="P3",
      headline="คลายกล้ามเนื้อได้เองที่บ้าน", sub="Foam Roller ขนาด 13 นิ้ว พกพาง่าย",
      hook="กล้ามเนื้อตึงหลังวิ่ง คลายได้ใน 5 นาที", mp="Bwell Foam Roller Matrix 13 นิ้ว คลายกล้ามเนื้อ พกพา", icons="13 นิ้ว | พกพาง่าย | คลายกล้ามเนื้อ",
      kol="สาธิตท่าคลายกล้ามเนื้อ 1 ท่า", specs=[], note="ขายดีกว่า 24\" (39 vs 5.7/เดือน)"),
 dict(cat="sport", sku="Matrix-24inch", name="Foam Roller รุ่น Matrix 24 นิ้ว", price="990", role="Core", push=C, persona="P3",
      headline="คลายหลังทั้งแนว ด้วยโฟมขนาดยาว", sub="Foam Roller ขนาด 24 นิ้ว สำหรับหลังและขาทั้งแนว",
      hook="นั่งทั้งวัน หลังตึง ลองนอนบนสิ่งนี้", mp="Bwell Foam Roller Matrix 24 นิ้ว คลายหลัง ออกกำลังกายที่บ้าน", icons="24 นิ้ว | คลายหลัง | ใช้ที่บ้าน",
      kol="สาธิตท่าคลายหลัง", specs=[], note="สต็อก ~356 (~63 เดือน) → bundle กับ Move/เก้าอี้"),
]

BEAUTY = [
 ("BAW-02", "Bwell เครื่องจัดแต่งทรงผม BLDC 7 หัว รุ่น BAW-02", "5,990", "Flagship", L, "จบทุกทรงในเครื่องเดียว", "ม้วน เป่า แปรง ยืดผม ด้วยมอเตอร์ BLDC 7 หัว", "7 หัว ทำได้กี่ทรงในเช้าเดียว", "BLDC | 7 หัว | ม้วน-เป่า-ยืด", "สต็อกเหลือ ~12 (~4 วัน)"),
 ("BDR-04", "Bwell เครื่องหนีบลมร้อน เป่าผม BLDC รุ่น BDR-04", "5,990", "Premium", L, "เป่าแห้งและยืดตรงในขั้นตอนเดียว", "เครื่องหนีบลมร้อน BLDC สำหรับผมตรงสวยแบบเร็วขึ้น", "ผมเปียกถึงผมตรงในขั้นตอนเดียว", "BLDC | เป่า+ยืด | ประหยัดเวลา", "สต็อก ~56 (~17 วัน) · น้ำหนัก 490 g [VERIFIED-SOURCE]"),
 ("BDR-03", "Bwell ไดร์เป่าผม BLDC ดิจิตอล BDR-03", "2,690", "Core", P, "ไดร์เบา เป่าเร็ว ทุกเช้า", "ไดร์เป่าผม BLDC ดิจิทัล น้ำหนักเบา", "ไดร์หนักจนเมื่อยแขน เปลี่ยนเถอะ", "BLDC | ดิจิทัล | น้ำหนักเบา", "น้ำหนัก 398 g [VERIFIED-SOURCE] · น้ำหนักกล่อง CONFLICT"),
 ("BDR-02", "Bwell ไดร์เป่าผม BLDC BDR-02", "1,690", "Entry (Hero)", P, "ไดร์ BLDC ในราคาที่เข้าถึงได้", "ไดร์เป่าผม BLDC น้ำหนักเบา สำหรับใช้ทุกวัน", "ไดร์ BLDC ไม่ต้องแพงเสมอไป", "BLDC | น้ำหนักเบา | ใช้ทุกวัน", "สต็อก ~285 (~19 วัน) · Panasonic ขึ้นราคา +36% · น้ำหนัก 410 g [VERIFIED-SOURCE]"),
 ("BSL-01", "Bwell หวีไดร์จัดแต่งทรงผม BLDC รุ่น BSL-01", "2,990", "Core", P, "เป่าและจัดทรงไปพร้อมกัน", "หวีไดร์ BLDC สำหรับวอลลุ่มและทรงสวยในขั้นตอนเดียว", "ผมแบนทั้งวัน แก้ได้ด้วยหวีไดร์", "BLDC | เป่า+แปรง | วอลลุ่ม", "ห้ามใช้ 38 มม. กับ BSL-01 (UNVERIFIED)"),
 ("BSL-02", "Bwell หวีลมร้อน ดิจิตอล 38 มม. รุ่น BSL-02", "2,190", "Core", L, "ปลายผมงุ้มสวย เป่าแล้วจบ", "หวีลมร้อนดิจิทัล แกน 38 มม.", "ปลายงุ้มแบบร้านทำผม ทำเองได้", "แกน 38 มม. | ดิจิทัล | ปลายงุ้ม", "สต็อกเหลือ ~20 (~7 วัน)"),
 ("BCL-02", "Bwell เครื่องม้วนผมอัตโนมัติ ดิจิตอล 40 มม. รุ่น BCL-02", "2,490", "Core", P, "ลอนสวยอัตโนมัติ มือใหม่ก็ทำได้", "เครื่องม้วนผมอัตโนมัติ ดิจิทัล แกน 40 มม.", "ม้วนผมไม่เป็น ให้เครื่องม้วนให้", "ม้วนอัตโนมัติ | 40 มม. | ดิจิทัล", ""),
 ("BCL-03", "Bwell เครื่องม้วนผม ดิจิตอล 28 มม. รุ่น BCL-03", "1,990", "Entry", P, "ลอนเล็กชัด สำหรับผมสั้นถึงประบ่า", "เครื่องม้วนผมดิจิทัล แกน 28 มม.", "ลอนเล็กแบบเกาหลี ใน 10 นาที", "แกน 28 มม. | ลอนเล็ก | ดิจิทัล", ""),
 ("BCL-04", "Bwell เครื่องม้วนผม ดิจิตอล 32 มม. รุ่น BCL-04", "2,490", "Core", P, "ลอนกลางธรรมชาติ ใช้ได้ทุกวัน", "เครื่องม้วนผมดิจิทัล แกน 32 มม.", "ลอนธรรมชาติไปทำงาน ไม่ดูตั้งใจเกินไป", "แกน 32 มม. | ลอนกลาง | ดิจิทัล", ""),
 ("BCL-05", "Bwell เครื่องม้วนผม ดิจิตอล 40 มม. รุ่น BCL-05", "2,790", "Core", P, "ลอนใหญ่พลิ้ว สำหรับผมยาว", "เครื่องม้วนผมดิจิทัล แกน 40 มม.", "ลอนใหญ่ปลายผมยาว แบบไปงาน", "แกน 40 มม. | ลอนใหญ่ | ดิจิทัล", ""),
 ("BCL-06", "Bwell เครื่องหนีบผมลอน 40 มม. รุ่น BCL-06", "2,190", "Core", P, "ลอนมาม่าเทรนด์ ทำเองได้", "เครื่องหนีบผมลอน แกน 40 มม.", "ลอนมาม่าใน 5 นาที", "หนีบลอน | 40 มม. | ทำเองง่าย", ""),
 ("BST-03", "Bwell เครื่องหนีบผม ดิจิตอล 40 มม. รุ่น BST-03", "2,190", "Core", P, "ผมตรงเงา หนีบไว ผมยาวก็จบเร็ว", "เครื่องหนีบผมดิจิทัล แผ่นหนีบ 40 มม.", "ผมยาวหนีบนาน ใช้แผ่นกว้างขึ้น", "แผ่น 40 มม. | ผมยาว | ดิจิทัล", ""),
 ("BST-02", "Bwell เครื่องหนีบผม ดิจิตอล 23 มม. รุ่น BST-02", "1,690", "Entry", P, "หนีบตรงถึงโคน ผมสั้นก็ง่าย", "เครื่องหนีบผมดิจิทัล แผ่นหนีบ 23 มม.", "ผมสั้น หน้าม้า หนีบให้เป๊ะ", "แผ่น 23 มม. | ผมสั้น/หน้าม้า | ดิจิทัล", ""),
]
for sku, nm, price, role, push, headline, sub, hook, icons, note in BEAUTY:
    SKUS.append(dict(cat="beauty", sku=sku, name=nm, price=price, role=role, push=push, persona="P3",
        headline=headline, sub=sub, hook=hook, mp=f"{nm.replace('Bwell ', 'Bwell Beauty ')}", icons=icons,
        kol="ใส่ชื่อ Bwell Beauty + โลโก้ · สาธิตก่อน-หลังจริง · ห้ามเคลมปกป้องผมจากความร้อนแบบไม่มีหลักฐาน",
        specs=[S("ช่วงอุณหภูมิ / ระดับความร้อน", "", "UNVERIFIED")], note=note))

# ---------------------------------------------------------------- EXECUTIVE DIRECTION (สรุปแนวทางทำ Content @5/11/69)
# Source: Key_Message.docx from management, 5 Nov 2026. Overrides category key messages, focus SKUs and FB/IG + TikTok formats.
# v1.2 (19 Nov 2026): every exec claim checked against bwell.co.th, Google Drive, Product Master and the NSF listing
# (see claim-evidence/). "km_exec" keeps the original wording from management; "km" is the approved wording to use.
# evidence rows: [claim from management, verdict, approved wording / rule, evidence + source]
# verdict: OK = ใช้ได้ · ADJUST = ใช้ได้แต่ปรับคำ/จำกัดรุ่น · STOP = ห้ามใช้ (ขัดข้อมูล/เสี่ยงกฎหมาย) · PENDING = ไม่พบหลักฐาน รอเอกสาร/ผู้บริหาร
EXEC_DATE = "5 พ.ย. 2026"
EVIDENCE_DATE = "19 พ.ย. 2026"
EVIDENCE_LEGEND = [
    ["OK", "มีหลักฐาน ใช้ได้เลย", "ok"],
    ["ADJUST", "ใช้ได้ แต่ต้องใช้คำที่ปรับแล้ว หรือจำกัดเฉพาะรุ่นที่ระบุ", "warn"],
    ["STOP", "หยุดใช้ทันที ขัดกับข้อมูลของ Bwell เอง หรือเสี่ยงผิดกฎหมาย", "risk"],
    ["PENDING", "ไม่พบหลักฐาน ห้ามใส่ใน copy จนกว่าจะได้เอกสาร/คำยืนยัน (แสดงเป็น [ช่องรอ] ใน copy)", "risk"],
]
EXEC = [
 dict(cats=["ap"], name="เครื่องฟอกอากาศ",
      km_exec=["เครื่องฟอกอากาศสำหรับเด็กและคนเป็นภูมิแพ้โดยเฉพาะ", "ปลอดภัย ไม่ปล่อยประจุไฟฟ้าระคายระบบทางเดินหายใจ"],
      km=["ออกแบบเพื่อบ้านที่มีเด็กและคนแพ้ง่าย", "ไม่มีระบบ Ionizer"],
      focus=["AP-M1536S", "AP-H2219S", "AP-P4019US"],
      series=["PM2.5 Series (AP-M1536S, AP-H2219S): กรอง PM2.5 · ดูดกลิ่นไม่พึงประสงค์ · เชื่อมต่อ WiFi (แอป Smartlife) · ไม่มีระบบฆ่าเชื้อ ใช้คำว่า \"กรอง\" เท่านั้น",
              "Virus Series (AP-P4019US): ฟอกอากาศ 8 ขั้นตอน (Pre-filter · Anti-virus · HEPA H13 · Charcoal · Zeolite · Potassium Permanganate · UV-C · TiO2) · กรองฝุ่น ดูดกลิ่น ฆ่าเชื้อด้วย UV-C จบในเครื่องเดียว"],
      fbig="3D แสดงขั้นตอนการฟอกภายในเครื่อง (อากาศไหลผ่านทีละชั้น)", tt="บรรยายสรรพคุณ (presenter/voice-over อธิบายจุดเด่นทีละข้อ)",
      mp="Bwell + เครื่องฟอกอากาศ + รุ่น + เด็ก/แพ้ง่าย + กรอง PM2.5/8 ขั้นตอน + ไม่มี Ionizer",
      posm="Headline: \"ออกแบบเพื่อบ้านที่มีเด็กและคนแพ้ง่าย\" · Icons: กรอง PM2.5 | ดูดกลิ่น | WiFi (PM2.5 Series) / 8 ขั้นตอน | UV-C ฆ่าเชื้อ | ไม่มี Ionizer (Virus Series)",
      kol="แม่ลูกอ่อน/ครอบครัวมีคนแพ้ง่าย · พูด 2 ข้อ: ออกแบบเพื่อบ้านที่มีเด็กและคนแพ้ง่าย + ไม่มีระบบ Ionizer · ห้ามพูดตัวเลข % ฆ่าเชื้อ",
      line="ต้นฤดูฝุ่น: แนะนำรุ่นตามห้องลูก + เตือนเปลี่ยนไส้กรอง",
      evidence=[
        ["สำหรับเด็กและคนเป็นภูมิแพ้โดยเฉพาะ", "ADJUST", "ใช้ \"ออกแบบเพื่อบ้านที่มีเด็กและคนแพ้ง่าย\" · ห้ามใช้ \"Allergist's Choice\"",
         "ไม่มีใบรับรองภูมิแพ้ (Allergy UK/AAFA/ECARF) มีแค่โบรชัวร์ Bwell เอง (Drive 1N9_c_gIjR9lBonrH8BbFhuVsHomFO-SH)"],
        ["ไม่ปล่อยประจุไฟฟ้าระคายระบบทางเดินหายใจ", "ADJUST", "ใช้ \"ไม่มีระบบ Ionizer\" · ห้ามเคลมโอโซน/ความปลอดภัยทางเดินหายใจจนกว่าจะมีผลทดสอบ",
         "Manual ทั้ง 3 รุ่นไม่มีฟังก์ชัน ion/anion/plasma แต่ไม่มีเอกสารที่ระบุตรงๆ และไม่มีผลทดสอบโอโซน"],
        ["ฟอกอากาศ 8 ขั้นตอน (AP-P4019US)", "OK", "ใช้ได้ พร้อมรายชื่อ 8 ขั้นตอน",
         "หน้าเว็บ AP-P4019US (อัปเดตเป็น 8 แล้ว) ตรงกับ manual และโบรชัวร์"],
        ["ฆ่าเชื้อ (AP-P4019US)", "ADJUST", "ใช้ \"ฆ่าเชื้อด้วย UV-C\" · ตัวเลข \"ลดไวรัส H1N1 >99.99%*\" ใช้ได้หลัง QA ยืนยันว่ารายการนี้ได้ CMA · ห้ามตัวเลขแบคทีเรีย/coronavirus",
         "รายงาน KJ202302756 Guangzhou Institute of Microbiology (Drive 15q3gk5RJalmaUfDkR6gktLRYqgZxCV4u) · ไม่มีผลทดสอบแบคทีเรีย"],
        ["ฆ่าเชื้อ (AP-M1536S, AP-H2219S)", "STOP", "ห้ามใช้ ใช้คำว่า \"กรอง\" เท่านั้น", "2 รุ่นนี้ไม่มี UV หรือระบบฆ่าเชื้อ"],
        ["เชื่อมต่อ WiFi (AP-M1536S, AP-H2219S)", "OK", "ใช้ได้", "หน้าเว็บ + manual (Tuya/Smartlife) + กล่องสินค้า"],
      ],
      flags=["ตัวเลข H1N1 >99.99%: QA ต้องเช็ก PDF ต้นฉบับ KJ202302756 ว่ารายการนี้ได้ CMA ก่อนใช้ในแอด/POSM",
             "หน้าเว็บขัดกันเอง: AP-H2219S ค่า HEPA 0.1 vs 0.01 µm · AP-M1536S พัดลม 3 ระดับ (เว็บ) vs 4 ระดับ (manual)",
             "สต็อก AP-M1536S (~6) และ AP-H2219S (~36, ไส้กรอง 1) ต่ำ ต้อง restock ก่อนยิงแอด"]),
 dict(cats=["beauty"], name="Beauty (อุปกรณ์จัดแต่งทรงผม)",
      km_exec=["Digital", "มอเตอร์ BLDC 110,000 รอบต่อนาที"],
      km=["มอเตอร์ BLDC 110,000 รอบ/นาที (ทุกรุ่น)", "Digital Display (เฉพาะ BDR-03, BDR-04)"],
      focus=["BDR-03", "BDR-04", "BAW-02", "BSL-01"], series=[],
      fbig="3D โชว์เทคโนโลยี (มอเตอร์ BLDC + หน้าจอดิจิทัลในรุ่นที่มี)", tt="สาธิตการใช้งาน Before/After",
      mp="Bwell Beauty + ประเภทเครื่อง + รุ่น + มอเตอร์ BLDC 110,000 รอบ/นาที + ดิจิทัล (เฉพาะ BDR-03/04)",
      posm="Headline: \"BLDC 110,000 รอบ/นาที\" · Icons: BLDC 110,000 rpm | Digital Display (BDR-03/04) หรือจุดขายรุ่น (BAW-02/BSL-01) | น้ำหนักเบา",
      kol="Beauty creator · Before/After จริงในคลิปเดียว · พูด BLDC 110,000 รอบ/นาที · พูด Digital เฉพาะ BDR-03/04",
      line="ของขวัญ (Mother's Day/12.12) + bundle ไดร์ + หวีไดร์",
      evidence=[
        ["มอเตอร์ BLDC 110,000 รอบ/นาที", "OK", "ใช้ได้ทั้ง 4 รุ่น", "หน้าเว็บ BDR-03, BDR-04, BAW-02, BSL-01 ระบุ 110,000 rpm ทุกรุ่น"],
        ["Digital", "ADJUST", "ใช้เฉพาะ BDR-03 และ BDR-04 · ห้ามใช้กับ BAW-02, BSL-01", "BDR-03 \"Digital Display\" · BDR-04 \"หน้าจอ Digital\" · BAW-02/BSL-01 ไม่พบ"],
      ],
      flags=["สต็อก BAW-02 (~12) และ BDR-04 (~56) ต่ำ"]),
 dict(cats=["dh"], name="เครื่องลดความชื้น",
      km_exec=["มี Compressor", "ขนาดเล็กประหยัดพื้นที่", "เชื่อมต่อ WiFi ได้"],
      km=["ระบบ Compressor", "ขนาดเล็ก ประหยัดพื้นที่", "เชื่อมต่อ WiFi ได้ (BDH-30A, BDH-53A)"],
      focus=["BDH-12A", "BDH-30A", "BDH-53A"], series=[],
      fbig="3D โชว์เทคโนโลยี (ระบบ Compressor ภายในเครื่อง)", tt="บรรยายสรรพคุณ",
      mp="Bwell + เครื่องลดความชื้น + รุ่น + Compressor + ประหยัดพื้นที่ + WiFi (เฉพาะ 30A/53A)",
      posm="Headline: \"ระบบ Compressor ในเครื่องเล็ก\" · Icons: Compressor | ประหยัดพื้นที่ | WiFi (30A/53A) หรือรับประกัน Compressor 3 ปี (12A)",
      kol="คอนโด/บ้านหลังน้ำลด · โชว์ขนาดเครื่องเทียบมุมห้อง · สั่งผ่านแอปเฉพาะ 30A/53A",
      line="ปลายฝน/หลังน้ำลด: เลือกรุ่นตามพื้นที่",
      evidence=[
        ["มี Compressor", "ADJUST", "ใช้ \"ระบบ Compressor\" · ห้ามเขียน Inverter/Rotary", "หน้าเว็บทุกรุ่น \"ระบบคอมเพรสเซอร์\" ไม่ระบุประเภท · รับประกันคอมเพรสเซอร์ 3 ปี"],
        ["ขนาดเล็กประหยัดพื้นที่", "OK", "ใช้ได้ (BDH-53A ใช้ \"ประหยัดพื้นที่\")", "12A 280×195×386 · 30A 310×229×500 · 53A 390×268×612 มม."],
        ["เชื่อมต่อ WiFi", "ADJUST", "ใช้เฉพาะ BDH-30A และ BDH-53A · ห้ามใช้กับ BDH-12A", "หน้าเว็บ 30A/53A มี WiFi · 12A ไม่พบ"],
      ],
      flags=["ยังไม่มี manual รุ่น A ใน Drive"]),
 dict(cats=["ac"], name="แอร์เคลื่อนที่",
      km_exec=["ขนาดเล็กประหยัดพื้นที่", "เย็นเต็ม BTU", "ประหยัดไฟ"],
      km=["ขนาดเล็ก ประหยัดพื้นที่", "ความเย็น 9,000 / 12,000 BTU", "[ประหยัดไฟ: รอใบฉลากเบอร์ 5]"],
      focus=["BPAC-09B", "BPAC-12B"], series=[],
      fbig="3D โชว์เทคโนโลยี (ระบบทำความเย็น + ขนาดตัวเครื่อง)", tt="บรรยายสรรพคุณ",
      mp="Bwell + แอร์เคลื่อนที่ + รุ่น + 9,000/12,000 BTU + ขนาดเล็ก ประหยัดพื้นที่ + [ฉลากเบอร์ 5 เมื่อได้เอกสาร]",
      posm="Headline: \"เย็นทันที ไม่ต้องติดตั้ง\" · Icons: ประหยัดพื้นที่ | 9,000/12,000 BTU | [ฉลากเบอร์ 5: รอเอกสาร]",
      kol="คอนโด/ห้องทำงาน · โชว์ห้องเย็นจริง · ห้ามพูดค่าไฟ/ประหยัดไฟจนกว่าจะมีฉลาก",
      line="ก่อนหน้าร้อน (ก.พ.–มี.ค.)",
      evidence=[
        ["ขนาดเล็กประหยัดพื้นที่", "OK", "ใช้ได้", "หน้าเว็บ BPAC-09B/12B"],
        ["เย็นเต็ม BTU", "ADJUST", "ใช้ \"ความเย็น 9,000 / 12,000 BTU\" · ห้ามใช้ \"เย็นเต็ม\" (ไม่มีผลวัดจริง)", "BPAC-09B 9,000 BTU/h 1,000 W · BPAC-12B 12,000 BTU/h 1,400 W"],
        ["ประหยัดไฟ", "PENDING", "ห้ามใส่ใน copy จนกว่าจะได้ใบฉลากเบอร์ 5 / ค่า EER ของรุ่น B", "ฉลากเบอร์ 5 พบแค่บน HomePro · EER 2.6 เป็นของ BPAC-12 รุ่นเก่า ใช้กับรุ่น B ไม่ได้"],
      ],
      flags=["ขอใบฉลากประหยัดไฟเบอร์ 5 + ค่า EER ของ BPAC-09B/12B จาก PM"]),
 dict(cats=["vac"], name="เครื่องดูดฝุ่น",
      km_exec=["เครื่องดูดฝุ่นสำหรับคนเป็นภูมิแพ้"],
      km=["เครื่องดูดฝุ่นสำหรับคนเป็นภูมิแพ้"],
      focus=["201A", "Flomo Lite"], series=[],
      fbig="3D โชว์เทคโนโลยี (ระบบกรองฝุ่น)", tt="โชว์การทำงานจริง (ที่นอน/โซฟา/พื้น)",
      mp="Bwell + เครื่องดูดฝุ่น + สำหรับคนเป็นภูมิแพ้ + รุ่น + ไร้สาย/ดูด+ถู",
      posm="Headline: \"สำหรับคนเป็นภูมิแพ้\" · Icons: ภูมิแพ้ | ไร้สาย | ดูด+ถู (Flomo Lite)",
      kol="บ้านมีสัตว์เลี้ยง/คนแพ้ฝุ่น · ดูดจริงให้เห็นฝุ่นในถัง",
      line="ทำความสะอาดปีใหม่ + bundle ไส้กรอง",
      evidence=[
        ["สำหรับคนเป็นภูมิแพ้", "PENDING", "ยังไม่ได้ตรวจหลักฐานในรอบ 19 พ.ย. (ไม่อยู่ในรายการ claim ที่ตรวจ) ใช้ตามผู้บริหารได้ใน Organic แต่ควรตรวจก่อนขึ้นแอด/POSM",
         "ยังไม่ได้ตรวจ"],
      ],
      flags=["T12 Allergy Plus/Pro ไม่อยู่ใน Focus แล้ว", "ตรวจหลักฐาน \"สำหรับคนเป็นภูมิแพ้\" (ระดับการกรอง/HEPA) ของ 201A และ Flomo Lite"]),
 dict(cats=["robot"], name="หุ่นยนต์ดูดฝุ่น",
      km_exec=["หุ่นยนต์ที่ดูดขอบมุมได้ชิดที่สุด"],
      km=["ดูดชิดขอบผนังและมุมห้อง ด้วยแปรงข้างและม็อบที่ยืดออกได้"],
      focus=["Ultra T20"], series=[],
      fbig="3D โชว์เทคโนโลยี (แปรงข้างยืดเข้ามุม + ม็อบยืดตามแนวผนัง + แท่น OmniBase)", tt="โชว์การทำงานจริง (มุมห้อง/ขอบผนัง)",
      mp="Bwell + หุ่นยนต์ดูดฝุ่นถูพื้น + Ultra T20 OmniBase + ดูดชิดขอบผนังและมุม + ซัก-เป่าม็อบอัตโนมัติ",
      posm="Headline: \"ชิดขอบ ชิดมุม\" · Icons: แปรงข้าง-ม็อบยืดได้ | ซัก-เป่าม็อบเอง | เก็บฝุ่นอัตโนมัติ",
      kol="ถ่ายมุมห้องก่อน-หลัง · พูดเรื่องแปรงข้าง/ม็อบยืดเป็นข้อแรก · ห้ามพูด \"ลมร้อน/Hot Air\" และ \"ที่สุด\"",
      line="11.11 / 12.12 / ของขวัญปีใหม่",
      evidence=[
        ["ดูดขอบมุม (เทคโนโลยี)", "OK", "\"แปรงข้างและม็อบยืดออกเพื่อทำความสะอาดตามแนวผนังและมุม\"",
         "หน้าเว็บ T20 + User manual (\"side brush will only extend in corners\" / \"mop cloth will only extend along walls\")"],
        ["ชิดที่สุด", "STOP", "ห้ามใช้ superlative ใช้ \"ดูดชิดขอบผนังและมุมห้อง\"", "ไม่มีผลทดสอบเทียบจาก third-party · เสี่ยงผิด สคบ."],
      ],
      flags=["คลิป KOL เดิมพูด \"เป่าผ้าแห้งด้วยลมร้อน\" ขัด Product_Facts (Hot Air UNVERIFIED) ห้ามนำมา reuse ในแอด"]),
 dict(cats=["wp", "wh"], name="เครื่องกรองน้ำ",
      km_exec=["มี NSF มาตรฐานอเมริกา"],
      km=["ไส้กรองและกระบอกกรองผ่านการรับรองตามมาตรฐาน NSF/ANSI 42 (สหรัฐอเมริกา)"],
      focus=["BW-D10UF5", "BW-D10RO5", "BW-BB20PP"], series=["BW-BB20PP เป็นเครื่องกรองน้ำใช้ ห้ามใช้คำว่า \"น้ำดื่ม\""],
      fbig="3D โชว์เทคโนโลยี (ไส้กรองแต่ละชั้น + ไส้กรอง/กระบอกที่ได้ NSF/ANSI 42)", tt="บรรยายสรรพคุณ",
      mp="Bwell + เครื่องกรองน้ำ + ระบบ (UF/RO/น้ำใช้) + รุ่น + ไส้กรอง NSF/ANSI 42",
      posm="Headline: \"ไส้กรองผ่านมาตรฐาน NSF/ANSI 42\" · Icons: ไส้กรอง NSF/ANSI 42 | ระบบกรอง | ไม่ผูกสัญญา · footnote: Cert C0840467-01 รับรองไส้กรองและกระบอกกรอง",
      kol="ครอบครัว/คอนโด · โชว์ใบรับรอง NSF จริง (Cert C0840467-01) และพูดว่ารับรอง \"ไส้กรองและกระบอกกรอง\" · ห้ามพูดว่าเครื่องได้ NSF",
      line="เตือนเปลี่ยนไส้กรองตามรอบ (ไส้กรองแท้ NSF/ANSI 42)",
      evidence=[
        ["มี NSF มาตรฐานอเมริกา", "STOP", "หยุดใช้ในความหมายว่าทั้งเครื่องได้ NSF · ใช้ \"ไส้กรองและกระบอกกรองผ่านการรับรองตามมาตรฐาน NSF/ANSI 42 (สหรัฐอเมริกา)\"",
         "NSF listing: B-well International ได้ NSF/ANSI 42 เฉพาะ cartridge/housing (ส่วนใหญ่ material only) · ตัวเครื่อง 3 รุ่นไม่อยู่ใน listing · Cert C0840467-01 (Drive 1bWIewEjJV-zC-DwFDu-tZK8tTkdtoKcA)"],
        ["BW-BB20PP \"มาตรฐานน้ำดื่ม\" (หน้าเว็บ)", "STOP", "ห้ามใช้คำว่าน้ำดื่มกับ BW-BB20PP · แจ้งทีมเว็บแก้", "รุ่นนี้เป็นเครื่องกรองน้ำใช้"],
      ],
      flags=["ยืนยันว่ากระบอกของ BW-BB20PP คือ BW-BBH20 ที่อยู่ใน NSF listing",
             "ราคา Power Buy ของ UF5 (+33%) และ RO5 (+38%) ยังไม่ตรงเว็บ"]),
 dict(cats=["heat"], name="เครื่องทำน้ำอุ่น",
      km_exec=["EV charger design", "ระบบความปลอดภัย 10 จุด", "ร้อนเร็ว อุณหภูมิสม่ำเสมอ"],
      km=["5 ระบบความปลอดภัย: ELSD · Flow Switch · Double Thermostat · IP25 · Surge Protector", "ร้อนเร็ว อุณหภูมิสม่ำเสมอ (ELKA, FELIX, Konrad)", "[EV Charger Design: รอผู้บริหารยืนยันซีรีส์]"],
      focus=["LUKA", "ELKA", "FELIX", "Konrad"], series=["ทุกรุ่นมีหลายขนาดให้เลือก (วัตต์สูง = ร้อนเร็ว)", "ELSD 15 mA ตัดภายใน 0.01 วินาที + IP25 ครบทั้ง 9 รุ่น"],
      fbig="3D โชว์เทคโนโลยี (5 ระบบความปลอดภัยบนตัวเครื่อง)", tt="บรรยายสรรพคุณ",
      mp="Bwell + เครื่องทำน้ำอุ่น + รุ่น + วัตต์ + ตัดไฟรั่ว ELSD + กันน้ำ IP25 + 5 ระบบความปลอดภัย",
      posm="Headline: \"5 ระบบความปลอดภัย\" · Icons: ELSD 15 mA | IP25 | ร้อนเร็ว (ELKA/FELIX/Konrad) หรือวัตต์ (LUKA)",
      kol="ครอบครัวมีผู้สูงอายุ/เด็ก · ชี้ 5 ระบบความปลอดภัยบนเครื่องจริงทีละข้อ",
      line="หน้าหนาว + ช่วงย้ายบ้าน/รีโนเวท",
      evidence=[
        ["ระบบความปลอดภัย 10 จุด", "STOP", "ใช้ \"5 ระบบความปลอดภัย\" และระบุชื่อครบทั้ง 5",
         "ไม่มีรายการ 10 จุดในเอกสารทางการ · ที่ยืนยันได้: ELSD, Flow Switch Sensor, Double Function Thermostat, IP25, Voltage Surge Protector · HITACHI ใช้ \"ปลอดภัย 10 ระบบ\" อยู่แล้ว"],
        ["EV Charger Design", "PENDING", "ห้ามใส่ใน copy จนกว่าผู้บริหารยืนยันว่าใช้กับซีรีส์ไหน",
         "ไม่อยู่ในหน้าเว็บ/กราฟิก/manual · พบแค่ใน content draft ภายใน 12 พ.ย. และเฉพาะ LUKA"],
        ["ร้อนเร็ว อุณหภูมิสม่ำเสมอ", "ADJUST", "ใช้ได้กับ ELKA, FELIX, Konrad · ห้ามใช้กับ LUKA · ห้ามใส่ตัวเลขเวลา/±°C",
         "ELKA/FELIX: UK Technology Heating Element · Konrad: ถังทองแดง · LUKA: ไม่มีเคลมความเร็ว · ทุกรุ่น: Stepless/Electronic Temperature Control"],
        ["ELSD / IP25 / มอก.", "OK", "ELSD 15 mA ภายใน 0.01 วินาที + IP25 ทุกรุ่น · มอก.1693 + 2066 (LUKA, ELKA, FELIX) / มอก.1693 (Konrad)",
         "หน้าเว็บทั้ง 9 รุ่น"],
      ],
      flags=["หน้ารวมน้ำอุ่นพิมพ์ผิด LUKA \"ภายใน 01 วินาที\" ต้องแก้เป็น 0.01",
             "LUKA manual: แนะนำ RCD 10 mA และช่วงวัตต์ EN/TH ไม่ตรงกัน", "LUKA 3500W สต็อกต่ำ · ราคาห้างต่ำกว่าเว็บ"]),
 dict(cats=["chair"], name="เก้าอี้เพื่อสุขภาพ",
      km_exec=["ลิขสิทธิ์แท้", "ขาเหล็กแข็งแรงทนทาน", "ผ่านมาตรฐาน BIFMA"],
      km=["ขาอะลูมิเนียม แข็งแรงทนทาน", "Lumbar Support", "[BIFMA: รอใบรับรองรายรุ่น]", "[ลิขสิทธิ์แท้: รอผู้บริหารนิยาม]"],
      focus=["Stella เทา", "Astrid ขาว", "Agnes เทา", "Bjorn เทา", "Greta เทา"], series=[],
      fbig="โชว์เทคโนโลยี Lumbar Support + ขาอะลูมิเนียม", tt="สาธิตการใช้งาน (ปรับจริง นั่งจริง)",
      mp="Bwell Ergo + เก้าอี้เพื่อสุขภาพ + รุ่น + สี + Lumbar Support + ขาอะลูมิเนียม",
      posm="Headline: \"หลังสบาย ด้วย Lumbar Support\" · Icons: ขาอะลูมิเนียม | Lumbar Support | [BIFMA: รอใบรับรอง]",
      kol="WFH/ออฟฟิศ · ปรับ Lumbar ให้ดู · ชื่อ Bwell Ergo ในช่วง 3 วินาทีแรก · ห้ามพูด \"ขาเหล็ก\" / ลิขสิทธิ์แท้ / BIFMA จนกว่าจะมีเอกสาร",
      line="ลองนั่งที่ Showroom CDC + โปรผ่อน",
      evidence=[
        ["ขาเหล็กแข็งแรงทนทาน", "STOP", "ใช้ \"ขาอะลูมิเนียม แข็งแรงทนทาน\"", "หน้าเว็บทั้ง 5 รุ่น \"ขาเก้าอี้ทำจาก Aluminum\" · Product Intelligence \"Aluminum Base ทุกรุ่น\""],
        ["ผ่านมาตรฐาน BIFMA", "PENDING", "ห้ามใส่ใน copy รายรุ่นจนกว่าจะได้ใบรับรอง/รายงานรายรุ่น",
         "หน้าหมวดเขียนกว้างๆ \"ผ่านการทดสอบมาตรฐานสากลระดับ BIFMA\" · กราฟิกเก่า \"BIFMA X5.1:2017 / 20 ด่าน\" (Drive 12yzkAUyD79IxXI7gXo1m9G3dg11IDZbZ) · ไม่มีชื่อแล็บ/เลขรายงาน"],
        ["ลิขสิทธิ์แท้", "PENDING", "ห้ามใส่ใน copy จนกว่าผู้บริหารนิยามและมีหลักฐาน", "ไม่พบคำนี้บนหน้าเก้าอี้ ไม่มีชื่อผู้ให้ลิขสิทธิ์"],
      ],
      flags=["คำอธิบายสั้นบนหน้าเว็บเก้าอี้ยังเป็นข้อความเครื่องฟอกอากาศ (CMS bug)"]),
 dict(cats=["cush"], name="หมอนเพื่อสุขภาพ",
      km_exec=["ลิขสิทธิ์แท้"],
      km=["[ลิขสิทธิ์แท้: รอผู้บริหารนิยาม]", "จุดขายรายรุ่น: Cool Gel (Seat Cushion) / ผ้าระบายความร้อน (Car Lumbar, Car Neck, Lumbar)"],
      focus=["ทุกรุ่น (6 SKU)"], series=["Cool Gel Memory Foam: เฉพาะเบาะรองนั่ง (Seat Cushion)",
                                       "\"Cool Fabric\" ไม่มีรุ่นไหนใช้คำนี้ ใช้ \"Cooling Soft Cotton\" (Car Lumbar, Car Neck) / \"ผ้าระบายความร้อน\" (Lumbar) แทน"],
      fbig="เน้นจุดขายรายรุ่น (Cool Gel เฉพาะ Seat Cushion / ผ้าระบายความร้อน) + ภาพการใช้งานจริง", tt="สาธิตการใช้งาน",
      mp="Bwell Ergo + หมอน/เบาะ + จุดใช้งาน + จุดขายรุ่น (Cool Gel เฉพาะ Seat Cushion)",
      posm="Headline: ชื่อจุดใช้งาน (เช่น \"นั่งนานแค่ไหนก็สบายขึ้น\") · Icons: จุดขายรุ่น | รองรับสรีระ | Bwell Ergo",
      kol="ใช้จริงในรถ/บนเครื่องบิน/ที่โต๊ะทำงาน · ห้ามพูด \"ลิขสิทธิ์แท้\" จนกว่าจะมีนิยาม",
      line="Add-on กับเก้าอี้ + ของขวัญ",
      evidence=[
        ["ลิขสิทธิ์แท้", "PENDING", "ห้ามใส่ใน copy จนกว่าผู้บริหารนิยาม", "พบแค่ใน CTA คลิป TikTok 3 คลิป ไม่มีนิยามหรือผู้ให้ลิขสิทธิ์"],
        ["Cool Gel", "ADJUST", "ใช้ได้เฉพาะเบาะรองนั่ง (Seat Cushion)", "หน้าเว็บ Seat Cushion \"Cool Gel Memory Foam\""],
        ["Cool Fabric", "ADJUST", "ไม่ใช้คำ \"Cool Fabric\" · ใช้ \"Cooling Soft Cotton\" (Car Lumbar/Car Neck) หรือ \"ผ้าระบายความร้อน\" (Lumbar)", "หน้าเว็บรายรุ่น"],
      ],
      flags=["\"ทุกรุ่น\" = 6 SKU ในเว็บ (Travel Neck, Seat, Lumbar, Car Lumbar, Car Neck, Footrest) ยืนยันกับผู้บริหารว่ารวม Footrest หรือไม่"]),
 dict(cats=["sport"], name="เสื่อออกกำลังกาย",
      km_exec=["ลิขสิทธิ์แท้", "ความหนาแน่นสูงรับน้ำหนักได้ดีกว่าป้องกันการบาดเจ็บ"],
      km=["High Density NBR หนา 1.2 cm", "ช่วยรองรับแรงกระแทก", "[ลิขสิทธิ์แท้: รอผู้บริหารนิยาม]"],
      focus=["Move"], series=["คลิปซูมเทียบเสื่อ 199 บาท: รอผลวัดความหนาแน่นก่อนใช้ในแอด (Organic ใช้ได้โดยไม่ระบุตัวเลขและไม่ระบุยี่ห้อ)"],
      fbig="เน้นเนื้อวัสดุ High Density NBR (ภาพซูมเนื้อเสื่อ)", tt="ซูมเนื้อเสื่อ + ท่าที่ลงน้ำหนัก (ไม่ระบุยี่ห้ออื่น)",
      mp="Bwell + เสื่อโยคะ Move + High Density NBR + หนา 1.2 cm + รองรับแรงกระแทก",
      posm="Headline: \"High Density NBR\" · Icons: NBR หนาแน่นสูง | หนา 1.2 cm | รองรับแรงกระแทก",
      kol="ฟิตเนส/โยคะ · ซูมเนื้อเสื่อ + ท่าที่ลงน้ำหนัก · ห้ามพูด \"ป้องกันการบาดเจ็บ\" / \"รับน้ำหนักได้ดีกว่า\"",
      line="New year resolution (ม.ค.)",
      evidence=[
        ["ความหนาแน่นสูง (NBR)", "OK", "\"High Density NBR\" หนา 1.2 cm ขนาด 183×61 cm", "หน้าเว็บ Move ตรงกับ Product_Facts"],
        ["ป้องกันการบาดเจ็บ", "ADJUST", "ใช้ \"ช่วยรองรับแรงกระแทก\"", "หน้าเว็บมีแค่ brand copy ไม่มีผลทดสอบ"],
        ["รับน้ำหนักได้ดีกว่า / รูพรุนน้อยกว่าเสื่อ 199", "PENDING", "ห้ามใส่ใน copy เชิงเปรียบเทียบจนกว่าจะมีผลวัดความหนาแน่น", "ไม่มีตัวเลขความหนาแน่นและผลเทียบ"],
        ["ลิขสิทธิ์แท้", "PENDING", "ห้ามใส่ใน copy จนกว่าผู้บริหารนิยาม", "หน้าเว็บเป็นคอลแลบ \"Bwell x illuztika\" ไม่ใช่ลิขสิทธิ์"],
      ],
      flags=["Foam Roller Matrix ไม่อยู่ใน Focus"]),
]

def _o(**k): return k
SKU_EXEC = {
 "AP-M1536S": _o(headline="ห้องนอนลูก หายใจสบาย กรองฝุ่น PM2.5", sub="PM2.5 Series กรอง PM2.5 ดูดกลิ่นไม่พึงประสงค์ เชื่อมต่อ WiFi ไม่มีระบบ Ionizer",
      hook="เครื่องฟอกในห้องลูก ควรมี Ionizer ไหม", mp="Bwell เครื่องฟอกอากาศ PM2.5 AP-M1536S บ้านมีเด็ก แพ้ง่าย กรอง PM2.5 ดูดกลิ่น WiFi ไม่มี Ionizer",
      icons="กรอง PM2.5 | ดูดกลิ่น | WiFi", kol="ออกแบบเพื่อบ้านที่มีเด็กและคนแพ้ง่าย · ไม่มีระบบ Ionizer · สั่งผ่าน WiFi"),
 "AP-H2219S": _o(headline="ออกแบบเพื่อบ้านที่มีเด็กและคนแพ้ง่าย", sub="PM2.5 Series กรอง PM2.5 ดูดกลิ่นไม่พึงประสงค์ เชื่อมต่อ WiFi ไม่มีระบบ Ionizer",
      hook="ค่าฝุ่นสีแดง ห้องลูกคุณปลอดภัยแค่ไหน", mp="Bwell เครื่องฟอกอากาศ PM2.5 AP-H2219S บ้านมีเด็ก แพ้ง่าย กรอง PM2.5 ดูดกลิ่น WiFi ไม่มี Ionizer",
      icons="กรอง PM2.5 | ดูดกลิ่น | WiFi", kol="ออกแบบเพื่อบ้านที่มีเด็กและคนแพ้ง่าย · ไม่มีระบบ Ionizer · กรอง PM2.5 ดูดกลิ่น สั่งผ่าน WiFi"),
 "AP-P4019US": _o(headline="8 ขั้นตอน จบในเครื่องเดียว", sub="Virus Series กรองฝุ่น ดูดกลิ่น ฆ่าเชื้อด้วย UV-C ออกแบบเพื่อบ้านที่มีเด็กและคนแพ้ง่าย",
      hook="อากาศผ่านเครื่องนี้ 8 ขั้นตอนก่อนถึงลูกคุณ", mp="Bwell เครื่องฟอกอากาศ Virus Series AP-P4019US 8 ขั้นตอน HEPA H13 UV-C กรองฝุ่น ดูดกลิ่น ฆ่าเชื้อ บ้านมีเด็ก",
      icons="8 ขั้นตอน | UV-C ฆ่าเชื้อ | ไม่มี Ionizer", kol="ฟอก 8 ขั้นตอนจบในเครื่องเดียว · ฆ่าเชื้อด้วย UV-C · ไม่มีระบบ Ionizer · ห้ามพูดตัวเลข %"),
 "BDR-03": _o(headline="แห้งไว ด้วยมอเตอร์ BLDC 110,000 รอบ/นาที", sub="ไดร์เป่าผม BDR-03 หน้าจอ Digital Display น้ำหนักเบา ใช้ได้ทุกเช้า",
      hook="ผมแห้งในกี่นาที ถ้ามอเตอร์หมุน 110,000 รอบ", mp="Bwell Beauty ไดร์เป่าผม ดิจิทัล BDR-03 มอเตอร์ BLDC 110,000 รอบ/นาที น้ำหนักเบา",
      icons="Digital Display | BLDC 110,000 rpm | น้ำหนักเบา", kol="Before/After ผมเปียกถึงแห้ง · พูด Digital + BLDC 110,000 รอบ/นาที"),
 "BDR-04": _o(headline="เป่าแห้งและยืดตรงในขั้นตอนเดียว", sub="เครื่องหนีบลมร้อน BDR-04 หน้าจอ Digital มอเตอร์ BLDC 110,000 รอบ/นาที",
      hook="ผมเปียกถึงผมตรง ไม่ต้องเปลี่ยนเครื่อง", mp="Bwell Beauty เครื่องหนีบลมร้อน เป่าผม BDR-04 ดิจิทัล BLDC 110,000 รอบ/นาที",
      icons="Digital Display | BLDC 110,000 rpm | เป่า+ยืด", kol="Before/After ผมเปียกถึงตรง · Digital + BLDC 110,000 รอบ/นาที"),
 "BAW-02": _o(headline="7 หัว จบทุกทรง ด้วย BLDC 110,000 รอบ/นาที", sub="เครื่องจัดแต่งทรงผม BAW-02 ม้วน เป่า แปรง ยืด ในเครื่องเดียว",
      hook="เช้าเดียว 3 ทรง ด้วยเครื่องเดียว", mp="Bwell Beauty เครื่องจัดแต่งทรงผม BAW-02 7 หัว มอเตอร์ BLDC 110,000 รอบ/นาที",
      icons="7 หัว | BLDC 110,000 rpm | ม้วน-เป่า-ยืด", kol="Before/After หลายทรง · BLDC 110,000 รอบ/นาที · ห้ามพูดว่า Digital"),
 "BSL-01": _o(headline="เป่าและจัดทรงพร้อมกัน", sub="หวีไดร์ BSL-01 มอเตอร์ BLDC 110,000 รอบ/นาที เพิ่มวอลลุ่มในขั้นตอนเดียว",
      hook="ผมแบนทั้งวัน แก้ได้ใน 5 นาที", mp="Bwell Beauty หวีไดร์จัดแต่งทรงผม BSL-01 มอเตอร์ BLDC 110,000 รอบ/นาที วอลลุ่ม",
      icons="BLDC 110,000 rpm | เป่า+แปรง | วอลลุ่ม", kol="Before/After วอลลุ่ม · BLDC 110,000 รอบ/นาที · ห้ามพูดว่า Digital"),
 "BDH-12A": _o(headline="เล็ก แต่มีระบบ Compressor", sub="เครื่องลดความชื้น BDH-12A ขนาดเล็กประหยัดพื้นที่ สำหรับห้องนอนและคอนโด รับประกันคอมเพรสเซอร์ 3 ปี",
      hook="เครื่องลดความชื้นตัวเล็ก ทำไมต้องมี Compressor", mp="Bwell เครื่องลดความชื้น BDH-12A ระบบ Compressor ขนาดเล็ก ประหยัดพื้นที่ คอนโด",
      icons="Compressor | ประหยัดพื้นที่ | รับประกันคอมเพรสเซอร์ 3 ปี", kol="ระบบ Compressor · ขนาดเล็กวางมุมห้องได้ · ห้ามพูดเรื่อง WiFi (รุ่นนี้ไม่มี)"),
 "BDH-30A": _o(headline="ห้องแห้ง ผ้าแห้ง ด้วยระบบ Compressor", sub="เครื่องลดความชื้น BDH-30A ดีไซน์ประหยัดพื้นที่ เชื่อมต่อ WiFi",
      hook="ฝนตกทั้งสัปดาห์ ผ้าไม่แห้งสักตัว", mp="Bwell เครื่องลดความชื้น BDH-30A ระบบ Compressor ประหยัดพื้นที่ WiFi ตากผ้าในบ้าน",
      icons="Compressor | ประหยัดพื้นที่ | WiFi", kol="ระบบ Compressor · ประหยัดพื้นที่ · สั่งผ่าน WiFi"),
 "BDH-53A": _o(headline="ความจุสูง ในดีไซน์ประหยัดพื้นที่", sub="เครื่องลดความชื้น BDH-53A ระบบ Compressor เชื่อมต่อ WiFi สำหรับบ้านเดี่ยวและพื้นที่หลังน้ำลด",
      hook="หลังน้ำลด ผนังยังชื้น", mp="Bwell เครื่องลดความชื้น BDH-53A ระบบ Compressor ความจุสูง ประหยัดพื้นที่ WiFi บ้านเดี่ยว",
      icons="Compressor | ประหยัดพื้นที่ | WiFi", kol="ระบบ Compressor · ความจุสูงแต่ไม่กินที่ · สั่งผ่าน WiFi"),
 "BPAC-12B": _o(headline="ความเย็น 12,000 BTU ในตัวเครื่องกะทัดรัด", sub="แอร์เคลื่อนที่ BPAC-12B ขนาดเล็กประหยัดพื้นที่ ไม่ต้องติดตั้ง",
      hook="ห้องร้อนแต่ติดแอร์ไม่ได้ ใช้ตัวนี้แทน", mp="Bwell แอร์เคลื่อนที่ BPAC-12B 12,000 BTU ประหยัดพื้นที่ ไม่ต้องติดตั้ง",
      icons="ประหยัดพื้นที่ | 12,000 BTU | [ฉลากเบอร์ 5: รอเอกสาร]", kol="12,000 BTU · ตัวเล็กไม่กินที่ · ห้ามพูดค่าไฟ/ประหยัดไฟจนกว่าจะมีฉลาก"),
 "BPAC-09B": _o(headline="เล็ก ประหยัดพื้นที่ ความเย็น 9,000 BTU", sub="แอร์เคลื่อนที่ BPAC-09B สำหรับห้องนอนและห้องทำงาน ไม่ต้องติดตั้ง",
      hook="ห้องนอนติดแอร์ไม่ได้ ใช้ตัวนี้แทน", mp="Bwell แอร์เคลื่อนที่ BPAC-09B 9,000 BTU ขนาดเล็ก ห้องนอน ไม่ต้องติดตั้ง",
      icons="ประหยัดพื้นที่ | 9,000 BTU | [ฉลากเบอร์ 5: รอเอกสาร]", kol="ขนาดเล็ก · 9,000 BTU · ห้ามพูดค่าไฟ/ประหยัดไฟจนกว่าจะมีฉลาก"),
 "201A": _o(headline="เครื่องดูดฝุ่นสำหรับคนเป็นภูมิแพ้", sub="เครื่องดูดฝุ่นไร้สาย 201A หยิบใช้ได้ทันที ดูดฝุ่นที่ทำให้แพ้ได้ทุกวัน",
      hook="ดูดที่นอน 1 รอบ ฝุ่นออกมาเท่านี้", mp="Bwell เครื่องดูดฝุ่นไร้สาย 201A สำหรับคนเป็นภูมิแพ้ ไรฝุ่น ใช้ทุกวัน",
      icons="สำหรับภูมิแพ้ | ไร้สาย | ใช้ทุกวัน", kol="สำหรับคนเป็นภูมิแพ้ · ดูดจริงให้เห็นฝุ่นในถัง"),
 "Flomo Lite": _o(headline="ดูดและถู สำหรับบ้านคนเป็นภูมิแพ้", sub="เครื่องดูดฝุ่นพร้อมถูพื้น Flomo Lite เก็บฝุ่นที่ทำให้แพ้และถูพื้นในเครื่องเดียว",
      hook="ดูดเสร็จไม่ต้องถูต่อ", mp="Bwell เครื่องดูดฝุ่นพร้อมถูพื้น Flomo Lite สำหรับคนเป็นภูมิแพ้ ดูดและถูในเครื่องเดียว",
      icons="สำหรับภูมิแพ้ | ดูด+ถู | ประหยัดเวลา", kol="สำหรับคนเป็นภูมิแพ้ · ดูดและถูจริงบนพื้นบ้าน"),
 "Ultra T20": _o(headline="ชิดขอบ ชิดมุม ทุกซอกห้อง", sub="Bwell Ultra T20 OmniBase แปรงข้างและม็อบยืดออกได้ ดูดชิดขอบผนังและมุมห้อง พร้อมแท่นซัก-เป่าม็อบและเก็บฝุ่นอัตโนมัติ",
      hook="มุมห้องที่หุ่นยนต์ทั่วไปเข้าไม่ถึง", mp="Bwell หุ่นยนต์ดูดฝุ่นถูพื้น Ultra T20 OmniBase แปรงข้าง ม็อบยืดได้ ดูดชิดขอบมุม ซัก-เป่าม็อบ เก็บฝุ่นอัตโนมัติ",
      icons="แปรงข้าง-ม็อบยืดได้ | ซัก-เป่าม็อบเอง | เก็บฝุ่นอัตโนมัติ", kol="ถ่ายมุมห้องก่อน-หลัง · พูดเรื่องแปรงข้าง/ม็อบยืดเป็นข้อแรก · ห้ามพูด \"ที่สุด\" / \"ลมร้อน\""),
 "BW-D10UF5": _o(headline="น้ำดื่มสะอาด ไส้กรองผ่านมาตรฐาน NSF/ANSI 42", sub="เครื่องกรองน้ำระบบ UF BW-D10UF5 ไส้กรองและกระบอกกรองผ่านการรับรองตามมาตรฐาน NSF/ANSI 42 (สหรัฐอเมริกา) ติดตั้งง่าย ไม่ผูกสัญญา",
      hook="ไส้กรองในเครื่องของคุณ มีมาตรฐานอะไรรับรอง", mp="Bwell เครื่องกรองน้ำ ระบบ UF BW-D10UF5 ไส้กรอง NSF/ANSI 42 น้ำดื่ม ติดตั้งง่าย",
      icons="ไส้กรอง NSF/ANSI 42 | ระบบ UF | ติดตั้งง่าย", kol="โชว์ใบรับรอง NSF (C0840467-01) · พูดว่ารับรองไส้กรองและกระบอกกรอง · ติดตั้งจริงในครัว"),
 "BW-D10RO5": _o(headline="น้ำดื่มระบบ RO ไส้กรองผ่านมาตรฐาน NSF/ANSI 42", sub="เครื่องกรองน้ำระบบ RO BW-D10RO5 ไส้กรองและกระบอกกรองผ่านการรับรองตามมาตรฐาน NSF/ANSI 42 (สหรัฐอเมริกา) จ่ายครั้งเดียว ไม่ผูกสัญญา",
      hook="ไส้กรอง RO ของคุณ ผ่านมาตรฐานอะไร", mp="Bwell เครื่องกรองน้ำ ระบบ RO BW-D10RO5 ไส้กรอง NSF/ANSI 42 น้ำดื่ม ครอบครัว",
      icons="ไส้กรอง NSF/ANSI 42 | ระบบ RO | ไม่ผูกสัญญา", kol="โชว์ใบรับรอง NSF (C0840467-01) · พูดว่ารับรองไส้กรองและกระบอกกรอง · ระบบ RO สำหรับครอบครัว"),
 "BW-BB20PP": _o(headline="กรองน้ำใช้ทั้งบ้าน ไส้กรองผ่านมาตรฐาน NSF/ANSI 42", sub="เครื่องกรองน้ำใช้ 20 นิ้ว BW-BB20PP ดักตะกอนก่อนเข้าทุกก๊อก ไส้กรองและกระบอกกรองผ่านการรับรองตามมาตรฐาน NSF/ANSI 42 (สหรัฐอเมริกา)",
      hook="ตะกอนในน้ำประปา หยุดได้ตั้งแต่หน้าบ้าน", mp="Bwell เครื่องกรองน้ำใช้ 20 นิ้ว BW-BB20PP ไส้กรอง NSF/ANSI 42 ดักตะกอน ทั้งบ้าน",
      icons="ไส้กรอง NSF/ANSI 42 | กรองน้ำใช้ทั้งบ้าน | ดักตะกอน", kol="โชว์ใบรับรอง NSF · ติดตั้งก่อนเข้าบ้าน · ย้ำว่าเป็นน้ำใช้ ห้ามพูดว่าน้ำดื่ม"),
}
SAFETY5 = "5 ระบบความปลอดภัย: ตัดไฟรั่ว ELSD · Flow Switch · Double Thermostat · กันน้ำ IP25 · กันไฟกระชาก"
HEATER_EXEC = {
 "LUKA":   _o(headline="อุ่นใจทุกเช้า ด้วย 5 ระบบความปลอดภัย", sub="เครื่องทำน้ำอุ่น LUKA ตัดไฟรั่ว ELSD 15 mA ใน 0.01 วินาที กันน้ำ IP25 เลือกวัตต์ตามการใช้งาน",
             hook="เครื่องทำน้ำอุ่นที่บ้าน มีระบบความปลอดภัยกี่ระบบ", fast=False),
 "ELKA":   _o(headline="ร้อนเร็ว อุณหภูมิสม่ำเสมอ ทุกครั้งที่อาบ", sub="เครื่องทำน้ำอุ่น ELKA ฮีตเตอร์ UK Technology พร้อม 5 ระบบความปลอดภัย", hook="น้ำอุ่นสลับเย็นตอนอาบ แก้ได้", fast=True),
 "FELIX":  _o(headline="5 ระบบความปลอดภัย อุ่นใจทั้งครอบครัว", sub="เครื่องทำน้ำอุ่น FELIX ร้อนเร็ว อุณหภูมิสม่ำเสมอ ฮีตเตอร์ UK Technology", hook="5 ระบบความปลอดภัยในเครื่องทำน้ำอุ่น มีอะไรบ้าง", fast=True),
 "Konrad": _o(headline="วัตต์สูง ร้อนเร็ว ใช้ได้หลายจุด", sub="เครื่องทำน้ำร้อน Konrad ถังทองแดง อุณหภูมิสม่ำเสมอ พร้อม 5 ระบบความปลอดภัย", hook="บ้านหลายคน อาบต่อกัน น้ำยังร้อนไหม", fast=True),
}
CHAIR_EXEC = {
 "Stella": ("เทา", "หลังสบาย ด้วย Lumbar Support", "Stella สีเทา ขาอะลูมิเนียมแข็งแรงทนทาน รุ่นเริ่มต้นของ Bwell Ergo"),
 "Astrid": ("ขาว", "ขาอะลูมิเนียมแข็งแรง ในโทนขาว", "Astrid สีขาว พร้อม Lumbar Support สำหรับมุมทำงานที่บ้าน"),
 "Greta":  ("เทา", "หลังสบายด้วย Lumbar Support", "Greta สีเทา ขาอะลูมิเนียมแข็งแรงทนทาน"),
 "Agnes":  ("เทา", "แข็งแรงทนทานด้วยขาอะลูมิเนียม", "Agnes สีเทา พร้อม Lumbar Support สำหรับคนทำงานเต็มวัน"),
 "Bjorn":  ("เทา", "รุ่นท็อป สำหรับคนนั่งทำงานทั้งวัน", "Bjorn สีเทา ขาอะลูมิเนียมแข็งแรงทนทาน Lumbar Support สำหรับคนนั่งทำงานวันละ 8 ชั่วโมงขึ้นไป"),
}
CUSH_POINT = {
 "Ergonomic-Chair-Seat-Cushion": "Cool Gel Memory Foam",
 "Ergonomic-Car-Lumbar-Cushion": "Cooling Soft Cotton",
 "Ergonomic-Car-Neck-Cushion": "Cooling Soft Cotton",
 "Ergonomic-Chair-Lumbar-Cushion": "ผ้าระบายความร้อน",
}
MOVE_EXEC = _o(headline="High Density NBR รองรับทุกท่า", sub="เสื่อโยคะ Bwell Move วัสดุ NBR ความหนาแน่นสูง หนา 1.2 cm ช่วยรองรับแรงกระแทกระหว่างออกกำลังกาย",
      hook="ซูมเนื้อเสื่อให้ดู เนื้อแน่นแค่ไหน", mp="Bwell เสื่อโยคะ Move High Density NBR หนา 1.2 cm รองรับแรงกระแทก",
      icons="NBR หนาแน่นสูง | หนา 1.2 cm | รองรับแรงกระแทก", kol="ซูมเนื้อเสื่อ (ไม่เทียบยี่ห้อ) · ท่าที่ลงน้ำหนัก · ห้ามพูด \"ป้องกันการบาดเจ็บ\" / \"ลิขสิทธิ์แท้\"")

exec_by_cat = {}
for e in EXEC:
    for c in e["cats"]:
        exec_by_cat[c] = e
# apply to categories
for p in PILLARS:
    for c in p["categories"]:
        e = exec_by_cat.get(c["id"])
        if e:
            c["key_message_prev"] = c["key_message"]
            c["key_message"] = " · ".join(e["km"])
            c["exec"] = True
        else:
            c["exec"] = False
            c["key_message"] += " (นอก Focus ผู้บริหาร 5 พ.ย.)"

def is_focus(s):
    e = exec_by_cat.get(s["cat"])
    if not e: return False
    if s["cat"] == "heat": return True
    if s["cat"] == "cush": return True
    if s["cat"] == "chair": return s["sku"].split(" ")[0] in CHAIR_EXEC
    return s["sku"] in e["focus"]

for s in SKUS:
    e = exec_by_cat.get(s["cat"])
    s["fbig"] = e["fbig"] if e else ""
    s["tt"] = e["tt"] if e else ""
    s["focus"] = is_focus(s)
    ov = None
    if s["sku"] in SKU_EXEC: ov = SKU_EXEC[s["sku"]]
    elif s["cat"] == "heat":
        series = s["sku"].split("-")[0]; h = dict(HEATER_EXEC[series]); fast = h.pop("fast"); watt = s["sku"].split("-")[1].replace("W", "")
        kind = "ร้อน" if series == "Konrad" else "อุ่น"
        ov = dict(h, mp=f"Bwell เครื่องทำน้ำ{kind} {series} {int(watt):,} W ตัดไฟรั่ว ELSD กันน้ำ IP25 5 ระบบความปลอดภัย" + (" ร้อนเร็ว" if fast else ""),
                  icons=f"ELSD 15 mA | IP25 | " + ("ร้อนเร็ว" if fast else f"{int(watt):,} W"),
                  kol="ชี้ 5 ระบบความปลอดภัยบนเครื่องจริง · ELSD + IP25" + (" · ร้อนเร็ว อุณหภูมิสม่ำเสมอ" if fast else " · ห้ามพูดร้อนเร็ว (LUKA)") + " · ห้ามพูด \"10 จุด\" / EV Charger")
    elif s["cat"] == "chair":
        m = s["sku"].split(" ")[0]; color, hl, sub = CHAIR_EXEC[m]
        ov = dict(headline=hl, sub=sub, hook="ปรับ Lumbar Support ให้ดูใน 10 วินาที",
                  mp=f"Bwell Ergo เก้าอี้เพื่อสุขภาพ {m} สี{color} Lumbar Support ขาอะลูมิเนียม",
                  icons="ขาอะลูมิเนียม | Lumbar Support | [BIFMA: รอใบรับรอง]",
                  kol=f"ชื่อ Bwell Ergo {m} ใน 3 วินาทีแรก · สาธิตปรับ Lumbar Support · ขาอะลูมิเนียม · ห้ามพูดขาเหล็ก/ลิขสิทธิ์แท้/BIFMA จนกว่าจะมีเอกสาร")
        s["sku"] = f"{m} ({color} = Focus)"
    elif s["cat"] == "cush":
        pt = CUSH_POINT.get(s["sku"])
        ov = dict(sub=s["sub"] + (f" · {pt}" if pt else ""),
                  mp=s["mp"] + (f" {pt}" if pt else ""),
                  icons=(pt + " | " if pt else "") + "รองรับสรีระ | Bwell Ergo",
                  kol="สาธิตใช้งานจริง" + (f" · บอกจุดขาย {pt}" if pt else "") + " · ห้ามพูด \"ลิขสิทธิ์แท้\" จนกว่าจะมีนิยาม · ห้ามพูดว่ารักษาอาการ")
    elif s["sku"] == "Move":
        ov = MOVE_EXEC
    if ov:
        s.update(ov)
    if s["focus"]:
        s["push"] = "FOCUS 5 พ.ย. · " + s["push"]
    elif e:
        s["push"] = "นอก Focus · " + s["push"]
    else:
        s["push"] = "นอก Focus (หมวดไม่อยู่ใน brief) · " + s["push"]

# ---------------------------------------------------------------- OPEN DECISIONS
OPEN = [
    ["ความหมาย \"ลิขสิทธิ์แท้\"", "ไม่พบนิยาม/ผู้ให้ลิขสิทธิ์ในทุกแหล่ง (เสื่อเป็นคอลแลบ Bwell x illuztika) ตอนนี้ถอดออกจาก copy เก้าอี้/หมอน/เสื่อ เป็น [ช่องรอ]", "Bass + ผู้บริหาร"],
    ["EV Charger Design (น้ำอุ่น)", "พบแค่ใน content draft ภายใน และเฉพาะ LUKA ต้องยืนยันว่าใช้กับซีรีส์ไหน ตอนนี้ไม่อยู่ใน copy", "ผู้บริหาร"],
    ["เอกสารที่ต้องขอ", "ใบ BIFMA รายรุ่น (5 รุ่น) · ใบฉลากเบอร์ 5 + EER ของ BPAC-09B/12B · PDF ต้นฉบับ KJ202302756 (เช็ก CMA) · ผลวัดความหนาแน่นเสื่อ Move · ยืนยัน housing BW-BB20PP = BW-BBH20", "PM / QA"],
    ["แก้หน้าเว็บ", "BW-BB20PP คำว่า \"มาตรฐานน้ำดื่ม\" · AP-H2219S HEPA 0.1 vs 0.01 µm · AP-M1536S พัดลม 3 vs 4 ระดับ · LUKA \"ภายใน 01 วินาที\" · คำอธิบายสั้นหน้าเก้าอี้ (CMS bug)", "Web / E-com"],
    ["\"สำหรับคนเป็นภูมิแพ้\" (เครื่องดูดฝุ่น)", "ยังไม่ได้ตรวจหลักฐานในรอบนี้ ควรตรวจก่อนขึ้นแอด/POSM", "Product"],
    ["สต็อกค้างที่ไม่อยู่ใน Focus", "AP-8119US, CF-8428, CF-8005, G9, AICSN, BW-D10UV5, BW-BB20CTO, Matrix 24\" จะระบายผ่าน bundle/CRM ต่อหรือไม่", "Bass"],
    ["Focus SKU สต็อกต่ำ", "AP-M1536S, AP-H2219S, BAW-02, BDR-04, LUKA 3500W ต้อง restock ก่อนยิงแอด", "Bass + Supply"],
    ["Brand line ที่จะใช้", "เลือก 1 จาก 3 ตัวเลือก (แนะนำ \"สุขภาพดี เริ่มที่บ้าน\")", "Bass"],
    ["สีหลักใน Profile", "Profile ยังเป็น #005D9D แต่ CI ปัจจุบันเป็น #0D99DB → อัปเดต Profile", "Bass"],
    ["ลำดับรุ่นเก้าอี้", "Guideline เดิมจัด Stella เป็น Premium แต่ราคาเว็บต่ำสุด → ยืนยัน tier + feature รายรุ่น", "Product"],
    ["นโยบายราคาข้ามช่องทาง", "Power Buy/HomePro ราคาไม่ตรงเว็บ (สูงและต่ำ) ต้องเคลียร์ก่อนใส่ราคาใน POSM/แอด", "Bass + Sales"],
    ["ถอด claim บนเว็บ", "800 เท่า / กรองเค็ม 100% / รับรองโดยแพทย์ / 20 ปี", "Web team"],
    ["ผูก SKU ใน Product_Facts", "37 fact ยัง BLOCKED_SKU_MAPPING → ผูก exact SKU + asset เพื่อเปลี่ยนเป็น CLAIM-READY", "Product"],
]

DATA = dict(meta=dict(title="Bwell Key Message Playbook", version="v1.2", date="2026-11-19",
                      sources=["claim-evidence/ — ตรวจหลักฐาน claim ผู้บริหารกับ bwell.co.th, Google Drive, Product Master, NSF listing (19 พ.ย. 2026)",
                               "Key_Message.docx — สรุปแนวทางทำ Content จากผู้บริหาร 5 พ.ย. 2026 (มีผลเหนือข้อความเดิม)",
                               "Bwell Product Master — Consolidated Review 2026-09-29 (Products, Prices, Product_Facts)",
                               "Bwell สรุปผู้บริหาร 111 SKU (3 ต.ค. 2026) — สต็อก WICE 8 ก.ย. 2026",
                               "Bwell_Brand_Guidelines_2026.md / Bwell Project Knowledge / CI 10-10 Production Standard",
                               "bwell.co.th (ดึง 2 พ.ย. 2026) — ใช้เป็นข้อมูลประกอบเท่านั้น"]),
            brand=BRAND, claims=CLAIM_RULES, ci=CI, channels=CHANNELS, headline_rules=HEADLINE_RULES,
            funnel=FUNNEL, pillars=PILLARS, skus=SKUS, open=OPEN, exec=EXEC, exec_date=EXEC_DATE, evidence_date=EVIDENCE_DATE, evidence_legend=EVIDENCE_LEGEND)

with open(os.path.join(HERE, "data.json"), "w", encoding="utf-8") as f:
    json.dump(DATA, f, ensure_ascii=False, indent=1)

catmap = {c["id"]: (p["name"], c["name"]) for p in PILLARS for c in p["categories"]}

def spec_str(sp):
    return " ; ".join(f"{s['label']}{(': ' + s['value']) if s['value'] else ''} [{s['status']}{(' · ' + s['fact']) if s['fact'] else ''}]" for s in sp)

with open(os.path.join(HERE, "sku_matrix.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Pillar", "Category", "SKU / Model", "Product name", "Price ref (web 26 ก.ย.)", "Role", "Push status", "Persona",
                "Headline", "Sub-headline", "Video / TikTok hook (0–3s)", "Marketplace title", "POSM 3 icon claims",
                "KOL must-say", "Spec slots [status · fact_id]", "Notes (stock 8 ก.ย. / price / page)", "FB/IG direction (ผู้บริหาร)", "TikTok direction (ผู้บริหาร)"])
    for s in SKUS:
        pn, cn = catmap[s["cat"]]
        w.writerow([pn, cn, s["sku"], s["name"], s["price"], s["role"], s["push"], s["persona"], s["headline"], s["sub"], s["hook"],
                    s["mp"], s["icons"], s["kol"], spec_str(s["specs"]), s["note"], s["fbig"], s["tt"]])

with open(os.path.join(HERE, "category_message_house.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Umbrella", "Pillar", "Category", "Key Message", "Pain", "Benefit", "Reasons to Believe", "Persona", "Competitor frame",
                "TOFU", "MOFU", "BOFU", "Season", "Don't say", "Font"])
    um = {u["id"]: u["name"] for u in BRAND["umbrellas"]}
    for p in PILLARS:
        for c in p["categories"]:
            w.writerow([um[p["umbrella"]], p["name"], c["name"], c["key_message"], c["pain"], c["benefit"], " | ".join(c["rtb"]), c["persona"],
                        c["competitor"], c["funnel"]["TOFU"], c["funnel"]["MOFU"], c["funnel"]["BOFU"], c["season"], c["dont"], c["font"]])

with open(os.path.join(HERE, "channel_rules.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Channel", "Funnel", "Objective", "Message layer", "Tone", "Structure", "Length rule", "CTA", "KPI", "Example"])
    for c in CHANNELS:
        w.writerow([c["name"], c["funnel"], c["objective"], c["layer"], c["tone"], c["structure"], c["length"], c["cta"], c["kpi"], c["example"]])

with open(os.path.join(HERE, "exec_direction.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["หมวด", "Key Message ที่ใช้ (ผ่านตรวจหลักฐาน 19 พ.ย.)", "Key Message ต้นฉบับผู้บริหาร 5 พ.ย.", "SKU ที่เน้น", "จุดขายรายซีรีส์ / Proof", "FB/IG", "TikTok", "Marketplace title formula", "POSM", "KOL", "LINE OA", "ผลตรวจหลักฐาน", "สิ่งที่ต้องทำต่อ"])
    for e in EXEC:
        w.writerow([e["name"], " | ".join(f"{i+1}) {k}" for i, k in enumerate(e["km"])), " | ".join(e["km_exec"]), ", ".join(e["focus"]), " | ".join(e["series"]),
                    e["fbig"], e["tt"], e["mp"], e["posm"], e["kol"], e["line"],
                    " | ".join(f"[{v}] {c} → {r}" for c, v, r, src_ in e["evidence"]), " | ".join(e["flags"])])

with open(os.path.join(HERE, "claim_evidence.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["หมวด", "Claim จากผู้บริหาร", "ผลตรวจ", "คำที่ใช้ / กฎ", "หลักฐาน / แหล่งที่มา"])
    for e in EXEC:
        for c, v, r, src_ in e["evidence"]:
            w.writerow([e["name"], c, v, r, src_])

print("SKUs:", len(SKUS), "| categories:", len(catmap))
