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
