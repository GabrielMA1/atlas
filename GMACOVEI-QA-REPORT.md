# GMACOVEI QA Report

Test date: October 8, 2026

## Hero refinement (October 9, 2026)

The hero was refined: hierarchy inside the headline, larger disciplines on measured leaders, hover/focus isolation, a phone index, an arrival mark, and a GSAP-sequenced act two on wide screens. Results:

- `python tools/site_audit.py`: PASS, 0 findings (audit unchanged). `node --check assets/js/site.js` and `git diff --check`: pass.
- **Overflow and headline:** 0 px horizontal overflow at 320, 360, 600, 768, 961, 1024, 1180, 1280, and 1920. The headline is four single lines at every width.
- **Leader geometry (721, 800, 960, 1024, 1180, 1280, 1440, 1920):**
  - Every leader ends exactly 20px (tablet) or 24px (desktop) before its discipline.
  - The shortest leader is 68px on tablet and 134px on desktop.
  - Discipline labels sit within 1–3px of their leader's centre line.
  - No label crosses the container edge.
- **Interaction:**
  - Hovering or tabbing to a discipline lights its leader and switches the other clauses to `#94aaf1` (3.65:1 light, 4.06:1 dark).
  - The keyboard focus ring is visible.
  - Enter lands the target 0px below the 72px header and draws the arrival rule.
- **Motion paths:**
  - **Default:** act two hands from CSS to GSAP and clears its inline styles.
  - **Reduced motion:** static from the first frame, and GSAP is not requested.
  - **GSAP blocked:** final state immediately.
  - **JavaScript disabled:** everything visible.
  - **Both scripts blocked:** the CSS fallback reveals act two at 2.4s.
  - **Resize from 1440 to 390 mid-sequence:** no errors, and the final state is correct.
  - **GSAP requests:** made only at 721px and up with motion allowed. None at 390px, and none under reduced motion.
  - **CTA timing:** the summary and button are visible from the first frame on every path and width.
- **Console and network:** no console errors, warnings, or failed requests at 1440, 820, or 390, in either theme.
- **Computed contrast:** no failures in either theme.
  - The lowest settled text is 5.61:1 (light) and 5.95:1 (dark).
  - The mid-scroll Focus clause state is 3.33:1 and 3.5:1, on large text.
- **Lighthouse 12.6 (local):**
  - Mobile: 100 / 100 / 100 / 100 (LCP 1.7s, CLS 0, TBT 0ms).
  - Desktop: 100 / 100 / 100 / 100 (LCP 0.5s, CLS 0, TBT 0ms).
  - An intermediate build that loaded GSAP on every device scored 95 on mobile (TBT 220ms); this is why GSAP now loads only at 721px and up.
- **Payload:**
  - `site.js` is 7.8 KB raw / 2.7 KB gzip.
  - CSS is 31.1 KB raw / 8.0 KB gzip.
  - GSAP adds 28.3 KB gzip, and only for wide screens with motion allowed.

## Hero revision (later on October 8, 2026)

The portrait and the hero name/focus lines were removed. The hero became a typographic contents page with clause-to-discipline leaders, a one-time entrance, and two scroll-linked reading aids. The re-run results are below. The rest of this report records the earlier pass the same day.

- `python tools/site_audit.py`: PASS, 0 findings. The audit no longer requires a portrait; if one returns, it must still have no caption.
- Horizontal overflow: 0 px at 320, 360, 600, 768, 961, 1024, 1180, 1280, and 1920. The headline is one line per clause at every width.
- **Hero notes:**
  - Vertical offset between each note and its leader is 0 px at 721, 768, 820, 1024, 1280, 1440, and 1920.
  - No note crosses the container edge.
  - Hovering a note lights only its own leader.
  - Each note link lands its focus item exactly below the 72px header.
- Entrance captured at 250, 700, 1100, and 2200 ms. The headline is readable by about 1 s, and the sequence completes in about 1.9 s.
- **Scroll-linked motion:**
  - The muted focus-clause colour was raised to 3.33:1 (light) and 3.5:1 (dark); the clauses are large text.
  - The principles originally dimmed on entry, which failed contrast for 20px mobile text. They now only move.
- **Computed contrast:** no element fails in either theme. Settled text is at least 5.61:1 (light) and 5.95:1 (dark).
- **Lighthouse 12.6 (local):** 100 / 100 / 100 / 100 on mobile (LCP 1.6 s, CLS 0, TBT 0 ms) and on desktop (LCP 0.4 s, CLS 0, TBT 0 ms).
- **Payload:** CSS 27,957 bytes raw / 7,071 gzip. No hero image is loaded.

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
