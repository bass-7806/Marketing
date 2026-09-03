// Global site data: brand, navigation, contact and shared content blocks.

const brand = {
  name: 'Bwell',
  domain: 'bwell.co.th',
  shop: 'https://shop.bwell.co.th',
  taglineTh: 'เรามอบประสบการณ์แบรนด์ที่ดีที่สุดให้แก่คุณ',
  taglineEn: 'We Deliver The Top Brand Experiences.',
  positioning: 'สุขภาพดีในทุกมิติของชีวิต',
  since: 2011,
};

// Primary navigation — mirrors the approved site structure (3 levels deep).
const nav = [
  { title: 'Home', url: '/' },
  {
    title: 'About us',
    url: '/about-us/',
    children: [
      { title: 'ทำไมต้อง Bwell', url: '/why-bwell/' },
      { title: 'ลูกค้าของเรา', url: '/our-client/' },
    ],
  },
  { title: 'Product', url: '/product-bwell/', mega: true },
  { title: 'ช่องทางจัดจำหน่าย', url: '/distribution-channels/' },
  { title: 'บทความ', url: '/blog/' },
  { title: 'ติดต่อเรา', url: '/contact/' },
];

const contact = {
  showroom: {
    label: 'Bwell Showroom',
    address: '46/14 ถนนเจริญราษฎร์ แขวงบางโคล่ เขตบางคอแหลม กรุงเทพฯ 10120',
    phone: '02-294-3211',
    hours: 'จันทร์ – เสาร์ 08.30 – 17.30 น.',
  },
  flagship: {
    label: 'Bwell Flagship Store',
    address: 'ชั้น 1 โซน K1 ศูนย์การค้า CDC (ตรงข้าม KBANK) ถ.ประดิษฐ์มนูธรรม แขวงคลองจั่น เขตบางกะปิ กรุงเทพฯ',
    phone: '02-100-5075',
    hours: 'จันทร์ – อาทิตย์ 10.00 – 20.00 น.',
  },
  line: 'https://lin.ee/xULzTdA',
};

const offlinePartners = ['Emporium', 'Paragon', 'Samitivej', 'Bangkok Hospital', 'The Mall'];

const onlinePartners = [
  { name: 'Lazada', url: 'https://www.lazada.co.th/shop/bwell' },
  { name: 'Shopee', url: 'https://shopee.co.th/bwell_officialstore' },
  { name: 'NocNoc', url: 'https://nocnoc.com/' },
];

const clients = ['กระทรวงสาธารณสุข', 'Goethe Institut', 'Samitivej', 'Bangkok Hospital'];

const reviews = [
  { name: 'Patcharin', text: 'เครื่องดีมาก ใช้มา 2 เดือนแล้ว อากาศในห้องสะอาดขึ้นชัดเจน' },
  { name: 'Manunya', text: 'สั่งซื้อง่าย จัดส่งไว บริการหลังการขายดีมากค่ะ' },
  { name: 'Suppawut', text: 'เครื่องฟอกอากาศ PM2.5 ตัวนี้ทำงานเงียบ ใช้ในห้องนอนได้สบาย' },
  { name: 'Pattaraa', text: 'คุณภาพดีเกินราคา ใช้แล้วประทับใจมากครับ' },
];

const blogPosts = [
  { title: 'HEPA Filter คืออะไร? สำคัญแค่ไหนในเครื่องฟอกอากาศ',
    tag: 'เครื่องฟอกอากาศ', img: 'blog-hepa-filter.webp' },
  { title: 'เลือกซื้อเครื่องดูดฝุ่นต้องดูอะไรบ้าง? เคล็ดลับเลือกให้เหมาะกับบ้านและไลฟ์สไตล์ของคุณ',
    tag: 'เครื่องดูดฝุ่นไร้สาย', img: 'blog-choose-vacuum.webp' },
  { title: 'เปรียบเทียบข้อดีข้อเสียของหุ่นยนต์ดูดฝุ่น vs เครื่องดูดฝุ่นทั่วไป แบบไหนคุ้มค่ากว่ากัน?',
    tag: 'หุ่นยนต์ดูดฝุ่น', img: 'blog-robot-vs-stick.webp' },
  { title: 'เครื่องดูดฝุ่นไร้สายเหมาะกับใคร? ข้อดี-ข้อเสียที่ควรรู้ก่อนซื้อ',
    tag: 'เครื่องดูดฝุ่นไร้สาย', img: 'blog-cordless-vacuum.webp' },
  { title: 'ข้อแนะนำการเลือกเครื่องกรองน้ำสำหรับบ้านและคอนโดมิเนียม เลือกให้เหมาะกับที่อยู่อาศัย',
    tag: 'เครื่องกรองน้ำ', img: 'blog-water-purifier.webp' },
];

// Homepage "สินค้าแนะนำ"
// Names, prices and images taken from the live bwell.co.th homepage.
const featuredProducts = [
  { title: 'เครื่องฟอกอากาศ PM2.5 รุ่น AP-M1536S', was: '฿6,990', price: '฿3,990', img: 'prod-ap-m1536s.webp' },
  { title: 'เครื่องฟอกอากาศ PM2.5 รุ่น AP-H2219S', was: '฿9,990', price: '฿6,990', img: 'prod-ap-h2219s.webp' },
  { title: 'เครื่องฟอกอากาศในรถยนต์ รุ่น G9', price: '฿4,990', img: 'prod-g9.webp' },
  { title: 'Bwell เก้าอี้ Ergonomic รุ่น Stella สีเทา', price: '฿7,990', img: 'prod-stella.webp' },
];

const footer = {
  pages: [
    { title: 'เกี่ยวกับ Bwell', url: '/about-us/' },
    { title: 'ทำไมต้อง Bwell', url: '/why-bwell/' },
    { title: 'ลูกค้าของเรา', url: '/our-client/' },
    { title: 'บทความ', url: '/blog/' },
    { title: 'ช่องทางจัดจำหน่าย', url: '/distribution-channels/' },
    { title: 'ค้นหาสาขาของ Bwell', url: '/findbwell/' },
    { title: 'ติดต่อเรา', url: '/contact/' },
  ],
  policies: [
    { title: 'นโยบายความเป็นส่วนตัว', url: '/privacy-policy/' },
    { title: 'นโยบายการใช้คุกกี้', url: '/cookies-policy/' },
    { title: 'นโยบายการจัดส่งสินค้า', url: '/shipping-policy/' },
    { title: 'นโยบายคืนเงินและรับประกันสินค้า', url: '/warranty-policy/' },
  ],
};

module.exports = {
  brand, nav, contact, offlinePartners, onlinePartners,
  clients, reviews, blogPosts, featuredProducts, footer,
};
