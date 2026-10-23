# Ultra T20 คลิป 30 วิ (ไฟล์ agency) แก้ตาม QC ข้อ 1–4 (23/10/2569)

ไฟล์ต้นฉบับ: pikaso.cdnpk.net .../ym5ddvmwec-h264-1080p.mp4 (1920×1080, 30 วิ)
ไฟล์แก้ v1: https://d2ol7oe51mr4n9.cloudfront.net/user_3Dy6Z3ucZX6ucLB5u9pTBF68wRy/aba3b020-5ffc-4ccf-9ac2-a1580bc2e9ae.mp4

| ข้อ | ปัญหา | ที่แก้ |
|---|---|---|
| 1 | ช็อตแท่นแบรนด์อื่น ("eƒvic / Omnima G7 Box") + ปิดอัปแปรงแดงของแท่นนั้น (ต้นฉบับ ~0:13.2–0:14.2) | ตัดออก แล้วยืดช็อตแปรงข้าง (0:11.2–0:13.2) ให้ช้าลงเป็น 3 วิ เพื่อเติมเวลา คลิปยังยาว 30 วิ เสียงเดิมไม่ขยับ |
| 2 | ช็อตมุมต่ำ ตัวอักษร Bwell บนเครื่องกลับด้าน (0:14.2–0:15.2) | กลับภาพ (hflip) ทั้งช็อต แล้ววางข้อความ "ภาพจำลองการทำงาน" กลับด้านปกติ |
| 3 | super ฟอนต์ไม่ตรง CI, "Bwell" พิมพ์เป็น serif, ไม่มีโลโก้มุมซ้ายบน | ลบ super เดิมทุกช็อต ตั้งใหม่ด้วย DB Helvethaica X Bold + เส้น #0D99DB · โลโก้ขาวมุมซ้ายบน 0:00–0:25.9 · end card ใช้ไฟล์โลโก้แนวนอนทางการ (เปลี่ยนเป็นสีขาว ไม่แตะรูปทรง) + ULTRA T20 + tagline + url ฟอนต์ DBHX |
| 4 | "ล้างและอบผ้าม็อบอัตโนมัติ" | เปลี่ยนเป็น "ซักและเป่าม็อบแห้งอัตโนมัติ" ตามเว็บ |

เพิ่มเติม: ปรับความดังเป็น -14 LUFS (เดิม -17.8)

ยังไม่ได้แก้ (นอกขอบเขตข้อ 1–4): "ระบบนำทาง LiDAR" (เว็บใช้ "นำทางด้วยเลเซอร์"), tagline "ให้บ้านสะอาด เป็นเรื่องง่าย" (ยังรอยืนยัน), แปรงหลักสีแดง/ไฟหน้าเครื่องตอนจอดแท่น (ยืนยันไม่ได้)

Overlay: text/ (a–g = super, endcard.png, logo_tl.png)

## Fix v2 (2026-10-23)
URL: https://d2ol7oe51mr4n9.cloudfront.net/user_3Dy6Z3ucZX6ucLB5u9pTBF68wRy/4d21e21b-f9d7-4ad7-887c-a9a511bf82b9.mp4

| Item | Change |
|---|---|
| Voiceover | Removed. Audio = stereo side + low-end (<110Hz) of original mix; whisper finds no speech. Loudnorm -14 LUFS, fade out 28.8s |
| Underside shots | Replaced with 2 Seedance 2.5 clips (11.2-14.2s, 15.2-18.2s): teal main brush, teal side brush, 2 rear mops, wheels on floor |
| Logo top-left | Bwell Electric white |
| Disclaimer | "ภาพจำลองการทำงาน" removed everywhere |
| Supers | Bwell Ultra T20 / นำทางด้วยเลเซอร์ / วางแผนเส้นทางทำความสะอาด / ดูดฝุ่น / ถูพื้นด้วยผ้าม็อบหมุนคู่ / ซักและเป่าม็อบแห้งอัตโนมัติ / All-in-One Station |
| Purple light | Re-graded to CI blue via 3D LUT |
| End | 25.9s end card (logo + Ultra T20 + tagline + www.bwell.co.th), 28.2s Bwell logo slate |
