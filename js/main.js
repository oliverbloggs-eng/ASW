/* ASW Law Advocates LLP: shared behaviour. Vanilla JS, no dependencies. */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------- mobile menu ---------- */
  var burger = $('[data-menu-toggle]');
  var menu = $('#mobile-menu');
  if (burger && menu) {
    var OPEN = 'M6 6l12 12M18 6L6 18', SHUT = 'M4 7h16M4 12h16M4 17h16';
    var setMenu = function (open) {
      menu.hidden = !open;
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      var p = $('path', burger); if (p) p.setAttribute('d', open ? OPEN : SHUT);
    };
    burger.addEventListener('click', function () { setMenu(menu.hidden); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !menu.hidden) { setMenu(false); burger.focus(); } });
    $$('a', menu).forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    window.addEventListener('resize', function () { if (window.innerWidth > 1023 && !menu.hidden) setMenu(false); });
  }

  /* ---------- fade up on scroll ---------- */
  var fades = $$('.nv, .rv');
  if (reduce || !('IntersectionObserver' in window)) {
    fades.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    fades.forEach(function (el) { io.observe(el); });
  }

  /* ---------- accordions (About page rows) ---------- */
  $$('.ac-btn').forEach(function (btn) {
    var row = btn.closest('.ac');
    btn.addEventListener('click', function () {
      var open = !row.classList.contains('open');
      row.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });

  /* ---------- carousels: native scroll snap + counter + buttons ---------- */
  function carousel(track, count, opt) {
    if (!track) return;
    var root = opt.root || track.parentElement;
    var cur = $(opt.cur, root), fill = $(opt.fill, root);
    var btns = $$('.at-btn', root); var prev = btns[0], next = btns[1];
    var dots = opt.dots ? $$(opt.dots) : [];
    var idx = 0;
    var step = function () { return track.children[1].offsetLeft - track.children[0].offsetLeft; };
    var paint = function () {
      if (cur) cur.textContent = ('0' + (idx + 1)).slice(-2);
      if (fill) fill.className = 'at-fill ' + opt.fillPrefix + idx;
      [[prev, idx === 0], [next, idx === count - 1]].forEach(function (p) {
        if (!p[0]) return; p[0].classList.toggle('dis', p[1]); p[0].setAttribute('aria-disabled', p[1] ? 'true' : 'false');
      });
      if (opt.liClass) $$(':scope > li', track).forEach(function (li, i) { li.classList.toggle('on', i === idx); });
      dots.forEach(function (d, i) { d.setAttribute('aria-current', i === idx ? 'true' : 'false'); var s = $('.tm-dot', d); if (s) s.classList.toggle('on', i === idx); });
    };
    var go = function (i) {
      if (i < 0 || i > count - 1) return;
      track.scrollTo({ left: track.children[i].offsetLeft - track.children[0].offsetLeft, behavior: reduce ? 'auto' : 'smooth' });
    };
    track.addEventListener('scroll', function () {
      var i = Math.max(0, Math.min(count - 1, Math.round(track.scrollLeft / step())));
      if (i !== idx) { idx = i; paint(); }
    }, { passive: true });
    if (prev) prev.addEventListener('click', function () { go(idx - 1); });
    if (next) next.addEventListener('click', function () { go(idx + 1); });
    dots.forEach(function (d, i) { d.addEventListener('click', function () { go(i); }); });
    if (opt.liClass) $$(':scope > li', track).forEach(function (li) { li.classList.add('ta-l'); });
    paint();
  }
  var ar = $('#ar-track');
  if (ar) carousel(ar, 6, { root: ar.closest('section'), cur: '.at-cur', fill: '.at-fill', fillPrefix: 's' });
  var tm = $('#tm-track');
  if (tm && document.body.classList.contains('pg-home')) carousel(tm, 3, { root: tm.closest('section'), cur: '.at-cur', fill: '.at-fill', fillPrefix: 't', liClass: true });
  var tmm = $('#tm-m-track');
  if (tmm) carousel(tmm, 3, { root: tmm.closest('.m-only'), cur: '.at-cur', fill: '.at-fill', fillPrefix: 't', liClass: true });
  if (tm && document.body.classList.contains('pg-about')) carousel(tm, 3, { root: tm.closest('section'), cur: '.__none', fill: '.__none', fillPrefix: 't', dots: '.tm-dotb' });

  /* ---------- FAQ filter pills ---------- */
  var pills = $$('.fq-pill');
  if (pills.length) {
    var items = $$('.fq-i');
    pills.forEach(function (p) {
      p.addEventListener('click', function () {
        var f = p.getAttribute('data-filter');
        pills.forEach(function (q) { var on = q === p; q.classList.toggle('on', on); q.setAttribute('aria-pressed', on ? 'true' : 'false'); });
        items.forEach(function (li) { var show = f === 'all' || li.getAttribute('data-tag') === f; li.hidden = !show; li.style.display = show ? '' : 'none'; });
      });
    });
  }

  /* ---------- Areas page: sticky anchor bar with scroll tracking ---------- */
  var bar = $('.ab-list');
  if (bar) {
    var links = $$('.ab-pill', bar);
    var secs = links.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
    var setOn = function (i) {
      links.forEach(function (a, k) { a.classList.toggle('on', k === i); if (k === i) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current'); });
      var a = links[i], tr = $('#ab-track');
      if (tr && a && tr.scrollWidth > tr.clientWidth) tr.scrollTo({ left: a.offsetLeft - 20, behavior: reduce ? 'auto' : 'smooth' });
      if (bar.scrollWidth > bar.clientWidth) bar.scrollTo({ left: a.offsetLeft - 20, behavior: reduce ? 'auto' : 'smooth' });
    };
    var cur = 0, ticking = false;
    var onScroll = function () {
      ticking = false;
      var y = window.scrollY + 170, best = 0;
      secs.forEach(function (s, i) { if (s && s.offsetTop <= y) best = i; });
      if (best !== cur) { cur = best; setOn(best); }
    };
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
    links.forEach(function (a, i) { a.addEventListener('click', function () { cur = i; setOn(i); }); });
    secs.forEach(function (s) { if (s) s.style.scrollMarginTop = '150px'; });
  }

  /* ---------- About page: timeline scroll progress ---------- */
  var steps = $$('.pg-about .hw3-s, .pg-about .hw-m .ac');
  if (steps.length) {
    var mark = function () {
      var line = window.innerHeight * 0.62;
      steps.forEach(function (s, i) {
        if (!s.offsetParent) return;
        s.classList.toggle('reached', i % 4 === 0 || reduce || s.getBoundingClientRect().top < line);
      });
    };
    steps.forEach(function (s) { s.classList.add('reached'); });
    if (!reduce) { steps.forEach(function (s) { s.classList.remove('reached'); }); window.addEventListener('scroll', mark, { passive: true }); window.addEventListener('resize', mark); mark(); }
  }

  /* ---------- floating WhatsApp button ---------- */
  var wa = $('#wa');
  if (wa) {
    var isHome = document.body.classList.contains('pg-home');
    var hero = $('.h-hero');
    var guards = $$('.at-foot, .ta-foot, .mt-ctl');
    var seen = {};
    var upd = function () {
      var after = isHome && hero ? (hero.getBoundingClientRect().bottom < 0) : window.scrollY > 260;
      wa.classList.toggle('show', after);
    };
    window.addEventListener('scroll', upd, { passive: true }); upd();
    if ('IntersectionObserver' in window && guards.length) {
      var go = new IntersectionObserver(function (es) {
        es.forEach(function (e) { seen[guards.indexOf(e.target)] = e.isIntersecting; });
        var any = Object.keys(seen).some(function (k) { return seen[k]; });
        wa.classList.toggle('hide', any && window.innerWidth <= 640);
      });
      guards.forEach(function (g) { go.observe(g); });
    }
  }

  /* ---------- contact form ---------- */
  var form = $('#contact-form');
  if (form) {
    var fields = $$('.ct-f', form);
    var ok = $('#contact-ok');
    var errBox = document.createElement('p'); errBox.className = 'ct-formerr'; errBox.setAttribute('role', 'alert'); errBox.hidden = true;
    errBox.textContent = 'Sorry, your message could not be sent. Please try again or email info@aswlaw.africa.';
    form.insertBefore(errBox, form.querySelector('.ct-submit'));
    var valid = function (f) {
      var inp = $('.ct-in', f); if (!inp || !inp.required) return true;
      var v = inp.value.trim(); var ok1 = v !== '' && (inp.type !== 'email' || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v));
      f.classList.toggle('is-err', !ok1); inp.setAttribute('aria-invalid', ok1 ? 'false' : 'true');
      if (inp.id) { var e = $('#' + inp.id + '-e'); if (e) inp.setAttribute('aria-describedby', inp.id + '-e'); }
      return ok1;
    };
    fields.forEach(function (f) { var i = $('.ct-in', f); if (i) { i.addEventListener('blur', function () { if (i.value || f.classList.contains('is-err')) valid(f); }); i.addEventListener('input', function () { if (f.classList.contains('is-err')) valid(f); }); } });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var all = fields.map(valid); if (all.indexOf(false) > -1) { var bad = $('.is-err .ct-in', form); if (bad) bad.focus(); return; }
      if (form.elements._gotcha && form.elements._gotcha.value) return; /* honeypot */
      var btn = $('.ct-submit', form); btn.disabled = true; errBox.hidden = true;
      var show = function () { form.hidden = true; if (ok) { ok.hidden = false; ok.focus && ok.setAttribute('tabindex', '-1'); ok.focus(); } };
      var action = form.getAttribute('action') || '';
      if (/YOUR_FORM_ID/.test(action)) { show(); return; } /* placeholder endpoint: preview the success state */
      fetch(action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
        .then(function (r) { if (r.ok) show(); else throw new Error('bad'); })
        .catch(function () { btn.disabled = false; errBox.hidden = false; });
    });
  }
})();
