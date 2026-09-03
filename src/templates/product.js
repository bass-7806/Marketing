const { esc, catUrl, catName } = require('./layout');
const S = require('../data/site');
const C = require('./components');
const { comparison, productUrl } = require('../data/products');

const SHOP = 'https://shop.bwell.co.th';

/**
 * Product detail page — mirrors the live bwell.co.th product page:
 * title + price → gallery → "ระบบการทำงานที่แตกต่าง" → "รายละเอียดสินค้า" →
 * related models → contact CTA, restyled to the new Apple-referenced system.
 *
 * @param {object} p        product from data/products.js
 * @param {object[]} all    every product (for related + comparison links)
 * @param {object} cat      parent category
 */
module.exports = function product(p, all, cat) {
  const url = productUrl(p);
  const siblings = all.filter((x) => x.category === p.category && x.slug !== p.slug);
  const bySlug = Object.fromEntries(all.map((x) => [x.slug, x]));
  const priceHtml = p.price
    ? `<div class="pdp-price"><span class="sr-only">ราคา</span>${esc(p.price)}</div>`
    : `<div class="pdp-price pdp-price-ask">สอบถามราคา <span>เปิดตัวใหม่ — ติดต่อทีมงานเพื่อรับราคาและโปรโมชั่น</span></div>`;

  const gallery = `
      <div class="pdp-gallery" data-gallery>
        <div class="pdp-main">
          ${C.media(p.gallery[0].alt, '1-1', { src: p.gallery[0].src, fit: 'contain', eager: true })}
        </div>
        ${p.gallery.length > 1 ? `
        <div class="pdp-thumbs" role="group" aria-label="รูปภาพสินค้า">
          ${p.gallery.map((g, i) => `
          <button type="button" data-src="/assets/img/${esc(g.src)}" data-alt="${esc(g.alt)}"
                  aria-pressed="${i === 0}" aria-label="รูปที่ ${i + 1}: ${esc(g.alt)}">
            <img src="/assets/img/${esc(g.src)}" alt="" loading="lazy" width="120" height="120">
          </button>`).join('')}
        </div>` : ''}
      </div>`;

  const compareTable = comparison && comparison.columns.includes(p.slug) ? `
  <section class="section bg-light">
    <div class="wrap">
      <div class="section-head center reveal">
        <h2 class="t-display">${esc(comparison.title)}</h2>
        <p class="t-body">ดูภาพรวมทุกรุ่นเพื่อเลือกหุ่นยนต์ที่เหมาะกับบ้านของคุณ</p>
      </div>
      <div class="table-scroll reveal">
        <table class="compare">
          <thead>
            <tr>
              <th scope="col">หัวข้อเปรียบเทียบ</th>
              ${comparison.columns.map((s) => `<th scope="col"${s === p.slug ? ' class="is-current"' : ''}>${
                s === p.slug ? esc(bySlug[s].shortTitle) : `<a href="${productUrl(bySlug[s])}">${esc(bySlug[s].shortTitle)}</a>`
              }</th>`).join('')}
            </tr>
          </thead>
          <tbody>
            ${comparison.rows.map(([label, ...cells]) => `
            <tr>
              <th scope="row">${esc(label)}</th>
              ${cells.map((c, i) => `<td${comparison.columns[i] === p.slug ? ' class="is-current"' : ''}>${esc(c)}</td>`).join('')}
            </tr>`).join('')}
          </tbody>
        </table>
      </div>
    </div>
  </section>` : '';

  const body = `
  <!-- 1. Product hero: gallery + summary -->
  <section class="pdp-hero">
    <div class="wrap">
      <nav class="crumbs reveal" aria-label="เส้นทางหน้าเว็บ">
        <a href="/">Home</a><span>/</span>
        <a href="/product-bwell/">Product</a><span>/</span>
        <a href="${catUrl(cat)}">${esc(catName(cat))}</a><span>/</span>
        ${esc(p.shortTitle)}
      </nav>
      <div class="pdp-grid reveal">
        ${gallery}
        <div class="pdp-info">
          <p class="t-eyebrow">${esc(p.model)}${p.badge ? ` <span class="badge">${esc(p.badge)}</span>` : ''}</p>
          <h1 class="t-display">${esc(p.title)}</h1>
          ${p.subtitle ? `<p class="pdp-subtitle">${esc(p.subtitle)}</p>` : ''}
          <p class="t-body">${esc(p.intro || p.tagline)}</p>
          ${priceHtml}
          ${p.chips && p.chips.length ? `<ul class="pdp-chips" aria-label="จุดเด่น">${p.chips.map((c) => `<li>${esc(c)}</li>`).join('')}</ul>` : ''}
          <div class="cta-row">
            <a class="btn btn-primary" href="${SHOP}" rel="noopener">${p.price ? 'หยิบใส่ตะกร้า' : 'สอบถามราคา'}</a>
            <a class="btn btn-ghost" href="${S.contact.line}" rel="noopener">สอบถามผ่าน LINE</a>
          </div>
          <p class="pdp-meta">รับประกันสินค้า ${esc(p.specs.find(([k]) => /รับประกัน/.test(k))[1])} · จัดส่งทั่วประเทศ · ศูนย์บริการ Bwell</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. Key numbers -->
  <section class="section-tight bg-light">
    <div class="wrap">
      <ul class="pdp-stats reveal">
        ${p.stats.map((s) => `<li><strong>${esc(s.value)}</strong><span>${esc(s.label)}</span></li>`).join('')}
      </ul>
    </div>
  </section>

  <!-- 3. ระบบการทำงานที่แตกต่าง -->
  ${C.featureBlock(
    { title: 'ระบบการทำงานที่แตกต่าง', image: p.featureImage.alt, imageSrc: p.featureImage.src },
    C.checkedList(p.features), true, cat.slug
  )}

  <!-- 4. รายละเอียดสินค้า -->
  <section class="section bg-light">
    <div class="wrap">
      <div class="spec-wrap reveal">
        <div class="section-head">
          <h2 class="t-display">รายละเอียดสินค้า</h2>
          <p class="t-body">สเปกของ ${esc(p.model)}</p>
        </div>
        <dl class="spec-table">
          ${p.specs.map(([k, v]) => `<div><dt>${esc(k)}</dt><dd>${esc(v)}</dd></div>`).join('')}
        </dl>
        ${p.footnote ? `<p class="pdp-note">${esc(p.footnote)}</p>` : ''}
      </div>
    </div>
  </section>

  ${p.suitableFor ? `
  <!-- 5. เหมาะสำหรับ -->
  <section class="section bg-gray">
    <div class="wrap">
      <div class="feature reveal">
        <div>
          <h2 class="t-title">เหมาะสำหรับ</h2>
          <p class="t-body" style="margin-top:14px">${esc(p.suitableFor)}</p>
        </div>
        <div>
          <h3 class="t-eyebrow" style="margin-bottom:14px">กลุ่มผู้ใช้งาน</h3>
          ${C.checkedList(p.persona || [])}
        </div>
      </div>
    </div>
  </section>` : ''}

  <!-- 6. เปรียบเทียบรุ่น -->
  ${compareTable}

  <!-- 7. Related products -->
  ${siblings.length ? C.productGrid(siblings.map((s) => ({
    title: s.title, price: s.price || 'สอบถามราคา', img: s.img, url: productUrl(s), badge: s.badge,
  })), 'รุ่นอื่นในหมวดหุ่นยนต์ดูดฝุ่น') : ''}

  <!-- 8. Contact CTA -->
  ${C.ctaBand(
    'สอบถามข้อมูลเพิ่มเติม',
    `สนใจ ${p.model} หรืออยากให้ทีมงานช่วยเลือกรุ่นที่เหมาะกับบ้านคุณ ติดต่อเราได้ทุกช่องทาง`,
    `<a class="btn btn-light" href="/contact/">ติดต่อเรา</a>` +
    `<a class="link-chevron on-dark" href="${S.contact.line}" rel="noopener">สอบถามผ่าน LINE</a>`,
    true
  )}
`;

  const jsonld = {
    '@context': 'https://schema.org',
    '@type': 'Product',
    name: p.title,
    brand: { '@type': 'Brand', name: 'Bwell' },
    model: p.model,
    image: p.gallery.map((g) => `https://bwell.co.th/assets/img/${g.src}`),
    description: p.metaDescription || `${p.title} — ${p.tagline}`,
    url: `https://bwell.co.th${url}`,
    ...(p.price ? {
      offers: {
        '@type': 'Offer',
        priceCurrency: 'THB',
        price: p.price.replace(/[^\d.]/g, ''),
        availability: 'https://schema.org/InStock',
        url: SHOP,
      },
    } : {}),
  };

  return {
    title: p.seoTitle || p.title,
    description: (p.metaDescription || `${p.title} — ${p.tagline}`).slice(0, 160),
    url,
    current: catUrl(cat),
    body,
    jsonld,
  };
};
