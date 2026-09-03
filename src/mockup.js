/**
 * Mockup artwork for image slots that have no photograph yet.
 *
 * Draws an on-brand illustrated interior scene per product category — a room,
 * a product silhouette and a motif — so a page reads as a finished design in
 * review instead of a grid of grey boxes. Deliberately illustrative, never
 * photographic, and each frame carries a MOCKUP tag so it is never mistaken
 * for real photography.
 */
'use strict';

const BLUE = '#008ad0';
const NAVY = '#005d9d';
const INK = '#40566a';

const esc = (s) => String(s)
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

/* ----------------------------------------------------- product silhouettes */
/* Each returns SVG drawn in an 800x600 frame, standing on the floor at y=430. */

const tower = (x, w, h, r = 18) => `
  <rect x="${x}" y="${430 - h}" width="${w}" height="${h}" rx="${r}" fill="#ffffff"/>
  <rect x="${x}" y="${430 - h}" width="${w}" height="${h}" rx="${r}" fill="none" stroke="#cfdbe6" stroke-width="2"/>`;

const vent = (cx, cy, r) => `
  <circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="#dbe6ef" stroke-width="7"/>
  <circle cx="${cx}" cy="${cy}" r="${r * 0.45}" fill="${BLUE}" opacity="0.16"/>`;

const grille = (x, y, w, h, rows) => Array.from({ length: rows }, (_, i) =>
  `<rect x="${x}" y="${y + i * (h / rows)}" width="${w}" height="${h / rows * 0.45}" rx="3" fill="#e3edf5"/>`
).join('');

const shapes = {
  air: () => `${tower(470, 150, 250)}${vent(545, 250, 46)}${grille(492, 330, 106, 70, 5)}`,

  filter: () => `
    ${[0, 1, 2].map((i) => `
    <g transform="translate(${430 + i * 62} ${250 + i * 14})">
      <rect width="120" height="170" rx="10" fill="#ffffff" stroke="#cfdbe6" stroke-width="2"/>
      ${Array.from({ length: 9 }, (_, k) => `<path d="M8 ${18 + k * 17} h104" stroke="#dfeaf3" stroke-width="6" stroke-linecap="round"/>`).join('')}
    </g>`).join('')}`,

  hair: () => `
    <g transform="translate(430 190) rotate(18)">
      <rect width="46" height="190" rx="22" fill="#ffffff" stroke="#cfdbe6" stroke-width="2"/>
      <rect x="6" y="16" width="34" height="80" rx="17" fill="${BLUE}" opacity="0.14"/>
      <circle cx="23" cy="150" r="9" fill="#dbe6ef"/>
    </g>
    <g transform="translate(560 235)">
      <rect width="40" height="150" rx="20" fill="#ffffff" stroke="#cfdbe6" stroke-width="2"/>
      <circle cx="20" cy="26" r="13" fill="#e3edf5"/>
    </g>`,

  chair: () => `
    <rect x="492" y="150" width="84" height="42" rx="16" fill="#eef4f9" stroke="#cfdbe6" stroke-width="2"/>
    <rect x="478" y="198" width="112" height="112" rx="20" fill="#ffffff" stroke="#cfdbe6" stroke-width="2"/>
    ${Array.from({ length: 4 }, (_, i) => `<path d="M${500 + i * 23} 212 v84" stroke="#e3edf5" stroke-width="4"/>`).join('')}
    <rect x="452" y="240" width="26" height="12" rx="6" fill="#dbe6ef"/>
    <rect x="590" y="240" width="26" height="12" rx="6" fill="#dbe6ef"/>
    <rect x="464" y="312" width="140" height="26" rx="12" fill="#eef4f9" stroke="#cfdbe6" stroke-width="2"/>
    <rect x="526" y="338" width="16" height="50" fill="#dbe6ef"/>
    <path d="M472 424 L534 388 L596 424" fill="none" stroke="#cfdbe6" stroke-width="9" stroke-linecap="round"/>
    <circle cx="472" cy="428" r="9" fill="#dbe6ef"/><circle cx="596" cy="428" r="9" fill="#dbe6ef"/>`,

  cushion: () => `
    <path d="M430 400 q-14-92 78-92 q92 0 78 92 z" fill="#ffffff" stroke="#cfdbe6" stroke-width="2"/>
    <path d="M452 372 q56-26 112 0" fill="none" stroke="#dfeaf3" stroke-width="6" stroke-linecap="round"/>
    <rect x="556" y="352" width="132" height="50" rx="24" fill="#eef4f9" stroke="#cfdbe6" stroke-width="2"/>`,

  heater: () => `
    ${tower(462, 128, 176, 16)}
    <circle cx="526" cy="330" r="20" fill="none" stroke="#dbe6ef" stroke-width="6"/>
    <path d="M620 262 h44 v104" fill="none" stroke="#cfdbe6" stroke-width="5"/>
    <ellipse cx="664" cy="372" rx="22" ry="9" fill="#eef4f9" stroke="#cfdbe6" stroke-width="2"/>
    ${[0, 1, 2].map((i) => `<circle cx="${652 + i * 12}" cy="${396 + (i % 2) * 16}" r="4" fill="${BLUE}" opacity="0.3"/>`).join('')}`,

  water: () => `
    ${tower(468, 116, 190, 14)}
    <circle cx="500" cy="300" r="15" fill="none" stroke="#dbe6ef" stroke-width="5"/>
    <circle cx="552" cy="300" r="15" fill="none" stroke="#dbe6ef" stroke-width="5"/>
    <path d="M626 240 v78 q0 22 22 22 h14" fill="none" stroke="#cfdbe6" stroke-width="7" stroke-linecap="round"/>
    ${[0, 1, 2].map((i) => `<path d="M664 ${356 + i * 26} q6 9 0 14 q-6-5 0-14z" fill="${BLUE}" opacity="${0.35 - i * 0.08}"/>`).join('')}`,

  dehum: () => `
    ${tower(468, 140, 214, 16)}
    ${grille(492, 264, 92, 66, 4)}
    <rect x="492" y="352" width="92" height="46" rx="8" fill="#eef4f9" stroke="#cfdbe6" stroke-width="2"/>
    <circle cx="486" cy="434" r="8" fill="#dbe6ef"/><circle cx="590" cy="434" r="8" fill="#dbe6ef"/>
    ${[0, 1, 2, 3].map((i) => `<path d="M${628 + i * 22} ${232 + (i % 2) * 30} q7 11 0 17 q-7-6 0-17z" fill="${BLUE}" opacity="0.28"/>`).join('')}`,

  ac: () => `
    ${tower(462, 136, 196, 14)}
    ${grille(486, 258, 88, 64, 4)}
    <rect x="486" y="344" width="88" height="34" rx="7" fill="#eef4f9" stroke="#cfdbe6" stroke-width="2"/>
    <path d="M598 280 q70-6 70-76" fill="none" stroke="#dbe6ef" stroke-width="16" stroke-linecap="round"/>
    <circle cx="480" cy="434" r="8" fill="#dbe6ef"/><circle cx="556" cy="434" r="8" fill="#dbe6ef"/>`,

  vacuum: () => `
    <g transform="translate(506 168) rotate(9)">
      <rect x="18" y="0" width="26" height="196" rx="13" fill="#ffffff" stroke="#cfdbe6" stroke-width="2"/>
      <rect x="-6" y="-4" width="74" height="52" rx="20" fill="#eef4f9" stroke="#cfdbe6" stroke-width="2"/>
      <circle cx="31" cy="22" r="11" fill="${BLUE}" opacity="0.18"/>
    </g>
    <rect x="470" y="384" width="150" height="34" rx="14" fill="#ffffff" stroke="#cfdbe6" stroke-width="2"/>
    <path d="M486 402 h118" stroke="#dfeaf3" stroke-width="7" stroke-linecap="round"/>`,

  robot: () => `
    <ellipse cx="540" cy="396" rx="112" ry="40" fill="#ffffff" stroke="#cfdbe6" stroke-width="2"/>
    <ellipse cx="540" cy="384" rx="112" ry="40" fill="#f5f9fc" stroke="#cfdbe6" stroke-width="2"/>
    <ellipse cx="540" cy="372" rx="30" ry="12" fill="#e3edf5"/>
    <circle cx="500" cy="386" r="6" fill="${BLUE}" opacity="0.4"/>`,

  fitness: () => `
    <g transform="translate(452 330)">
      <rect x="0" y="14" width="34" height="52" rx="10" fill="#eef4f9" stroke="#cfdbe6" stroke-width="2"/>
      <rect x="34" y="32" width="96" height="16" rx="8" fill="#ffffff" stroke="#cfdbe6" stroke-width="2"/>
      <rect x="130" y="14" width="34" height="52" rx="10" fill="#eef4f9" stroke="#cfdbe6" stroke-width="2"/>
    </g>
    <g transform="translate(624 306)">
      <rect width="52" height="124" rx="26" fill="#ffffff" stroke="#cfdbe6" stroke-width="2"/>
      <ellipse cx="26" cy="14" rx="26" ry="11" fill="#e3edf5"/>
    </g>`,
};

/* -------------------------------------------------------------- motifs */

const airflow = (o = 0.3) => Array.from({ length: 4 }, (_, i) =>
  `<path d="M${180 + i * 12} ${208 + i * 42} q120-56 250-18" fill="none" stroke="${BLUE}"
     stroke-width="${5 - i * 0.6}" stroke-linecap="round" opacity="${o - i * 0.05}"/>`
).join('');

const motes = (n, o = 0.35) => Array.from({ length: n }, (_, i) => {
  const x = 130 + ((i * 97) % 560);
  const y = 170 + ((i * 143) % 240);
  return `<circle cx="${x}" cy="${y}" r="${2 + (i % 3)}" fill="${NAVY}" opacity="${o - (i % 4) * 0.05}"/>`;
}).join('');

const motifs = {
  air: () => airflow(0.34) + motes(14, 0.28),
  filter: () => airflow(0.26),
  dehum: () => airflow(0.22) + motes(10, 0.3),
  ac: () => airflow(0.3),
  vacuum: () => motes(16, 0.32),
  robot: () => motes(18, 0.34),
  water: () => airflow(0.16),
  heater: () => airflow(0.18),
  hair: () => airflow(0.2),
  chair: () => '',
  cushion: () => '',
  fitness: () => '',
};

/* Map a category slug onto a scene. */
const THEME = {
  'air-purifier-bwell': 'air',
  'pm25-air-purifier': 'air',
  'air-purifier': 'air',
  'portable-air-purifiers': 'air',
  'air-purification-filters': 'filter',
  'hair-styling-tools': 'hair',
  'hair-straightener': 'hair',
  'hair-curler': 'hair',
  'electric-hair-brush': 'hair',
  'hair-dryer': 'hair',
  'bwell-ergonomic-chair': 'chair',
  'ergonomic-cushion-bwell': 'cushion',
  'water-heater-bwell': 'heater',
  'water-purifier': 'water',
  'air-dehumidifier': 'dehum',
  'portable-air-conditioner': 'ac',
  'vacuum-cleaner': 'vacuum',
  'robot-vacuum': 'robot',
  'sport-gadgets': 'fitness',
};

/** Wrap a caption to fit the chip, Thai included (no spaces to break on). */
function wrap(text, max) {
  const out = [];
  let line = '';
  for (const ch of text) {
    if (line.length >= max && (ch === ' ' || line.length >= max + 8)) { out.push(line.trim()); line = ''; }
    line += ch;
  }
  if (line.trim()) out.push(line.trim());
  return out.slice(0, 2);
}

function mockupSvg(label, theme) {
  const key = THEME[theme] || 'air';
  const scene = (shapes[key] || shapes.air)();
  const motif = (motifs[key] || (() => ''))();
  const lines = wrap(String(label), 30);

  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600" role="img" aria-label="${esc(label)}">
  <defs>
    <linearGradient id="wall" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f7fbfe"/><stop offset="100%" stop-color="#e4eef6"/>
    </linearGradient>
    <linearGradient id="floor" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#dde8f1"/><stop offset="100%" stop-color="#ccdae6"/>
    </linearGradient>
    <linearGradient id="shaft" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <rect width="800" height="600" fill="url(#wall)"/>
  <rect y="430" width="800" height="170" fill="url(#floor)"/>

  <!-- window and light -->
  <rect x="64" y="86" width="212" height="264" rx="10" fill="#ffffff" opacity="0.72"/>
  <path d="M170 86 v264 M64 218 h212" stroke="#d5e3ee" stroke-width="4"/>
  <rect x="64" y="86" width="212" height="264" rx="10" fill="none" stroke="#cfdbe6" stroke-width="3"/>
  <path d="M276 120 L640 430 L276 430 z" fill="url(#shaft)" opacity="0.6"/>

  ${motif}
  ${scene}

  <!-- product shadow -->
  <ellipse cx="540" cy="436" rx="120" ry="14" fill="#9db4c6" opacity="0.28"/>

  <!-- caption -->
  <g transform="translate(48 ${lines.length > 1 ? 470 : 486})">
    <rect width="${Math.min(660, 26 + lines[0].length * 12)}" height="${lines.length > 1 ? 76 : 46}"
          rx="12" fill="#ffffff" opacity="0.92"/>
    ${lines.map((t, i) => `<text x="16" y="${30 + i * 28}" font-family="Kanit, Arial, sans-serif" font-size="19" fill="${INK}">${esc(t)}</text>`).join('\n    ')}
  </g>
  <text x="752" y="566" text-anchor="end" font-family="Kanit, Arial, sans-serif"
        font-size="12" fill="#8aa4ba" letter-spacing="2.5">MOCKUP</text>
</svg>`;
}

module.exports = { mockupSvg, THEME };
