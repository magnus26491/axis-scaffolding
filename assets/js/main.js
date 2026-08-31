(() => {
  const CONTACT_EMAIL = 'axis-scaffolding@outlook.com';
  const header = document.getElementById('site-header');
  const menuToggle = document.getElementById('menu-toggle');
  const siteMenu = document.getElementById('site-menu');
  const setHeaderState = () => {
    if (!header) return;
    header.classList.toggle('scrolled', window.scrollY > 12);
  };
  const currentHost = window.location.hostname.toLowerCase();
  if (currentHost === 'axisscaffolding.co.uk' || currentHost === 'www.axisscaffolding.co.uk') {
    const nextUrl = `https://axisscaffoldingessex.co.uk${window.location.pathname}${window.location.search}${window.location.hash}`;
    const moveBanner = document.getElementById('domain-move-banner');
    const canonicalTag = document.querySelector('link[rel="canonical"]');
    if (canonicalTag) canonicalTag.setAttribute('href', nextUrl);
    if (moveBanner) moveBanner.hidden = false;
    window.setTimeout(() => {
      window.location.replace(nextUrl);
    }, 2200);
  }
  setHeaderState();
  window.addEventListener('scroll', setHeaderState, { passive: true });

  // ── HERO PARALLAX ──
  // Cinematic and restrained by design: over a 500px scroll the hero photo
  // lags the page by ~100px and the hex layer by ~50px (0.2 / 0.1 of the
  // scroll delta). Transform-only, rAF-batched, desktop-pointer-only.
  (function heroParallax() {
    const hero = document.querySelector('.hero');
    const heroMedia = hero && hero.querySelector('.hero-media');
    const heroHex = hero && hero.querySelector('.hero-hex');
    if (!hero || !heroMedia || !heroHex) return;

    const HERO_RATIO = 0.2;
    const HEX_RATIO = 0.1;
    const canAnimate = () =>
      window.matchMedia('(min-width: 769px)').matches &&
      window.matchMedia('(hover: hover)').matches &&
      !window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    let active = false;
    let ticking = false;

    function reset() {
      heroMedia.style.removeProperty('--hero-parallax-y');
      heroHex.style.removeProperty('--hex-parallax-y');
    }

    function update() {
      ticking = false;
      const rect = hero.getBoundingClientRect();
      if (rect.bottom < 0 || rect.top > window.innerHeight) return;
      const scrolled = Math.max(0, -rect.top);
      heroMedia.style.setProperty('--hero-parallax-y', (scrolled * HERO_RATIO) + 'px');
      heroHex.style.setProperty('--hex-parallax-y', (scrolled * HEX_RATIO) + 'px');
    }

    function onScroll() {
      if (!active || ticking) return;
      ticking = true;
      requestAnimationFrame(update);
    }

    function sync() {
      const should = canAnimate();
      if (should === active) return;
      active = should;
      if (active) {
        update();
      } else {
        reset();
      }
    }

    sync();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', sync, { passive: true });
  })();
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

  const track = document.getElementById('testimonial-track');
  const carousel = document.getElementById('testimonial-carousel');
  let idx = 0;
  let timer = null;
  const start = () => {
    if (!track || track.children.length <= 1) return;
    timer = window.setInterval(() => {
      idx = (idx + 1) % track.children.length;
      track.style.transform = `translateX(-${idx * 100}%)`;
    }, 4500);
  };
  const stop = () => {
    if (timer) clearInterval(timer);
    timer = null;
  };
  if (carousel) {
    carousel.addEventListener('mouseenter', stop);
    carousel.addEventListener('mouseleave', start);
  }
  start();

  // ── ANALYTICS (consent-gated, no-op until a real GA4 ID is configured) ──
  const CATEGORIES_KEY = 'axis_cookie_categories';
  function loadGA4() {
    if (!window.AXIS_GA4_ID || window.__axisGA4Loaded) return;
    window.__axisGA4Loaded = true;
    var s = document.createElement('script');
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + window.AXIS_GA4_ID;
    s.async = true;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function() { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', window.AXIS_GA4_ID, { anonymize_ip: true });
  }
  function trackEvent(name, params) {
    if (typeof window.gtag === 'function') window.gtag('event', name, params || {});
  }
  function applyConsentCategories(categories) {
    localStorage.setItem(CATEGORIES_KEY, JSON.stringify(categories));
    if (categories.analytics) loadGA4();
  }
  (function restoreConsent() {
    try {
      const stored = JSON.parse(localStorage.getItem(CATEGORIES_KEY) || 'null');
      if (stored && stored.analytics) loadGA4();
    } catch (_err) { /* ignore malformed stored consent */ }
  })();
  document.querySelectorAll('a[href^="tel:"]').forEach((link) => {
    link.addEventListener('click', () => {
      trackEvent('phone_click', { event_category: 'Lead', link_url: link.getAttribute('href') });
    });
  });
  document.querySelectorAll('.axis-quote-form').forEach((form) => {
    let started = false;
    form.addEventListener('input', () => {
      if (started) return;
      started = true;
      trackEvent('quote_start', { event_category: 'Lead', event_label: form.dataset.formName || 'quote_form' });
    }, { once: false, capture: true });
  });
  // ── END ANALYTICS ──

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
      applyConsentCategories({ analytics: true, marketing: true });
    });
  }
  var rejectBtn = document.getElementById('axis-cookie-reject');
  if (rejectBtn) {
    rejectBtn.addEventListener('click', function() {
      setConsent('rejected');
      applyConsentCategories({ analytics: false, marketing: false });
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
        '<button id="axis-pref-save" style="margin-top:1rem;background:linear-gradient(135deg,#e8eaed,#c8cdd4);color:#000;' +
        'border:none;border-radius:9999px;padding:0.5rem 1.5rem;font-weight:700;cursor:pointer;">' +
        'Save Preferences</button>';
      document.body.appendChild(panel);
      var save = document.getElementById('axis-pref-save');
      if (save) {
        save.addEventListener('click', function() {
          var analyticsChecked = document.getElementById('axis-pref-analytics');
          var marketingChecked = document.getElementById('axis-pref-marketing');
          panel.remove();
          setConsent('custom');
          applyConsentCategories({
            analytics: !!(analyticsChecked && analyticsChecked.checked),
            marketing: !!(marketingChecked && marketingChecked.checked),
          });
        });
      }
    });
  }
  var footerBtn = document.getElementById('axis-footer-cookie-btn');
  if (footerBtn) {
    footerBtn.addEventListener('click', function() {
      localStorage.removeItem(CONSENT_KEY);
      localStorage.removeItem(CATEGORIES_KEY);
      showBar();
    });
  }

  document.querySelectorAll('.axis-quote-form').forEach((form) => {
    form.addEventListener('submit', async (event) => {
      const webhook = window.AXIS_QUOTE_WEBHOOK;

      // No webhook is configured: allow the form's native FormSubmit action to run.
      // The previous code prevented the native POST and then displayed a false success
      // message, which could silently discard every quote enquiry.
      if (!webhook) {
        trackEvent('generate_lead', { event_category: 'Lead', event_label: form.dataset.formName || 'quote_form' });
        return;
      }

      event.preventDefault();
      const message = form.querySelector('.form-message');
      const data = Object.fromEntries(new FormData(form).entries());
      const payload = { ...data, notification_email: CONTACT_EMAIL };
      let ok = false;

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
          ? 'Thanks. Your quote request has been received. We will respond within one working day.'
          : 'There was a problem submitting your request. Please call 01702 820468 to reach us directly.';
      }

      if (ok) {
        trackEvent('generate_lead', { event_category: 'Lead', event_label: form.dataset.formName || 'quote_form' });
        form.reset();
        window.setTimeout(() => {
          window.location.assign('/thank-you');
        }, 250);
      } else {
        trackEvent('quote_error', { event_category: 'Lead', event_label: form.dataset.formName || 'quote_form' });
      }
    });
  });
})();

// ── WHITE MOUSE GLOW ──────────────────────
(function() {
  if (window.matchMedia('(hover: none)').matches) return;
  if (window.matchMedia('(max-width: 768px)').matches) return;

  var glow = document.getElementById('mouse-glow');
  if (!glow) return;

  var mouseX = window.innerWidth / 2;
  var mouseY = window.innerHeight / 2;
  var currentX = mouseX;
  var currentY = mouseY;

  function lerp(start, end, factor) {
    return start + (end - start) * factor;
  }

  function animate() {
    currentX = lerp(currentX, mouseX, 0.12);
    currentY = lerp(currentY, mouseY, 0.12);
    glow.style.left = currentX + 'px';
    glow.style.top  = currentY + 'px';
    requestAnimationFrame(animate);
  }

  document.addEventListener('mousemove', function(e) {
    mouseX = e.clientX;
    mouseY = e.clientY;
  }, { passive: true });

  animate();

  document.addEventListener('mouseleave', function() {
    glow.style.opacity = '0';
  });
  document.addEventListener('mouseenter', function() {
    glow.style.opacity = '1';
  });
})();
// ── END MOUSE GLOW ────────────────────────
