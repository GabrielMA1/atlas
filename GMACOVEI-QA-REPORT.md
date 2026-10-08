# GMACOVEI QA Report

Test date: October 8, 2026

## Executive result

The October 2026 redesign passes all of the following:

- the repository audit
- the JavaScript syntax and whitespace checks
- a computed-contrast scan in both themes
- a responsive overflow matrix
- keyboard and mobile-menu interaction tests
- theme persistence
- reduced motion
- the no-JavaScript fallback
- local Lighthouse runs

Final disposition: **READY FOR PRODUCTION REVIEW**

No deployment, DNS change, hosting change, or external-service change was performed.

## Automated repository checks

- `python tools/site_audit.py`: PASS. 8 HTML pages, 0 findings.
- `node --check assets/js/site.js`: PASS.
- `git diff --check`: PASS.

## Browser review (Playwright + Chromium, local static server)

Horizontal overflow was measured at 320, 360, 390, 600, 768, 820, 961, 1024, 1180, 1280, 1440, and 1920 pixels. Every width returned 0 px.

The hero headline was measured at every width above. It renders as exactly four single lines (one per clause) at all of them.

Visual review covered the following:

- **1440 × 900, light and dark:** full page, every section, and scroll-through frames
- **1280 × 720 and 1024 × 768:** hero fit
- **820 × 1180:** tablet, light and dark
- **390 × 844, light and dark:** every section
- **320:** hero and header
- **Secondary routes:** Privacy, 404, and a legacy writing fallback. The fallback was rendered with its meta refresh removed, because the RielArt target is unreachable from the test container.

Issues found and fixed during review:

- **Hero headline:** it broke into six lines at 1440px, splitting the four-clause structure. It is now sized from its column width (`11.6cqi`) and from viewport height (`9svh`).
- **Hero on short viewports:** at 1280 × 720 the hero overflowed the viewport. It now fits, and the paper below the field is visible.
- **Portrait crop:** the desk filled about a sixth of the portrait. It was recropped so only the desk's front edge remains, which now meets the field's edge.
- **Tablet hero:** the portrait hung left-aligned in a single column. The two-column hero now holds down to 721px.
- **Inline lists:** they wrapped one item per line with dangling separators on phones. They are now set as running text.
- **Section rules:** rules between paper sections were inconsistent (some full-bleed, some container-width). They are now all container-width.
- **Dark-mode header:** the G mark was nearly invisible. It is now a knockout.
- **320px header:** the name wrapped onto two lines. The Menu button is icon-only at 360px and below, and keeps "Menu" as its accessible name.
- **Legal pages:** the body text was centred instead of aligned with the title.

## Interaction and accessibility

- **Skip link:** hidden until focused. The first Tab reveals it at the top of the viewport.
- **Mobile menu:**
  - Opening it sets `aria-expanded="true"` and moves focus to Work.
  - Tab and Shift+Tab are trapped inside the menu.
  - Escape closes it and returns focus to the Menu button.
- **Focus rings:** every control has a 3px focus ring. It is white on the cobalt field and cobalt (dark theme: pale blue) on paper.
- **Theme:**
  - Dark mode persists across a reload and onto `/privacy-policy/`.
  - The theme toggle updates its `aria-label` and `aria-pressed`.
- **Writing rows:** the whole row is clickable, and link names include "(read on RielArt, opens in a new tab)".
- **Headings:**
  - One H1 per page.
  - Homepage H2s mark the sections.
  - H3s mark focus areas, RielArt, the "How I work" and "Skills in practice" groups, articles, and contact routes.
  - H4s mark the Client Portal and the four principles.
- **No JavaScript (390px):** the primary navigation stays visible, with 0 px overflow.
- **Reduced motion:** scroll behaviour computes to `auto` and transitions to roughly 0.

Computed contrast, lowest value across all visible text:

| Route | Light | Dark |
|---|---|---|
| `/` | 5.61:1 | 5.95:1 |
| `/privacy-policy/` | 5.61:1 | 5.95:1 |
| `/404.html` | 5.61:1 | 5.95:1 |

No text element falls below its WCAG AA threshold.

## Lighthouse 12.6 (local `python -m http.server`, headless Chromium)

| Preset | Performance | Accessibility | Best Practices | SEO | LCP | CLS | TBT |
|---|---|---|---|---|---|---|---|
| Mobile | 98 | 100 | 100 | 100 | 2.0 s | 0 | 120 ms |
| Desktop | 100 | 100 | 100 | 100 | 0.4 s | 0 | 0 ms |

## Payload

- CSS: 23,873 bytes raw / 6,131 gzip (previously 38,063 raw)
- JavaScript: 5,230 bytes raw / 1,687 gzip (unchanged)
- Homepage HTML: 21,818 bytes raw / 5,477 gzip (previously 26,621 raw)
- Fonts: 33,996 bytes, one preloaded file (previously 81,672 bytes across two files)
- Images: the hero uses a new 42.7 KB 640 × 800 WebP crop with explicit dimensions and high fetch priority. The footer uses a 4 KB white knockout G.

## Routes, SEO, and legacy behaviour

The following are preserved:

- **Homepage:** title, description, canonical, Open Graph and X metadata, JSON-LD graph, `index,follow`, and the approved H1 and focus phrase
- **Legal, 404, and legacy fallbacks:** `noindex,follow`
- **Legacy fallbacks:** external canonicals, meta refresh, and visible continuation links
- **Site files:** CNAME, robots.txt, sitemap, `_redirects`, and `_config.yml` exclusions

The `#business` anchor was removed with its section. No navigation, footer, or internal link pointed to it.

## Limitations

- rielart.com, portal.rielart.com, and gmacovei.com were unreachable from the test container, so external destinations were not re-verified in this pass.
- Safari and Firefox were not available. The layout relies on container-query units, `:has()`, and `text-wrap`, all supported in current evergreen browsers.
  - Without container queries, the headline falls back to a viewport-based size.
  - Without `:has()`, pages without a contact band show one extra rule above the footer.
- Screen-reader output was checked structurally, not with a physical screen reader.
- Lighthouse ran against a local server. Production numbers depend on GitHub Pages or CDN delivery.
