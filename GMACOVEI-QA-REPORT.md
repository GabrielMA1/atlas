# GMACOVEI QA Report

Test date: August 26, 2026

## Executive result

The complete personal-brand redesign passes the repository audit, JavaScript syntax validation, HTML/link/ARIA checks, computed light/dark contrast review, responsive overflow matrix, theme persistence, mobile-menu keyboard behavior, anchor navigation, local route checks, external RielArt destination checks, payload review, and tracked-file privacy scan.

Final disposition: **READY FOR PRODUCTION REVIEW**

This status means the local clone is ready for stakeholder and deployment review. No deployment, push, DNS change, hosting change, form submission, or third-party account change was performed.

## Automated repository checks

`tools/site_audit.py` (executed with the workspace-bundled Python 3 runtime)

- PASS
- 8 HTML pages audited
- 0 findings
- Required routes, titles, descriptions, canonicals, indexability, schema, sitemap parity, local assets, internal anchors, image dimensions, external-link security, approved positioning, commercial routing, legacy fallbacks, and deployment exclusions passed

`node --check assets/js/site.js`

- PASS
- Exit code 0

`git diff --check`

- PASS
- Exit code 0
- PowerShell/Git reported informational LF-to-CRLF normalization warnings only

Independent HTML audit:

- 8 of 8 pages have exactly one H1
- 37 IDs checked; no duplicates
- 183 local references resolved, including 97 fragment references
- 8 `aria-controls` values point to existing IDs
- 43 `_blank` links include `noopener noreferrer`
- 19 images have alt text and numeric width/height attributes
- All 8 pages use one CSS and one JavaScript reference with the same `?v=20260901final1` cache version

## Browser and responsive review

The homepage was rendered and measured in both light and dark mode at these viewport widths:

- 1600, 1440, 1366, 1280, 1180, 1101, 1100, 1099, and 1080 pixels
- 1024, 861, 860, 859, 820, and 768 pixels
- 621, 620, 619, 430, 390, 375, 360, and 320 pixels

Focused visual review was completed at:

- 1440 x 900, light and dark
- 1024 x 1024, light
- 768 x 1024, light
- 390 x 844, light and dark
- 320 x 844, light

Section-level pixel review covered Work and Contact at 1101, 1100, and 1099 pixels; Focus, Work, About, Writing, and Contact around 861/860/859 pixels; Writing and Contact around 621/620/619 pixels; the complete section sequence at 320 pixels; and the footer at representative desktop, tablet, and phone boundaries in both themes.

At every measured width:

- document horizontal overflow was 0 pixels
- the hero remained within the layout width
- desktop navigation changed to the mobile control at the 1100-pixel breakpoint
- the hero changed from two columns to one column at the 861/860-pixel boundary
- no section, work treatment, writing row, contact route, or footer was clipped
- the exact 1101/1100/1099, 861/860/859, and 621/620/619 transitions changed layout without mixed states

The complete mobile homepage was inspected section by section: Hero, Professional Focus, both Selected Work chapters, About and principles, skills, the RielArt relationship panel, Writing, Contact, and footer.

Secondary-route visual review covered Privacy Policy at 390 pixels, Terms & Conditions at 1440 pixels, the 404 page at 1440 pixels, and `/blog/website-costing-you-leads/` before its redirect.

## Theme behavior

- Light and dark compositions rendered correctly on desktop and phone.
- Theme-button accessible name and `aria-pressed` updated correctly.
- Dark mode persisted after a full reload without reading browser storage directly.
- System color-scheme fallback and change handling remain in the inline initialization and shared script.

## Navigation and keyboard interaction

- Desktop Work, About, Writing, and Contact links moved to their intended sections.
- URL hashes updated to `#work`, `#about`, `#writing`, and `#contact`.
- Exactly one matching desktop link received `aria-current="location"` after each move.
- The mobile menu opened, set `aria-expanded="true"`, removed `hidden`, locked body scrolling, and focused Work.
- Shift+Tab from Work wrapped to the final RielArt link.
- Escape closed the menu, restored body scrolling, reset the accessible label/state, and returned focus to the menu button.
- Selecting About from the mobile menu closed the menu, released the body lock, moved to `#about`, and updated the active state.
- Resizing an open mobile menu to desktop closed it safely before the toggle became hidden.
- No-JavaScript CSS keeps the primary navigation visible and horizontally scrollable below the responsive breakpoint.

## Accessibility

Structural checks confirmed:

- a skip link targeting focusable `main`
- one H1 per page with logical section headings
- labelled navigation and regions
- concise portrait alt text and empty alt text for decorative logos
- valid ARIA control targets
- visible focus styling
- readable DOM order
- accessible theme state
- mobile focus trapping, Escape handling, and focus restoration
- reduced-motion CSS that disables smooth scrolling, transitions, and animations

A computed-style contrast scan checked 133 visible homepage text/link/button elements in each theme and the visible text on legal and fallback layouts. Final minimum tested ratios were:

- Homepage light: 4.91:1
- Homepage dark: 6.40:1
- Legal light: 4.57:1
- Legal dark: 6.40:1

Three issues found during the full review were corrected: small muted writing summaries in light mode, dark-mode skip-link text, and the 320-pixel header brand cap. The legal breadcrumb token was also strengthened to clear 4.5:1.

## Routes, SEO, and legacy behavior

Local HTTP checks returned 200 for:

- `/`
- `/privacy-policy/`
- `/terms-conditions/`
- `/404.html`
- `/blog/website-costing-you-leads/`
- shared CSS, shared JavaScript, and the WebP portrait

Preserved:

- homepage title, description, canonical, indexability, and structured data
- `Digital Presence · Advertising Management · Practical Systems`
- approved H1 and `Digital Professional` schema job title
- one indexable sitemap entry for `https://gmacovei.com/`
- `noindex,follow` on legal, 404, and legacy fallback pages
- external canonicals, visible continuation links, and meta refreshes on legacy fallbacks
- CNAME, robots, redirect documentation, and Jekyll exclusions

The sitemap `lastmod` was updated to `2026-08-26` for the redesigned homepage.

The tested legacy page displayed its local explanation and action, then redirected after two seconds to its matching RielArt article.

## External destinations

Read-only verification found:

- RielArt homepage: 200
- RielArt project inquiry page: 200, with the `project-inquiry` fragment target present
- RielArt Client Portal: 200
- all three current RielArt writing destinations: 200 with matching article titles

LinkedIn returned its automated-request status 999. The same public profile slug is indexed, so it is not treated as broken, but the automated reachability check is recorded as inconclusive.

No link was used to submit a form, send a message, start an email, place a call, log in, or change an external service.

## Performance and payload

Current source payloads:

- HTML: 59,422 bytes across 8 pages
- CSS: 27,573 bytes
- JavaScript: 5,231 bytes
- complete image library: 464,548 bytes across 8 images
- deployable image set after Jekyll exclusions: 232,325 bytes across 6 images
- generated Open Graph JPEG: 74,350 bytes at 1200 x 630

Compared with the immediate pre-redesign baseline:

- CSS decreased from 30,767 to 27,573 bytes
- JavaScript decreased from 5,257 to 5,231 bytes
- deployable images decreased from 266,849 to 232,325 bytes while the social card was refreshed

The homepage has no external font, framework, analytics, animation library, or third-party runtime dependency. The hero portrait is an existing 66,062-byte WebP with explicit dimensions and high fetch priority. Shared JavaScript remains deferred.

Local HTTP transfers returned 200 and completed in approximately 2–19 milliseconds on the loopback server; those timings confirm local delivery only and are not used as public hosting metrics.

The Chrome DevTools performance MCP was unavailable, so no Lighthouse score, Core Web Vitals trace, or lab-performance claim is made.

## Privacy hygiene

A scan across 35 tracked files found:

- 0 sensitive filenames
- 0 local absolute Windows paths
- 0 private-key markers
- 0 known secret formats
- 0 credential assignments
- 0 credential-bearing URLs

The approved public email, phone, LinkedIn, RielArt, and portal destinations remain intentionally present. No private location, token, password, account identifier, unpublished client data, or machine-specific path was added to the site.

## Limitations and production-review items

- Lighthouse/Core Web Vitals tracing was unavailable because the Chrome DevTools MCP is not configured.
- Browser zoom at 200%/400% and an operating-system reduced-motion preference could not be emulated; their markup/CSS paths were inspected, but a physical manual pass is still appropriate.
- First-Tab skip-link traversal was not reliably emulated by the available in-app browser, although the link, target, focusability, focus style, and mobile keyboard loop were verified.
- Automated LinkedIn reachability is inconclusive because LinkedIn blocks the test client.
- Live CDN caching, compression, security headers, redirects, analytics absence, and deployment exclusions must be confirmed after an authorized deployment.
- Standard GitHub Pages does not process `_redirects`; static fallback pages remain the guaranteed behavior unless the active hosting layer implements redirects.

## Final disposition

**READY FOR PRODUCTION REVIEW**
