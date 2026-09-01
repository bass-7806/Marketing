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

The hero uses Apple's stacked product-family treatment — copy on a pale ground
with the lineup shot beneath — rather than a full-bleed photo with overlaid
text, because the Bwell banner is a wide shot on a bright background where
white text would be unreadable.

**Still placeholders (51 slots):** the four SEO feature blocks on each category
page, which need lifestyle photography the current site does not have. Each is
a real `<img>` at a stable path — drop a file into `src/assets/img/` and set the
matching `image:` value in `src/data/categories.js` to fill one.

## Before launch

These need real assets or a sign-off — none of them block the build:

- **Lifestyle photography.** 51 slots are still placeholders — see Images above.
- **Catalogue accuracy.** Every product name, price and photo now comes from the
  live bwell.co.th category pages, captured on 2026-09-01. Prices move, so
  re-check them against the shop before publishing. Each category grid shows the
  first few products the live page lists, not a curated selection.
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
