# GMACOVEI QA Report

Test date: September 24, 2026

## Executive result

The September 2026 redesign passes the repository audit, the JavaScript syntax check, the whitespace check, a computed-contrast scan in both themes, a responsive overflow matrix, keyboard and mobile-menu interaction tests, theme persistence, reduced-motion verification, a no-JavaScript fallback check, and local Lighthouse runs.

Final disposition: **READY FOR PRODUCTION REVIEW**

No deployment, DNS change, hosting change, or external-service change was performed.

## Automated repository checks

`python tools/site_audit.py`

- PASS: 8 HTML pages, 0 findings
- New checks added in this pass: one shared CSS/JS cache version across all shells, the pre-paint `js` class in every shell, no external font services, font files present, and the font licence present
- The new cache-version check was confirmed to fail on a deliberately mismatched shell before the value was restored

`node --check assets/js/site.js`: PASS (exit 0)

`git diff --check`: PASS (exit 0)

## Browser review (Playwright + Chromium, local static server)

Horizontal overflow was measured at 1440, 1280, 1024, 961, 960, 768, 390, 375, and 320 pixels, in light and dark. Every width returned 0 pixels.

Visual review, full page and section by section:

- 1440 × 900: light and dark (hero, Focus, Selected Work, About, RielArt band, Writing, Contact, footer)
- 1024: light (hero, Selected Work, full page)
- 961 / 960: navigation breakpoint, both themes
- 768: light (hero lockup, Selected Work)
- 390 × 844: light and dark, every section
- 320: light (hero, Selected Work, header)
- Secondary routes: 404, Privacy, and a legacy writing fallback at 1440 light and 390 dark (0 px overflow)

Issues found and fixed during review:

- The RielArt plate frame rendered as broken dashes, because `pathLength` combined with `non-scaling-stroke` misbehaves in Chromium. It is now a solid frame with a clip-path reveal.
- The frame line crossed the plate content on phones; padding and inset were corrected.
- The blue R mark had too little contrast on the blue relationship band, so it was removed from that band.
- "portal.rielart.com" appeared twice in the Portal chapter; the plate label now reads "Approved clients only".
- Headline tracking was too tight at display and phone sizes; small headings now use the normal font width.
- The dark-mode RielArt plate was too close to the page background and was lifted.

## Interaction and accessibility

- Skip link: first Tab focuses it, it is visible at the top of the viewport, and Enter moves focus to `main`.
- Mobile menu: opens with `aria-expanded="true"`, locks body scroll, and focuses Work. Shift+Tab wraps to RielArt and Tab wraps back to Work. Escape closes it and returns focus to the Menu button. Choosing About closes the menu, releases the lock, and scrolls to `#about`. Resizing to desktop while it is open closes it.
- The Menu button's visible label is part of its accessible name (WCAG 2.5.3), and the theme button updates its `aria-label` and `aria-pressed`.
- Desktop anchors: Work, About, Writing, and Contact each set exactly one `aria-current="location"`.
- Theme: dark persists across a reload and onto `/privacy-policy/`.
- Writing rows: the whole row is clickable, the focus ring outlines the entire row, and the link names include "(read on RielArt, opens in a new tab)".
- Headings: one H1 per page. Principles moved to H4 beneath the "How I work" H3.
- No JavaScript (390 px): the primary navigation stays visible, with 0 px overflow.
- Reduced motion: frame animations compute to `none` and scroll behaviour to `auto`. With motion allowed, they compute to `frame-draw` / `frame-wipe` and `smooth`.

Computed contrast, minimum across all visible text:

| Route | Light | Dark |
|---|---|---|
| `/` (148 text elements) | 5.65:1 | 6.50:1 |
| `/privacy-policy/` | 5.65:1 | 7.07:1 |
| `/404.html` | 5.86:1 | 7.07:1 |
| `/blog/` | 5.86:1 | 7.07:1 |

## Lighthouse 12 (local `python -m http.server`, headless Chromium)

| Preset | Performance | Accessibility | Best Practices | SEO | LCP | CLS | TBT |
|---|---|---|---|---|---|---|---|
| Mobile | 98 | 100 | 100 | 100 | 2.3 s | 0 | 0 ms |
| Desktop | 100 | 100 | 100 | 100 | 0.5 s | 0 | 0 ms |

The first mobile run measured CLS 0.114. The cause was a latent issue that also existed in the previous design: the no-JavaScript navigation fallback appeared until the deferred script added the `js` class. The class is now set in the inline head script before first paint, which brought CLS to 0.

The remaining Lighthouse suggestions (text compression, cache TTL) come from the local Python server, not the site; GitHub Pages serves compressed, cached assets.

## Payload

- CSS: 38,063 bytes raw / 8,169 gzip (previously 27,573 raw)
- JavaScript: 5,230 bytes raw / 1,687 gzip
- Homepage HTML: 26,621 bytes raw / 6,178 gzip
- Fonts: 81,672 bytes total (Instrument Sans variable 57,332; Newsreader Italic 24,340). Only the sans file is preloaded.
- Images: unchanged. The hero portrait is the existing 66 KB WebP with explicit dimensions and high fetch priority; the RielArt logos are lazy-loaded.

## Routes, SEO, and legacy behaviour

Preserved: the homepage title, description, canonical, Open Graph and X metadata, JSON-LD graph, `index,follow`, and the approved H1 and focus phrase; `noindex,follow` on legal, 404, and legacy fallbacks; external canonicals, meta refresh, and visible continuation links on the fallbacks; CNAME, robots.txt, `_redirects`, and `_config.yml` exclusions. The sitemap `lastmod` was updated to 2026-09-24.

## Limitations

- rielart.com, portal.rielart.com, and gmacovei.com were unreachable from the test container, so external destinations were not re-verified in this pass (they were last verified on August 26, 2026).
- Safari and Firefox were not available. Scroll-driven animation is progressive (it is gated behind `@supports`), and everything else uses broadly supported CSS.
- Screen-reader output was checked structurally, not with a physical screen reader. Zoom at 200% / 400% was not emulated.
- Lighthouse ran against a local server; production numbers depend on GitHub Pages or CDN delivery.
