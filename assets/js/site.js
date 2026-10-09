(() => {
  const root = document.documentElement;
  const header = document.querySelector("[data-site-header]");
  const themeToggle = document.querySelector("[data-theme-toggle]");
  const menuToggle = document.querySelector("[data-menu-toggle]");
  const mobileMenu = document.querySelector("[data-mobile-menu]");
  const systemTheme = window.matchMedia("(prefers-color-scheme: dark)");
  // Keep in step with the navigation breakpoint in site.css.
  const desktopLayout = window.matchMedia("(min-width: 961px)");

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
    if (restoreFocus) menuReturnFocus?.focus();
  };

  const openMenu = () => {
    if (!menuToggle || !mobileMenu) return;
    menuReturnFocus = document.activeElement;
    mobileMenu.hidden = false;
    document.body.classList.add("menu-open");
    menuToggle.setAttribute("aria-expanded", "true");
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
    if (desktopLayout.matches) closeMenu(false);
    requestPageState();
  }, { passive: true });
  window.addEventListener("hashchange", requestPageState);
  window.addEventListener("load", requestPageState, { once: true });
  updatePageState();

  document.querySelectorAll("[data-year]").forEach((element) => {
    element.textContent = String(new Date().getFullYear());
  });

  // Hero, act two, from 721px up. The clauses rise in CSS on first paint;
  // here GSAP draws each leader at one speed (so longer lines take longer) and
  // brings in its discipline as the line arrives. GSAP is fetched only for
  // this layout; phones use a CSS sequence and never download it. Without
  // GSAP, or with reduced motion, the hero is shown in its final state.
  const hero = document.querySelector(".hero[data-motion]");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const wideHero = window.matchMedia("(min-width: 721px)");

  const showHeroFinalState = () => {
    hero.dataset.motion = "done";
  };

  const runHeroSequence = () => {
    const { gsap } = window;
    if (!gsap || hero.dataset.motion !== "pending") {
      showHeroFinalState();
      return;
    }

    const leaders = [...hero.querySelectorAll(".hero-title .leader")];
    const labels = [...hero.querySelectorAll(".hero-notes a")];
    const targets = [...leaders, ...labels];

    // Measure before scaling; offsetWidth ignores transforms.
    const lengths = leaders.map((leader) => leader.offsetWidth);

    gsap.set(leaders, { scaleX: 0, transformOrigin: "left center" });
    gsap.set(labels, { opacity: 0, x: -10 });
    hero.dataset.motion = "running";

    // Start once the outcome clauses have mostly risen, measured from
    // navigation start so a slow script load never stacks extra delay.
    const timeline = gsap.timeline({
      delay: Math.max(0, 0.55 - performance.now() / 1000),
      defaults: { ease: "power3.out" },
      onComplete: () => {
        gsap.set(targets, { clearProps: "transform,opacity" });
        showHeroFinalState();
      }
    });

    leaders.forEach((leader, index) => {
      const duration = gsap.utils.clamp(0.35, 0.85, lengths[index] / 760);
      const at = index * 0.13;
      timeline
        .to(leader, { scaleX: 1, duration, ease: "power2.inOut" }, at)
        .to(labels[index], { opacity: 1, x: 0, duration: 0.5 }, at + duration * 0.78);
    });

    // Keyboard users never wait on the sequence.
    hero.addEventListener("focusin", () => timeline.progress(1), { once: true });
  };

  if (hero) {
    if (reducedMotion.matches || !wideHero.matches) {
      showHeroFinalState();
    } else {
      const script = document.createElement("script");
      script.src = "/assets/vendor/gsap/gsap.min.js?v=3.15.0";
      script.onload = runHeroSequence;
      script.onerror = showHeroFinalState;
      document.head.append(script);
    }
  }
})();
