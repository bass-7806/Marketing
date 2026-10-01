const { esc, catUrl, catName } = require('./layout');
const S = require('../data/site');
const C = require('./components');

/**
 * Product Category page — follows the approved category wireframe:
 * hero → sub-category nav → SEO intro → product grid → online partners →
 * four alternating SEO feature blocks → contact CTA → related posts.
 */
module.exports = function category(cat, opts = {}) {
  const name = catName(cat);
  const heroLead = opts.heroLead || cat.heroLead;
  const url = opts.url || catUrl(cat);
  const parentCrumb = opts.parent
    ? `<a href="${catUrl(opts.parent)}">${esc(catName(opts.parent))}</a><span>/</span>`
    : '';

  const related = S.blogPosts.filter((p) => p.tag === name).concat(S.blogPosts).slice(0, 4);

  const body = `
  <!-- 1. Category Hero -->
  <section class="cat-hero">
    <div class="wrap">
      <nav class="crumbs reveal" aria-label="เส้นทางหน้าเว็บ">
        <a href="/">Home</a><span>/</span>
        <a href="/product-bwell/">Product</a><span>/</span>
        ${parentCrumb}${esc(opts.title || name)}
      </nav>
      <h1 class="t-display reveal">${esc(opts.title || name)}</h1>
      <p class="t-body reveal">${esc(heroLead)}</p>
    </div>
  </section>

  ${cat.subCategories && cat.subCategories.length ? `
  <!-- 2. Sub-category Nav -->
  <section class="section-tight bg-light">
    <div class="wrap">
      <div class="subcat-nav reveal">
        ${cat.subCategories.map((s) => `
        <a class="subcat" href="${s.url}">
          <svg class="dot" viewBox="0 0 40 40" aria-hidden="true">
            <circle cx="20" cy="20" r="20" fill="rgba(0,138,208,.1)"/>
            <path d="M17 14l6 6-6 6" fill="none" stroke="#008ad0" stroke-width="2.4"
                  stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <span><strong>${esc(s.title)}</strong><span>${esc(s.desc)}</span></span>
        </a>`).join('\n')}
      </div>
    </div>
  </section>` : ''}

  <!-- 3. SEO Intro -->
  ${C.seoIntro(cat.introTitle, cat.introBody, cat.introMore)}

  <!-- 4. Product Grid -->
  ${C.productGrid(opts.products || cat.products, 'สินค้าขายดี')}

  <!-- 5. ตัวแทนจำหน่ายออนไลน์ -->
  ${C.logoRow(S.onlinePartners, 'ตัวแทนจำหน่ายทางออนไลน์', '', true)}

  <!-- 6–9. SEO feature blocks, alternating sides -->
  ${C.featureBlock(cat.whyChoose, C.titledList(cat.whyChoose.items), false, cat.slug)}
  ${C.featureBlock(cat.benefits, C.checkedList(cat.benefits.items), true, cat.slug)}
  ${C.featureBlock(cat.howToChoose, C.numberedList(cat.howToChoose.items), false, cat.slug)}
  ${C.featureBlock(cat.maintenance, C.numberedList(cat.maintenance.items), true, cat.slug)}

  <!-- 10. Contact CTA -->
  ${C.ctaBand(
    'สอบถามข้อมูลกับ Bwell',
    'ไม่แน่ใจว่ารุ่นไหนเหมาะกับบ้านคุณ ทีมงานของเรายินดีให้คำแนะนำ',
    `<a class="btn btn-light" href="/contact/">ติดต่อเรา</a>` +
    `<a class="link-chevron on-dark" href="${S.contact.line}" rel="noopener">สอบถามผ่าน LINE</a>`
  )}

  <!-- 11. บทความที่เกี่ยวข้อง -->
  ${C.blogSection(related, 'บทความที่เกี่ยวข้อง', 'ทำความเข้าใจก่อนตัดสินใจซื้อ', true)}
`;

  return {
    title: opts.title || name,
    description: `${opts.title || name} จาก Bwell — ${heroLead}`.slice(0, 160),
    url,
    body,
  };
};
