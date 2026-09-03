const { brand, nav, footer, onlinePartners } = require('../data/site');
const { categories } = require('../data/categories');

const esc = (s) => String(s)
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;');

// The 4-circle Bwell mark, per the brand guidelines' SVG construction.
const mark = (color = '#008ad0', size = 22) => `
<svg class="mark" width="${size}" height="${size}" viewBox="0 0 56 56" aria-hidden="true" focusable="false">
  <circle cx="16" cy="16" r="13" fill="${color}"/>
  <circle cx="40" cy="16" r="13" fill="none" stroke="${color}" stroke-width="6"/>
  <circle cx="16" cy="40" r="13" fill="none" stroke="${color}" stroke-width="6"/>
  <circle cx="40" cy="40" r="13" fill="${color}"/>
</svg>`;

const check = `<svg viewBox="0 0 24 24" fill="none" stroke="#008ad0" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>`;

const catUrl = (c) => `/${c.slug}/`;
const catName = (c) => c.shortTitle || c.title;

function header(current) {
  const isCur = (url) => (url === current ? ' aria-current="page"' : '');

  const megaPanel = `
      <div class="nav-panel mega">
        ${categories.map((c) => `<a href="${catUrl(c)}">${esc(catName(c))}</a>`).join('\n        ')}
      </div>`;

  const links = nav.map((item) => {
    let panel = '';
    if (item.mega) panel = megaPanel;
    else if (item.children) {
      panel = `
      <div class="nav-panel">
        ${item.children.map((ch) => `<a href="${ch.url}">${esc(ch.title)}</a>`).join('\n        ')}
      </div>`;
    }
    return `      <li><a class="nav-link" href="${item.url}"${isCur(item.url)}>${esc(item.title)}</a>${panel}</li>`;
  }).join('\n');

  return `
<header class="site-header">
  <nav class="nav" aria-label="เมนูหลัก">
    <a class="nav-logo" href="/" aria-label="Bwell หน้าแรก">
      ${mark('#008ad0', 22)}
      <span class="word">Bwell</span>
    </a>
    <ul class="nav-links">
${links}
    </ul>
    <a class="nav-shop" href="${brand.shop}" rel="noopener">สั่งซื้อออนไลน์</a>
    <button class="nav-toggle" type="button" aria-expanded="false"
            aria-controls="mobile-menu" aria-label="เปิดเมนู">
      <span></span><span></span>
    </button>
  </nav>
</header>

<div class="mobile-menu" id="mobile-menu">
  ${nav.map((i) => `<a href="${i.url}">${esc(i.title)}</a>` +
      (i.children ? `<div class="sub">${i.children.map((c) => `<a href="${c.url}">${esc(c.title)}</a>`).join('')}</div>` : '')
    ).join('\n  ')}
  <a href="${brand.shop}" rel="noopener">สั่งซื้อออนไลน์</a>
  <div class="group-label">สินค้า</div>
  ${categories.map((c) => `<a href="${catUrl(c)}">${esc(catName(c))}</a>`).join('\n  ')}
</div>`;
}

function siteFooter() {
  const half = Math.ceil(categories.length / 2);
  const colA = categories.slice(0, half);
  const colB = categories.slice(half);

  return `
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <span class="word">Bwell</span>
        <p>${esc(brand.taglineTh)}<br>ดูแลสุขภาพคนไทยตั้งแต่ปี ${brand.since}</p>
      </div>
      <div class="footer-col">
        <h4>หน้าเพจ</h4>
        <ul>${footer.pages.map((p) => `<li><a href="${p.url}">${esc(p.title)}</a></li>`).join('')}</ul>
      </div>
      <div class="footer-col">
        <h4>สินค้า</h4>
        <ul>${colA.map((c) => `<li><a href="${catUrl(c)}">${esc(catName(c))}</a></li>`).join('')}</ul>
      </div>
      <div class="footer-col">
        <h4>สินค้า (ต่อ)</h4>
        <ul>${colB.map((c) => `<li><a href="${catUrl(c)}">${esc(catName(c))}</a></li>`).join('')}
          <li><a href="${brand.shop}" rel="noopener">สั่งซื้อออนไลน์</a></li>
          ${onlinePartners.map((p) => `<li><a href="${p.url}" rel="noopener">${esc(p.name)}</a></li>`).join('')}
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© ${new Date().getFullYear()} Bwell. สงวนลิขสิทธิ์ทุกประการ</span>
      <nav aria-label="นโยบาย">
        ${footer.policies.map((p) => `<a href="${p.url}">${esc(p.title)}</a>`).join('')}
      </nav>
    </div>
  </div>
</footer>`;
}

/**
 * Wraps page body HTML in the full document shell.
 * @param {{title:string, description:string, url:string, current?:string, body:string}} page
 */
function layout(page) {
  const title = page.title === 'Bwell' ? 'Bwell — สุขภาพดีในทุกมิติของชีวิต'
    : `${page.title} | Bwell`;
  const canonical = `https://bwell.co.th${page.url}`;

  return `<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(title)}</title>
<meta name="description" content="${esc(page.description)}">
<link rel="canonical" href="${canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Bwell">
<meta property="og:title" content="${esc(title)}">
<meta property="og:description" content="${esc(page.description)}">
<meta property="og:url" content="${canonical}">
<meta property="og:locale" content="th_TH">
<meta name="theme-color" content="#008ad0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;700&family=Poppins:wght@300;400;500;600;700&display=swap">
<link rel="stylesheet" href="/assets/css/bwell.css">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<script type="application/ld+json">
${JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: 'Bwell',
    url: 'https://bwell.co.th/',
    slogan: brand.taglineEn,
    foundingDate: String(brand.since),
    address: {
      '@type': 'PostalAddress',
      streetAddress: '46/14 ถนนเจริญราษฎร์ แขวงบางโคล่ เขตบางคอแหลม',
      addressLocality: 'กรุงเทพมหานคร',
      postalCode: '10120',
      addressCountry: 'TH',
    },
    telephone: '+66-2-294-3211',
  }, null, 2)}
</script>
${page.jsonld ? `<script type="application/ld+json">\n${JSON.stringify(page.jsonld, null, 2)}\n</script>` : ''}
</head>
<body>
<a class="sr-only" href="#main">ข้ามไปยังเนื้อหาหลัก</a>
${header(page.current || page.url)}
<main id="main">
${page.body}
</main>
${siteFooter()}
<script src="/assets/js/bwell.js" defer></script>
</body>
</html>
`;
}

module.exports = { layout, esc, mark, check, catUrl, catName };
