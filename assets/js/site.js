(() => {
  const root = document.documentElement;
  const header = document.querySelector("[data-site-header]");
  const themeToggle = document.querySelector("[data-theme-toggle]");
  const menuToggle = document.querySelector("[data-menu-toggle]");
  const mobileMenu = document.querySelector("[data-mobile-menu]");

  root.classList.add("js");

  const syncTheme = () => {
    const dark = root.dataset.theme === "dark";
    themeToggle?.setAttribute("aria-pressed", String(dark));
    themeToggle?.setAttribute("aria-label", dark ? "Switch to light mode" : "Switch to dark mode");
  };

  syncTheme();

  themeToggle?.addEventListener("click", () => {
    root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
    try {
      localStorage.setItem("theme", root.dataset.theme);
    } catch (_) {
      // Theme persistence is optional when browser storage is unavailable.
    }
    syncTheme();
  });

  let menuReturnFocus = null;

  const menuLinks = () => mobileMenu
    ? [...mobileMenu.querySelectorAll("a[href], button:not([disabled])")]
    : [];

  const closeMenu = () => {
    if (!menuToggle || !mobileMenu || mobileMenu.hidden) return;
    mobileMenu.hidden = true;
    document.body.classList.remove("menu-open");
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-label", "Open navigation");
    menuReturnFocus?.focus();
  };

  const openMenu = () => {
    if (!menuToggle || !mobileMenu) return;
    menuReturnFocus = document.activeElement;
    mobileMenu.hidden = false;
    document.body.classList.add("menu-open");
    menuToggle.setAttribute("aria-expanded", "true");
    menuToggle.setAttribute("aria-label", "Close navigation");
    menuLinks()[0]?.focus();
  };

  menuToggle?.addEventListener("click", () => {
    if (mobileMenu?.hidden) openMenu();
    else closeMenu();
  });

  mobileMenu?.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", closeMenu);
  });

  document.addEventListener("keydown", (event) => {
    if (!mobileMenu || mobileMenu.hidden) return;

    if (event.key === "Escape") {
      event.preventDefault();
      closeMenu();
      return;
    }

    if (event.key !== "Tab") return;
    const focusable = menuLinks();
    if (!focusable.length) return;
    const first = focusable[0];
    const last = focusable[focusable.length - 1];

    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  });

  const internalNavLinks = [
    ...document.querySelectorAll('.desktop-nav a[href^="/#"], .mobile-menu a[href^="/#"]')
  ];

  const sectionIds = [...new Set(internalNavLinks.map((link) => new URL(link.href).hash.slice(1)))];
  const sections = sectionIds
    .map((id) => document.getElementById(id))
    .filter(Boolean)
    .sort((a, b) => a.offsetTop - b.offsetTop);

  const setActiveSection = (id) => {
    internalNavLinks.forEach((link) => {
      if (new URL(link.href).hash === `#${id}`) link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    });
  };

  let scrollFrame = null;

  const updatePageState = () => {
    scrollFrame = null;
    header?.classList.toggle("is-scrolled", window.scrollY > 12);

    if (location.pathname.replace(/index\.html$/, "") !== "/") return;
    if (!sections.length) return;

    const marker = window.scrollY + (header?.offsetHeight || 0) + Math.min(180, window.innerHeight * 0.25);
    let active = "";

    if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 6) {
      active = sections[sections.length - 1].id;
    } else {
      sections.forEach((section) => {
        if (section.offsetTop <= marker) active = section.id;
      });
    }

    setActiveSection(active);
  };

  const requestPageState = () => {
    if (scrollFrame !== null) return;
    scrollFrame = requestAnimationFrame(updatePageState);
  };

  window.addEventListener("scroll", requestPageState, { passive: true });
  window.addEventListener("resize", requestPageState, { passive: true });
  window.addEventListener("hashchange", requestPageState);
  updatePageState();

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const reveals = [...document.querySelectorAll(".reveal")];

  if (reducedMotion || !("IntersectionObserver" in window)) {
    reveals.forEach((element) => element.classList.add("is-visible"));
  } else {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    }, {
      threshold: 0.08,
      rootMargin: "0px 0px -7% 0px"
    });

    reveals.forEach((element) => observer.observe(element));
  }

  document.querySelectorAll("[data-year]").forEach((element) => {
    element.textContent = String(new Date().getFullYear());
  });
})();
