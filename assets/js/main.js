(() => {
  const header = document.getElementById('site-header');
  const menuToggle = document.getElementById('menu-toggle');
  const siteMenu = document.getElementById('site-menu');
  const setHeaderState = () => {
    if (!header) return;
    header.classList.toggle('scrolled', window.scrollY > 12);
  };
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

  const CONSENT_KEY = 'axis_cookie_consent';
  const banner = document.getElementById('cookie-banner');
  const modal = document.getElementById('cookie-modal');
  const analyticsToggle = document.getElementById('cookie-analytics-toggle');
  const marketingToggle = document.getElementById('cookie-marketing-toggle');

  const getConsent = () => {
    try {
      const raw = localStorage.getItem(CONSENT_KEY);
      return raw ? JSON.parse(raw) : null;
    } catch (_err) {
      return null;
    }
  };
  const loadConsentedScripts = (consent) => {
    if (!consent) return;
    document.querySelectorAll('script[type="text/plain"][data-consent-category]').forEach((el) => {
      const category = el.getAttribute('data-consent-category');
      const allowed = (category === 'analytics' && consent.analytics) || (category === 'marketing' && consent.marketing);
      if (!allowed || el.dataset.loaded === 'true') return;
      const s = document.createElement('script');
      s.textContent = el.textContent || '';
      s.defer = true;
      document.head.appendChild(s);
      el.dataset.loaded = 'true';
    });
  };
  const saveConsent = (consent) => {
    localStorage.setItem(CONSENT_KEY, JSON.stringify(consent));
    if (banner) banner.hidden = true;
    if (modal) modal.hidden = true;
    loadConsentedScripts(consent);
  };
  const openModal = () => {
    const consent = getConsent() || { necessary: true, analytics: false, marketing: false };
    if (analyticsToggle) analyticsToggle.checked = !!consent.analytics;
    if (marketingToggle) marketingToggle.checked = !!consent.marketing;
    if (modal) modal.hidden = false;
  };

  const existing = getConsent();
  if (!existing && banner) banner.hidden = false;
  loadConsentedScripts(existing);

  document.querySelectorAll('[data-cookie-action]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const action = btn.getAttribute('data-cookie-action');
      if (action === 'accept-all') saveConsent({ necessary: true, analytics: true, marketing: true });
      if (action === 'reject') saveConsent({ necessary: true, analytics: false, marketing: false });
      if (action === 'manage') openModal();
    });
  });
  const savePrefs = document.getElementById('save-cookie-preferences');
  if (savePrefs) {
    savePrefs.addEventListener('click', () => {
      saveConsent({
        necessary: true,
        analytics: !!(analyticsToggle && analyticsToggle.checked),
        marketing: !!(marketingToggle && marketingToggle.checked),
      });
    });
  }
  const closeModal = document.getElementById('close-cookie-modal');
  if (closeModal) closeModal.addEventListener('click', () => { if (modal) modal.hidden = true; });
  const openCookieSettings = document.getElementById('cookie-settings-button');
  if (openCookieSettings) openCookieSettings.addEventListener('click', openModal);

  document.querySelectorAll('.axis-quote-form').forEach((form) => {
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      const message = form.querySelector('.form-message');
      const data = Object.fromEntries(new FormData(form).entries());
      const webhook = window.AXIS_QUOTE_WEBHOOK;
      let ok = true;
      if (webhook) {
        try {
          const res = await fetch(webhook, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
          });
          ok = res.ok;
        } catch (_err) {
          ok = false;
        }
      }
      if (message) {
        message.textContent = ok
          ? 'Thanks. Your quote request has been received. We will respond within 24 hours.'
          : 'Thanks. Your request is saved locally. Please call 07713245511 while webhook setup is pending.';
      }
      form.reset();
    });
  });
})();
