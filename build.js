#!/usr/bin/env node
/**
 * Static site generator for bwell.co.th.
 * Renders every page in the approved site structure into dist/.
 * No dependencies — run with `node build.js`.
 */
'use strict';

const fs = require('fs');
const path = require('path');

const { layout, catUrl, catName } = require('./src/templates/layout');
const { categories, subPages } = require('./src/data/categories');
const policies = require('./src/data/policies');
const S = require('./src/data/site');
const C = require('./src/templates/components');
const home = require('./src/templates/home');
const category = require('./src/templates/category');
const P = require('./src/templates/pages');
const { mockupSvg } = require('./src/mockup');

const OUT = path.join(__dirname, 'dist');
const SITE = 'https://bwell.co.th';

function write(url, html) {
  const dir = url === '/' ? OUT : path.join(OUT, url.replace(/^\/|\/$/g, ''));
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'index.html'), html);
}

function copyDir(from, to) {
  fs.mkdirSync(to, { recursive: true });
  for (const entry of fs.readdirSync(from, { withFileTypes: true })) {
    const s = path.join(from, entry.name);
    const d = path.join(to, entry.name);
    if (entry.isDirectory()) copyDir(s, d);
    else fs.copyFileSync(s, d);
  }
}

const FAVICON = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 56 56">
  <circle cx="16" cy="16" r="13" fill="#008ad0"/>
  <circle cx="40" cy="16" r="13" fill="none" stroke="#008ad0" stroke-width="6"/>
  <circle cx="16" cy="40" r="13" fill="none" stroke="#008ad0" stroke-width="6"/>
  <circle cx="40" cy="40" r="13" fill="#008ad0"/>
</svg>`;

// ----------------------------------------------------------------- Build --

fs.rmSync(OUT, { recursive: true, force: true });
fs.mkdirSync(OUT, { recursive: true });

const pages = [];
const add = (page) => { pages.push(page); write(page.url, layout(page)); };

// Homepage + hub + editorial pages
add(home());
add(P.productHub());
add(P.aboutUs());
add(P.whyBwell());
add(P.ourClient());
add(P.distribution());
add(P.findBwell());
add(P.blog());
add(P.contact());

// Category pages (level 2)
for (const cat of categories) add(category(cat));

// Sub-category pages (level 3) reuse the parent's content with their own hero
for (const sub of subPages) {
  const parent = categories.find((c) => c.slug === sub.parent);
  add(category(parent, {
    title: sub.title,
    heroLead: sub.heroLead,
    url: `/${sub.slug}/`,
    products: sub.products,
    parent,
  }));
}

// Policy pages
for (const p of policies) add(P.policy({ ...p, url: `/${p.slug}/` }));

// Assets
copyDir(path.join(__dirname, 'src/assets'), path.join(OUT, 'assets'));

const imgDir = path.join(OUT, 'assets/img');
fs.mkdirSync(imgDir, { recursive: true });
fs.writeFileSync(path.join(imgDir, 'favicon.svg'), FAVICON);
for (const { file, label, theme } of C.media.registry) {
  fs.writeFileSync(path.join(imgDir, `${file}.svg`), mockupSvg(label, theme));
}

// sitemap.xml + robots.txt
const today = new Date().toISOString().slice(0, 10);
fs.writeFileSync(path.join(OUT, 'sitemap.xml'),
  `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${pages.map((p) => `  <url><loc>${SITE}${p.url}</loc><lastmod>${today}</lastmod>` +
    `<priority>${p.url === '/' ? '1.0' : p.url.split('/').length > 3 ? '0.6' : '0.8'}</priority></url>`).join('\n')}
</urlset>
`);
fs.writeFileSync(path.join(OUT, 'robots.txt'),
  `User-agent: *\nAllow: /\n\nSitemap: ${SITE}/sitemap.xml\n`);

// 404
write('/404', layout({
  title: 'ไม่พบหน้าที่คุณค้นหา',
  description: 'ไม่พบหน้าที่คุณค้นหาบนเว็บไซต์ Bwell',
  url: '/404/',
  body: `
  <section class="section bg-light" style="min-height:60vh;display:grid;place-items:center">
    <div class="wrap center">
      <p class="t-eyebrow">404</p>
      <h1 class="t-display">ไม่พบหน้าที่คุณค้นหา</h1>
      <p class="t-body" style="margin:16px auto 28px;max-width:460px">หน้านี้อาจถูกย้ายหรือลบไปแล้ว ลองกลับไปที่หน้าแรกหรือดูสินค้าทั้งหมดของเรา</p>
      <div class="cta-row center">
        <a class="btn btn-primary" href="/">กลับหน้าแรก</a>
        <a class="link-chevron" href="/product-bwell/">ดูสินค้าทั้งหมด</a>
      </div>
    </div>
  </section>`,
}));
fs.renameSync(path.join(OUT, '404/index.html'), path.join(OUT, '404.html'));
fs.rmdirSync(path.join(OUT, '404'));

console.log(`Built ${pages.length} pages + 404, ${C.media.registry.length} mockup images → dist/`);
for (const p of pages) console.log(`  ${p.url.padEnd(30)} ${p.title}`);
