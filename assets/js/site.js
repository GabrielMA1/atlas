(() => {
  const root = document.documentElement;
  const header = document.querySelector("[data-site-header]");
  const themeToggle = document.querySelector("[data-theme-toggle]");
  const menuToggle = document.querySelector("[data-menu-toggle]");
  const mobileMenu = document.querySelector("[data-mobile-menu]");
  const systemTheme = window.matchMedia("(prefers-color-scheme: dark)");

  root.classList.add("js");

  const savedTheme = () => {
    try {
      const value = localStorage.getItem("theme");
      return value === "dark" || value === "light" ? value : null;
    } catch (_) {
      return null;
    }
  };

  const syncThemeControl = () => {
    const dark = root.dataset.theme === "dark";
    themeToggle?.setAttribute("aria-pressed", String(dark));
    themeToggle?.setAttribute("aria-label", dark ? "Switch to light mode" : "Switch to dark mode");
  };

  syncThemeControl();

  themeToggle?.addEventListener("click", () => {
    root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
    try {
      localStorage.setItem("theme", root.dataset.theme);
    } catch (_) {
      // Persistence is optional when browser storage is unavailable.
    }
    syncThemeControl();
  });

  const followSystemTheme = (event) => {
    if (savedTheme()) return;
    root.dataset.theme = event.matches ? "dark" : "light";
    syncThemeControl();
  };

  if (typeof systemTheme.addEventListener === "function") {
    systemTheme.addEventListener("change", followSystemTheme);
  } else if (typeof systemTheme.addListener === "function") {
    systemTheme.addListener(followSystemTheme);
  }

  let menuReturnFocus = null;

  const menuLinks = () => mobileMenu
    ? [...mobileMenu.querySelectorAll("a[href], button:not([disabled])")]
    : [];

  const closeMenu = (restoreFocus = true) => {
    if (!menuToggle || !mobileMenu || mobileMenu.hidden) return;
    mobileMenu.hidden = true;
    document.body.classList.remove("menu-open");
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-label", "Open navigation");
    if (restoreFocus) menuReturnFocus?.focus();
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
    link.addEventListener("click", () => closeMenu(false));
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
  const sections = sectionIds.map((id) => document.getElementById(id)).filter(Boolean);

  const setActiveSection = (id) => {
    internalNavLinks.forEach((link) => {
      if (new URL(link.href).hash === `#${id}`) link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    });
  };

  let scrollFrame = null;

  const updatePageState = () => {
    scrollFrame = null;
    header?.classList.toggle("is-scrolled", window.scrollY > 10);

    if (location.pathname.replace(/index\.html$/, "") !== "/" || !sections.length) return;

    const marker = window.scrollY + (header?.offsetHeight || 0) + Math.min(180, window.innerHeight * 0.24);
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
  window.addEventListener("resize", () => {
    if (window.innerWidth > 1100) closeMenu(false);
    requestPageState();
  }, { passive: true });
  window.addEventListener("hashchange", requestPageState);
  window.addEventListener("load", requestPageState, { once: true });
  updatePageState();

  document.querySelectorAll("[data-year]").forEach((element) => {
    element.textContent = String(new Date().getFullYear());
  });
})();
