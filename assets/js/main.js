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
    const nextUrl = `https://www.axisscaffoldingessex.co.uk${window.location.pathname}${window.location.search}${window.location.hash}`;
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
  // lags the page by ~100px (0.2 of the scroll delta). Transform-only,
  // rAF-batched, desktop-pointer-only. Photo-only — no hex layer here,
  // see .hex-texture in generate_css() for the structural signature.
  (function heroParallax() {
    const hero = document.querySelector('.hero');
    const heroMedia = hero && hero.querySelector('.hero-media');
    if (!hero || !heroMedia) return;

    const HERO_RATIO = 0.2;
    const canAnimate = () =>
      window.matchMedia('(min-width: 769px)').matches &&
      window.matchMedia('(hover: hover)').matches &&
      !window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    let active = false;
    let ticking = false;

    function reset() {
      heroMedia.style.removeProperty('--hero-parallax-y');
    }

    function update() {
      ticking = false;
      const rect = hero.getBoundingClientRect();
      if (rect.bottom < 0 || rect.top > window.innerHeight) return;
      const scrolled = Math.max(0, -rect.top);
      heroMedia.style.setProperty('--hero-parallax-y', (scrolled * HERO_RATIO) + 'px');
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

  // ── SPLIT-IMAGE PARALLAX ──
  // Same guarded pattern as the hero, applied to the one other homepage
  // section that pairs large text with a single photo. Ratio is
  // deliberately much smaller than the hero's (0.06 vs 0.2) so it reads as
  // barely-there depth, not a second hero effect.
  (function splitParallax() {
    const images = document.querySelectorAll('.parallax-split .parallax-image');
    if (!images.length) return;

    const RATIO = 0.06;
    const canAnimate = () =>
      window.matchMedia('(min-width: 769px)').matches &&
      window.matchMedia('(hover: hover)').matches &&
      !window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    let active = false;
    let ticking = false;

    function reset() {
      images.forEach((img) => img.style.removeProperty('--split-parallax-y'));
    }

    function update() {
      ticking = false;
      images.forEach((img) => {
        const section = img.closest('.parallax-split');
        const rect = section.getBoundingClientRect();
        if (rect.bottom < 0 || rect.top > window.innerHeight) return;
        const scrolled = -rect.top;
        img.style.setProperty('--split-parallax-y', (scrolled * RATIO) + 'px');
      });
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

  const projectFilters = document.querySelector('.project-filters');
  if (projectFilters) {
    // Scoped to the grid, not project-item-featured — a page's single
    // editorial "featured" card (outside .projects-grid) stays visible
    // regardless of the active filter; it's a fixed editorial choice,
    // not part of the filterable set.
    const items = document.querySelectorAll('.projects-grid .project-item');
    projectFilters.addEventListener('click', (event) => {
      const btn = event.target.closest('.project-filter-btn');
      if (!btn) return;
      projectFilters.querySelectorAll('.project-filter-btn').forEach((b) => {
        b.setAttribute('aria-pressed', b === btn ? 'true' : 'false');
      });
      const filter = btn.dataset.filter;
      items.forEach((item) => {
        item.hidden = filter !== 'all' && item.dataset.category !== filter;
      });
    });
  }

  (function projectLightbox() {
    const lightbox = document.getElementById('project-lightbox');
    if (!lightbox) return;
    const imgEl = lightbox.querySelector('.project-lightbox-img');
    const labelEl = lightbox.querySelector('.project-lightbox-label');
    const metaEl = lightbox.querySelector('.project-lightbox-meta');
    const descEl = lightbox.querySelector('.project-lightbox-desc');
    const prevBtn = lightbox.querySelector('.project-lightbox-prev');
    const nextBtn = lightbox.querySelector('.project-lightbox-next');
    const closeBtn = lightbox.querySelector('.project-lightbox-close');
    const triggers = document.querySelectorAll('.project-item-media');
    if (!triggers.length) return;

    let items = [];
    let idx = 0;
    let lastFocused = null;

    function visibleItems() {
      return Array.from(document.querySelectorAll('.project-item')).filter((el) => !el.hidden);
    }

    function preload(item) {
      if (!item) return;
      const srcImg = item.querySelector('img');
      if (!srcImg) return;
      const pre = new Image();
      pre.src = srcImg.currentSrc || srcImg.src;
    }

    function render() {
      const item = items[idx];
      if (!item) return;
      const srcImg = item.querySelector('img');
      imgEl.src = srcImg.currentSrc || srcImg.src;
      imgEl.alt = srcImg.alt;
      labelEl.textContent = item.dataset.label || '';
      metaEl.textContent = item.dataset.location ? (item.dataset.location + ' · Essex') : '';
      descEl.textContent = item.dataset.desc || '';
      const multiple = items.length > 1;
      prevBtn.hidden = !multiple;
      nextBtn.hidden = !multiple;
      // Lazy-load neighbours only — not all 14 photos up front.
      preload(items[(idx - 1 + items.length) % items.length]);
      preload(items[(idx + 1) % items.length]);
    }

    function open(item) {
      items = visibleItems();
      idx = items.indexOf(item);
      if (idx === -1) idx = 0;
      lastFocused = document.activeElement;
      lightbox.hidden = false;
      document.body.classList.add('lightbox-open');
      render();
      closeBtn.focus();
      document.addEventListener('keydown', onKeydown);
    }

    function close() {
      lightbox.hidden = true;
      document.body.classList.remove('lightbox-open');
      document.removeEventListener('keydown', onKeydown);
      if (lastFocused && typeof lastFocused.focus === 'function') lastFocused.focus();
    }

    function show(delta) {
      if (items.length < 2) return;
      idx = (idx + delta + items.length) % items.length;
      render();
    }

    function onKeydown(event) {
      if (event.key === 'Escape') {
        close();
      } else if (event.key === 'ArrowRight') {
        show(1);
      } else if (event.key === 'ArrowLeft') {
        show(-1);
      } else if (event.key === 'Tab') {
        const focusable = Array.from(lightbox.querySelectorAll('button')).filter((b) => !b.hidden);
        const first = focusable[0];
        const last = focusable[focusable.length - 1];
        if (event.shiftKey && document.activeElement === first) {
          event.preventDefault();
          last.focus();
        } else if (!event.shiftKey && document.activeElement === last) {
          event.preventDefault();
          first.focus();
        }
      }
    }

    triggers.forEach((btn) => {
      btn.addEventListener('click', () => open(btn.closest('.project-item')));
    });
    closeBtn.addEventListener('click', close);
    prevBtn.addEventListener('click', () => show(-1));
    nextBtn.addEventListener('click', () => show(1));
    lightbox.addEventListener('click', (event) => {
      if (event.target === lightbox) close();
    });

    let touchStartX = null;
    lightbox.addEventListener('touchstart', (event) => {
      touchStartX = event.changedTouches[0].clientX;
    }, { passive: true });
    lightbox.addEventListener('touchend', (event) => {
      if (touchStartX === null) return;
      const dx = event.changedTouches[0].clientX - touchStartX;
      if (Math.abs(dx) > 40) show(dx > 0 ? -1 : 1);
      touchStartX = null;
    }, { passive: true });
  })();

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

  // ── ATTRIBUTION (captured on every page, read by the quote wizard) ──
  (function captureAttribution() {
    try {
      const params = new URLSearchParams(window.location.search);
      const utmKeys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'];
      const stored = JSON.parse(localStorage.getItem('axis_attribution') || '{}');
      let changed = false;
      utmKeys.forEach((key) => {
        const value = params.get(key);
        if (value) { stored[key] = value; changed = true; }
      });
      if (!sessionStorage.getItem('axis_landing_page')) {
        sessionStorage.setItem('axis_landing_page', window.location.pathname);
        sessionStorage.setItem('axis_referrer', document.referrer || '');
      }
      if (changed) localStorage.setItem('axis_attribution', JSON.stringify(stored));
    } catch (_err) { /* storage unavailable — attribution is best-effort, never blocking */ }
  })();

  // ── QUOTE WIZARD ──
  (function quoteWizard() {
    const form = document.querySelector('.quote-wizard-form');
    if (!form) return;

    // Populate hidden attribution fields from what's been captured
    // sitewide (see captureAttribution above), not just this page.
    try {
      const attribution = JSON.parse(localStorage.getItem('axis_attribution') || '{}');
      form.querySelectorAll('.quote-attr-field[data-attr]').forEach((field) => {
        const key = field.dataset.attr;
        if (key === 'referrer') field.value = sessionStorage.getItem('axis_referrer') || '';
        else if (key === 'landingPage') field.value = sessionStorage.getItem('axis_landing_page') || window.location.pathname;
        else if (attribution[key]) field.value = attribution[key];
      });
    } catch (_err) { /* best-effort only */ }

    const steps = Array.from(form.querySelectorAll('.quote-step'));
    const progress = document.querySelector('.quote-progress');
    const progressSteps = progress ? Array.from(progress.querySelectorAll('.quote-progress-step')) : [];
    const backBtn = form.querySelector('.quote-back');
    const nextBtn = form.querySelector('.quote-next');
    const submitBtn = form.querySelector('.quote-submit');
    const emergencyBanner = form.querySelector('[data-emergency-banner]');
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    let current = 0;
    const stepEventNames = ['quote_project_type', 'quote_location', 'quote_timing', 'quote_details', 'quote_photo_upload'];

    function updateAudience() {
      const checked = form.querySelector('input[name="projectType"]:checked');
      const audience = checked ? checked.dataset.audience : '';
      form.querySelectorAll('[data-audience-fields]').forEach((block) => {
        block.hidden = block.dataset.audienceFields !== audience;
      });
      if (emergencyBanner) emergencyBanner.hidden = audience !== 'emergency';
    }

    function showStep(index) {
      steps.forEach((step, i) => { step.hidden = i !== index; });
      if (progress) {
        progress.hidden = false;
        progressSteps.forEach((el, i) => {
          el.classList.toggle('is-active', i === index);
          el.classList.toggle('is-done', i < index);
          if (i === index) el.setAttribute('aria-current', 'step');
          else el.removeAttribute('aria-current');
        });
      }
      backBtn.hidden = index === 0;
      const isLast = index === steps.length - 1;
      nextBtn.hidden = isLast;
      submitBtn.hidden = !isLast;
      current = index;
      (steps[index].querySelector('input, select, textarea') || steps[index]).focus({ preventScroll: true });
      steps[index].scrollIntoView({ block: 'nearest', behavior: reduceMotion ? 'auto' : 'smooth' });
    }

    function stepIsValid(index) {
      const fields = steps[index].querySelectorAll('input, select, textarea');
      let valid = true;
      fields.forEach((field) => {
        if (field.closest('[hidden]')) return; // conditional fields not currently shown
        if (!field.checkValidity()) { valid = false; field.reportValidity(); }
      });
      return valid;
    }

    // Progressive enhancement: JS now takes over from "all fields visible,
    // real submit button showing" (the no-JS state) into stepped mode.
    nextBtn.hidden = false;
    showStep(0);

    // Belt-and-suspenders for the checked-state highlight: CSS :has() does
    // this alone in current browsers, but toggling a class works everywhere.
    form.querySelectorAll('.quote-choice-grid input[type="radio"]').forEach((radio) => {
      radio.addEventListener('focus', () => radio.closest('.quote-choice').classList.add('is-focused'));
      radio.addEventListener('blur', () => radio.closest('.quote-choice').classList.remove('is-focused'));
      radio.addEventListener('change', () => {
        // Re-evaluate every choice in this group, not just the one that
        // fired — the previously-checked sibling's radio doesn't emit its
        // own 'change' event when it becomes unchecked.
        radio.closest('.quote-choice-grid').querySelectorAll('.quote-choice').forEach((label) => {
          const input = label.querySelector('input');
          label.classList.toggle('is-checked', !!input && input.checked);
        });
        // Emergency banner reacts immediately on selection — the whole
        // point is to surface "call us" before the visitor clicks
        // Continue, not after.
        if (radio.name === 'projectType') updateAudience();
      });
    });

    nextBtn.addEventListener('click', () => {
      if (!stepIsValid(current)) return;
      const eventName = stepEventNames[current];
      if (eventName) trackEvent(eventName, { event_category: 'Lead', event_label: form.dataset.formName });
      if (current < steps.length - 1) showStep(current + 1);
    });
    backBtn.addEventListener('click', () => {
      if (current > 0) showStep(current - 1);
    });
    form.addEventListener('keydown', (event) => {
      // Enter on a non-final step advances instead of submitting early
      // (textarea keeps its normal newline behaviour).
      if (event.key === 'Enter' && event.target.tagName !== 'TEXTAREA' && !nextBtn.hidden) {
        event.preventDefault();
        nextBtn.click();
      }
    });

    // ── Photos: validate, compress client-side, list, allow removal ──
    const photoInput = form.querySelector('#qw-photos');
    const photoList = form.querySelector('.quote-photo-list');
    const photoStatus = form.querySelector('.quote-photo-status');
    const MAX_PHOTOS = 5;
    const MAX_SOURCE_MB = 15;
    let acceptedFiles = [];

    function compressImage(file) {
      return new Promise((resolve) => {
        try {
          const img = new Image();
          const url = URL.createObjectURL(file);
          img.onload = () => {
            URL.revokeObjectURL(url);
            const maxEdge = 1600;
            const scale = Math.min(1, maxEdge / Math.max(img.width, img.height));
            const canvas = document.createElement('canvas');
            canvas.width = Math.round(img.width * scale);
            canvas.height = Math.round(img.height * scale);
            const ctx = canvas.getContext('2d');
            if (!ctx) { resolve(file); return; }
            ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
            canvas.toBlob((blob) => {
              if (!blob) { resolve(file); return; }
              resolve(new File([blob], file.name.replace(/\.\w+$/, '.jpg'), { type: 'image/jpeg' }));
            }, 'image/jpeg', 0.72);
          };
          img.onerror = () => { URL.revokeObjectURL(url); resolve(file); };
          img.src = url;
        } catch (_err) {
          resolve(file); // compression is best-effort — never block the upload over it
        }
      });
    }

    function renderPhotoList() {
      photoList.innerHTML = '';
      acceptedFiles.forEach((file, i) => {
        const li = document.createElement('li');
        const sizeKb = Math.round(file.size / 1024);
        li.innerHTML = '<span>' + file.name + ' (' + sizeKb + 'KB)</span>';
        const removeBtn = document.createElement('button');
        removeBtn.type = 'button';
        removeBtn.setAttribute('aria-label', 'Remove ' + file.name);
        removeBtn.textContent = '×';
        removeBtn.addEventListener('click', () => {
          acceptedFiles.splice(i, 1);
          syncPhotoInput();
          renderPhotoList();
        });
        li.appendChild(removeBtn);
        photoList.appendChild(li);
      });
    }

    function syncPhotoInput() {
      try {
        const dt = new DataTransfer();
        acceptedFiles.forEach((file) => dt.items.add(file));
        photoInput.files = dt.files;
      } catch (_err) { /* DataTransfer unsupported — files still submit as originally selected */ }
    }

    if (photoInput) {
      photoInput.addEventListener('change', async () => {
        const incoming = Array.from(photoInput.files || []);
        if (!incoming.length) return;
        photoStatus.textContent = 'Processing photos…';
        let rejected = 0;
        for (const file of incoming) {
          if (acceptedFiles.length >= MAX_PHOTOS) { rejected++; continue; }
          if (!file.type.startsWith('image/')) { rejected++; continue; }
          if (file.size > MAX_SOURCE_MB * 1024 * 1024) { rejected++; continue; }
          const compressed = await compressImage(file);
          acceptedFiles.push(compressed);
        }
        syncPhotoInput();
        renderPhotoList();
        const parts = [acceptedFiles.length + ' photo' + (acceptedFiles.length === 1 ? '' : 's') + ' added.'];
        if (rejected) parts.push(rejected + ' skipped (over ' + MAX_PHOTOS + ' photos, too large, or not an image).');
        photoStatus.textContent = parts.join(' ');
        trackEvent('quote_photo_upload', { event_category: 'Lead', event_label: form.dataset.formName, value: acceptedFiles.length });
      });
    }
  })();

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
      panel.className = 'cookie-prefs-panel';
      panel.innerHTML = '<p class="cookie-prefs-title">Cookie Preferences</p>' +
        '<div>' +
        '<label class="cookie-prefs-row">' +
        '<span>Necessary <span style="color:#6b7280;font-size:0.75rem;">(always on)</span></span>' +
        '<input type="checkbox" checked disabled></label>' +
        '<label class="cookie-prefs-row">' +
        '<span>Analytics</span><input type="checkbox" id="axis-pref-analytics"></label>' +
        '<label class="cookie-prefs-row">' +
        '<span>Marketing</span><input type="checkbox" id="axis-pref-marketing"></label>' +
        '</div>' +
        '<button id="axis-pref-save" class="btn-save-prefs">Save Preferences</button>';
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
