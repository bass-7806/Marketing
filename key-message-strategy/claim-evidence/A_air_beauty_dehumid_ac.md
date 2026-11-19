# Bwell claim evidence — A (air purifiers), B (beauty), C (dehumidifiers), D (portable AC)

Checked 2026-11-19. Sources: live bwell.co.th product pages (fetched/curl'd today), Google Drive files (name + ID given), Product Master sheet `15OrOZ4sSnuYgYST2am1mp6xvUs7RP32hTqMPZq_Qmyg` (tab Product_Facts), and third-party retailer pages where noted. Quotes are verbatim (Thai/English as in source). Nothing here is inferred beyond what the quote says.

Short URLs used below:
- **P4019-web** = https://bwell.co.th/product/ap-p4019us/
- **M1536-web** = https://bwell.co.th/product/เครื่องฟอกอากาศ-pm-bwell-รุ่น-ap-m1536s/
- **H2219-web** = https://bwell.co.th/product/เครื่องฟอกอากาศ-bwell-รุ่น-ap-h2219s/
- **AP-cat** = https://bwell.co.th/air-purifier-bwell/

Product Master `Product_Facts` tab: **no rows** for AP-M1536S, AP-H2219S, AP-P4019US, BDR-03 rpm, BDR-04 rpm, BAW-02, BSL-01 rpm, BDH-12A, BDH-53A, BPAC-09B, BPAC-12B. The only relevant rows are BDH30A_ROOM_AREA (20–40 m²) and BDH30A_DEHUMIDIFY_CAPACITY (30 L/day), both VERIFIED source-text, BLOCKED_SKU_MAPPING.

---

## A1. "สำหรับเด็กและคนเป็นภูมิแพ้" (certification or lab test)

| Claim | SKU | Verdict | Evidence quote | Source link |
|---|---|---|---|---|
| For children/allergy sufferers | AP-P4019US | PARTIAL (the brand's own wording only; no allergy certification found) | Brochure: "An air purifier specifically designed for children and people with allergies" and "Allergist's Choice" (no issuer, criteria or body named). The web filter list says "สารก่อภูมิแพ้จากแมลงสาบ และสารก่อภูมิแพ้อื่นๆ" (HEPA). | Drive: `brochure_AP-P4019US_compressed 31012024.pdf` (ID 1N9_c_gIjR9lBonrH8BbFhuVsHomFO-SH); P4019-web |
| For children/allergy sufferers | AP-M1536S | NOT FOUND (no certification; only a general HEPA allergen mention) | "ช่วยกรองฝุ่นขนาดเล็ก PM2.5 สารก่อภูมิแพ้ ละอองเกสร ขนสัตว์"; "มีระบบ Child lock ป้องกันเด็กกดเล่น" (this is a button lock, not a health claim). Manual: "HEPA FILTER：Captures dust, smoke, pollen and other allergens." | M1536-web; Drive `User Manual AP-M1536S [EN-TH].pdf` (1fUGVz7Ri8pVSTfMqjpBbUshueE1cjUNp) |
| For children/allergy sufferers | AP-H2219S | NOT FOUND (same as M1536S) | "ช่วยกรองฝุ่นขนาดเล็ก PM2.5 สารก่อภูมิแพ้ ละอองเกสร ขนสัตว์"; "มีระบบ Child lock ป้องกันเด็กกดเล่น". The color box says only "Sensitive Air Purifier". | H2219-web; Drive `color box AP-H2219S.pdf` (1JTToaJimYhJIc8ZPcBeytYT3CRoFQY-q) |
| Category-level wording | all | PARTIAL (general marketing copy, not tied to a model or a test) | AP-cat: "โดยเฉพาะทารก เด็ก และผู้ป่วยที่มีอาการภูมิแพ้ สามารถฟอกอากาศได้ครบวงจร"; "เหมาะสำหรับผู้ที่มีภูมิแพ้หรือโรคทางเดินหายใจ" | AP-cat |

Places searched for an Allergy UK / AAFA / asthma & allergy friendly / ECARF / CAC / "Allergist" / test report: all 3 product pages, AP-cat, 2 manuals, 2 color boxes, the P4019US brochure, and Drive full-text. Result: **no third-party allergy certification exists in any of these sources**. The only certification marks found are "มอก. 60335 เล่ม 2(65)-2564" (all 3 color boxes and the brochure) and "CE" (P4019US brochure). Both are electrical-safety marks, not allergy marks.

## A2. "ไม่ปล่อยประจุไฟฟ้า" (ionizer / plasma / anion?)

| Claim | SKU | Verdict | Evidence quote | Source link |
|---|---|---|---|---|
| No ionizer | AP-M1536S | PARTIAL (no ionizer is listed anywhere, but no source states "no ion" positively) | Manual filtration: "PRE-FILTER… HEPA FILTER… CARBON FILTER". Buttons: POWER/WIFI, SPEED, TIMER, AUTO, SLEEP, NIGHT LIGHT, CHILD LOCK, FILTER RESET. None of these is an ion, anion or plasma function. The web page spec also has no ion item. | Drive 1fUGVz7Ri8pVSTfMqjpBbUshueE1cjUNp; M1536-web |
| No ionizer | AP-H2219S | PARTIAL (same as M1536S) | Manual: "PRE-FILTER… HEPA FILTER… CARBON FILTER". Buttons: POWER/WIFI, CHILD LOCK, SPEED, SLEEP, AUTO, TIMER, FILTER RESET. No ion function. | Drive `User Manual AP-H2219S [EN-TH].pdf` (1AhAFF0PQbvRjwX0uTLvyBY03PJhRbrLX); H2219-web |
| No ionizer | AP-P4019US | PARTIAL (no ionizer listed; the unit does have UV-C + TiO2 PCO, which is not an ionizer) | Manual: "7) UV-C LIGHT… 8) TiO2: Uses along with UV light to create Photocatalytic Oxidation (PCO)"; "“UV” BUTTON: Press this button to turn on/off UV function." No ion or anion button. | Drive `TISI_Eng_Thai_AP-P4019US-Manual (คู่มือ).pdf` (1yhmhLnKj-t7cfgBl4X2O8p50XR3Fd9AX) |
| Caveat | all 3 pages | — | The shared article block on every product page describes Ionizer as a *generic type*: "เครื่องฟอกอากาศประเภทที่ปล่อยประจุลบ…" and says HEPA type "ไม่ปล่อยสารเคมีหรือโอโซน". This is not a model spec. No ozone or emission test was found. | P4019-web / M1536-web / H2219-web |

## A3. AP-P4019US "ฟอกอากาศ 8 ขั้นตอน"

| Claim | SKU | Verdict | Evidence quote | Source link |
|---|---|---|---|---|
| 8 stages | AP-P4019US | SUPPORTED (website, manual and brochure all list 8; the live page today lists 8, not 7) | Web: "ฟอกอากาศ 8 ขั้นตอน" + list: "1.แผ่นกรอง Pre-filter / 2.แผ่นกรอง Anti-virus / 3.แผ่นกรอง HEPA : เกรด H13 ละเอียด 0.003 ไมครอน / 4.แผ่นกรอง Charcoal / 5.แผ่นกรอง Zeolite / 6.Potassium Permanganate Filter / 7.Ultraviolet Germicidal Irradiation (UVGI) / 8.Titanium dioxide (TiO2)…Photocatalytic Oxidation (PCO)". Manual: "your 8-stage air cleaning system 1) PRE-FILTER 2) ANTIBACTERIA/VIRUS 3) HEPA FILTER 4) CHARCOAL FILTER 5) ZEOLITE FILTER 6) POTASSIUM PERMANGANATE FILTER 7) UV-C LIGHT 8) TiO2". | P4019-web (modified 2026-06-09); Drive 1yhmhLnKj-t7cfgBl4X2O8p50XR3Fd9AX; brochure 1N9_c_gIjR9lBonrH8BbFhuVsHomFO-SH ("ระบบฟอกอากาศ 8 ขั้นตอน") |
| Note | AP-P4019US | — | Stages 7 and 8 are UV lamp and PCO coating, not filter media. "8 ขั้นตอน" = 6 filter layers + 2 light/catalyst stages. | same |

## A4. "ฆ่าเชื้อ" (technology and lab result)

| Claim | SKU | Verdict | Evidence quote | Source link |
|---|---|---|---|---|
| Kills germs | AP-P4019US | SUPPORTED (virus, H1N1 only, chamber test) | Lab: Guangzhou Institute of Microbiology Group Co., Ltd. / National Center of Quality Inspection and Testing on Air Purification Products, Report No. **KJ202302756**, Type "AP-P4019US", standard "GB/T 18801-2022", "Virus Removal Rate (Influenza A virus A/PR/8/34 H1N1)", 30 m³ chamber, 60 min, running state "the highest wind speed”, “UV”", result "Mean >99.99". Report date 2024-01-04. Also tested: CADR (Formaldehyde) 124.9 m³/h. | Drive `Bwell_Virus_Test_Report.pdf` (15q3gk5RJalmaUfDkR6gktLRYqgZxCV4u) |
| Report limitation | AP-P4019US | — | Report statement: "The items marked with“\*”in the report are not accredited by CNAS and CMA… results of items which are not accredited by CMA, only can be used as scientific research, teaching or internal quality control." The text extraction does not show which items carry \*/#/+, so the accreditation status of the virus item is unknown and needs a check against the original PDF. The test covers **virus (H1N1) only, not bacteria**. | same |
| Technology | AP-P4019US | SUPPORTED | Web: "ฆ่าเชื้อไวรัสในอากาศด้วยแสง UV-C"; manual: "This appliance has a built-in UV-C emitter". | P4019-web; Drive 1yhmhLnKj-t7cfgBl4X2O8p50XR3Fd9AX |
| Brochure % figures | AP-P4019US | PARTIAL (no lab is cited for these numbers) | "ใช้รังสีจากหลอด UV ในการฆ่าเชื้อแบคทีเรียและเชื้อไวรัสในอากาศได้ถึง 99.99%"; "Antibacteria/Virus Filter…กรองแบคทีเรียและเชื้อไวรัสได้ถึง 99.91%"; "ช่วยเพิ่มประสิทธิภาพในการทำลายเชื้อไวรัสโคโรนา"; "ตามมาตรฐาน U.S. Environmental Protection Agency (EPA)". No bacteria or coronavirus test report was found in Drive. | Drive 1N9_c_gIjR9lBonrH8BbFhuVsHomFO-SH |
| Kills germs | AP-M1536S, AP-H2219S | NOT FOUND (no UV or germicidal function) | Specs and manuals list only Pre-filter / HEPA / Carbon. The category page's "UV+PCO" refers to the brand line in general, not these models. Internal brief: "ไม่เติม UV ให้ AP-M1536S/AP-H2219S". | M1536-web, H2219-web, manuals above; Drive `Category-Directions.csv` (1L2ccdGGuo2sCtofdZl1r2MkZ-sEi3nok) |

## A5. WiFi

| Claim | SKU | Verdict | Evidence quote | Source link |
|---|---|---|---|---|
| WiFi | AP-M1536S | SUPPORTED | "สามารถเชื่อมต่อ Wifi และควบคุมการทำงานด้วยแอพ Smartlife"; manual: "Press and hold for 3-5 seconds to active or reset wifi connection and connect with TUYA SMART app."; box: "WIFI Connected" | M1536-web; Drive 1fUGVz7Ri8pVSTfMqjpBbUshueE1cjUNp; `color box AP-M1536S.pdf` (1uPHvCxfsj03fdoy-ie4ByRtBWXXvUvA9) |
| WiFi | AP-H2219S | SUPPORTED | "สามารถเชื่อมต่อ Wifi และควบคุมการทำงานด้วยแอพ Smartlife"; manual: "...reset wifi connection ad connect with TUYA SMART app"; box: "WIFI Connected" | H2219-web; Drive 1AhAFF0PQbvRjwX0uTLvyBY03PJhRbrLX; 1JTToaJimYhJIc8ZPcBeytYT3CRoFQY-q |

Side notes (data conflicts):
- AP-H2219S HEPA is "ละเอียด 0.1 ไมครอน" in the spec list but "0.01 ไมครอน" in the filter list on the same page.
- The AP-M1536S manual says speed I/II/III in the English section, but the Thai section adds "IV (เทอรโบ)". The web page says "3 ระดับ".

---

## B. Beauty: "Digital" and "มอเตอร์ BLDC 110,000 รอบ/นาที"

| Claim | SKU | Verdict | Evidence quote | Source link |
|---|---|---|---|---|
| BLDC 110,000 rpm | BDR-03 | SUPPORTED | "มอเตอร์ BLDC Brushless ความเร็วสูง 110,000 รอบ/นาที – แรงลมทรงพลัง เป่าผมแห้งเร็วกว่าไดร์ทั่วไปถึง 5 เท่า" | https://bwell.co.th/product/bldc-hair-dryer-bdr03/ |
| Digital | BDR-03 | SUPPORTED | Title "Bwell ไดร์เป่าผม BLDC ดิจิตอล"; "Digital Display – แสดงผลการตั้งค่าลมและอุณหภูมิชัดเจน ใช้งานง่าย" | same |
| BLDC 110,000 rpm | BDR-04 | SUPPORTED | "มอเตอร์ BLDC Brushless ความเร็วสูง 110,000 รอบ/นาที – เป่าและหนีบผมตรงได้ในเวลาเดียวกัน" | https://bwell.co.th/product/magic-air-straightener-bdr04/ |
| Digital | BDR-04 | SUPPORTED | "หน้าจอ Digital แสดงอุณหภูมิ สามารถปรับอุณหภูมิได้ 5 ระดับ" | same |
| BLDC 110,000 rpm | BAW-02 | SUPPORTED | "BLDC Brushless มอเตอร์ความเร็วสูง 110,000RPM (รอบ/นาที)" | https://bwell.co.th/product/bldc-multi-hair-styler-baw02/ |
| Digital | BAW-02 | NOT FOUND | The product spec has no Digital/display line. On this page "ดิจิตอล" appears only in related-product titles (BCL-02/03/04/05, BDR-03). | same |
| BLDC 110,000 rpm | BSL-01 | SUPPORTED | "BLDC มอเตอร์ความเร็วสูง 110,000 รอบ/นาที ให้แรงลมทรงพลังระดับซาลอน พร้อมอายุการใช้งานยาวนาน" | https://bwell.co.th/product/bldc-hot-air-styler-bsl01/ |
| Digital | BSL-01 | NOT FOUND | No Digital/display spec line. "ดิจิตอล" appears only for BSL-02 ("Bwell หวีลมร้อน ดิจิตอล 38 มม. รุ่น BSL-02") in related products. | same |

Wattage, for reference: BDR-03 1600W; BDR-04 1200W; BAW-02 1480W; BSL-01 1400W (each from its page).

No rpm test or motor datasheet was found in Drive for these 4 SKUs. The Drive file `Product Test TISI.pdf` (1sarzu0TmFGmWM7fibXa77d4tsWYY8cC9) shows "110000RPM BLDC" for **LN-2415A / LN-2423**, which are OEM codes. It does not map them to BDR/BAW/BSL, so I did not use it.

---

## C. Dehumidifiers: compressor, WiFi, dimensions

| Claim | SKU | Verdict | Evidence quote | Source link |
|---|---|---|---|---|
| Compressor | BDH-12A | PARTIAL (compressor confirmed; type such as rotary or inverter not stated) | "ลดความชื้นด้วยระบบคอมเพรสเซอร์ ช่วยให้ดูดความชื้นได้มาก และรวดเร็วต่อเนื่องกว่าระบบทั่วไป"; "(ตัวคอมเพรสเซอร์ 3 ปี)" | https://bwell.co.th/product/เครื่องลดความชื้น-bwell-รุ่น-bdh/ |
| WiFi | BDH-12A | NOT FOUND (absent from the spec, which suggests no WiFi) | The spec list has no WiFi line; the 30A and 53A pages do have one. | same |
| Dimensions | BDH-12A | SUPPORTED | "ขนาดเครื่อง 280 x 195 x 386 มิลมิเมตร"; "น้ำหนัก 9.7 กิโลกรัม"; 270 W; 12 L/day; 10–20 ตร.ม. | same |
| Compressor | BDH-30A | PARTIAL (type not stated) | "ลดความชื้นด้วยระบบคอมเพรสเซอร์…"; "(ตัวคอมเพรสเซอร์ 3 ปี)" | https://bwell.co.th/product/เครื่องลดความชื้น-bwell-bdh-30a/ |
| WiFi | BDH-30A | SUPPORTED | "สามารถเชื่อมต่อ Wifi ควบคุมการทำงาน"; "ตรวจสอบและควบคุมระดับความชื้นได้อย่างแม่นยำผ่านแอป พร้อมรับการแจ้งเตือน" | same |
| Dimensions | BDH-30A | SUPPORTED | "ขนาดเครื่อง 310 x 229 x 500 มิลมิเมตร"; 13.3 kg; 590 W; 30 L/day; 20–40 ตร.ม. (also Product_Facts BDH30A rows) | same; Product Master Product_Facts |
| Compressor | BDH-53A | PARTIAL (type not stated) | "ลดความชื้นด้วยระบบคอมเพรสเซอร์…"; "(ตัวคอมเพรสเซอร์ 3 ปี)" | https://bwell.co.th/product/เครื่องลดความชื้น-bwell-bdh-53a/ |
| WiFi | BDH-53A | SUPPORTED | "สามารถเชื่อมต่อ Wifi ควบคุมการทำงาน" | same |
| Dimensions | BDH-53A | SUPPORTED | "ขนาดเครื่อง 390 x 268 x 612 มิลมิเมตร"; 17.9 kg; 980 W; 53 L/day; 40–80 ตร.ม. | same |

No user manual for BDH-12A, BDH-30A or BDH-53A was found in Drive. Drive has manuals only for the older BDH-20 and BDH-30 (no "A"); these were not used.

---

## D. Portable AC: BTU, energy label No. 5, EER/CSPF, watts

| Claim | SKU | Verdict | Evidence quote | Source link |
|---|---|---|---|---|
| BTU | BPAC-09B | SUPPORTED (rated) | "ขนาดทำความเย็น 9,000 บีทียู/ชม." | https://bwell.co.th/product/แอร์เคลื่อนที่/ |
| Wattage | BPAC-09B | SUPPORTED | "กำลังไฟฟ้า 1,000 วัตต์"; "ระบบไฟฟ้า 220V/50Hz"; "สารทำความเย็น (น้ำยาแอร์) R410" | same |
| ฉลากเบอร์ 5 | BPAC-09B | PARTIAL (retailer only; not on the Bwell page or in Drive) | HomePro: "ฉลากประหยัดไฟ, ฉลากประหยัดไฟเบอร์5"; Power Buy: "ขนาด(BTU ที่ระบุในฉลากประหยัดไฟ):9000" | https://www.homepro.co.th/p/1264609 ; https://www.powerbuy.co.th/th/product/BWELL-Portable-Air-Conditioner-9000-BTU-BPAC-09B-299326 |
| BTU | BPAC-12B | SUPPORTED (rated) | "ขนาดทำความเย็น 12,000 บีทียู/ชม." | https://bwell.co.th/product/แอร์เคลื่อนที่-bwell-รุ่น-bpac-12b/ |
| Wattage | BPAC-12B | SUPPORTED | "กำลังไฟฟ้า 1,400 วัตต์"; 220V/50Hz; R410; 33 x 28 x 70 cm; 21.7 kg | same |
| ฉลากเบอร์ 5 | BPAC-12B | PARTIAL (retailer only) | HomePro spec table: "ฉลากประหยัดไฟเบอร์5" | https://www.homepro.co.th/p/1264635 |
| EER / CSPF | BPAC-09B, BPAC-12B | NOT FOUND | Neither Bwell page lists EER, CSPF or SEER; neither do HomePro or Power Buy. | pages above |
| EER (older model) | BPAC-12 (no "B") | DO NOT TRANSFER (different model) | Manual: "Rated Energy Efficiency Ratio(EER rated ) 2.6", "EER rated Class A", "Cooling Input Power/Current 1300W/6.2A", 30 kg. BPAC-12B is 1,400 W and 21.7 kg, so these figures cannot be applied to it. | Drive `BPAC-12_Eng_Thai_User_Manual.pdf` (1uegzaFf6Up6qbG87g2CmFvLQTrCYGK-C) |
| "ประหยัดไฟ" | both | NOT FOUND on Bwell sources (only the retailer label above) | The Bwell AC category page has no ประหยัดไฟ / EER / label wording. | https://bwell.co.th/portable-air-conditioner/ |
| "เย็นเต็ม BTU" | both | NOT FOUND (only rated BTU exists; no measured-capacity test) | The only evidence is the rated "9,000 / 12,000 บีทียู/ชม."; no capacity test report was found in Drive. | pages above; Drive search |

Arithmetic from the stated figures, which is not an official EER: 9,000/1,000 = 9.0 BTU/Wh and 12,000/1,400 ≈ 8.6 BTU/Wh. The input watts may not be the rated cooling input, so do not publish these as EER.

---

### Where I looked (summary)
- bwell.co.th: the 3 air purifier pages, the air-purifier category page, the hair-styling category page and 4 beauty pages, the dehumidifier category page and 3 dehumidifier pages, the portable-AC category page and 2 AC pages.
- Retailers: HomePro (BPAC-09B and BPAC-12B), Power Buy (BPAC-09B). Shopee and Lazada snippets only confirm the BTU and rpm wording.
- Drive: full-text and title searches for each SKU, plus allergy/certification/test-report terms. Files read: P4019US brochure, P4019US / M1536S / H2219S manuals, M1536S / H2219S color boxes, Bwell_Virus_Test_Report, BPAC-12 manual, BPAC docx (2021, older BPAC-09/12).
- Product Master: Product_Facts (whole tab) and the Products header.
