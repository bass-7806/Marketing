const { esc, catUrl, catName } = require('./layout');
const S = require('../data/site');
const { categories } = require('../data/categories');
const C = require('./components');

module.exports = function home() {
  const hero = categories.find((c) => c.hero);
  const rest = categories.filter((c) => !c.hero);

  const body = `
  <!-- 1. Hero Banner — copy above, product lineup below.
       The Bwell lineup banner is a wide shot on a bright ground, so overlaid
       white text would be unreadable; Apple uses this same stacked treatment
       for its product-family heroes. -->
  <section class="hero hero-light">
    <div class="hero-inner">
      <p class="t-eyebrow">${esc(S.brand.positioning)}</p>
      <h1 class="t-hero">รู้สึกดีได้ในทุกวัน<br>กับ Bwell</h1>
      <p class="t-sub">ยกระดับการดูแลสุขภาพของคุณและครอบครัว ด้วยสินค้าเพื่อสุขภาพที่ผ่านการคัดสรรมาแล้วตั้งแต่ปี ${S.brand.since}</p>
      <div class="cta-row center">
        <a class="btn btn-primary" href="${S.brand.shop}" rel="noopener">เลือกซื้อสินค้า</a>
        <a class="link-chevron" href="/product-bwell/">ดูเพิ่มเติม</a>
      </div>
    </div>
    <div class="hero-lineup">
      ${C.media('สินค้าเพื่อสุขภาพจาก Bwell ทั้งหมด', '16-9', { src: 'hero-lineup.webp', eager: true })}
    </div>
  </section>

  <!-- 2. Category Intro -->
  <section class="section bg-light">
    <div class="wrap">
      <div class="section-head center reveal">
        <p class="t-eyebrow">Bwell เครื่องฟอกอากาศ</p>
        <h2 class="t-display">สำหรับเด็ก ผู้สูงอายุ<br>และผู้ที่มีปัญหาระบบทางเดินหายใจ</h2>
        <p class="t-body">ปกป้องคนที่คุณรักจากมลภาวะทางอากาศในบ้าน ด้วยเครื่องฟอกอากาศคุณภาพสูงจาก Bwell ดักจับฝุ่น PM2.5 กำจัดเชื้อโรคและกลิ่นไม่พึงประสงค์ ให้ทุกลมหายใจในบ้านคุณสะอาดปลอดภัยยิ่งขึ้น</p>
        <div class="cta-row center" style="margin-top:24px">
          <a class="btn btn-primary" href="/air-purifier-bwell/">ดูสินค้าเครื่องฟอกอากาศ</a>
          <a class="link-chevron" href="/why-bwell/">อ่านเพิ่มเติม</a>
        </div>
      </div>
    </div>
  </section>

  <!-- 3. Product Category — hero product + 2-up grid -->
  <section class="section bg-gray">
    <div class="wrap">
      <div class="section-head center reveal">
        <h2 class="t-display">สินค้าตามหมวดหมู่</h2>
        <p class="t-body">ครอบคลุมทุกมุมของการดูแลสุขภาพในบ้าน ตั้งแต่อากาศที่คุณหายใจ ไปจนถึงเก้าอี้ที่คุณนั่งทุกวัน</p>
      </div>

      <div class="tile-hero reveal">
        <div>
          <p class="t-eyebrow">Hero Product</p>
          <h3 class="t-title">${esc(hero.title)}</h3>
          <p class="t-body">${esc(hero.tagline)}</p>
          <a class="btn btn-primary" href="${catUrl(hero)}">ดูสินค้า</a>
        </div>
        ${C.media(hero.title, '4-3', { src: hero.img, fit: hero.img ? 'contain' : 'cover' })}
      </div>

      <div class="tile-grid">
        ${rest.map((c, i) => `
        <a class="tile reveal ${i % 2 ? 'd1' : ''}" href="${catUrl(c)}">
          <h3 class="t-title">${esc(catName(c))}</h3>
          <p class="t-body">${esc(c.hubDesc)}</p>
          <span class="link-chevron" style="margin-bottom:22px">ดูสินค้า</span>
          ${C.media(catName(c), '4-3', { src: c.img, fit: c.img ? 'contain' : 'cover' })}
        </a>`).join('\n')}
      </div>
    </div>
  </section>

  <!-- 4. ตัวแทนจำหน่าย -->
  ${C.logoRow(S.offlinePartners, 'ตัวแทนจำหน่าย', 'พบสินค้า Bwell ได้ที่ห้างสรรพสินค้าและโรงพยาบาลชั้นนำทั่วประเทศ', false)}

  <!-- 5. ตัวแทนจำหน่ายออนไลน์ -->
  ${C.logoRow(S.onlinePartners, 'ตัวแทนจำหน่ายทางออนไลน์', 'สั่งซื้อได้ทันทีผ่านร้านค้าทางการของเราบนทุกแพลตฟอร์ม', true)}

  <!-- 6. บทความ -->
  ${C.blogSection(S.blogPosts.slice(0, 4), 'บทความ', 'อ่านสาระดี ๆ จากทาง Bwell', false)}

  <!-- 7. ลูกค้าของเรา -->
  ${C.logoRow(S.clients, 'ลูกค้าของเรา', 'องค์กรและโรงพยาบาลชั้นนำที่ไว้วางใจเลือกใช้สินค้าของ Bwell', true)}

  <!-- 8. สินค้าแนะนำ -->
  ${C.productGrid(S.featuredProducts, 'สินค้าแนะนำ')}

  <!-- 9. รีวิวลูกค้า -->
  <section class="section bg-gray">
    <div class="wrap">
      <div class="section-head center reveal">
        <h2 class="t-display">ความคิดเห็นจากผู้ใช้จริง</h2>
      </div>
      <div class="review-grid reveal">
        ${S.reviews.map((r) => `
        <article class="review">
          <div class="stars" aria-label="ให้คะแนน 5 จาก 5">★★★★★</div>
          <p>${esc(r.text)}</p>
          <div class="who">
            <span class="avatar" aria-hidden="true">${esc(r.name.slice(0, 1))}</span>
            <strong>${esc(r.name)}</strong>
          </div>
        </article>`).join('\n')}
      </div>
    </div>
  </section>

  <!-- 10. Download Brochure CTA -->
  ${/* TODO: when the catalogue PDF is supplied, drop it at
        src/assets/brochure/bwell-catalogue.pdf and point this button there
        with the label 'คลิกเพื่อดาวน์โหลด'. */ ''}
  ${C.ctaBand(
    'โบรชัวร์สินค้าของเรา',
    'รวมสินค้าทุกหมวดหมู่ พร้อมสเปกและราคาในไฟล์เดียว ขอรับได้จากทีมงาน',
    '<a class="btn btn-light" href="/contact/">ขอรับโบรชัวร์สินค้า</a>' +
    `<a class="link-chevron on-dark" href="${S.contact.line}" rel="noopener">สอบถามผ่าน LINE</a>`
  )}
`;

  return {
    title: 'Bwell',
    description: 'Bwell สินค้าเพื่อสุขภาพสำหรับทุกบ้าน เครื่องฟอกอากาศ PM2.5 เครื่องกรองน้ำ เครื่องลดความชื้น หุ่นยนต์ดูดฝุ่น และเก้าอี้เพื่อสุขภาพ ดูแลสุขภาพคนไทยตั้งแต่ปี 2011',
    url: '/',
    body,
  };
};
