# GMACOVEI Personal-Site Design Notes

Updated: September 24, 2026

## Concept: the open frame and the three clauses

The approved headline already contains the site's structure. "I help businesses / look better online, / reach more people, / and work smarter." sets as four even lines, and its three clauses map directly to the three professional focus areas:

- look better online → Digital Presence
- reach more people → Advertising Management
- work smarter → Practical Systems

The hero sets the headline in exactly those four lines on every width, and Professional Focus opens each area with its clause in a serif italic. A visitor reads the promise in the hero and sees the same words again beside the matching area in the next section. No copy was invented for this; it is the approved headline, split.

The second device is the open frame from the GMACOVEI mark and the Open Graph card: a thin line bracket, open on one side, finished with a short blue diagonal step. It appears in only three places: around the hero portrait, inside the RielArt plate in Selected Work, and around the not-found and legacy-writing cards. It is not repeated as a clip-path on every panel.

## Palette and themes

- Light: warm stone background (`#f3f1ec`), paper surfaces, deep ink text, GMACOVEI blue for links, labels, and the frame step.
- Dark: a neutral, warm charcoal base (`#0d1016`) with navy reserved for the contrast bands. Dark mode is art-directed rather than inverted. The navy bands stay distinct from the charcoal page, the portrait is slightly dimmed, the frame turns light grey, and the RielArt plate is lifted so it separates from the page.
- Contrast bands: Professional Focus and Contact use deep navy; the footer uses a darker ink; the RielArt relationship uses a deep GMACOVEI blue band. The page reads as light / dark / light / light / blue / light / dark, with the dark sections opening and closing the page.

## Typography

- **Instrument Sans** (variable weight 400–700, width 75–100%, SIL OFL, self-hosted, 57 KB latin subset) carries the whole system. Display headings use a slightly condensed width (86–88%) for composed line lengths; body copy uses the normal width. Small headings step back to normal width so they never feel cramped.
- **Newsreader Italic** (400, SIL OFL, self-hosted, 24 KB) is reserved for human accents: the three focus clauses, one phrase in the About lead, the "You are here" note, and the skills separators.
- The previous stack depended on Aptos, which is installed only on recent Windows and Office systems; every other platform fell back to a generic sans. Self-hosting one family gives every visitor the same identity with no third-party request. A metric-adjusted local fallback face limits reflow while the font loads, and the sans file is preloaded.
- Small labels are sentence case, not tracked uppercase. There is no monospace.

## Composition by section

- **Header:** G mark and name on the left, navigation and RielArt ↗ on the right, and a drawn sun/moon theme icon. Below 961px it becomes a labelled "Menu" button that opens a full-screen list set in large type.
- **Hero (desktop):** the name and focus line sit above the four-line headline in the left seven columns; the portrait in its open frame takes the right four. The frame draws once on load (skipped with reduced motion).
- **Hero (tablet and mobile):** a portrait-and-name lockup, like a business card, with the focus areas stacked beside the photo, followed by the full four-line headline, summary, RielArt route, and both actions. On a 390 × 844 phone the whole statement and both buttons fit in the first viewport.
- **Professional Focus:** a navy band with three rows. Each row has the clause (serif italic), then the area name and description, then its three details.
- **Selected Work:** two chapters instead of cards. RielArt uses a large ink plate with the real R mark, an oversized RielArt wordmark, and the open frame. The frame opens with the scroll where CSS scroll-driven animation is supported and is simply present elsewhere. The Client Portal uses a pale-blue typographic plate with its statement and its four verified capabilities. Each chapter's copy adds one short, factual note on how it is shaped, with a blue rule. The chapters alternate sides on desktop. On phones the plates run edge to edge.
- **About:** a large reading-size lead paragraph, then "How I work" (four principles with short blue rules) and "Skills in practice" set as one flowing typographic line with serif slashes. The separator that would start a new line is clipped, so no line begins or ends with a stray slash.
- **RielArt relationship:** a blue band pairing the approved copy with a short list of the three sites and their jobs: gmacovei.com (you are here), rielart.com, and portal.rielart.com. This states the cross-property model in plain language.
- **Writing:** a sticky heading column on desktop beside large article rows. Each title is the link, and the whole row is clickable. Screen readers hear "read on RielArt, opens in a new tab".
- **Contact:** a navy closing band, with the heading on the left and the three routes as rows on the right. The business route is marked with a blue top rule.
- **Footer:** darker ink with Explore and Connect groups (now including the Client Portal), legal links, and the small tracked GMACOVEI wordmark (`aria-hidden`).

## Motion

- The hero portrait frame draws once on load (about 1.4 s, then the blue step).
- The RielArt plate frame opens with the scroll (CSS `animation-timeline: view()`, progressive enhancement only).
- Navigation underlines, arrow nudges on links and buttons, a short menu entrance, and stretched-link hover on articles.
- No reveal-on-scroll choreography, parallax, scroll-jacking, or JavaScript animation. `prefers-reduced-motion: reduce` removes all of it and disables smooth scrolling.

## Personal specificity and truth rules

Everything on the page comes from first-party material: Gabriel's portrait, the G and R marks, the approved positioning, headline, focus areas, biography, principles and skills, the verified RielArt and Client Portal descriptions, and the real writing, contact, legal, and legacy destinations. The two new "how it is shaped" notes restate facts already recorded in `GMACOVEI-STRATEGY.md`: RielArt's two primary services, and the Client Portal's passwordless sign-in restricted to approved emails. There are no fabricated projects, metrics, testimonials, screenshots, status indicators, or technical metadata.

## Deliberately avoided

Gradients, glass, glow, orbs, bento grids, pill clusters, big rounded cards, centred SaaS heroes, fade-in-on-scroll, decorative numbering, fake telemetry or dashboards, monospace styling, tracked-uppercase label overload, and AI imagery.

## Architecture and maintenance

- Static HTML, CSS, and vanilla JavaScript. No framework, build step, analytics, or runtime dependency.
- `assets/css/site.css` is a single token-driven stylesheet. Colour, type, and spacing tokens live on `:root` and `[data-theme="dark"]`.
- `assets/fonts/` holds the two self-hosted WOFF2 files and `OFL.txt`.
- All eight HTML shells share identical header, mobile menu, and footer markup, and the same `?v=20260924r1` cache version for CSS and JavaScript.
- The inline head script sets the `js` class and the theme before first paint, which prevents the no-JavaScript navigation fallback from causing layout shift.

## Responsive breakpoints

- Above 1180px: full desktop composition.
- 961–1180px: Focus details move beneath each description; Selected Work copy widens.
- 960px and below: menu button, hero lockup, single-column sections, sticky Writing heading released.
- 640px and below: phone spacing, full-width actions, edge-to-edge work plates, stacked contact methods.
- 360px and below: compact header so the full name, theme toggle, and Menu fit at 320px.

This redesign is local only. Deployment, DNS, live hosting, external services, and third-party systems were not changed.
