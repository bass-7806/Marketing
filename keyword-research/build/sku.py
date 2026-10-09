import json
# Google Merchant Center, last 90 days (product_impressions, product_clicks); rows with >= 1,000 impressions
R = [
("เครื่องฟอกอากาศ PM2.5 รุ่น AP-M1536S","Air purifier",23254,96),
("Bwell เครื่องทําน้ําอุ่น ELKA ขนาด 3,500 วัตต์","Water heater",10431,16),
("เครื่องกรองน้ําระบบ UV รุ่น BW-D10UV5","Water purifier",10211,42),
("Bwell เสื่อออกกําลังกาย เสื่อโยคะ รุ่น Move","Fitness",9653,24),
("(ไม่มี title ใน feed)","Unknown",8820,35),
("เครื่องดูดฝุ่นไร้สาย รุ่น 201A","Vacuum",8814,13),
("Bwell เบาะรองนั่งเพื่อสุขภาพ - Ergonomic Chair Seat Cushion","Ergonomic",8179,53),
("Bwell หมอนรองคอเพื่อสุขภาพสําหรับรถยนต์","Ergonomic",7731,40),
("เครื่องกรองน้ํา ระบบ RO รุ่น BW-D10RO5","Water purifier",6568,3),
("แอร์เคลื่อนที่ Bwell รุ่น BPAC-12B","Portable AC",5431,13),
("Bwell เบาะรองนั่งเพื่อสุขภาพ (listing ที่ 2)","Ergonomic",5187,40),
("หุ่นยนต์ดูดฝุ่น Bwell รุ่น L6C","Vacuum",5130,11),
("Bwell เบาะรองหลังสําหรับรถยนต์","Ergonomic",5029,12),
("Bwell เบาะรองหลังเพื่อสุขภาพ","Ergonomic",4872,29),
("Foam Roller รุ่น Matrix 24 นิ้ว","Fitness",4376,1),
("หุ่นยนต์ดูดฝุ่น Bwell รุ่น Y1","Vacuum",3786,11),
("เครื่องฟอกอากาศพกพา / ในรถยนต์ Bwell","Air purifier",3472,50),
("Bwell เครื่องดูดฝุ่นไร้สาย 170 AW รุ่น T12 Allergy Pro","Vacuum",3328,5),
("แอร์เคลื่อนที่ BWELL","Portable AC",3213,25),
("เครื่องฟอกอากาศรถยนต์ รุ่น G8","Air purifier",3115,40),
("เครื่องลดความชื้น Bwell รุ่น BDH-53A","Dehumidifier",3046,34),
("เครื่องลดความชื้น Bwell รุ่น BDH-53","Dehumidifier",2950,41),
("เครื่องลดความชื้น Bwell รุ่น BDH-26","Dehumidifier",2941,21),
("Bwell เก้าอี้ Ergonomic รุ่น Agnes สีดํา","Ergonomic",2464,6),
("เครื่องฟอกอากาศในรถยนต์ รุ่น G9","Air purifier",2248,12),
("แอร์เคลื่อนที่ Bwell รุ่น BPAC-09B","Portable AC",2245,4),
("Foam Roller รุ่น Matrix 13 นิ้ว","Fitness",2110,1),
("Bwell เก้าอี้ Ergonomic รุ่น Agnes สีเทา","Ergonomic",2026,2),
("Bwell หวีไดร์จัดแต่งทรงผม BLDC รุ่น BSL-01","Hair",1985,3),
("Bwell เครื่องกรองน้ําดื่ม UV 5 ขั้นตอน รุ่น BW-D10UV5 (listing ที่ 2)","Water purifier",1949,0),
("เครื่องกรองน้ํา RO แบบไร้ถัง","Water purifier",1853,32),
("เครื่องกรองน้ําระบบ UF รุ่น BW-D10UF5","Water purifier",1845,17),
("เครื่องดูดฝุ่นพร้อมถูพื้น Bwell รุ่น Flomo Lite","Vacuum",1827,6),
("Bwell ที่วางเท้าเพื่อสุขภาพ","Ergonomic",1764,12),
("เครื่องฟอกอากาศกําจัดไวรัส รุ่น CF-8005","Air purifier",1691,22),
("เครื่องลดความชื้น Bwell รุ่น BDH-12A","Dehumidifier",1493,18),
("Bwell เครื่องจัดแต่งทรงผม BLDC 7 หัว รุ่น BAW-02","Hair",1485,13),
("Bwell Ergonomic Set-01","Ergonomic",1358,4),
("เครื่องลดความชื้น Bwell รุ่น BDH-30A","Dehumidifier",1217,34),
("Bwell เก้าอี้ Ergonomic รุ่น Stella สีเทา","Ergonomic",1215,6),
("เครื่องปรับอากาศเคลื่อนที่ BPAC-12 (OUT_OF_STOCK ใน feed)","Portable AC",1081,3),
("(สินค้าตัวโชว์) BDH-53","Dehumidifier",1027,5),
("Bwell เครื่องกรองน้ําใช้ PP 1 ขั้นตอน รุ่น BW-BB20PP","Water purifier",1004,0),
]
out=[]
for t,c,i,k in R:
    ctr=k/i*100
    if ctr>=1.0: a="Scale: CTR ดี ใช้ title นี้เป็นต้นแบบ"
    elif ctr>=0.5: a="Keep"
    elif i>=5000: a="Fix title/image/price: impressions สูงแต่ CTR ต่ำ"
    else: a="Optimize title (ใส่ keyword spec + ประโยชน์ด้านสุขภาพ)"
    out.append(dict(product=t,category=c,impr=i,clicks=k,ctr=round(ctr,2),action=a))
json.dump(out,open("sku.json","w"),ensure_ascii=False,indent=1)
print(len(out), sum(r["impr"] for r in out), sum(r["clicks"] for r in out))
