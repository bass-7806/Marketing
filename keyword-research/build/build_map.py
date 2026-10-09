import json, re, csv, sys, collections
C = json.load(open(sys.argv[1]))
def ev(rx, cat=None):
    s=t=n=0
    for r in C:
        if cat and not r["cat"].startswith(cat): continue
        if re.search(rx, r["qn"]): s+=r["s"]; t+=r["t"]; n+=1
    return s,t,n
NEG = r"bewell|บีเวล|มือสอง|เช่า|ราคาถูก|ไม่เกิน\d|ซ่อม|วิธี|ช่วยอะไร|ดียังไง|ทํางานยังไง|ทำงานยังไง"
# cat, cluster, funnel, keywords, evidence regex, channels, match, action, priority, note
CL = [
 # Brand
 ("Brand","Bwell brand core","BOFU","bwell; บีเวลล์; bwell thailand; bwell group; bwell official","^bwell$|bwellthailand|bwellgroup|wwwbwell|bwellofficial","Google Search; Marketplace; SEO","Exact + Phrase","Protect - always on","P1","Own brand queries ได้ 5 จาก 6 transactions ที่ track ได้ใน paid search ระดับ query ต้องใส่ negative 'bewell' ให้ campaign นี้ด้วย"),
 ("Brand","Bwell + category","BOFU","bwell เครื่องฟอกอากาศ; เครื่องฟอกอากาศ bwell; bwell air purifier; bwell เครื่องดูดความชื้น; bwell แอร์เคลื่อนที่; bwell เครื่องกรองน้ำ; bwell ไดร์เป่าผม; bwell เครื่องดูดฝุ่น","^(?!bwell(thailand|group|official)?$)(?!wwwbwell).*bwell","Google Search; Marketplace; SEO","Phrase","Protect - always on","P1","Category landing page ต้อง match กับ category ใน query"),
 ("Brand","Bwell model numbers","BOFU","CF-8608; CF-8005; CF-8428; CF-8400; AP-M1536S; AP-H2219S; AP-H3029US; AP-P4019US; AP-8119US; PM1330; BDH-12A; BDH-26; BDH-30A; BDH-53A; BPAC-09B; BPAC-12B; BW-D10RO5; BW-D10UV5; BW-D10UF5; T12 Allergy Pro; Flomo Lite; G8; G9","cf-?8\\d{3}|ap-?[mhp]\\d{4}|ap-?8119|bdh|bpac|bw-?d\\d|pm1330|t12|flomo","Google Search; Shopping; Marketplace","Exact (ทั้งแบบมีขีด/ไม่มีขีด)","Add - low CPC, high intent","P1","cf8608 มี 44 sessions จาก generic match ยังไม่มี exact keyword ของตัวเอง ใน site search ก็พิมพ์ชื่อรุ่นบ่อย (G8, AP-P4019US, BDR-02)"),
 ("Brand","Filter / spare part replenishment","BOFU","แผ่นกรองอากาศ bwell; ไส้กรอง bwell; filter CF-8005; แผ่นฟอกอากาศ AP-M1536S; ไส้กรองน้ำ RO-500; อะไหล่หุ่นยนต์ดูดฝุ่น bwell","ไส้กรอง|แผ่นกรอง|แผ่นฟอก|filter|อะไหล่","Google Search; Shopping; Marketplace; CRM/LINE","Exact + Phrase (+ ชื่อรุ่น)","Add - repeat purchase","P1","ใน site search มีคำค้นหาแผ่นกรองหลายคำ (ไส้กรอง 6 ครั้ง) เป็น recurring revenue ควรทำ retention ผ่าน LINE OA ควบคู่"),
 # Air purifier
 ("Air - Air purifier","Generic category","TOFU","เครื่องฟอกอากาศ; เครื่องกรองอากาศ; air purifier; เครื่องฟอกอากาศพกพา","^เครื่องฟอกอากาศ$|^เครื่องกรองอากาศ$|^airpurifier$|ฟอกอากาศพกพา|ฟอกอากาศแบบพกพา","Google Search; Shopping; Marketplace; SEO","Phrase (ไม่ใช้ Broad)","Keep - tighten match, bid by season (PM2.5 Dec-Mar)","P2","Generic intent ทั้งหมวดได้ 1,056 sessions แต่ 0 txn คนค้นกว้างจะเทียบราคา ให้ Shopping/Marketplace รับแทน"),
 ("Air - Air purifier","Health need-state (positioning fit)","MOFU","เครื่องฟอกอากาศ pm2.5; เครื่องฟอกอากาศ ภูมิแพ้; เครื่องฟอกอากาศ ฆ่าเชื้อโรค; เครื่องฟอกอากาศ ห้องนอน; เครื่องฟอกอากาศ เด็ก; เครื่องฟอกอากาศ ขนสัตว์","ฟอกอากาศ.*(pm2|ภูมิแพ้|เชื้อ|ไวรัส|ห้องนอน|เด็ก|ทารก|สัตว์|แมว|หมา)|กรองอากาศ.*(pm2|ภูมิแพ้)","Google Search; SEO; Marketplace","Phrase","Scale - core positioning","P1","Fit กับ Home Environment Wellness มากที่สุด ไม่แข่งราคา ตอนนี้ยังได้ traffic น้อยเพราะยังไม่ได้ทำ ad group แยก"),
 ("Air - Air purifier","Car / portable","MOFU","เครื่องฟอกอากาศในรถ; เครื่องฟอกอากาศในรถยนต์; เครื่องฟอกอากาศพกพา","ฟอกอากาศ.*(ในรถ|รถยนต์)","Google Search; Shopping; Marketplace","Phrase","Keep - map ไป G8/G9","P2","G8 มี Shopping CTR 1.3% สูงกว่าค่าเฉลี่ยบัญชี (0.47%)"),
 ("Air - Air purifier","Room size spec","MOFU","เครื่องฟอกอากาศ 40 ตรม; เครื่องฟอกอากาศ 60 ตรม; เครื่องฟอกอากาศ ห้องใหญ่","ฟอกอากาศ.*(ตรม|ตารางเมตร|ห้องใหญ่)","Google Search; Marketplace","Phrase","Test","P3","ใน Ads data ยังมีน้อย แต่ตรงกับวิธีตั้งชื่อ listing ของ Bwell บน marketplace"),
 ("Air - Air purifier","Comparison","MOFU","เครื่องฟอกอากาศ ยี่ห้อไหนดี; เครื่องฟอกอากาศ pantip; รีวิว เครื่องฟอกอากาศ","ฟอกอากาศ.*(ยี่ห้อไหน|รีวิว|pantip|แนะนํา|แนะนำ|ดีไหม)|กรองอากาศ.*ยี่ห้อไหน","SEO; Google Search (low bid)","Phrase","Move to SEO (comparison article) + bid ต่ำ","P2","0 txn ต้องมี content เทียบ spec/CADR/HEPA ซึ่งเป็นจุดที่ Bwell ได้เปรียบโดยไม่ต้องลงไปแข่งราคา"),
 ("Air - Air purifier","Informational","TOFU","เครื่องฟอกอากาศ ช่วยอะไร; ประโยชน์ของเครื่องฟอกอากาศ; วิธีใช้เครื่องฟอกอากาศ","ฟอกอากาศ.*(ช่วยอะไร|ดียังไง|ประโยชน์|วิธี|ทํางาน)|ประโยชน์.*ฟอกอากาศ|วิธี.*ฟอกอากาศ","SEO only","-","Negate in paid; cover with blog","P3","ใช้ทำ blog/FAQ บน website ใหม่ได้"),
 # Dehumidifier
 ("Air - Dehumidifier","Generic category","TOFU","เครื่องดูดความชื้น; เครื่องลดความชื้น; เครื่องกำจัดความชื้น; เครื่องไล่ความชื้น","^เครื่อง(ดูด|ลด|กําจัด|กำจัด|ไล่)ความชื้น$","Google Search; Shopping; Marketplace; SEO","Phrase","Keep - bid up ช่วงฤดูฝน (May-Oct)","P1","ใน Shopping หมวด dehumidifier Bwell ติด Top 5 (HomePro อยู่อันดับ 1) แข่งได้กว่าหมวด air purifier"),
 ("Air - Dehumidifier","Use-case (laundry / bedroom / allergy)","MOFU","เครื่องดูดความชื้น ตากผ้า; เครื่องดูดความชื้น ห้องนอน; เครื่องลดความชื้น ภูมิแพ้; เครื่องดูดความชื้น ในบ้าน","ความชื้น.*(ตากผ้า|ห้องนอน|ภูมิแพ้|ในบ้าน|เชื้อรา|คอนโด)","Google Search; SEO; Marketplace","Phrase","Scale","P1","คำว่า 'ตากผ้า' มี 20 sessions เป็น use-case ของคนเมือง/คอนโดที่เชื่อมกับ health message ได้"),
 ("Air - Dehumidifier","Capacity spec","MOFU","เครื่องลดความชื้น 12 ลิตร; เครื่องลดความชื้น 30 ลิตร; เครื่องลดความชื้น 53 ลิตร","ความชื้น.*(ลิตร|\\d+l)","Marketplace; Google Search","Phrase","Test","P3","ตรงกับ product line BDH-12A / 26 / 30A / 53A"),
 ("Air - Dehumidifier","Comparison","MOFU","เครื่องดูดความชื้น ยี่ห้อไหนดี; รีวิว เครื่องดูดความชื้น","ความชื้น.*(ยี่ห้อไหน|รีวิว|ดีไหม)|รีวิว.*ความชื้น","SEO; Google Search (low bid)","Phrase","Move to SEO + low bid","P2","ทำ content เดียวกับ air purifier comparison"),
 ("Air - Dehumidifier","Informational","TOFU","เครื่องลดความชื้น ช่วยอะไร; เครื่องดูดความชื้น ช่วยอะไร","ความชื้น.*(ช่วยอะไร|ดียังไง|ทํางาน)","SEO only","-","Negate in paid; write article","P2","Informational ที่ traffic สูงสุดในบัญชี ควรทำ blog เรื่องนี้เป็นเรื่องแรก"),
 # Portable AC
 ("Air - Portable AC","Generic category","TOFU","แอร์เคลื่อนที่; เครื่องปรับอากาศเคลื่อนที่; แอร์พกพา; portable air conditioner","^แอร์เคลื่อนที่$|^เครื่องปรับอากาศเคลื่อนที่$|^แอร์พกพา$|^portableairconditioner$","Google Search; Shopping; Marketplace","Phrase","Keep - seasonal (Mar-May)","P2","Negate 'พัดลมแอร์' / 'แอร์มุ้ง' / 'ตู้แอร์' (คนละ product)"),
 ("Air - Portable AC","BTU spec","MOFU","แอร์เคลื่อนที่ 12000 btu; แอร์เคลื่อนที่ 9000 btu; แอร์เคลื่อนที่ ประหยัดไฟ","แอร์.*(btu|ประหยัดไฟ)","Google Search; Shopping; Marketplace","Phrase","Scale - map ไป BPAC-09B / BPAC-12B","P1","12000btu มี 55 sessions spec ตรงกับ SKU"),
 ("Air - Portable AC","Purchase intent","BOFU","แอร์เคลื่อนที่ ราคา; ร้านขายแอร์เคลื่อนที่","แอร์เคลื่อนที่.*(ราคา|ร้าน)|ราคาแอร์เคลื่อนที่|ร้านขายแอร์","Google Search; Shopping","Phrase","Keep - ไม่ต้องเน้นราคาใน ad copy","P2","คนกลุ่มนี้ใกล้ซื้อ ให้ ad copy เน้น value (รับประกัน/service) ไม่ต้องลงไปแข่งราคา"),
 # Vacuum
 ("Clean Home - Vacuum/Robot","Robot vacuum generic","TOFU","หุ่นยนต์ดูดฝุ่น; โรบอทดูดฝุ่น; robot vacuum; หุ่นยนต์ดูดฝุ่นถูพื้น","หุ่นยนต์ดูดฝุ่น|โรบอทดูดฝุ่น|robotvacuum","Shopping; Marketplace","Phrase","Reduce on Search - shift to Shopping/Marketplace","P3","มี query ชื่อคู่แข่ง (Xiaomi, Roborock, Dreame) หนาแน่น CPC น่าจะสูง Bwell แข่งที่ราคาไม่ได้"),
 ("Clean Home - Vacuum/Robot","Allergy / dust mite (positioning fit)","MOFU","เครื่องดูดไรฝุ่น; เครื่องดูดไรฝุ่นที่นอน; เครื่องดูดฝุ่น ภูมิแพ้; เครื่องดูดฝุ่น allergy","ไรฝุ่น|ดูดฝุ่น.*(ภูมิแพ้|allergy|ที่นอน)","Google Search; SEO; Marketplace","Phrase","Scale - map ไป T12 Allergy Plus/Pro","P1","ชื่อรุ่น 'Allergy' ตรงกับ positioning health พอดี"),
 ("Clean Home - Vacuum/Robot","Cordless vacuum","MOFU","เครื่องดูดฝุ่นไร้สาย; เครื่องดูดฝุ่นไร้สาย ขนาดเล็ก","ดูดฝุ่นไร้สาย","Google Search; Shopping; Marketplace","Phrase","Keep","P2","Dyson ครองตลาดนี้ ให้ขาย angle allergy แทน"),
 # Water purifier
 ("Water - Purifier","Generic category","TOFU","เครื่องกรองน้ำ; เครื่องกรองน้ำดื่ม; เครื่องกรองน้ำ ในบ้าน","^เครื่องกรองน้ํา$|^เครื่องกรองน้ำ$|กรองน้ำดื่ม|กรองน้ําดื่ม|กรองน้ำ.*ในบ้าน","Google Search; Shopping; Marketplace; SEO","Phrase","Keep - tighten match","P2","Generic intent ทั้งหมวด 909 sessions, 0 txn"),
 ("Water - Purifier","Technology (RO / UV / UF)","MOFU","เครื่องกรองน้ำ RO; เครื่องกรองน้ำ ระบบ RO; เครื่องกรองน้ำ UV; เครื่องกรองน้ำ UF; เครื่องกรองน้ำ RO แบบไร้ถัง","กรองน้.*(ro|uv|uf)","Google Search; Shopping; Marketplace","Phrase","Scale - map ไป BW-D10RO5/UV5/UF5","P1","RO มี 160+ sessions เป็น spec-led ซึ่งตรงกับ positioning safety"),
 ("Water - Purifier","Point-of-entry (whole house)","MOFU","เครื่องกรองน้ำใช้; เครื่องกรองน้ำประปา; เครื่องกรองน้ำใช้ก่อนเข้าบ้าน; เครื่องกรองน้ำบาดาล","กรองน้.*(ใช้|ประปา|บาดาล|ก่อนเข้าบ้าน)","Google Search; Marketplace","Phrase","Keep","P2","Map ไป BW-BB20PP / BB20CTO"),
 ("Water - Purifier","Comparison","MOFU","เครื่องกรองน้ำ RO ยี่ห้อไหนดี; เครื่องกรองน้ำ ยี่ห้อไหนดี","กรองน้.*(ยี่ห้อไหน|รีวิว|pantip|ดีไหม)","SEO; Google Search (low bid)","Phrase","Move to SEO","P2","ทำ content เทียบ RO/UV/UF"),
 # Water heater
 ("Water - Heater (นอก brief)","Generic + purchase","BOFU","เครื่องทำน้ำอุ่น; ราคาเครื่องทำน้ำอุ่น; เครื่องทำน้ำอุ่น พร้อมติดตั้ง","น้ําอุ่น|น้ำอุ่น","Google Search; Shopping; Marketplace","Phrase","Review - ยืนยันว่ายังเป็น focus หรือไม่","P3","0 txn; ELKA 3,500W ได้ 10.4K Shopping impressions แต่ CTR 0.15% และ category นี้ไม่อยู่ใน pillar Air/Water/Clean"),
 # Hair
 ("Hair styling","Generic hair tools","TOFU","ไดร์เป่าผม; ที่หนีบผม; เครื่องม้วนผม; หวีไดร์","^ไดร์เป่าผม$|^ที่หนีบผม$|^เครื่องหนีบผม$|^เครื่องม้วนผม$|^หวีไดร์","Marketplace; Shopping","Phrase","Reduce on Search","P3","Generic intent ทั้งหมวด 891 sessions, 0 txn ตลาดถูกครองโดย Dyson/Panasonic และแบรนด์ราคา"),
 ("Hair styling","BLDC / quiet / tech spec","MOFU","ไดร์เป่าผม BLDC; ไดร์เป่าผม เสียงเงียบ; ไดร์เป่าผม ไอออน; ไดร์จัดแต่งทรง 7 หัว","bldc|เสียงเงียบ|ไอออน|ion|7หัว","Google Search; Marketplace","Phrase","Test - differentiator","P2","'เสียงเงียบ' 24+ sessions ใน site search มีคน search 'ไดร์เป่าผม BLDC' 8 ครั้ง"),
 # Ergonomic
 ("Ergonomic","Health chair generic","TOFU","เก้าอี้เพื่อสุขภาพ; เก้าอี้สุขภาพ; เก้าอี้ทำงานเพื่อสุขภาพ; ergonomic chair","เก้าอี้(สุขภาพ|เพื่อสุขภาพ|ทํางาน|ทำงาน|ergonomic)|ergonomicchair","Google Search; Marketplace","Phrase + negative 'bewell'","Restructure - Bewell เป็นเจ้าตลาดคำนี้","P2","Keyword 'ergonomic chair' 41% ของ traffic เป็น query 'bewell' และ 'เก้าอี้ เพื่อ สุขภาพ' มี txn 1"),
 ("Ergonomic","Pain / office syndrome","MOFU","เก้าอี้แก้ปวดหลัง; เก้าอี้ออฟฟิศซินโดรม; เบาะรองนั่งเพื่อสุขภาพ; เบาะรองหลัง; หมอนรองคอรถยนต์","ปวดหลัง|ออฟฟิศซินโดรม|เบาะรอง|หมอนรองคอ","Google Search; Shopping; Marketplace; SEO","Phrase","Scale - accessory ราคาเข้าถึงง่าย","P1","ใน Shopping เบาะรองนั่ง/หมอนรองคอได้ CTR 0.5-0.8% (ดีกว่าค่าเฉลี่ย) ใช้เป็น entry product ได้"),
]
rows=[]
for c in CL:
    cat,cl,fun,kws,rx,ch,mt,act,pr,note=c
    s,t,n=ev("^(?!.*bewell)(?=.*(%s))"%rx, None if cat=="Brand" else cat.split(" (")[0])
    rows.append(dict(category=cat,cluster=cl,funnel=fun,keywords=kws,channels=ch,match=mt,action=act,priority=pr,
      sessions=s,txn=t,queries=n,note=note))
json.dump(rows, open("map.json","w"), ensure_ascii=False, indent=1)
for r in rows: print(r["priority"], r["category"][:22].ljust(22), r["cluster"][:34].ljust(34), r["sessions"], r["txn"], r["queries"])
# Negatives
NEGS=[
 ("Brand confusion","bewell; be well; บีเวล; บีเวลล์","Phrase","Account-level negative list (ทุก campaign รวม PMax)","คนตั้งใจหา Bewell (แบรนด์ ergonomic คนละบริษัท) txn 0","bewell|บีเวล"),
 ("Bewell product names","frozen; glory; enlight; enfold; foster; topper; ที่นอน; ผ้าห่มเย็น; หมอนหนุน; โต๊ะปรับระดับ; เตียงไฟฟ้า","Phrase","Ergonomic + Brand campaigns","ชื่อสินค้า/รุ่นของ Bewell ที่เจอใน site search และ Ads query","frozen|glory|enlight|enfold|foster|topper|ที่นอน|ผ้าห่ม|หมอนหนุน|โต๊ะปรับระดับ|เตียง"),
 ("Bargain / used","มือสอง; เช่า; ราคาถูก; ราคาไม่เกิน; รับซื้อ","Phrase","Account-level","ไม่ตรง positioning premium health","มือสอง|เช่า|ราคาถูก|ไม่เกิน|รับซื้อ"),
 ("Informational / DIY","ช่วยอะไร; ดียังไง; วิธี; ทำงานยังไง; ซ่อม; ล้าง; ติดตั้งเอง; คู่มือ","Phrase","Generic campaigns (ย้ายไปทำ SEO)","Research intent, 0 txn","ช่วยอะไร|ดียังไง|วิธี|ทํางานยังไง|ทำงานยังไง|ซ่อม|ล้าง"),
 ("Wrong product","พัดลมแอร์; แอร์มุ้ง; ตู้แอร์; พัดลมไอเย็น","Phrase","Portable AC ad group","คนละ product","พัดลมแอร์|แอร์มุ้ง|ไอเย็น"),
 ("Competitor brands (decision required)","xiaomi; dyson; philips; sharp; coway; panasonic; roborock; dreame; samsung; electrolux; mazuma; stiebel; safe; amway","Phrase","Generic campaigns (ถ้าไม่ทำ conquest)","คนตั้งใจหาแบรนด์คู่แข่ง txn 0 ถ้าจะทำ conquest ให้แยก campaign ตั้ง budget cap","xiaomi|dyson|philips|sharp|coway|panasonic|roborock|dreame|samsung|electrolux|mazuma|stiebel|safe|amway|แอมเวย์"),
 ("Retailers","homepro; โฮมโปร; powerbuy; central; makro; lotus; big c","Phrase","Generic campaigns","เป็น retail partner ไม่ควรประมูลแข่งกับ partner","homepro|โฮมโปร|powerbuy|central|makro|lotus|bigc|บิ๊กซี"),
 ("Out of category (site search)","ไม้เท้า; ถุงเท้า; sofa; โต๊ะ","Phrase","PMax / Shopping brand exclusions","Traffic ไม่ตรง product line","ไม้เท้า|ถุงเท้า|sofa|โต๊ะ"),
]
negrows=[]
for g,k,m,lvl,why,rx in NEGS:
    s,t,n=ev(rx); negrows.append(dict(group=g,keywords=k,match=m,level=lvl,reason=why,sessions=s,txn=t,queries=n))
json.dump(negrows, open("negatives.json","w"), ensure_ascii=False, indent=1)
print(); [print(r["group"], r["sessions"], r["txn"]) for r in negrows]
# intent summary
ia=collections.defaultdict(lambda:[0,0,0])
for r in C: a=ia[r["intent"]]; a[0]+=r["s"]; a[1]+=r["t"]; a[2]+=1
json.dump({k:v for k,v in ia.items()}, open("intent.json","w"), ensure_ascii=False)
