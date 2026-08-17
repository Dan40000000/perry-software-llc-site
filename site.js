(() => {
  const navToggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');
  const mobileNav = window.matchMedia('(max-width: 1100px)');

  const setMenuState = (open, { moveFocus = false } = {}) => {
    if (!navToggle || !navLinks) return;
    navToggle.classList.toggle('active', open);
    navLinks.classList.toggle('active', open);
    navToggle.setAttribute('aria-expanded', String(open));
    navToggle.setAttribute('aria-label', open ? 'Close navigation menu' : 'Open navigation menu');
    navLinks.hidden = mobileNav.matches && !open;
    navLinks.setAttribute('aria-hidden', String(mobileNav.matches && !open));
    document.body.classList.toggle('nav-open', open);

    if (open && moveFocus) {
      navLinks.querySelector('a')?.focus();
    }
  };

  if (navToggle && navLinks) {
    setMenuState(false);
    navToggle.addEventListener('click', () => {
      const open = navToggle.getAttribute('aria-expanded') !== 'true';
      setMenuState(open, { moveFocus: open });
    });

    navLinks.addEventListener('click', (event) => {
      if (event.target.closest('a')) setMenuState(false);
    });

    document.addEventListener('click', (event) => {
      if (
        navToggle.getAttribute('aria-expanded') === 'true' &&
        !event.target.closest('.main-nav')
      ) {
        setMenuState(false);
      }
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && navToggle.getAttribute('aria-expanded') === 'true') {
        setMenuState(false);
        navToggle.focus();
      }
    });

    window.addEventListener('resize', () => {
      if (!mobileNav.matches) setMenuState(false);
      else if (navToggle.getAttribute('aria-expanded') !== 'true') setMenuState(false);
    });
  }

  document.querySelectorAll('[data-current-year]').forEach((element) => {
    element.textContent = String(new Date().getFullYear());
  });

  const marketingPages = new Set([
    '/',
    '/index.html',
    '/features.html',
    '/clinical.html',
    '/billing.html',
    '/pricing.html',
    '/about.html',
    '/contact.html',
    '/migration.html',
    '/dermatology-ehr.html',
    '/biopsy-pathology-tracking.html',
    '/dermatology-ehr-migration-checklist.html',
    '/resources.html',
  ]);

  if (marketingPages.has(window.location.pathname) && !document.querySelector('.mobile-demo-bar')) {
    const mobileDemoBar = document.createElement('a');
    mobileDemoBar.className = 'mobile-demo-bar';
    mobileDemoBar.href = window.location.pathname.includes('/account/') ? '../contact.html' : 'contact.html';
    mobileDemoBar.textContent = 'Request a Demo';
    document.body.append(mobileDemoBar);
  }
})();
