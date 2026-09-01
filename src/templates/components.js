const crypto = require('crypto');
const { esc, check } = require('./layout');

// Map a label to a stable placeholder filename. Identical labels intentionally
// share one file, so swapping in a real photo updates every slot that uses it.
const slugify = (label) =>
  'ph-' + crypto.createHash('sha1').update(String(label)).digest('hex').slice(0, 12);

/**
 * Image slot. Renders a real <img> pointing at a generated placeholder so a
 * production photo can be dropped in by replacing the file at the same path.
 */
function media(label, ratio = '4-3', extraClass = '') {
  const file = slugify(label);
  if (!media.registry.some((m) => m.file === file)) media.registry.push({ file, label });
  return `<div class="media ratio-${ratio} ${extraClass}">
      <img src="/assets/img/${file}.svg" alt="${esc(label)}" loading="lazy" width="800" height="600">
    </div>`;
}
media.registry = [];

/** Full-bleed hero artwork: no caption, so headline copy stays legible over it. */
function heroMedia(label) {
  return `<div class="media hero-art">
      <img src="/assets/img/hero-bg.svg" alt="${esc(label)}" width="1600" height="900" fetchpriority="high">
    </div>`;
}

const numberedList = (items) => `
    <ul class="feature-list">
      ${items.map((t, i) => `<li>
        <span class="num">${i + 1}</span>
        <div><p>${esc(t)}</p></div>
      </li>`).join('\n      ')}
    </ul>`;

const checkedList = (items) => `
    <ul class="feature-list">
      ${items.map((t) => `<li>
        <span class="bullet">${check}</span>
        <div><p>${esc(t)}</p></div>
      </li>`).join('\n      ')}
    </ul>`;

const titledList = (items) => `
    <ul class="feature-list">
      ${items.map((it) => `<li>
        <span class="bullet">${check}</span>
        <div><strong>${esc(it.title)}</strong><p>${esc(it.desc)}</p></div>
      </li>`).join('\n      ')}
    </ul>`;

/** Alternating image / copy block used by every category page. */
function featureBlock(block, listHtml, reverse) {
  return `
  <section class="section ${reverse ? 'bg-gray' : 'bg-light'}">
    <div class="wrap">
      <div class="feature${reverse ? ' reverse' : ''} reveal">
        <div class="feature-media">${media(block.image, '4-3')}</div>
        <div>
          <h2 class="t-title">${esc(block.title)}</h2>
          ${listHtml}
        </div>
      </div>
    </div>
  </section>`;
}

const productCard = (p) => `
      <article class="product-card">
        ${media(p.title, '1-1')}
        <h3>${esc(p.title)}</h3>
        <div class="price">${esc(p.price)}</div>
        <div class="actions">
          <a class="btn btn-primary" href="https://shop.bwell.co.th" rel="noopener">หยิบใส่ตะกร้า</a>
          <a class="btn btn-ghost" href="https://shop.bwell.co.th" rel="noopener">ดูสินค้า</a>
        </div>
      </article>`;

const productGrid = (products, heading) => `
  <section class="section bg-light">
    <div class="wrap">
      ${heading ? `<div class="section-head center reveal"><h2 class="t-display">${esc(heading)}</h2></div>` : ''}
      <div class="product-grid reveal">
        ${products.map(productCard).join('\n')}
      </div>
    </div>
  </section>`;

const blogCard = (post) => `
      <a class="blog-card" href="/blog/">
        ${media(post.title, '16-9')}
        <div class="body">
          <span class="tag">${esc(post.tag || 'บทความ')}</span>
          <h3>${esc(post.title)}</h3>
          <span class="link-chevron">อ่านต่อ</span>
        </div>
      </a>`;

const blogSection = (posts, title = 'บทความ', lead = 'อ่านสาระดี ๆ จากทาง Bwell', gray = true) => `
  <section class="section ${gray ? 'bg-gray' : 'bg-light'}">
    <div class="wrap">
      <div class="section-head center reveal">
        <h2 class="t-display">${esc(title)}</h2>
        <p class="t-body">${esc(lead)}</p>
      </div>
      <div class="blog-grid reveal">
        ${posts.map(blogCard).join('\n')}
      </div>
    </div>
  </section>`;

const logoRow = (names, title, lead, gray) => `
  <section class="section-tight ${gray ? 'bg-gray' : 'bg-light'}">
    <div class="wrap">
      <div class="section-head center reveal">
        <h2 class="t-title">${esc(title)}</h2>
        ${lead ? `<p class="t-body">${esc(lead)}</p>` : ''}
      </div>
      <div class="logo-row reveal">
        ${names.map((n) => (typeof n === 'string'
          ? `<span class="logo-chip">${esc(n)}</span>`
          : `<a class="logo-chip" href="${n.url}" rel="noopener">${esc(n.name)}</a>`)).join('\n        ')}
      </div>
    </div>
  </section>`;

const ctaBand = (title, lead, actions, gray = false) => `
  <section class="section ${gray ? 'bg-gray' : 'bg-light'}">
    <div class="wrap">
      <div class="cta-band reveal">
        <h2 class="t-title">${esc(title)}</h2>
        ${lead ? `<p class="t-body">${esc(lead)}</p>` : ''}
        <div class="cta-row center">${actions}</div>
      </div>
    </div>
  </section>`;

/** Collapsible SEO copy — full text is in the DOM for crawlers, visually clipped. */
let seoId = 0;
const seoIntro = (title, body, more) => {
  const id = `seo-${++seoId}`;
  return `
  <section class="section-tight bg-light">
    <div class="wrap">
      <div class="seo-intro reveal">
        <h2 class="t-title">${esc(title)}</h2>
        <div class="seo-body" id="${id}">
          <p class="t-body" style="margin-top:16px">${esc(body)}</p>
          ${more ? `<div class="extra"><div><p class="t-body">${esc(more)}</p></div></div>` : ''}
        </div>
        ${more ? `<button class="seo-toggle" type="button" aria-expanded="false" aria-controls="${id}">อ่านเพิ่มเติม </button>` : ''}
      </div>
    </div>
  </section>`;
};

module.exports = {
  media, heroMedia, numberedList, checkedList, titledList, featureBlock,
  productCard, productGrid, blogCard, blogSection, logoRow, ctaBand, seoIntro,
};
