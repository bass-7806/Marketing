/* Bwell — progressive enhancement only. The site is fully readable without JS. */
(function () {
  'use strict';

  // Mobile menu ------------------------------------------------------------
  var toggle = document.querySelector('.nav-toggle');
  var menu = document.getElementById('mobile-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      menu.classList.toggle('open', !open);
      document.body.style.overflow = !open ? 'hidden' : '';
    });
    menu.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        toggle.setAttribute('aria-expanded', 'false');
        menu.classList.remove('open');
        document.body.style.overflow = '';
      }
    });
  }

  // Collapsible SEO copy ---------------------------------------------------
  document.querySelectorAll('.seo-toggle').forEach(function (btn) {
    var body = document.getElementById(btn.getAttribute('aria-controls'));
    if (!body) return;
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
      body.classList.toggle('open', !open);
      btn.firstChild.nodeValue = !open ? 'แสดงน้อยลง ' : 'อ่านเพิ่มเติม ';
    });
  });

  // Scroll reveal ----------------------------------------------------------
  var targets = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window) ||
      window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    targets.forEach(function (el) { el.classList.add('in'); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        io.unobserve(entry.target);
      }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
  targets.forEach(function (el) { io.observe(el); });
})();
