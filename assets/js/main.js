(function () {
  const header = document.getElementById('site-header');
  const nav = document.getElementById('site-nav');
  const toggle = document.querySelector('.menu-toggle');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      const isOpen = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  }

  function updateHeader() {
    if (!header) return;
    if (window.scrollY > 24) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }

  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });

  document.addEventListener('mousemove', function (event) {
    document.body.style.setProperty('--mouse-x', event.clientX + 'px');
    document.body.style.setProperty('--mouse-y', event.clientY + 'px');
  });

  const revealItems = document.querySelectorAll('.reveal');
  if (revealItems.length) {
    const observer = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.18 });
    revealItems.forEach(function (item) { observer.observe(item); });
  }

  const lightbox = document.querySelector('.lightbox');
  const lightboxImg = lightbox ? lightbox.querySelector('img') : null;
  const galleryImgs = document.querySelectorAll('.gallery-item img');

  if (lightbox && lightboxImg && galleryImgs.length) {
    galleryImgs.forEach(function (img) {
      img.addEventListener('click', function () {
        lightboxImg.src = img.src;
        lightboxImg.alt = img.alt;
        lightbox.classList.add('active');
      });
    });

    lightbox.addEventListener('click', function () {
      lightbox.classList.remove('active');
      lightboxImg.src = '';
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') {
        lightbox.classList.remove('active');
        lightboxImg.src = '';
      }
    });
  }
})();
