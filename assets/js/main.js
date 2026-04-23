(() => {
  const header = document.getElementById('site-header');
  const menuToggle = document.getElementById('menu-toggle');
  const siteMenu = document.getElementById('site-menu');
  const heroBg = document.querySelector('.hero-bg-parallax');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const desktopParallax = window.matchMedia('(min-width: 768px)').matches && !reducedMotion;
  const setHeaderState = () => {
    if (!header) return;
    header.classList.toggle('scrolled', window.scrollY > 12);
  };
  setHeaderState();
  window.addEventListener('scroll', setHeaderState, { passive: true });
  if (heroBg && desktopParallax) {
    const updateHeroParallax = () => {
      const offset = window.scrollY * 0.4;
      heroBg.style.transform = `translateY(${offset}px)`;
    };
    updateHeroParallax();
    window.addEventListener('scroll', updateHeroParallax, { passive: true });
  }
  if (menuToggle && siteMenu) {
    menuToggle.addEventListener('click', () => {
      const open = siteMenu.classList.toggle('open');
      menuToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  const revealItems = document.querySelectorAll('.reveal-item');
  if (revealItems.length) {
    const revealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-visible');
          revealObserver.unobserve(entry.target);
        });
      },
      { threshold: 0.15 }
    );
    revealItems.forEach((item) => revealObserver.observe(item));
  }

  if (desktopParallax) {
    const parallaxPanels = document.querySelectorAll('.parallax-panel');
    const activePanels = new Set();
    if (parallaxPanels.length) {
      const panelObserver = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) activePanels.add(entry.target);
            else activePanels.delete(entry.target);
          });
        },
        { threshold: 0.15 }
      );
      parallaxPanels.forEach((panel) => panelObserver.observe(panel));

      const updatePanelParallax = () => {
        activePanels.forEach((panel) => {
          const inner = panel.querySelector('img');
          if (!inner) return;
          const rect = panel.getBoundingClientRect();
          const viewportCenter = window.innerHeight / 2;
          const delta = rect.top + rect.height / 2 - viewportCenter;
          inner.style.transform = `translateY(${delta * -0.15}px) scale(1.06)`;
        });
      };
      updatePanelParallax();
      window.addEventListener('scroll', updatePanelParallax, { passive: true });
      window.addEventListener('resize', updatePanelParallax, { passive: true });
    }
  }

  const trustBar = document.getElementById('trust-bar');
  const animateCounter = (element, target, suffix = '', duration = 1200) => {
    const startTime = performance.now();
    const tick = (now) => {
      const progress = Math.min((now - startTime) / duration, 1);
      const value = Math.floor(progress * target);
      element.textContent = `${value}${suffix}`;
      if (progress < 1) requestAnimationFrame(tick);
      else element.textContent = `${target}${suffix}`;
    };
    requestAnimationFrame(tick);
  };
  if (trustBar) {
    const counters = trustBar.querySelectorAll('[data-count], [data-counter-target]');
    let counted = false;
    const trustObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          if (!counted && !reducedMotion) {
            counters.forEach((counter) => {
              const target = Number(counter.getAttribute('data-counter-target') || counter.getAttribute('data-count') || '0');
              const suffix = counter.getAttribute('data-counter-suffix') || counter.getAttribute('data-suffix') || '';
              animateCounter(counter, target, suffix);
            });
            counted = true;
          } else {
            counters.forEach((counter) => {
              const target = counter.getAttribute('data-counter-target') || counter.getAttribute('data-count') || '';
              const suffix = counter.getAttribute('data-counter-suffix') || counter.getAttribute('data-suffix') || '';
              counter.textContent = `${target}${suffix}`;
            });
          }
          trustObserver.unobserve(entry.target);
        });
      },
      { threshold: 0.25 }
    );
    trustObserver.observe(trustBar);
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

  const faqSection = document.getElementById('faq');
  if (faqSection) {
    let faqAnimated = false;
    const faqItems = faqSection.querySelectorAll('.faq-item');
    faqSection.querySelectorAll('.faq-question').forEach((button) => {
      button.addEventListener('click', () => {
        if (faqAnimated) return;
        faqItems.forEach((item, index) => {
          item.style.transitionDelay = `${index * 0.08}s`;
          item.classList.add('is-visible');
        });
        faqAnimated = true;
      });
    });
  }

  document.querySelectorAll('.axis-quote-form').forEach((form) => {
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      const message = form.querySelector('.form-message');
      const data = Object.fromEntries(new FormData(form).entries());
      const webhook = window.AXIS_QUOTE_WEBHOOK;
      const fallbackMailto = `mailto:Axis-scaffolding@outlook.com?subject=Website Quote Request&body=${encodeURIComponent(
        `Name: ${data.fullName || ''}\nPhone: ${data.phone || ''}\nEmail: ${data.email || ''}\nPostcode: ${data.postcode || ''}\nType: ${data.scaffoldingType || ''}\nDescription: ${data.briefDescription || ''}\nSource: ${data.source || ''}`
      )}`;
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
          : 'Thanks. Your request is ready to send by email. Please check your email draft and send it to complete your quote request.';
      }
      if (!ok) {
        window.location.href = fallbackMailto;
      }
      form.reset();
    });
  });
})();
