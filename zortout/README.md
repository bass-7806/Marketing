# ZORT (ZORTOUT) API — วิธีสร้าง API Key และทดสอบการเชื่อมต่อ

## 1. สร้าง API Key ในระบบ ZORT

คีย์ต้องสร้างจากหน้าเว็บ ZORT ด้วยบัญชีของร้านเอง (สร้างผ่าน API ไม่ได้)

1. เข้าสู่ระบบที่ https://zortout.com ด้วยบัญชีที่มีสิทธิ์ระดับผู้ดูแล
2. ไปที่เมนู **ตั้งค่า (Settings)**
3. เลือก **เชื่อมต่อบริการอื่นๆ (Integration)**
4. เลือก **API Reference**
5. กด **เปิดใช้งาน API**
6. คัดลอกค่า 3 ตัวนี้เก็บไว้:
   - `storename` — ชื่อร้านในระบบ ZORT
   - `apikey`
   - `apisecret`

> หมายเหตุ: `apisecret` มีค่าเทียบเท่ารหัสผ่าน — เก็บไว้ใน `.env` หรือ secret manager เท่านั้น
> ห้ามใส่ในโค้ด ในไฟล์ที่ commit หรือส่งผ่านแชท/อีเมล
> ถ้าคีย์หลุด ให้กลับไปที่หน้าเดิมเพื่อ generate ใหม่ (คีย์เดิมจะใช้ไม่ได้ทันที)

## 2. ตั้งค่าในโปรเจกต์นี้

```bash
cp zortout/.env.example zortout/.env
# แก้ไข zortout/.env ใส่ค่าที่คัดลอกมาจากขั้นตอนที่ 1
```

`.env` ถูก ignore ไว้ใน `.gitignore` แล้ว จะไม่ถูก commit

## 3. ทดสอบว่าคีย์ใช้งานได้

```bash
bash zortout/test-connection.sh
```

ได้ `HTTP 200` = คีย์ใช้งานได้
ได้ `401` / `403` = คีย์ผิด หรือยังไม่ได้กดเปิดใช้งาน API ในขั้นตอนที่ 5

## 4. ข้อมูลอ้างอิงสำหรับเรียก API

- Base URL: `https://open-api.zortout.com/v4`
- Header ที่ต้องส่งทุก request: `storename`, `apikey`, `apisecret`
- Header เสริม: `X-Request-ID` (ไว้ track / debug)
- เอกสาร API: https://developers.zortout.com

ตัวอย่าง:

```bash
curl -X GET "https://open-api.zortout.com/v4/Product/GetProducts?page=1&limit=50" \
  -H "storename: $ZORTOUT_STORENAME" \
  -H "apikey: $ZORTOUT_APIKEY" \
  -H "apisecret: $ZORTOUT_APISECRET"
```

Endpoint ที่ใช้บ่อยสำหรับงาน Marketing:

| งาน | Endpoint |
|---|---|
| ดึงรายการสินค้า | `GET /v4/Product/GetProducts` |
| ดึงรายละเอียดสินค้า | `GET /v4/Product/GetProductDetail?id={id}` |
| ดึงหมวดหมู่สินค้า | `GET /v4/Product/GetCategorys` |
| ดึงรายการออเดอร์ | `GET /v4/Order/GetOrders` |
| ดึงรายชื่อลูกค้า | `GET /v4/Contact/GetContacts` |
