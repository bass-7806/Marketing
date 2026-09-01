# bwell.co.th — website rebuild

Static rebuild of the Bwell website. Structure follows the approved site map,
page layouts follow the approved homepage and product-category wireframes, and the
visual language references **apple.com** — sticky translucent nav, large display
type, generous whitespace, full-bleed sections and restrained motion — rendered in
Bwell's own palette and typography per the Bwell Brand Guidelines 2026.

## Quick start

```bash
npm start      # build + preview at http://localhost:3000
npm run build  # build only, output in dist/
```

No dependencies and no build tooling — `build.js` is plain Node (>=18).
`dist/` is generated and git-ignored; Netlify builds it from source
(`netlify.toml`).

## What gets built

32 pages plus a 404, matching the approved site structure:

| Group | Pages |
|---|---|
| Home | `/` |
| About | `/about-us/`, `/why-bwell/`, `/our-client/` |
| Product hub | `/product-bwell/` |
| Categories (12) | `/air-purifier-bwell/`, `/hair-styling-tools/`, `/bwell-ergonomic-chair/`, `/ergonomic-cushion-bwell/`, `/water-heater-bwell/`, `/water-purifier/`, `/air-dehumidifier/`, `/portable-air-conditioner/`, `/vacuum-cleaner/`, `/robot-vacuum/`, `/sport-gadgets/`, `/air-purification-filters/` |
| Sub-categories (7) | `/pm25-air-purifier/`, `/air-purifier/`, `/portable-air-purifiers/`, `/hair-straightener/`, `/hair-curler/`, `/electric-hair-brush/`, `/hair-dryer/` |
| Other | `/distribution-channels/`, `/findbwell/`, `/blog/`, `/contact/` |
| Policies | `/privacy-policy/`, `/cookies-policy/`, `/shipping-policy/`, `/warranty-policy/` |

Every URL matches the current bwell.co.th path, so existing inbound links and
search rankings carry over without redirects.

Also generated: `sitemap.xml`, `robots.txt`, a favicon and one SVG placeholder per
image slot.

## Layout

```
build.js                  # generator — renders every page into dist/
serve.js                  # local preview server
src/
  data/
    site.js               # brand, nav, contact, partners, reviews, footer
    categories.js         # all 12 category pages + 7 sub-category pages
    policies.js           # policy page copy
  templates/
    layout.js             # document shell, header, footer, JSON-LD
    components.js         # media slots, lists, product grid, CTA bands
    home.js               # homepage (per wireframe)
    category.js           # product category page (per wireframe)
    pages.js              # hub, about, contact, blog, policy pages
  assets/css/bwell.css    # design system
  assets/js/bwell.js      # mobile menu, read-more, scroll reveal
```

To change copy, edit `src/data/*`. To change layout, edit `src/templates/*`.

## Design system

Tokens live at the top of `src/assets/css/bwell.css`.

| Token | Value | Use |
|---|---|---|
| `--blue` | `#008ad0` | Logo mark, gradients, decorative accents |
| `--blue-text` | `#005d9d` | Links, buttons, any text-bearing fill |
| `--navy` | `#005d9d` | Headings, depth |
| `--ink` / `--ink-2` | `#1d1d1f` / `#6e6e73` | Body copy |
| `--surface-2` | `#f5f5f7` | Alternating section ground |

Brand blue `#008ad0` measures 3.8:1 on white, below the WCAG AA 4.5:1 threshold
for normal-size text. Text and button fills therefore use navy `#005d9d`
(6.9:1) — also an official brand colour — while blue keeps its role in the logo,
gradients and non-text accents. Every text/background pair in the built pages was
measured; none fall below its AA threshold.

Type is **Kanit** for Thai body copy and **Poppins** for display headings, both
loaded from Google Fonts per the brand guidelines.

## Images

Real Bwell photography from the live site now fills the main slots — the
homepage hero, all five blog covers, seven of the twelve category tiles and
every featured product. They live in `src/assets/img/` (~500KB total, resized
and re-encoded to WebP).

| Slot | File |
|---|---|
| Homepage hero | `hero-lineup.webp` (the product-lineup banner) |
| Blog covers ×5 | `blog-*.webp` |
| Category tiles ×7 | `cat-*.webp` |
| Featured products ×4 | `prod-*.webp` |

The hero uses Apple's stacked product-family treatment — copy on a pale ground
with the lineup shot beneath — rather than a full-bleed photo with overlaid
text, because the Bwell banner is a wide shot on a bright background where
white text would be unreadable.

Every remaining slot is a generated SVG placeholder at a real `<img>` path. To
fill one, drop a file into `src/assets/img/` and set `img:` on the matching
entry in `src/data/`. Still needing photography:

- **Category tiles (5):** hair styling, water heater, robot vacuum, fitness, filters
- **All category-page SEO blocks:** each needs a lifestyle shot (4 per category)

## Before launch

These need real assets or a sign-off — none of them block the build:

- **Remaining photography.** 104 slots are still placeholders — see Images above.
- **Product names, model codes and prices.** The four featured products and the
  five blog posts now carry real names, prices and images taken from the live
  bwell.co.th homepage. **The per-category product grids are still placeholder
  entries** invented to fill the layout, and must be replaced with the real
  catalogue before publishing.
- **Blog posts.** `/blog/` lists real titles but every card links to the blog index;
  article pages are not built yet.
- **Product brochure.** The homepage CTA currently points at `/contact/`. When the
  catalogue PDF exists, put it at `src/assets/brochure/bwell-catalogue.pdf` and
  restore the download link (marked with a `TODO` in `src/templates/home.js`).
- **Policy copy.** `src/data/policies.js` is a plain-language restatement of standard
  Thai e-commerce terms, written to be reviewed — it is not legal advice and needs
  Bwell's approval.
- **Cart and checkout.** "หยิบใส่ตะกร้า" links to `shop.bwell.co.th`; this build has
  no cart of its own.
