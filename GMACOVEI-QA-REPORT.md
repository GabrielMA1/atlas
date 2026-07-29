# GMACOVEI QA Report

Test date: July 29, 2026

## Executive result

The rebuilt and content-aligned static site passes the repository audit, JavaScript syntax check, route checks, browser console check, responsive viewport matrix, theme and mobile-menu interaction tests, card-alignment checks, and external destination verification.

Final disposition: **CONDITIONAL PASS — READY AFTER LISTED CHECKS**

The remaining checks require browser or platform capabilities unavailable in the current automated environment and are listed at the end of this report.

## Visual and copy refinement regression

The July 29, 2026 refinement pass confirmed:

- The portrait retains its approved alt text, 720 × 720 source dimensions, crop, and loading behavior; its visible caption and complete `figcaption` wrapper are removed.
- The hero headline is `I help businesses look better online, reach more people, and work smarter.`
- At 1280, 1440, and 1920 pixels, the headline resolves to the same three balanced lines without an isolated one-word line.
- At tablet and mobile widths, the headline wraps naturally without document-level horizontal overflow.
- Desktop and mobile primary navigation use Work, About, Writing, Contact on every HTML route.
- Work and About anchor navigation still updates the URL fragment and active-navigation state correctly.
- The visible capability disclaimer is removed without an empty wrapper.
- The footer wordmark text centre remained within three pixels of the footer centre across the full viewport matrix, remained `aria-hidden`, and retained `pointer-events: none`.
- At desktop widths, both Selected Work cards have equal outer heights; the two primary actions share the same vertical coordinate; and both preview panels share the same top coordinate and 430-pixel minimum height.
- At stacked widths, the cards retain natural content height and report no content clipping.
- No external destination, approved focus label, metadata value, structured-data value, portrait asset, or JavaScript behavior changed.

## Content-alignment regression update

The July 28, 2026 regression pass confirmed:

- The hero eyebrow uses `Digital Presence · Advertising Management · Practical Systems`.
- The then-approved headline was unchanged during that content-only pass; the July 29 refinement above supersedes it.
- The hero support, focus cards, About copy, skills, metadata, Open Graph copy, X copy, Person schema, accessible list labels, and shared footer descriptions align with the approved focus model.
- `Advertising Management` is used consistently; `Ads Management` is not present.
- Business IT, cloud tools, integrations, automation, and practical AI remain supporting details beneath Practical Systems.
- Advertising scope remains focused on Google Search or Meta advertising without guarantees, unlimited-platform claims, pricing, or package cards.
- Commercial brand, website, and advertising inquiries still route to `https://rielart.com/contact/#project-inquiry`.
- RielArt and Client Portal roles and destinations remain unchanged.
- No CSS, JavaScript, portrait, navigation, or layout change was made for this update.

## Automated repository audit

Command: `python tools/site_audit.py`

Result: PASS

- 8 HTML pages parsed
- Required routes present
- One H1 per page
- Titles and descriptions present
- Canonicals correct
- JSON-LD parsed with Person, WebSite, and Organization types
- Internal links and homepage anchors valid
- Referenced local assets present
- Images have alt, width, and height attributes with matching aspect ratios
- External `target="_blank"` links protected with `noopener noreferrer`
- Mail links do not use `target="_blank"`
- Indexable/noindex rules correct
- Sitemap matches the indexable canonical set
- Legacy fallback canonicals and visible continuation links correct
- No duplicate IDs
- No flagged outdated public positioning
- Approved hero phrase and three focus headings present
- Homepage metadata and social metadata match the approved positioning
- Person `jobTitle` and exact approved `knowsAbout` vocabulary present
- RielArt commercial inquiry route preserved
- Refined hero headline present and prior public headline absent
- Portrait `figcaption` and capability disclaimer absent
- Desktop and mobile navigation order verified on all eight routes
- Two structural Selected Work action regions present
- Decorative footer wordmark remains `aria-hidden`
- Deployment exclusions present
- CSS braces balanced

## JavaScript

`node --check assets/js/site.js`

Result: PASS

Browser console review:

- Homepage errors/warnings: 0
- Secondary-route errors/warnings: 0

## Routes tested

Each route was tested at 1024 × 768 and 320 × 568.

| Route | H1 | Robots | Horizontal overflow |
|---|---:|---|---|
| `/` | 1 | `index,follow` | None |
| `/privacy-policy/` | 1 | `noindex,follow` | None |
| `/terms-conditions/` | 1 | `noindex,follow` | None |
| `/404.html` | 1 | `noindex,follow` | None |
| `/blog/` | 1 | `noindex,follow` | None |
| `/blog/ai-chatbots-cut-support-costs/` | 1 | `noindex,follow` | None |
| `/blog/website-costing-you-leads/` | 1 | `noindex,follow` | None |
| `/blog/direct-mail-outperforms-digital-ads-toronto/` | 1 | `noindex,follow` | None |

## Responsive viewport matrix

The homepage was measured in the browser at:

- 320 × 568
- 360 × 800
- 390 × 844
- 430 × 932
- 768 × 1024
- 1024 × 768
- 1280 × 720
- 1440 × 900
- 1920 × 1080

At every tested viewport:

- No horizontal overflow was detected.
- The H1 remained inside the viewport.
- The portrait loaded at its natural 720 × 720 dimensions.
- Mobile navigation replaced desktop navigation at the intended breakpoint.
- No visible interactive target measured below the WCAG 2.2 AA 24 × 24 CSS-pixel minimum.

Visual inspection was completed for desktop and mobile hero layouts, professional-focus cards, selected-work treatments, the RielArt relationship panel, writing cards, contact cards, and footer.

## Card alignment

At 1440 × 900:

- All three professional-focus cards had matching top, bottom, and 507-pixel height measurements.
- Description regions remained comparable and list areas stayed aligned.
- Both selected-work cards had matching top, bottom, and height measurements.
- Selected Work actions shared the same top coordinate.
- Selected Work previews shared the same top coordinate and 430-pixel height.
- All three writing cards had matching heights and action positions.
- All three contact cards had matching heights and action positions.

Across the mobile viewport matrix, focus cards stacked naturally, used content-driven heights, and reported no scroll-height clipping.

## Theme and navigation interactions

Result: PASS

- Light theme rendered correctly.
- Dark theme rendered correctly.
- Theme toggle label and `aria-pressed` state updated.
- Dark preference persisted after reload.
- Mobile menu opened and moved focus to Work, the first visible link.
- Shift+Tab from the first menu link wrapped to the final link.
- Escape closed the menu.
- Focus returned to the menu button.
- Body scrolling was locked only while the menu was open.
- Scroll-aware active navigation updated across Work, About, Writing, and Contact.

## Accessibility review

Confirmed:

- Skip link is present and points to a focusable `main`.
- One H1 per page and logical H2/H3 hierarchy.
- Landmark and navigation labels present.
- Portrait alt text is concise and factual.
- Decorative logos use empty alt text.
- External link purpose and destination are visible.
- Email remains a standard `mailto:` link.
- Mobile-menu focus trapping, Escape handling, and focus restoration passed.
- Focus-visible styling is defined.
- Reading order matches DOM order.
- Reduced-motion CSS removes transitions/animations and the script bypasses reveal observation when reduction is requested.

Contrast calculations for representative smallest-text colour pairs:

- Light muted text on soft surface: 4.74:1
- Light accent link on soft surface: 5.20:1
- Light body text on page background: 9.12:1
- Dark muted text on dark surface: 7.04:1
- Dark accent link on dark page: 7.80:1
- Dark-theme primary button text: 7.80:1
- Footer secondary text: 5.82:1

## External destinations

Live browser verification confirmed:

- RielArt homepage uses the current Brand & Website Launch and Focused Ads Management model.
- `https://rielart.com/contact/#project-inquiry` exists and contains the `project-inquiry` target.
- RielArt Client Portal is deployed and restricted to approved portal emails.
- All three displayed RielArt article URLs resolve to the matching article titles.
- Both specific legacy article destinations resolve.
- The LinkedIn profile URL resolves.
- The direct email link is exactly `mailto:hello@gmacovei.com`.

## Performance and maintainability

- CSS reduced from 121,874 bytes to approximately 27.5 KB.
- JavaScript reduced from 10,149 bytes to approximately 5.1 KB.
- Header logo reduced from 90,066 bytes to 14,054 bytes.
- RielArt logo reduced from 92,374 bytes to 26,506 bytes.
- Portrait remains a 66,062-byte WebP and was not modified.
- Open Graph image remains a 108,874-byte 1200 × 630 JPEG.
- No external font, JavaScript framework, animation library, form library, or analytics request was added.

Lighthouse was not run because Lighthouse, Chrome CLI, Pa11y, and axe-core were not installed in the available workspace runtime. No Lighthouse score is claimed.

## Deployment behavior

- `CNAME` remains `gmacovei.com`.
- `_config.yml` excludes internal documentation, audit tools, the unused portrait JPG, and the outdated RielArt preview.
- `_redirects` documents the intended permanent redirects.
- Standard GitHub Pages does not process `_redirects`; static fallback pages remain in place.
- A real 301 must be confirmed at the active CDN or hosting layer after deployment.

## Remaining manual checks

Before publishing:

1. Verify the homepage and secondary routes at actual browser zoom levels of 200% and 400%. The browser-control environment could not change browser zoom.
2. Enable the operating system/browser reduced-motion preference and confirm the no-motion experience. The CSS and JavaScript paths were inspected, but the browser-control environment could not emulate the media preference.
3. Run one physical keyboard pass beginning with the first Tab press to confirm the skip link is visibly revealed, moves focus to `main`, and the desktop navigation proceeds through Work, About, Writing, and Contact. The markup order, target, and focus styles are correct, and the mobile keyboard loop passed, but first-focus and desktop-Tab emulation were unreliable in the browser-control environment.
4. Confirm the live deployment serves the expected files and excludes internal material.
5. Confirm server/CDN response headers for the four legacy routes if real HTTP 301 redirects are required.

## Final disposition

**CONDITIONAL PASS — READY AFTER LISTED CHECKS**
