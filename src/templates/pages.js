const { esc, catUrl, catName, check } = require('./layout');
const S = require('../data/site');
const { categories } = require('../data/categories');
const C = require('./components');

const pageHero = (title, lead, crumb) => `
  <section class="cat-hero">
    <div class="wrap">
      ${crumb ? `<nav class="crumbs reveal" aria-label="เส้นทางหน้าเว็บ"><a href="/">Home</a><span>/</span>${esc(crumb)}</nav>` : ''}
      <h1 class="t-display reveal">${esc(title)}</h1>
      ${lead ? `<p class="t-body reveal">${esc(lead)}</p>` : ''}
    </div>
  </section>`;

/* ------------------------------------------------------- Product hub page */

function productHub() {
  const hero = categories.find((c) => c.hero);
  const rest = categories.filter((c) => !c.hero);
  return {
    title: 'สินค้าทั้งหมด',
    description: 'สินค้าเพื่อสุขภาพจาก Bwell ครบทุกหมวดหมู่ เครื่องฟอกอากาศ เครื่องกรองน้ำ เครื่องลดความชื้น หุ่นยนต์ดูดฝุ่น เก้าอี้เพื่อสุขภาพ และอุปกรณ์จัดแต่งทรงผม',
    url: '/product-bwell/',
    body: `
  ${pageHero('สินค้าทั้งหมด', 'สินค้าเพื่อสุขภาพที่ครอบคลุมทุกมุมของบ้าน คัดสรรและพัฒนาโดย Bwell ตั้งแต่ปี ' + S.brand.since, 'Product')}

  <section class="section bg-gray">
    <div class="wrap">
      <div class="tile-hero reveal">
        <div>
          <p class="t-eyebrow">หมวดหมู่ยอดนิยม</p>
          <h2 class="t-title">${esc(hero.title)}</h2>
          <p class="t-body">${esc(hero.tagline)}</p>
          <a class="btn btn-primary" href="${catUrl(hero)}">ดูสินค้า</a>
        </div>
        ${C.media(hero.title, '4-3')}
      </div>
      <div class="tile-grid">
        ${rest.map((c, i) => `
        <a class="tile reveal ${i % 2 ? 'd1' : ''}" href="${catUrl(c)}">
          <h2 class="t-title">${esc(catName(c))}</h2>
          <p class="t-body">${esc(c.hubDesc)}</p>
          <span class="link-chevron" style="margin-bottom:22px">ดูสินค้า</span>
          ${C.media(catName(c), '4-3')}
        </a>`).join('\n')}
      </div>
    </div>
  </section>

  ${C.logoRow(S.onlinePartners, 'สั่งซื้อออนไลน์ได้ที่', '', false)}
  ${C.ctaBand('ไม่แน่ใจว่ารุ่นไหนเหมาะกับคุณ',
    'บอกเราว่าบ้านของคุณมีปัญหาอะไร แล้วให้ทีมงานช่วยแนะนำรุ่นที่ตรงที่สุด',
    '<a class="btn btn-light" href="/contact/">ติดต่อเรา</a>', true)}
`,
  };
}

/* ---------------------------------------------------------- About cluster */

function aboutUs() {
  return {
    title: 'เกี่ยวกับ Bwell',
    description: 'Bwell ถือกำเนิดในปี 2011 จากการพูดคุยกับแพทย์ว่าประเทศไทยยังไม่มีเครื่องฟอกอากาศที่ออกแบบมาสำหรับผู้ที่ต้องการความอ่อนโยนเป็นพิเศษ',
    url: '/about-us/',
    body: `
  ${pageHero('เกี่ยวกับ Bwell', S.brand.taglineTh, 'About us')}

  <section class="section bg-light">
    <div class="wrap">
      <div class="feature reveal">
        <div class="feature-media">${C.media('ทีมงานและโชว์รูม Bwell', '4-3')}</div>
        <div class="prose">
          <h2 class="t-title">เริ่มต้นจากคำถามของแพทย์</h2>
          <p>แบรนด์ Bwell ถือกำเนิดในปี ${S.brand.since} จากการพูดคุยกับแพทย์ว่าในประเทศไทยยังไม่มีเครื่องฟอกอากาศที่ออกแบบมาสำหรับคนที่ต้องการความอ่อนโยนเป็นพิเศษ ทั้งเด็กเล็ก ผู้สูงอายุ และผู้ที่มีปัญหาระบบทางเดินหายใจ</p>
          <p>ในเวลานั้นเครื่องฟอกอากาศส่วนใหญ่ในตลาดใช้ระบบไอออนไนซ์ที่ปล่อยโอโซนเป็นผลพลอยได้ เราจึงเลือกพัฒนาระบบฟอกอากาศด้วย UV และ Photocatalytic Oxidation ซึ่งจัดการเชื้อโรคได้โดยไม่ทิ้งผลข้างเคียงไว้ในอากาศที่คุณหายใจ</p>
          <p>จากเครื่องฟอกอากาศเครื่องแรก Bwell ขยายไปสู่สินค้าเพื่อสุขภาพอื่น ๆ ที่ตอบโจทย์ชีวิตประจำวัน ทั้งเครื่องดูดฝุ่นสำหรับผู้แพ้ไรฝุ่น ซึ่งได้รับรางวัล Red Dot Design Award เครื่องลดความชื้น แอร์เคลื่อนที่ ไปจนถึงเครื่องกรองน้ำ</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-gray">
    <div class="wrap">
      <div class="stat-grid reveal">
        <div class="stat"><div class="n">${new Date().getFullYear() - S.brand.since}+</div><div class="l">ปีในตลาดสินค้าเพื่อสุขภาพ</div></div>
        <div class="stat"><div class="n">${categories.length}</div><div class="l">หมวดหมู่สินค้า</div></div>
        <div class="stat"><div class="n">Red Dot</div><div class="l">รางวัลด้านการออกแบบ</div></div>
        <div class="stat"><div class="n">2</div><div class="l">สาขาในกรุงเทพฯ</div></div>
      </div>
    </div>
  </section>

  <section class="section bg-light">
    <div class="wrap">
      <div class="section-head center reveal">
        <h2 class="t-display">สิ่งที่เรายึดถือ</h2>
      </div>
      <div class="card-grid reveal">
        <div class="card"><h3 class="t-title">พูดตรง อิงข้อมูล</h3><p class="t-body">เราบอกสิ่งที่สินค้าทำได้จริงตามสเปกและผลทดสอบ ไม่ขายด้วยคำโฆษณาเกินจริง</p></div>
        <div class="card"><h3 class="t-title">ปลอดภัยมาก่อน</h3><p class="t-body">ทุกสินค้าผ่านมาตรฐานความปลอดภัย ออกแบบให้ใช้ได้กับเด็กและผู้สูงอายุในบ้านเดียวกัน</p></div>
        <div class="card"><h3 class="t-title">คุ้มค่าในระยะยาว</h3><p class="t-body">อะไหล่และไส้กรองหาซื้อได้ต่อเนื่อง เพราะสินค้าที่ดีต้องใช้ได้นานกว่าหนึ่งฤดูกาล</p></div>
      </div>
    </div>
  </section>

  ${C.logoRow(S.clients, 'ลูกค้าของเรา', 'องค์กรและโรงพยาบาลชั้นนำที่ไว้วางใจเลือกใช้สินค้าของ Bwell', true)}
  ${C.ctaBand('อยากรู้จัก Bwell มากขึ้น', 'อ่านเหตุผลที่ลูกค้าเลือกเรา หรือแวะมาทดลองสินค้าจริงที่โชว์รูม',
    '<a class="btn btn-light" href="/why-bwell/">ทำไมต้อง Bwell</a><a class="link-chevron on-dark" href="/findbwell/">ค้นหาสาขา</a>')}
`,
  };
}

function whyBwell() {
  const reasons = [
    { title: 'พัฒนาร่วมกับบุคลากรทางการแพทย์', desc: 'สินค้าชิ้นแรกของเราเกิดจากโจทย์ของแพทย์ และเรายังคงยึดแนวทางนี้ในการพัฒนาสินค้าทุกรุ่น' },
    { title: 'เทคโนโลยีที่ไม่ทิ้งผลข้างเคียง', desc: 'เราเลือกระบบ UV และ Photocatalytic Oxidation แทนระบบที่ปล่อยโอโซนตกค้างในอากาศ' },
    { title: 'ดีไซน์ระดับรางวัล', desc: 'การออกแบบเครื่องดูดฝุ่นของ Bwell ได้รับรางวัล Red Dot Design Award' },
    { title: 'อะไหล่หาง่ายตลอดอายุการใช้งาน', desc: 'ไส้กรองและอะไหล่มีจำหน่ายต่อเนื่อง ไม่ทิ้งลูกค้าไว้กับสินค้าที่ซ่อมไม่ได้' },
    { title: 'บริการหลังการขายในไทย', desc: 'ทีมงานและศูนย์บริการอยู่ในประเทศ ติดต่อได้จริงทั้งทางโทรศัพท์และ LINE' },
    { title: 'ราคาที่เข้าถึงได้', desc: 'คุณภาพระดับพรีเมียมในราคาที่ครอบครัวไทยจับต้องได้จริง' },
  ];
  return {
    title: 'ทำไมต้อง Bwell',
    description: 'เหตุผลที่ครอบครัวไทย โรงพยาบาล และองค์กรชั้นนำเลือกใช้สินค้าเพื่อสุขภาพจาก Bwell',
    url: '/why-bwell/',
    body: `
  ${pageHero('ทำไมต้อง Bwell', 'เหตุผลที่ครอบครัวไทย โรงพยาบาล และองค์กรชั้นนำเลือกใช้สินค้าของเรา', 'About us')}
  <section class="section bg-light">
    <div class="wrap">
      <div class="card-grid reveal">
        ${reasons.map((r) => `<div class="card"><span class="icon">${check}</span><h2 class="t-title">${esc(r.title)}</h2><p class="t-body">${esc(r.desc)}</p></div>`).join('\n')}
      </div>
    </div>
  </section>
  ${C.logoRow(S.clients, 'ลูกค้าของเรา', '', true)}
  ${C.ctaBand('พร้อมเริ่มดูแลสุขภาพที่บ้านแล้วหรือยัง', '', '<a class="btn btn-light" href="/product-bwell/">ดูสินค้าทั้งหมด</a>')}
`,
  };
}

function ourClient() {
  return {
    title: 'ลูกค้าของเรา',
    description: 'องค์กร โรงพยาบาล และหน่วยงานราชการที่ไว้วางใจเลือกใช้สินค้าเพื่อสุขภาพจาก Bwell',
    url: '/our-client/',
    body: `
  ${pageHero('ลูกค้าของเรา', 'องค์กร โรงพยาบาล และหน่วยงานที่ไว้วางใจเลือกใช้สินค้าของ Bwell', 'About us')}
  ${C.logoRow(S.clients, 'องค์กรที่ไว้วางใจ Bwell', '', false)}
  <section class="section bg-gray">
    <div class="wrap">
      <div class="section-head center reveal"><h2 class="t-display">ความคิดเห็นจากผู้ใช้จริง</h2></div>
      <div class="review-grid reveal">
        ${S.reviews.map((r) => `
        <article class="review">
          <div class="stars" aria-label="ให้คะแนน 5 จาก 5">★★★★★</div>
          <p>${esc(r.text)}</p>
          <div class="who"><span class="avatar" aria-hidden="true">${esc(r.name.slice(0, 1))}</span><strong>${esc(r.name)}</strong></div>
        </article>`).join('\n')}
      </div>
    </div>
  </section>
  ${C.ctaBand('สนใจสั่งซื้อในนามองค์กร', 'เรามีทีมดูแลลูกค้าองค์กรสำหรับการสั่งซื้อจำนวนมากและงานโครงการ',
    '<a class="btn btn-light" href="/contact/">ติดต่อฝ่ายขายองค์กร</a>')}
`,
  };
}

/* ------------------------------------------------------------ Other pages */

function distribution() {
  return {
    title: 'ช่องทางจัดจำหน่าย',
    description: 'ซื้อสินค้า Bwell ได้ที่ห้างสรรพสินค้าและโรงพยาบาลชั้นนำ หรือสั่งออนไลน์ผ่าน Shopee Lazada NocNoc และร้านค้าทางการ',
    url: '/distribution-channels/',
    body: `
  ${pageHero('ช่องทางจัดจำหน่าย', 'เลือกซื้อสินค้า Bwell ได้ทั้งหน้าร้านและออนไลน์ ผ่านช่องทางทางการที่รับประกันสินค้าแท้', 'ช่องทางจัดจำหน่าย')}
  ${C.logoRow(S.onlinePartners, 'ช่องทางออนไลน์', 'ร้านค้าทางการของ Bwell บนทุกแพลตฟอร์ม สั่งซื้อได้ตลอด 24 ชั่วโมง', false)}
  ${C.logoRow(S.offlinePartners, 'ช่องทางหน้าร้าน', 'พบสินค้า Bwell ได้ที่ห้างสรรพสินค้าและโรงพยาบาลชั้นนำทั่วประเทศ', true)}
  <section class="section bg-light">
    <div class="wrap">
      <div class="card-grid reveal" style="grid-template-columns:repeat(2,1fr)">
        ${[S.contact.showroom, S.contact.flagship].map((l) => `
        <div class="card">
          <h2 class="t-title">${esc(l.label)}</h2>
          <p class="t-body">${esc(l.address)}</p>
          <p class="t-body"><strong>โทร.</strong> <a href="tel:${l.phone.replace(/-/g, '')}">${esc(l.phone)}</a><br>
          <strong>เวลาทำการ</strong> ${esc(l.hours)}</p>
        </div>`).join('\n')}
      </div>
    </div>
  </section>
  ${C.ctaBand('สนใจเป็นตัวแทนจำหน่าย', 'เปิดรับตัวแทนจำหน่ายทั่วประเทศ ติดต่อทีมงานเพื่อรับรายละเอียด',
    '<a class="btn btn-light" href="/contact/">สมัครตัวแทนจำหน่าย</a>', true)}
`,
  };
}

function findBwell() {
  return {
    title: 'ค้นหาสาขาของ Bwell',
    description: 'ที่อยู่ เบอร์โทรศัพท์ และเวลาทำการของ Bwell Showroom และ Bwell Flagship Store',
    url: '/findbwell/',
    body: `
  ${pageHero('ค้นหาสาขาของ Bwell', 'แวะมาทดลองสินค้าจริงก่อนตัดสินใจ ที่สาขาของเราในกรุงเทพฯ', 'ค้นหาสาขา')}
  <section class="section bg-light">
    <div class="wrap">
      ${[S.contact.showroom, S.contact.flagship].map((l, i) => `
      <div class="feature${i ? ' reverse' : ''} reveal" style="margin-bottom:64px">
        <div class="feature-media">${C.media(l.label, '4-3')}</div>
        <div class="prose">
          <h2 class="t-title">${esc(l.label)}</h2>
          <p>${esc(l.address)}</p>
          <p><strong>โทร.</strong> <a href="tel:${l.phone.replace(/-/g, '')}">${esc(l.phone)}</a></p>
          <p><strong>เวลาทำการ</strong> ${esc(l.hours)}</p>
        </div>
      </div>`).join('\n')}
    </div>
  </section>
`,
  };
}

function blog() {
  return {
    title: 'บทความ',
    description: 'บทความและสาระความรู้เรื่องสุขภาพในบ้านจาก Bwell เรื่อง PM2.5 ไส้กรอง HEPA การเลือกเครื่องดูดฝุ่น และออฟฟิศซินโดรม',
    url: '/blog/',
    body: `
  ${pageHero('บทความ', 'อ่านสาระดี ๆ เรื่องสุขภาพในบ้าน ก่อนตัดสินใจเลือกสินค้าที่ใช่', 'บทความ')}
  <section class="section bg-light">
    <div class="wrap">
      <div class="blog-grid reveal">
        ${S.blogPosts.map(C.blogCard).join('\n')}
      </div>
    </div>
  </section>
  ${C.ctaBand('มีคำถามที่ยังไม่มีคำตอบ', 'ทีมงานของเรายินดีให้คำแนะนำเป็นรายบุคคล',
    '<a class="btn btn-light" href="/contact/">ติดต่อเรา</a>', true)}
`,
  };
}

function contact() {
  return {
    title: 'ติดต่อเรา',
    description: 'ติดต่อ Bwell — Showroom เจริญราษฎร์ โทร 02-294-3211 และ Flagship Store ศูนย์การค้า CDC โทร 02-100-5075 หรือสอบถามผ่าน LINE',
    url: '/contact/',
    body: `
  ${pageHero('ติดต่อเรา', 'ทีมงาน Bwell พร้อมให้คำแนะนำ ทั้งการเลือกสินค้า การใช้งาน และบริการหลังการขาย', 'ติดต่อเรา')}
  <section class="section bg-light">
    <div class="wrap">
      <div class="card-grid reveal" style="grid-template-columns:repeat(2,1fr)">
        ${[S.contact.showroom, S.contact.flagship].map((l) => `
        <div class="card">
          <h2 class="t-title">${esc(l.label)}</h2>
          <p class="t-body">${esc(l.address)}</p>
          <p class="t-body"><strong>โทร.</strong> <a href="tel:${l.phone.replace(/-/g, '')}">${esc(l.phone)}</a><br>
          <strong>เวลาทำการ</strong> ${esc(l.hours)}</p>
        </div>`).join('\n')}
      </div>
    </div>
  </section>
  ${C.ctaBand('สอบถามข้อมูลเพิ่มเติม', 'ทักหาเราทาง LINE เพื่อรับคำแนะนำแบบรวดเร็ว หรือสั่งซื้อผ่านร้านค้าทางการ',
    `<a class="btn btn-light" href="${S.contact.line}" rel="noopener">สอบถามผ่าน LINE</a>` +
    `<a class="link-chevron on-dark" href="${S.brand.shop}" rel="noopener">สั่งซื้อออนไลน์</a>`, true)}
`,
  };
}

/* ------------------------------------------------------------- Policies */

function policy(p) {
  return {
    title: p.title,
    description: p.description,
    url: p.url,
    body: `
  ${pageHero(p.title, p.lead, 'นโยบาย')}
  <section class="section bg-light">
    <div class="wrap-narrow prose reveal">
      ${p.sections.map((s) => `
      <h2>${esc(s.h)}</h2>
      ${s.p.map((t) => `<p>${esc(t)}</p>`).join('\n      ')}
      ${s.ul ? `<ul>${s.ul.map((t) => `<li>${esc(t)}</li>`).join('')}</ul>` : ''}`).join('\n')}
      <p class="t-small" style="margin-top:48px">มีคำถามเกี่ยวกับนโยบายนี้ ติดต่อเราได้ที่ <a href="/contact/">หน้าติดต่อเรา</a> หรือโทร ${esc(S.contact.showroom.phone)}</p>
    </div>
  </section>
`,
  };
}

module.exports = {
  productHub, aboutUs, whyBwell, ourClient,
  distribution, findBwell, blog, contact, policy,
};
