# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Marketing repository for **Bwell**, a Thai health-and-wellness appliance brand (air purifiers, water purifiers, robot vacuums, ergonomic chairs, hair styling tools, etc.). It currently contains the Bwell brand website as a static site.

## Structure

- `website/` — static Bwell site, 28 self-contained HTML pages (no build system; CSS/JS inlined per page). Recovered from the team's deployed prototype (`bwell-web-prototype-sep2026` → Netlify Drop capture), with capture artifacts stripped.
  - `index.html` — homepage: announcement ribbon, slim global nav with per-category mega-menu flyouts, full-bleed hero, product tiles with footnoted spec claims (`#fn1`), trust section, store links, footer directory
  - Category/product pages: `air-purifier.html`, `air-dehumidifier.html`, `portable-air-conditioner.html`, `air-purification-filters.html`, `air-purifier-{pm25,virus,car}.html`, `water-purifier.html`, `water-heater.html`, `robot-vacuum.html`, `vacuum-cleaner.html`, `ergonomic-chair.html`, `ergonomic-cushion.html`, `sport-gadgets.html`, `hair-{styling-tools,dryer,dryer-brush,straightener,curler}.html`
  - Support pages: `warranty.html`, `warranty-policy.html`, `user-manual.html`, `faq.html`, `shipping-policy.html`, `find-store.html`, `contact.html`, `support.html`
  - `assets/logos/` — official Bwell logo files from brand guidelines
  - Internal links are relative (`*.html`), so the folder deploys as-is to any static host
  - Product images hotlink to the live bwell.co.th CDN (`bwellcoth29b89.zapwp.com`); one hero image hotlinks to `bwell-redesign-preview.netlify.app` — self-host these before production
  - Pages carry `noindex,nofollow` — remove when the site goes to production

## Development

There is no build step, package manifest, or test suite. To preview locally:

```bash
python3 -m http.server 8000 --directory website
# then open http://localhost:8000
```

Or open `website/index.html` directly in a browser.

## Brand Conventions (must follow)

Defined by the `bwell-brand-guidelines-2026` skill — load it before making any brand-visible change. Key rules baked into the site:

- **Colors:** Primary Blue `#008ad0`, Navy `#005D9D`, Gray `#a8aaad`, White. Gradient: `linear-gradient(135deg, #008ad0 0%, #005D9D 100%)`. These are set as CSS variables in `style.css` — never hardcode other brand colors.
- **Fonts:** Kanit (Thai body), Poppins (display/EN), loaded from Google Fonts. The official wordmark font (DB Helvethaica X) is not web-licensed here; logo images are used instead.
- **Logo:** Use only approved variants in `website/assets/logos/`. The 4-circle icon can be drawn as inline SVG (top-left and bottom-right circles filled, the other two outlined, stroke-width 6 at 56×56 viewBox). Logo files with black backgrounds are placed on colored surfaces using `mix-blend-mode: screen`.
- **Voice:** Thai with mixed EN, "คุณ" pronoun, informative and trustworthy — no overclaiming. Website channel tone is educational/SEO-oriented.
- **Copy anchors:** Positioning "สุขภาพดีในทุกมิติของชีวิต / Total wellness for everyday life"; tagline "เรามอบประสบการณ์แบรนด์ที่ดีที่สุดให้แก่คุณ / We Deliver The Top Brand Experiences."

## Notes for Future Sessions

- Marketplace/social links in the contact section are placeholders (`#`) — replace with real Shopee/Lazada/TikTok Shop/social URLs when provided.
- If tooling (npm, bundler, CI) is introduced later, update this file with the real commands.
