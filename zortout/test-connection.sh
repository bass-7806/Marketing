#!/usr/bin/env bash
# ทดสอบว่า ZORT API key ใช้งานได้จริง
# วิธีใช้:  cp zortout/.env.example zortout/.env  →  ใส่ค่า  →  bash zortout/test-connection.sh
set -euo pipefail

ENV_FILE="$(dirname "$0")/.env"
if [ -f "$ENV_FILE" ]; then
  set -a; . "$ENV_FILE"; set +a
fi

: "${ZORTOUT_STORENAME:?ยังไม่ได้ตั้งค่า ZORTOUT_STORENAME (ดู zortout/.env.example)}"
: "${ZORTOUT_APIKEY:?ยังไม่ได้ตั้งค่า ZORTOUT_APIKEY}"
: "${ZORTOUT_APISECRET:?ยังไม่ได้ตั้งค่า ZORTOUT_APISECRET}"

BASE_URL="https://open-api.zortout.com/v4"

echo "กำลังเรียก ${BASE_URL}/Product/GetProducts (store: ${ZORTOUT_STORENAME}) ..."
HTTP_CODE=$(curl -sS -o /tmp/zort-test-response.json -w '%{http_code}' \
  -X GET "${BASE_URL}/Product/GetProducts?page=1&limit=1" \
  -H "storename: ${ZORTOUT_STORENAME}" \
  -H "apikey: ${ZORTOUT_APIKEY}" \
  -H "apisecret: ${ZORTOUT_APISECRET}" \
  -H "X-Request-ID: marketing-conn-test-$(date +%s)")

echo "HTTP ${HTTP_CODE}"
head -c 800 /tmp/zort-test-response.json; echo

case "$HTTP_CODE" in
  200) echo "✅ คีย์ใช้งานได้" ;;
  401|403) echo "❌ คีย์ไม่ถูกต้อง หรือยังไม่ได้กดเปิดใช้งาน API ในเมนู ตั้งค่า > เชื่อมต่อบริการอื่นๆ > API Reference"; exit 1 ;;
  *) echo "⚠️  ได้ HTTP ${HTTP_CODE} — ดู response ด้านบน"; exit 1 ;;
esac
