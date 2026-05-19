(() => {
  const hexCanvas = document.getElementById('hexBg');
  if (hexCanvas) {
    const ctx = hexCanvas.getContext('2d');
    let fadeTick = 0;
    const HEX_MIN_OPACITY = 0.08;
    const HEX_MAX_OPACITY = 0.15;

    const resizeHexCanvas = () => {
      hexCanvas.width = window.innerWidth;
      hexCanvas.height = window.innerHeight;
      drawHexGrid();
    };

    const drawHexGrid = () => {
      if (!ctx) return;
      const w = hexCanvas.width;
      const h = hexCanvas.height;
      ctx.clearRect(0, 0, w, h);
      const size = 36;
      const hexW = size * 2;
      const hexH = Math.sqrt(3) * size;
      const cols = Math.ceil(w / (hexW * 0.75)) + 2;
      const rows = Math.ceil(h / hexH) + 2;
      const opacity = HEX_MIN_OPACITY +
        (HEX_MAX_OPACITY - HEX_MIN_OPACITY) * ((Math.sin(fadeTick) + 1) / 2);
      ctx.strokeStyle = `rgba(232,234,237,${opacity.toFixed(3)})`;
      ctx.lineWidth = 0.8;
      for (let row = -1; row < rows; row += 1) {
        for (let col = -1; col < cols; col += 1) {
          const x = col * hexW * 0.75;
          const y = row * hexH + (col % 2 === 0 ? 0 : hexH / 2);
          ctx.beginPath();
          for (let i = 0; i < 6; i += 1) {
            const angle = (Math.PI / 180) * (60 * i - 30);
            const px = x + size * Math.cos(angle);
            const py = y + size * Math.sin(angle);
            if (i === 0) ctx.moveTo(px, py);
            else ctx.lineTo(px, py);
          }
          ctx.closePath();
          ctx.stroke();
        }
      }
    };

    const animateHexGrid = () => {
      fadeTick += 0.012;
      drawHexGrid();
      window.requestAnimationFrame(animateHexGrid);
    };

    window.addEventListener('resize', resizeHexCanvas);
    resizeHexCanvas();
    animateHexGrid();
  }

  const CONTACT_EMAIL = 'axis-scaffolding@outlook.com';
  const header = document.getElementById('site-header');
  const menuToggle = document.getElementById('menu-toggle');
  const siteMenu = document.getElementById('site-menu');
  const setHeaderState = () => {
    if (!header) return;
    header.classList.toggle('scrolled', window.scrollY > 12);
  };
  const currentHost = window.location.hostname.toLowerCase();
  const OLD_HOSTS = ['axisscaffolding.co.uk', 'www.axisscaffolding.co.uk'];
  const NEW_HOST  = 'axisscaffoldingessex.co.uk';
  if (OLD_HOSTS.includes(currentHost)) {
    const nextUrl = 'https://' + NEW_HOST +
      window.location.pathname +
      window.location.search +
      window.location.hash;
    const moveBanner = document.getElementById('domain-move-banner');
    const canonicalTag = document.querySelector('link[rel="canonical"]');
    if (canonicalTag) canonicalTag.setAttribute('href', nextUrl);
    if (moveBanner) moveBanner.hidden = false;
    window.setTimeout(function() {
      window.location.replace(nextUrl);
    }, 1500);
  }
  setHeaderState();
  window.addEventListener('scroll', setHeaderState, { passive: true });
  if (menuToggle && siteMenu) {
    menuToggle.addEventListener('click', () => {
      const open = siteMenu.classList.toggle('open');
      menuToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  document.querySelectorAll('.faq-question').forEach((button) => {
    button.addEventListener('click', () => {
      document.querySelectorAll('.faq-question').forEach((item) => {
        const panel = document.getElementById(item.getAttribute('aria-controls'));
        const open = item === button && item.getAttribute('aria-expanded') !== 'true';
        item.setAttribute('aria-expanded', open ? 'true' : 'false');
        if (panel) panel.style.display = open ? 'block' : 'none';
      });
    });
  });

  const track    = document.getElementById('testimonial-track');
  const carousel = document.getElementById('testimonial-carousel');
  const prevBtn  = document.getElementById('carousel-prev');
  const nextBtn  = document.getElementById('carousel-next');
  const dotsWrap = document.getElementById('carousel-dots');
  let idx   = 0;
  let timer = null;

  const total = () => track ? track.children.length : 0;

  const buildDots = () => {
    if (!dotsWrap || !track) return;
    dotsWrap.innerHTML = '';
    Array.from(track.children).forEach((_, i) => {
      const d = document.createElement('button');
      d.className = 'carousel-dot' + (i === 0 ? ' active' : '');
      d.setAttribute('aria-label', 'Go to review ' + (i + 1));
      d.addEventListener('click', () => { goTo(i); resetTimer(); });
      dotsWrap.appendChild(d);
    });
  };

  const updateDots = () => {
    if (!dotsWrap) return;
    dotsWrap.querySelectorAll('.carousel-dot').forEach((d, i) => {
      d.classList.toggle('active', i === idx);
    });
  };

  const goTo = (n) => {
    if (!track || total() === 0) return;
    idx = (n + total()) % total();
    track.style.transform = `translateX(-${idx * 100}%)`;
    updateDots();
  };

  const next = () => goTo(idx + 1);
  const prev = () => goTo(idx - 1);

  const resetTimer = () => {
    clearInterval(timer);
    if (total() > 1) timer = setInterval(next, 4500);
  };

  const start = () => {
    if (!track || total() <= 1) return;
    timer = setInterval(next, 4500);
  };

  const stop = () => { clearInterval(timer); timer = null; };

  if (nextBtn) nextBtn.addEventListener('click', () => { next(); resetTimer(); });
  if (prevBtn) prevBtn.addEventListener('click', () => { prev(); resetTimer(); });

  if (carousel) {
    carousel.addEventListener('mouseenter', stop);
    carousel.addEventListener('mouseleave', start);
  }

  buildDots();
  start();

  const CONSENT_KEY = 'axis_cookie_consent';
  var bar = document.getElementById('axis-cookie-bar');
  function showBar() {
    if (bar) bar.style.display = 'flex';
  }
  function hideBar() {
    if (bar) bar.style.display = 'none';
  }
  function setConsent(value) {
    localStorage.setItem(CONSENT_KEY, value);
    hideBar();
  }
  if (!localStorage.getItem(CONSENT_KEY)) {
    showBar();
  }
  var acceptBtn = document.getElementById('axis-cookie-accept');
  if (acceptBtn) {
    acceptBtn.addEventListener('click', function() {
      setConsent('accepted');
    });
  }
  var rejectBtn = document.getElementById('axis-cookie-reject');
  if (rejectBtn) {
    rejectBtn.addEventListener('click', function() {
      setConsent('rejected');
    });
  }
  var manageBtn = document.getElementById('axis-cookie-manage');
  if (manageBtn) {
    manageBtn.addEventListener('click', function() {
      var existing = document.getElementById('axis-cookie-prefs');
      if (existing) { existing.remove(); return; }
      var panel = document.createElement('div');
      panel.id = 'axis-cookie-prefs';
      panel.style.cssText = 'position:fixed;bottom:80px;left:0;right:0;z-index:99998;' +
        'background:rgba(15,15,15,0.97);border-top:1px solid rgba(255,255,255,0.1);' +
        'padding:1.5rem 2rem;font-family:Inter,sans-serif;color:#d1d5db;font-size:0.875rem;';
      panel.innerHTML = '<p style="color:#fff;font-weight:600;margin:0 0 1rem;">Cookie Preferences</p>' +
        '<div style="display:flex;flex-direction:column;gap:0.75rem;">' +
        '<label style="display:flex;justify-content:space-between;align-items:center;">' +
        '<span>Necessary <span style="color:#6b7280;font-size:0.75rem;">(always on)</span></span>' +
        '<input type="checkbox" checked disabled></label>' +
        '<label style="display:flex;justify-content:space-between;align-items:center;">' +
        '<span>Analytics</span><input type="checkbox" id="axis-pref-analytics"></label>' +
        '<label style="display:flex;justify-content:space-between;align-items:center;">' +
        '<span>Marketing</span><input type="checkbox" id="axis-pref-marketing"></label>' +
        '</div>' +
        '<button id="axis-pref-save" style="margin-top:1rem;background:#f97316;color:#000;' +
        'border:none;border-radius:9999px;padding:0.5rem 1.5rem;font-weight:700;cursor:pointer;">' +
        'Save Preferences</button>';
      document.body.appendChild(panel);
      var save = document.getElementById('axis-pref-save');
      if (save) {
        save.addEventListener('click', function() {
          panel.remove();
          setConsent('custom');
        });
      }
    });
  }
  var footerBtn = document.getElementById('axis-footer-cookie-btn');
  if (footerBtn) {
    footerBtn.addEventListener('click', function() {
      localStorage.removeItem(CONSENT_KEY);
      showBar();
    });
  }

  document.querySelectorAll('.axis-quote-form').forEach((form) => {
    form.addEventListener('submit', async (event) => {
      const webhook = window.AXIS_QUOTE_WEBHOOK;
      if (!webhook) return;
      event.preventDefault();
      const message = form.querySelector('.form-message');
      const data = Object.fromEntries(new FormData(form).entries());
      const payload = { ...data, notification_email: CONTACT_EMAIL };
      let ok = true;
      try {
        const res = await fetch(webhook, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
        });
        ok = res.ok;
      } catch (_err) {
        ok = false;
      }
      if (message) {
        message.textContent = ok
          ? 'Thanks. Your quote request has been received. We will respond within 24 hours.'
          : 'Thanks. Your request is saved locally. Please call 01702 820468 while webhook setup is pending.';
      }
      form.reset();
    });
  });
})();

// ── INSTANT MOUSE GLOW ───────────────────
(function() {
  if (window.matchMedia('(hover: none)').matches) return;
  if (window.matchMedia('(max-width: 768px)').matches) return;
  var glow = document.getElementById('mouse-glow');
  if (!glow) return;
  document.addEventListener('mousemove', function(e) {
    glow.style.left = e.clientX + 'px';
    glow.style.top  = e.clientY + 'px';
  }, { passive: true });
  document.addEventListener('mouseleave', function() {
    glow.style.opacity = '0';
  });
  document.addEventListener('mouseenter', function() {
    glow.style.opacity = '1';
  });
})();
// ── END MOUSE GLOW ───────────────────────

// ── PARALLAX BANNER ───────────────────────
(function() {
  var bannerBg = document.querySelector('.parallax-banner-bg');
  if (!bannerBg) return;
  if (window.matchMedia('(max-width: 768px)').matches) return;
  var banner = bannerBg.closest('.parallax-banner');
  var isVisible = false;
  var observer = new IntersectionObserver(function(entries) {
    isVisible = entries[0].isIntersecting;
  }, { threshold: 0.01 });
  observer.observe(banner);
  window.addEventListener('scroll', function() {
    if (!isVisible) return;
    var rect = banner.getBoundingClientRect();
    var offset = rect.top * 0.35;
    bannerBg.style.transform = 'translateY(' + offset + 'px)';
  }, { passive: true });
})();
// ── END PARALLAX BANNER ───────────────────



// ── SERVICES HERO PARALLAX ───────────────
(function() {
  var bg = document.querySelector('.services-hero-bg');
  if (!bg) return;
  if (window.matchMedia('(max-width: 768px)').matches) return;
  var hero = bg.closest('.services-hero');
  var visible = false;
  var obs = new IntersectionObserver(function(e) {
    visible = e[0].isIntersecting;
  }, { threshold: 0.01 });
  obs.observe(hero);
  window.addEventListener('scroll', function() {
    if (!visible) return;
    var rect = hero.getBoundingClientRect();
    bg.style.transform = 'translateY(' + (rect.top * 0.3) + 'px)';
  }, { passive: true });
})();
// ── END SERVICES HERO PARALLAX ───────────

// ── HERO PARALLAX ─────────────────────────
(function() {
  var heroMedia = document.querySelector('.hero-media');
  if (!heroMedia) return;
  if (window.matchMedia('(max-width: 768px)').matches) return;
  heroMedia.style.top    = '-20%';
  heroMedia.style.height = '140%';
  window.addEventListener('scroll', function() {
    heroMedia.style.transform = 'translateY(' + (window.scrollY * 0.4) + 'px)';
  }, { passive: true });
})();

// ── STEPPED SECTION PARALLAX ──────────────
(function() {
  if (window.matchMedia('(max-width: 768px)').matches) return;
  var bgs = document.querySelectorAll('.stepped-media-bg');
  if (!bgs.length) return;
  var visible = new Set();
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) {
      if (e.isIntersecting) visible.add(e.target);
      else visible.delete(e.target);
    });
  }, { threshold: 0.05 });
  bgs.forEach(function(bg) { observer.observe(bg); });
  window.addEventListener('scroll', function() {
    visible.forEach(function(bg) {
      var section = bg.closest('.stepped-section');
      if (!section) return;
      var rect = section.getBoundingClientRect();
      bg.style.transform = 'translateY(' + (rect.top * 0.12) + 'px)';
    });
  }, { passive: true });
})();

// ── SCROLL REVEAL ─────────────────────────
(function() {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var els = document.querySelectorAll(
    '.service-card, .testimonial-card, .faq-item, ' +
    '.stepped-content, .stepped-media, .project-item, ' +
    '.trust-item, .social-card, .area-pills li'
  );
  if (!els.length) return;
  els.forEach(function(el, i) {
    el.style.opacity   = '0';
    el.style.transform = 'translateY(24px)';
    el.style.transition = 'opacity 0.55s ease ' + (i % 4 * 0.08) +
                          's, transform 0.55s ease ' + (i % 4 * 0.08) + 's';
  });
  var ro = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.style.opacity   = '1';
        entry.target.style.transform = 'none';
        ro.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  els.forEach(function(el) { ro.observe(el); });
})();

// ── ANIMATED COUNTERS ─────────────────────
(function() {
  var counters = document.querySelectorAll('[data-counter-target]');
  if (!counters.length) return;
  var co = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (!entry.isIntersecting) return;
      var el     = entry.target;
      var target = parseInt(el.dataset.counterTarget, 10);
      var suffix = el.dataset.counterSuffix || '';
      var dur    = 1500;
      var start  = performance.now();
      (function tick(now) {
        var p = Math.min((now - start) / dur, 1);
        var e = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.floor(e * target) + suffix;
        if (p < 1) requestAnimationFrame(tick);
      })(performance.now());
      co.unobserve(el);
    });
  }, { threshold: 0.5 });
  counters.forEach(function(el) { co.observe(el); });
})();
