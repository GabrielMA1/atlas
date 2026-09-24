# GMACOVEI Implementation Log

Implementation date: July 28, 2026

## Baseline

- Eight HTML routes
- 121,874-byte stylesheet containing several stacked design systems
- 10,149-byte script containing theme, menu, FAQ, contact tabs, form state, blog filters, pointer glow, reveal, and duplicated navigation behavior
- Package-led homepage positioning
- Outdated RielArt AI-systems wording
- Indexable legal pages
- Static legacy fallbacks plus an `_redirects` file that GitHub Pages does not process

## Strategy and architecture

Created the strategy, information architecture, copy map, and URL migration plan before production changes. The personal site now has a distinct role from RielArt and the Client Portal.

## Homepage implementation

Rebuilt the homepage as:

1. Personal hero
2. Professional focus
3. Selected work and products
4. About and working approach
5. RielArt relationship
6. Writing
7. Contact routing
8. Footer

Removed:

- Digital Presence and AI & Automation package cards
- Generic industry grid
- Generic outcome cards
- Service-style FAQ
- Repeated RielArt proof points
- Hero email and LinkedIn buttons

## Selected work decisions

- Included RielArt as a labelled Business item.
- Replaced the outdated RielArt preview with a text-based interface treatment.
- Included the deployed Client Portal as a labelled Product item.
- Limited portal claims to progress, milestones, updates, requests, and approved-email access.
- Did not add a fabricated third project.

## Metadata and schema

- Updated title, description, canonical, Open Graph, and X metadata.
- Preserved the 1200 × 630 Open Graph image.
- Replaced the old `Digital Strategist & AI Expert` schema title.
- Added a Person, WebSite, and RielArt Organization graph.
- Used a broad Toronto Place and an affiliation/founder relationship.
- Removed street-address, LocalBusiness, awards, credentials, and exclusive-employer implications.

## Legal and legacy routes

- Set Privacy and Terms to `noindex,follow`.
- Updated Privacy to state that no personal inquiry form or analytics exists.
- Updated Terms to keep commercial scope on RielArt.
- Set 404 and all legacy fallbacks to `noindex,follow`.
- Gave each fallback a descriptive title, external canonical, meta refresh, and visible continuation link.
- Reduced the sitemap to the indexable canonical homepage.

## CSS and JavaScript cleanup

- Replaced the layered inherited stylesheet with one maintainable personal-site design system.
- Removed pricing, forms, contact tabs, FAQ, service-page, portal-page, blog-filter, and pointer-glow styling.
- Removed FAQ, contact-tab, form-submit, blog-filter, and pointer-glow JavaScript.
- Retained only theme persistence, mobile navigation and focus handling, active navigation, restrained reveal behavior, header state, and current year.

## Image work

- Preserved the portrait without modification.
- Confirmed portrait dimensions at 720 × 720.
- Preserved the Open Graph image at 1200 × 630.
- Reduced `logo.png` from 512 × 512 / 90,066 bytes to 160 × 160 / 14,054 bytes.
- Reduced `rielart-logo.png` from 512 × 512 / 92,374 bytes to 256 × 256 / 26,506 bytes.
- Excluded the unused JPG portrait duplicate and outdated RielArt preview from the GitHub Pages build.

## Deployment controls

- Added `_config.yml` exclusions for internal documentation, audit tools, and unused production images.
- Preserved `CNAME`, `robots.txt`, `sitemap.xml`, and `_redirects`.
- Added `GMACOVEI-DEPLOYMENT-MANIFEST.txt`.

## Audit tooling

Added `tools/site_audit.py` using Python standard-library parsing. It checks:

- Required routes
- Metadata and one-H1 rules
- Canonicals and indexability
- Internal links and anchors
- Missing assets and image ratios
- Alt attributes
- JSON-LD parsing and required graph types
- Sitemap parity
- Legacy fallback behavior
- External new-tab protection
- Mail-link target behavior
- Duplicate IDs
- Outdated public positioning
- Deployment exclusions
- CSS brace balance

## File-by-file production changes

- `index.html` — complete homepage, metadata, and schema rebuild
- `assets/css/site.css` — complete visual-system replacement
- `assets/js/site.js` — interaction cleanup and accessibility-focused menu behavior
- `privacy-policy/index.html` — legal copy, indexability, and shared layout
- `terms-conditions/index.html` — legal copy, indexability, and shared layout
- `404.html` — noindex recovery page and shared layout
- `blog/index.html` — descriptive RielArt library fallback
- `blog/ai-chatbots-cut-support-costs/index.html` — descriptive article fallback
- `blog/website-costing-you-leads/index.html` — descriptive article fallback
- `blog/direct-mail-outperforms-digital-ads-toronto/index.html` — library fallback where no one-to-one replacement exists
- `sitemap.xml` — indexable homepage only
- `_config.yml` — GitHub Pages exclusions
- `README.md` — current role, local preview, audit, and deployment
- `REDESIGN-NOTES.md` — neutral personal editorial design description
- `images/logo.png` — production resize and optimization
- `images/rielart-logo.png` — production resize and optimization

## Content-alignment update

On July 28, 2026, the approved primary focus model changed from Digital Strategy, IT Systems, and Practical AI to:

1. Digital Presence
2. Advertising Management
3. Practical Systems

The update preserved the visual system, layout, portrait, navigation, themes, responsive behavior, accessibility behavior, performance profile, RielArt relationship, Client Portal description, article destinations, and URL structure.

Business IT, cloud tools, integrations, automation, and practical AI remain supporting details beneath Practical Systems. Advertising Management is limited to focused Google Search or Meta advertising. No prices, packages, guarantees, checkout behavior, or additional commercial CTAs were added.

### Files modified for the content-alignment update

- `index.html` — hero, focus cards, supporting copy, skills, metadata, social metadata, Person schema, accessibility labels, and footer positioning
- `404.html` — shared footer positioning
- `privacy-policy/index.html` — shared footer positioning
- `terms-conditions/index.html` — shared footer positioning
- `blog/index.html` — shared footer positioning
- `blog/ai-chatbots-cut-support-costs/index.html` — shared footer positioning
- `blog/website-costing-you-leads/index.html` — shared footer positioning
- `blog/direct-mail-outperforms-digital-ads-toronto/index.html` — shared footer positioning
- `GMACOVEI-STRATEGY.md` — approved positioning and scope rules
- `GMACOVEI-COPY-MAP.md` — hero, focus, advertising scope, and footer copy map
- `GMACOVEI-INFORMATION-ARCHITECTURE.md` — approved focus-card labels and supporting hierarchy
- `README.md` — current site-role summary
- `tools/site_audit.py` — approved-positioning, social metadata, schema vocabulary, and commercial-routing assertions
- `GMACOVEI-QA-REPORT.md` — content-alignment regression results
- `GMACOVEI-IMPLEMENTATION-LOG.md` — complete update record and file list

## Visual and copy refinement

On July 29, 2026, a narrow production refinement:

- Removed the visible caption beneath the hero portrait while preserving the image, alt text, dimensions, crop, loading behavior, and responsive treatment.
- Replaced the hero headline with: `I help businesses look better online, reach more people, and work smarter.`
- Reordered primary navigation to Work, About, Writing, Contact across desktop and mobile markup on all routes.
- Removed the visible capability-area disclaimer beneath Professional Focus.
- Centered the decorative footer wordmark through a footer-relative inset layer with grid centering, predictable stacking, low contrast, `aria-hidden`, and disabled pointer interaction.
- Grouped each Selected Work action into an equivalent structural region and equalized the desktop preview minimum so card actions and previews align without filler content, JavaScript measurement, or clipping.
- Preserved the approved focus areas, section order, supporting copy, metadata, structured data, external routes, theme behavior, and static architecture.

### Files modified for the visual and copy refinement

- `index.html` — headline, portrait-caption removal, navigation order, disclaimer removal, and Selected Work action regions
- `assets/css/site.css` — hero wrapping, portrait spacing cleanup, work-card alignment, and centered footer wordmark
- `404.html` — shared desktop and mobile navigation order only
- `privacy-policy/index.html` — shared desktop and mobile navigation order only
- `terms-conditions/index.html` — shared desktop and mobile navigation order only
- `blog/index.html` — shared desktop and mobile navigation order only
- `blog/ai-chatbots-cut-support-costs/index.html` — shared desktop and mobile navigation order only
- `blog/website-costing-you-leads/index.html` — shared desktop and mobile navigation order only
- `blog/direct-mail-outperforms-digital-ads-toronto/index.html` — shared desktop and mobile navigation order only
- `GMACOVEI-STRATEGY.md` — approved hero headline
- `GMACOVEI-COPY-MAP.md` — navigation, hero, focus, and Selected Work refinement record
- `GMACOVEI-INFORMATION-ARCHITECTURE.md` — primary navigation order and hero content
- `tools/site_audit.py` — headline, portrait-caption, disclaimer, work-action, wordmark, and navigation-order assertions
- `GMACOVEI-QA-REPORT.md` — refinement regression results
- `GMACOVEI-IMPLEMENTATION-LOG.md` — exact change record and file list

## Complete personal-brand redesign

On August 26, 2026, the local test clone received a complete art-direction, UX, frontend, accessibility, and responsive redesign while preserving the approved content, route, SEO, legal, and static-hosting contracts.

### Direction and composition

- Reframed the site around a portrait-led warm-stone, paper, ink, navy, and GMACOVEI-blue system.
- Derived a restrained open, stepped aperture from the GMACOVEI G and used it in the portrait crop, selected-work imagery, and RielArt relationship panel.
- Rebuilt the hero with portrait left and exact approved positioning right on desktop, then copy before portrait on mobile.
- Replaced the numbered Focus cards with one continuous navy field and staggered, rule-led content.
- Replaced matching Selected Work cards with alternating full-width chapters for RielArt and the Client Portal.
- Rebuilt About, principles, skills, Writing, Contact, legal, 404, and fallback treatments around open layout, rules, and controlled spacing.
- Kept RielArt visually important without turning the personal site into an agency landing page.

### Removed patterns

- Numbered focus, principle, and contact systems
- Fake portal status, progress, phase, security, and pseudo-dashboard UI
- Universal reveal animations and IntersectionObserver choreography
- Repeated rounded cards, skill pills, decorative halos, backdrop blur, hover lift, and oversized footer wordmark
- Technical telemetry, control-panel, command-line, and architecture-diagram language
- Generic AI glow, glass, gradient, neon, or futuristic motifs

### Frontend and accessibility

- Replaced the shared stylesheet with one 27.6 KB responsive design system.
- Replaced the shared script with a 5.2 KB theme/navigation implementation without reveal logic.
- Preserved theme persistence and added live system-theme response when no explicit preference is stored.
- Added safe mobile-menu cleanup when resizing to desktop.
- Preserved focus entry, focus trapping, Escape close, focus restoration, body lock, and active-section navigation.
- Kept primary navigation available below 1100 pixels when JavaScript is unavailable.
- Strengthened muted light-mode text and dark-mode skip-link contrast after computed-style testing.
- Increased the 360-pixel-and-below header brand cap so the complete Gabriel Macovei name remains visible at 320 pixels.
- Kept reduced-motion rules for scrolling, transitions, and animations.

### Metadata, routes, and imagery

- Preserved title, description, canonical, indexability, schema vocabulary, legal rules, and all approved routes.
- Added the Apple touch icon to the four legacy fallback shells.
- Replaced visible `ERROR 404` language with a human-readable `Page not found` label.
- Applied one `?v=20260901final1` cache version to CSS and JavaScript across all eight HTML shells after the final shared-CSS refinement.
- Regenerated the Open Graph image with the built-in image-generation tool using the exact current positioning, portrait-led composition, and open-frame brand cue.
- Converted the generated card to an optimized 1200 x 630 JPEG, reducing it from 108,874 to 74,350 bytes.
- Updated the homepage sitemap `lastmod` to August 26, 2026.

### Validation completed during the redesign pass

- Static audit: PASS, 8 pages, 0 findings
- JavaScript syntax: PASS
- Git whitespace check: PASS
- Independent link, fragment, ARIA, image, and cache-version audit: PASS
- Responsive overflow and required light/dark visual review: PASS
- Theme persistence, desktop anchors, active navigation, mobile focus loop, Escape, link close, and resize cleanup: PASS
- Homepage and utility computed contrast checks: PASS
- External RielArt destinations and writing URLs: PASS
- Tracked-file privacy hygiene scan: PASS

No deployment, push, DNS, hosting, form submission, login, third-party account, or external service change was performed.

### Files modified for the redesign

- `index.html`
- `assets/css/site.css`
- `assets/js/site.js`
- `images/gabriel-macovei-og.jpg`
- `404.html`
- `privacy-policy/index.html`
- `terms-conditions/index.html`
- `blog/index.html`
- `blog/ai-chatbots-cut-support-costs/index.html`
- `blog/website-costing-you-leads/index.html`
- `blog/direct-mail-outperforms-digital-ads-toronto/index.html`
- `sitemap.xml`
- `REDESIGN-NOTES.md`
- `GMACOVEI-QA-REPORT.md`
- `GMACOVEI-IMPLEMENTATION-LOG.md`

## 2027-readiness redesign

On September 24, 2026, the site received a full art-direction, typography, layout, and frontend refinement. The approved positioning, routing, metadata, schema, legal and legacy routes, and static architecture were kept. The design rationale is in `REDESIGN-NOTES.md`; validation is in `GMACOVEI-QA-REPORT.md`.

### Direction

- Concept: "the open frame and the three clauses". The approved headline sets as four lines, and its three clauses introduce the three focus areas.
- Replaced the repeated stepped clip-path panels with a thin open line frame taken from the GMACOVEI mark and OG card. It is used only around the portrait, the RielArt plate, and the 404 / legacy cards.
- New hero: copy and portrait on desktop; a portrait-and-name lockup on tablet and phone, with the full statement and both actions in the first phone viewport.
- Selected Work became two chapters: an ink RielArt plate using the real R mark and an oversized wordmark, and a typographic Client Portal plate. Each chapter adds one short factual note on how it is shaped.
- Added a "Three sites, three jobs" list to the RielArt relationship band.
- Writing now uses a sticky heading column and whole-row article links. Contact became a navy closing band with route rows.
- Unified header, mobile menu, and footer across all eight shells; the footer now includes Contact and the Client Portal.

### Typography

- Self-hosted Instrument Sans (variable width and weight) and Newsreader Italic, both SIL OFL, replacing the Windows-only Aptos stack. A metric-adjusted fallback face is included, and the sans file is preloaded.

### Technical

- Rewrote `assets/css/site.css` as one token-driven system with separately art-directed light and dark themes.
- `assets/js/site.js`: the menu breakpoint now comes from `matchMedia("(min-width: 961px)")`, and the menu button keeps its visible "Menu" label instead of swapping `aria-label`.
- Inline head script on every shell now adds the `js` class before first paint, removing a layout shift (CLS 0.114 → 0).
- Theme toggle uses drawn SVG sun and moon icons; `theme-color` meta tags were added.
- Cache version `?v=20260924r1` on all eight shells.
- `tools/site_audit.py` gained shared-asset checks (cache-version parity, pre-paint `js` class, font files and licence, no external font services).

### Files modified

- `index.html`
- `404.html`
- `privacy-policy/index.html`
- `terms-conditions/index.html`
- `blog/index.html`
- `blog/ai-chatbots-cut-support-costs/index.html`
- `blog/website-costing-you-leads/index.html`
- `blog/direct-mail-outperforms-digital-ads-toronto/index.html`
- `assets/css/site.css`
- `assets/js/site.js`
- `assets/fonts/instrument-sans-latin-var.woff2` (new)
- `assets/fonts/newsreader-latin-400-italic.woff2` (new)
- `assets/fonts/OFL.txt` (new)
- `tools/site_audit.py`
- `sitemap.xml`
- `README.md`
- `REDESIGN-NOTES.md`
- `GMACOVEI-STRATEGY.md`
- `GMACOVEI-INFORMATION-ARCHITECTURE.md`
- `GMACOVEI-COPY-MAP.md`
- `GMACOVEI-DEPLOYMENT-MANIFEST.txt`
- `GMACOVEI-QA-REPORT.md`
- `GMACOVEI-IMPLEMENTATION-LOG.md`

No deployment, DNS, hosting, or external-service change was performed.
