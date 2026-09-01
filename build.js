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

/**
 * Placeholder artwork for an image slot. Replace the generated file at the
 * same path with a real photo to swap it in — no markup change needed.
 */
function placeholderSvg(label) {
  const safe = String(label)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  // Wrap the caption so long Thai labels stay inside the frame.
  const words = safe.split(' ');
  const lines = [];
  let line = '';
  for (const w of words) {
    if ((line + ' ' + w).trim().length > 26) { lines.push(line.trim()); line = w; }
    else line = (line + ' ' + w).trim();
  }
  if (line) lines.push(line);
  const shown = lines.slice(0, 3);
  const startY = 330 - (shown.length - 1) * 15;

  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600" role="img" aria-label="${safe}">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#eef4f9"/><stop offset="100%" stop-color="#dbe8f4"/>
    </linearGradient>
  </defs>
  <rect width="800" height="600" fill="url(#g)"/>
  <g transform="translate(372 210)" opacity="0.5">
    <circle cx="14" cy="14" r="12" fill="#008ad0"/>
    <circle cx="42" cy="14" r="12" fill="none" stroke="#008ad0" stroke-width="5"/>
    <circle cx="14" cy="42" r="12" fill="none" stroke="#008ad0" stroke-width="5"/>
    <circle cx="42" cy="42" r="12" fill="#008ad0"/>
  </g>
  ${shown.map((t, i) => `<text x="400" y="${startY + i * 30}" text-anchor="middle" font-family="Kanit, Arial, sans-serif" font-size="21" fill="#5b7c96">${t}</text>`).join('\n  ')}
  <text x="400" y="${startY + shown.length * 30 + 16}" text-anchor="middle" font-family="Kanit, Arial, sans-serif" font-size="13" fill="#9db4c6" letter-spacing="1.5">IMAGE PLACEHOLDER</text>
</svg>`;
}

// Abstract full-bleed hero artwork. Replace assets/img/hero-bg.svg (or point the
// hero <img> at a .jpg) with a real product photograph before launch.
const HERO_BG = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" width="1600" height="900" preserveAspectRatio="xMidYMid slice">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0a4f80"/>
      <stop offset="55%" stop-color="#008ad0"/>
      <stop offset="100%" stop-color="#0d6ca8"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.68" cy="0.32" r="0.62">
      <stop offset="0%" stop-color="#7fd0ff" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#7fd0ff" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1600" height="900" fill="url(#sky)"/>
  <rect width="1600" height="900" fill="url(#glow)"/>
  <g fill="none" stroke="#ffffff" stroke-opacity="0.16" stroke-width="1.5">
    <circle cx="1120" cy="300" r="150"/><circle cx="1120" cy="300" r="240"/>
    <circle cx="1120" cy="300" r="340"/><circle cx="1120" cy="300" r="450"/>
  </g>
  <g fill="#ffffff" fill-opacity="0.07">
    <circle cx="300" cy="700" r="220"/><circle cx="150" cy="200" r="130"/>
  </g>
</svg>`;

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
fs.writeFileSync(path.join(imgDir, 'hero-bg.svg'), HERO_BG);
for (const { file, label } of C.media.registry) {
  fs.writeFileSync(path.join(imgDir, `${file}.svg`), placeholderSvg(label));
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

console.log(`Built ${pages.length} pages + 404, ${C.media.registry.length} image placeholders → dist/`);
for (const p of pages) console.log(`  ${p.url.padEnd(30)} ${p.title}`);
