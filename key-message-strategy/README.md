# Bwell Key Message Strategy v1.0 (2 Nov 2026)

Single source for Bwell key messages: brand house, 13 categories, 10 channels, 68 main-unit SKUs.

| File | Purpose |
|---|---|
| `build_data.py` | Source of truth for all messaging data. Edit here, then rebuild. |
| `data.json` | Generated data used by the HTML playbook |
| `sku_matrix.csv`, `category_message_house.csv`, `channel_rules.csv` | Generated tables (mirrored in the Google Sheet "Bwell Key Message Matrix v1.0") |
| `playbook_template.html` → `bwell-key-message-playbook.html` | Interactive playbook (published as Claude artifact) |

Rebuild:

```bash
python3 key-message-strategy/build_data.py && python3 key-message-strategy/build_html.py
```

Sources: Bwell Product Master (Consolidated Review 2026-09-29), Executive summary 111 SKU (3 Oct 2026), Brand Guidelines 2026, CI 10-10 Production Standard, bwell.co.th.
Prices are website snapshots (26 Sep 2026); stock is WICE 8 Sep 2026. Spec numbers stay behind Product_Facts claim gates.
