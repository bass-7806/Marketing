import json, re, sys, collections
F = sys.argv[1]
rows = json.load(open(F))["result"]
def norm(s): return re.sub(r"\s+", "", (s or "").lower())
CAT = [
 ("Air - Air purifier", r"ฟอกอากาศ|กรองอากาศ|airpurifier|airfilter|ฟอก"),
 ("Air - Dehumidifier", r"ความชื้น|ความชื่น|dehumid"),
 ("Air - Portable AC", r"แอร์เคลื่อนที่|portableair|แอร์"),
 ("Clean Home - Vacuum/Robot", r"ดูดฝุ่น|robotvacuum|หุ่นยนต์|โรบอท|vacuum|ไรฝุ่น"),
 ("Water - Purifier", r"กรองน้ำ|กรองน้ํา|ro$|ro\b|uv|uf"),
 ("Water - Heater", r"น้ําอุ่น|น้ำอุ่น|น้ําร้อน|น้ำร้อน"),
 ("Ergonomic", r"เก้าอี้|ergonomic|chair|เบาะ|หมอน"),
 ("Hair styling", r"ไดร์|ผม|\bhair|^hair"),
 ("Brand - Bwell", r"bwell"),
 ("Brand - Bewell (confusion)", r"bewell"),
]
COMP = r"xiaomi|เสี่ยวหมี่|dyson|ไดสัน|philips|ฟิลิปส์|sharp|ชาร์ป|panasonic|พานา|hatari|ฮาตาริ|mitsubishi|มิตซู|dreame|roborock|ecovacs|samsung|ซัมซุง|\blg\b|แอลจี|coway|โคเวย์|tcl|toshiba|โตชิบา|electrolux|imarflex|smarthome|clarte|aiko|deerma|midea|stiebel|สตีเบล|mazuma|มาซูม่า|centon|ariston|daikin|ไดกิ้น|carrier|ergotrend|sihoo|erghome|blissful|bewell|ikea|อิเกีย|babyliss|vidal|brita|pure|safe|aquatek|unipure|treatton|shimono|tefal|บ้านกรองน้ำ|wells?เครื่อง|^well|wells|amway|แอมเวย์|superv|lenodi|hafele|bluesky|blueair|bionaire|irobot|roomba|karcher|hitachi|astina|richemuller|libernovo|xpanse|hbada|ergotrend|lazada|shopee|homepro|powerbuy|central|makro|lotus|bigc|บิ๊กซี|โฮมโปร"
def intent(q, kw):
    if re.search(r"bewell|บีเวล", q): return "Bewell confusion"
    OWN=r"cf-?8\d{3}|ap-?[mhp]\d{4}|ap-?8119|bdh-?\d|bpac|bw-?d\d|bsl-?0|bcl-?0|bst-?0|bdr-?0|baw-?0|t12allergy|pm1330|ro-?500|aicsn|flomo"
    if re.search(OWN, q) and not re.search(COMP, q): return "Own brand + model"
    if re.search(r"bwell", q):
        return "Own brand + model" if re.search(r"[a-z]{1,4}-?\d{2,}", q.replace("bwell","")) else "Own brand"
    if re.search(COMP, q): return "Competitor / retailer"
    if re.search(r"ช่วยอะไร|คืออะไร|วิธี|how|ทํางานยังไง|ทำงานยังไง|หลักการทํางาน|หลักการทำงาน|ข้อเสีย|ดียังไง|จําเป็น|จำเป็น|ต่างกัน|อันตราย|ใช้ยังไง|ซ่อม|ล้าง|ทําเอง|ทำเอง|diy|ประกอบ", q): return "Informational"
    if re.search(r"มือสอง|เช่า|ถูกๆ|ราคาถูก|ไม่เกิน|ร้อยบาท|\d{3}บาท", q): return "Low-value / bargain"
    if re.search(r"ยี่ห้อไหน|รีวิว|review|แนะนํา|แนะนำ|pantip|best|ตัวไหนดี|อันไหนดี|ดีไหม|ดีมั้ย|ที่ดีที่สุด|top", q): return "Comparison (MOFU)"
    if re.search(r"pm2\.?5|ฝุ่นpm|ฝุ่นละออง|กรองฝุ่น|ภูมิแพ้|แพ้|ไวรัส|เชื้อโรค|เด็ก|ทารก|baby|ขนแมว|ขนหมา|สัตว์|pet|เชื้อรา|อับชื้น|ห้องนอน|ปวดหลัง|ออฟฟิศ|office|ตรม|ตารางเมตร|เสียงเงียบ|ประหยัดไฟ|ในรถ|รถยนต์|ไร้สาย|ไรฝุ่น|ที่นอน|ดื่ม|ประปา|บาดาล|ในบ้าน|btu|ลิตร", q): return "Need-state / spec (MOFU)"
    if re.search(r"ราคา|price|โปร|ลดราคา|ซื้อ|ร้าน|ขาย", q): return "Purchase intent (BOFU)"
    if re.search(r"[a-z]{1,4}-?\d{3,}", q): return "Model number"
    return "Generic category (TOFU)"
out = []
for r in rows:
    q = norm(r["session_google_ads_query"]); kw = norm(r["session_google_ads_keyword"])
    cat = next((c for c,p in CAT if re.search(p, kw)), None) or next((c for c,p in CAT if re.search(p, q)), "Other")
    if re.search(r"bewell", q) : cat_q = "Brand - Bewell (confusion)"
    out.append(dict(cat=cat, kw=r["session_google_ads_keyword"], q=r["session_google_ads_query"], qn=q,
                    intent=intent(q, kw), s=r["sessions"], t=r["transactions"], rev=r["purchase_revenue"]))
json.dump(out, open(sys.argv[2], "w"), ensure_ascii=False)
agg = collections.defaultdict(lambda:[0,0,0])
for o in out: a=agg[(o["cat"],o["intent"])]; a[0]+=o["s"]; a[1]+=o["t"]; a[2]+=1
for k,v in sorted(agg.items(), key=lambda x:(x[0][0], -x[1][0])): print(f"{k[0]:32s} {k[1]:28s} sess={v[0]:5d} txn={v[1]} queries={v[2]}")
ia = collections.defaultdict(lambda:[0,0])
for o in out: ia[o["intent"]][0]+=o["s"]; ia[o["intent"]][1]+=o["t"]
print(); [print(f"{k:28s} {v[0]:6d} {v[1]}") for k,v in sorted(ia.items(), key=lambda x:-x[1][0])]
