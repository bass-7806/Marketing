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
| Product detail (4) | `/robot-vacuum/t20/`, `/robot-vacuum/l6c/`, `/robot-vacuum/l0/`, `/robot-vacuum/y1/` — data in `src/data/products.js`, template `src/templates/product.js` |
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

All imagery is Bwell's own, pulled from the live site: the homepage hero, every
blog cover, all twelve category tiles, and a real photo for every product in
every grid. 69 files, ~1.5MB, resized to at most 800px wide (1400px for the
hero) and re-encoded to WebP. They live in `src/assets/img/`.

| Slot | Files |
|---|---|
| Homepage hero | `hero-lineup.webp` |
| Blog covers | `blog-*.webp` (5) |
| Category tiles | `cat-*.webp` and lead product shots (12) |
| Product grids | `p-*.webp` (51) |
| Product galleries | `g-*.webp` (18) — L6C/Y1/L0 gallery graphics from the live site, T20 cutouts and marketing graphics from the Drive folder "Photo T20" |

The hero uses Apple's stacked product-family treatment — copy on a pale ground
with the lineup shot beneath — rather than a full-bleed photo with overlaid
text, because the Bwell banner is a wide shot on a bright background where
white text would be unreadable.

Three lifestyle photographs from Google Drive (`life-*.webp`) fill the SEO
feature blocks on the robot vacuum page.

**Mockup artwork (48 slots):** the SEO feature blocks on the other eleven
category pages are filled by `src/mockup.js`, which draws an illustrated
interior scene per category — a room, a product silhouette and a motif, in
brand colours. They are deliberately illustrative rather than photographic and
each carries a MOCKUP tag, so the pages present as finished design in review
without passing artwork off as real photography.

To replace one with a photograph, drop a file into `src/assets/img/` and add
`imageSrc: 'filename.webp'` next to that block's `image:` label in
`src/data/categories.js`. `src/mockup.js` maps each category slug to a scene;
a new category falls back to the air-purifier scene until it is added there.

A search of the Drive turned up little else usable for these: the asset library
is mostly white-background product cut-outs, marketplace graphics with burnt-in
Thai text, and other brands' material (BRITA, BaByliss) that should not appear
on Bwell category pages. Filling the remaining blocks needs a photo shoot.

## Before launch

These need real assets or a sign-off — none of them block the build:

- **Lifestyle photography.** 48 slots use generated mockup artwork — see Images
  above. The Drive holds nothing suitable for them, so real photography for these
  blocks still needs a shoot; the mockups make the pages presentable meanwhile.
- **Catalogue accuracy.** Every product name, price and photo now comes from the
  live bwell.co.th category pages, captured on 2026-09-01. Prices move, so
  re-check them against the shop before publishing. Each category grid shows the
  first few products the live page lists, not a curated selection.
- **T20 has no price yet.** The content document lists the Ultra T20 OmniBase price
  as "-", so its page and card show "สอบถามราคา" and the JSON-LD carries no offer.
  Set `price` in `src/data/products.js` once it is announced. Note the document
  states a 1-year warranty for T20 versus 2 years for Y1/L0/L6C.
- **Product detail pages** follow the live L6C page order (title, price, gallery,
  ระบบการทำงานที่แตกต่าง, รายละเอียดสินค้า, related models, contact CTA) plus a
  key-numbers band and the comparison table from the content document. Only the
  robot-vacuum category has detail pages so far; other categories still link
  cards to `shop.bwell.co.th`.
- **`/pm25-air-purifier/` does not exist on the live site** — it returns 404,
  even though the approved site structure lists it. This build generates the
  page and it currently falls back to the parent category's products. Either
  give it its own products or drop it from `src/data/categories.js`.
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
