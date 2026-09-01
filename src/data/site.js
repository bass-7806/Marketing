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
  { title: 'HEPA Filter คืออะไร? สำคัญแค่ไหนในเครื่องฟอกอากาศ', slug: 'hepa-filter', tag: 'เครื่องฟอกอากาศ' },
  { title: 'เลือกซื้อเครื่องดูดฝุ่นแบบไหนดี ต้องดูอะไรบ้าง', slug: 'choose-vacuum', tag: 'เครื่องดูดฝุ่น' },
  { title: 'เปรียบเทียบชนิดถังของเครื่องดูดฝุ่น แบบไหนเหมาะกับบ้านคุณ', slug: 'vacuum-bin-types', tag: 'เครื่องดูดฝุ่น' },
  { title: 'เครื่องดูดฝุ่นไร้สายเหมาะกับใคร?', slug: 'cordless-vacuum-for-who', tag: 'เครื่องดูดฝุ่น' },
  { title: 'PM2.5 อันตรายแค่ไหน และป้องกันในบ้านได้อย่างไร', slug: 'pm25-guide', tag: 'สุขภาพ' },
  { title: 'ออฟฟิศซินโดรม แก้ได้ด้วยการนั่งที่ถูกต้อง', slug: 'office-syndrome', tag: 'เก้าอี้เพื่อสุขภาพ' },
];

// Homepage "สินค้าแนะนำ"
const featuredProducts = [
  { title: 'เครื่องฟอกอากาศ PM2.5 รุ่น AP-N15365', price: '฿6,990', img: 'product-ap-n15365' },
  { title: 'เครื่องลดความชื้นแบบพกพา รุ่น G9', price: '฿4,990', img: 'product-g9' },
  { title: 'เครื่องฟอกอากาศ PM2.5 รุ่น AP-M22195', price: '฿9,990', img: 'product-ap-m22195' },
  { title: 'Bwell เก้าอี้ Ergonomic รุ่น Stella Ilon', price: '฿7,990', img: 'product-stella-ilon' },
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
