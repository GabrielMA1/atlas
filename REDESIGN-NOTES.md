# GMACOVEI Personal-Site Design Notes

Updated: October 9, 2026

## Why the site was redesigned again

The September system was competent but read as a template. Every section used the same eyebrow, H2 and right-hand intro. The page alternated navy, light and blue bands in a familiar SaaS rhythm. A condensed grotesk was paired with a serif-italic "human accent". Decorative plates stood in for the work. The RielArt relationship was also explained six times: the hero route line, the hero button, the work chapter, the About paragraph, a dedicated Business band, and Contact.

## Concept: plainly put

Gabriel's proposition is clarity: systems people can understand, work that is documented, and accounts the business owns. The site should feel like the clearest brief you have been handed across a desk. Every decision below follows from that.

1. **One colour field.** The cobalt of the G mark (`#0b3bcf`, sampled from the logo's median tone) is used flat and at full strength for the hero, Contact, and footer. Everything between is paper and ink. There are no gradients, and blue is not used as a tint everywhere.
2. **One typeface built for clarity.** Atkinson Hyperlegible Next (SIL OFL, self-hosted, variable 200–800, 34 KB) was designed so that no two letters can be confused. It suits someone whose principles are "keep systems understandable" and "make information clearer", and it looks nothing like the Inter/Instrument/Geist family that most templates use. Hierarchy comes only from size and weight. There are no italics, no second family, and no tracked uppercase.
3. **Outcome first, discipline second.** The three headline clauses lead the Focus section in large cobalt type ("Look better online."), and the discipline name ("Digital Presence") sits beneath as a label. A visitor reads the promise in the hero and then sees each part of it explained.
4. **The statement as a contents page.** The hero is type only. Each outcome clause runs on a leader line to the discipline it belongs to ("look better online, ——— Digital Presence ↓"), and each discipline links to its section. The hero shows the promise and how the page is organised in one composition. The portrait was removed at Gabriel's request: it already appears on LinkedIn, and the name is already in the header.
5. **Square corners.** Buttons, photo and bands are square, like stationery. The only round shape is the theme toggle's hover area.

## Information architecture changes

- **Removed** the RielArt relationship band (`#business`) and the "Three sites, three jobs" list. They repeated the work entry, the About paragraph and Contact.
- **Removed** all section eyebrows. They repeated the navigation and the headings.
- **Removed** the hero "Visit RielArt" button. The hero route sentence already links to RielArt.
- **Nested** the Client Portal inside the RielArt entry. It is a RielArt product, and a single cobalt rule shows that relationship.
- **Elevated** the four working principles into their own tinted band, set as large running sentences. "Protect ownership" is the most differentiating idea on the site and was previously small 2×2 text.
- **Retired** the open-frame SVG ornament everywhere, including the 404 and legacy pages.

## Composition by section

- **Header:** paper, sticky, with a hairline that appears on scroll. In dark mode the G mark becomes a knockout. Below 961px a solid ink Menu button opens a full-screen cobalt menu set in large type. At 360px and below the button shows only its icon, and its accessible name stays "Menu".
- **Hero:** a cobalt field holding the four-line headline at poster scale, centred above a ruled foot with the summary, one white button, and the RielArt route.
  - **Hierarchy inside the sentence:** "I help businesses" is the subject, set in the pale field colour (`#c8d4fa`, 5.61:1). The three outcomes are white.
  - **Disciplines (721px and up):** each outcome runs on a 2px leader to its discipline. The disciplines are white, bold, and sized at `clamp(1rem, 0.35rem + 1.1vw, 1.375rem)`, so they read as the second voice of the hero rather than footnotes.
  - **Sizing:** the headline size is calculated from the space left beside the disciplines: `min(6.5rem, (100cqi − notes − leader-min − gap) / 8.7, 12svh)`. The longest clause measures 8.3em, plus 0.32em before its leader, so every clause stays on one line. Every leader ends exactly 20px (tablet) or 24px (desktop) before its discipline, and keeps at least 4rem (tablet) or 8rem (desktop) of length.
  - **Hover and keyboard focus:** pointing at or tabbing to a discipline isolates its pairing. Its leader lights white from the discipline back to the clause, and the other outcomes and disciplines step back to `#94aaf1` (3.65:1 on the light-theme field, 4.06:1 on the dark one; large text). The idea is adapted from React Bits' TrueFocus, without its blur, glow frame or auto-cycling.
  - **Phones (720px and below):** the disciplines become a short index under the headline. Each row has its own leader running to a right-aligned discipline, in the same order as the clauses, with 48px tap targets. The summary and button stay in the first viewport at 390 × 844.
- **Arrival:** when a discipline link lands on its Focus item, a 3px rule draws under that outcome. It is the same line that left the hero, and it stays while the item is the URL target.
- **Focus:** the heading and intro sit in the margin column. The main column holds three outcome-led rows, each with its discipline and its details set as running text.
- **Work:** a full-width heading. RielArt is set at wordmark scale beside its real R mark. Its description, services and link sit in the main column, and the Client Portal is nested beneath with one cobalt rule.
- **About:** a reading-size lead paragraph. The principles band (pale cobalt tint) has each principle's name in cobalt followed by its sentence. Skills are set as one flowing line.
- **Writing:** a sticky heading in the margin. Article rows are fully clickable through the title link.
- **Contact:** the closing cobalt field. The destinations themselves are the large type ("Get started on RielArt", "Connect on LinkedIn", the email address), so they are easy to see and copy.
- **Footer:** continues the cobalt field, separated by one rule, with the knockout G mark and a small GMACOVEI wordmark (`aria-hidden`).

Paper-to-paper section changes are marked with a single content-width rule (`.section-ruled`) rather than a new colour band.

## Palette (all pairs measured)

| Role | Light | Dark |
|---|---|---|
| Paper | `#fbfaf7` | `#0b0f1c` |
| Tint (principles band) | `#eceef6` | `#131a2e` |
| Ink / secondary / muted | `#0f1733` / `#454c63` / `#5d6479` | `#eef0f6` / `#b4bacb` / `#9097ab` |
| Link | `#0b3bcf` | `#9fb6ff` |
| Field / text on field / secondary on field | `#0b3bcf` / `#fff` / `#c8d4fa` | `#1238b8` / `#fff` / `#c3cff7` |

The lowest computed contrast for settled text is 5.61:1 in light and 5.95:1 in dark. Focus clauses pass through a muted state on scroll that stays at 3.33:1 (light) and 3.5:1 (dark); they are large text, so that meets AA.

## Motion

Motion explains the structure; it is not decoration.

- **Hero entrance, act one (CSS, first paint):** the four clauses rise from a mask, 80ms apart, over 760ms. The headline never waits for a script, and the summary and button are never animated, so the message and the CTA are on screen from the first frame.
- **Hero entrance, act two (from 0.55s, done by about 1.5s):** each leader draws out from its clause, and its discipline appears as the line arrives.
  - **721px and up:** GSAP measures each leader and draws them at one speed (`length / 760` seconds, clamped 0.35–0.85s), so the longest line takes longest. The start time is measured from navigation start, so a slow script load never adds delay. Inline styles are cleared when the sequence finishes. Tabbing into the hero completes the sequence immediately.
  - **720px and below:** a CSS sequence of fixed delays. The index rows are short and similar, so measuring them would add nothing.
- **Fallbacks:**
  - With reduced motion, without JavaScript, or if GSAP fails to load, the hero shows its final state immediately.
  - If every script fails after the `js` class is set, a CSS fallback reveals act two at 2.4s.
- **Hero interaction:** the hover and focus isolation described above; the discipline's arrow drops 3px.
- **Focus clauses (scroll-linked, CSS only):** each outcome rises and brightens from a muted cobalt into full cobalt as it reaches reading position. The muted state stays above 3:1, so it is never illegible.
- **Principles (scroll-linked):** each principle settles 32px into place. There is no dimming, because body-size text cannot drop below 4.5:1.
- **State changes:** nav underlines, button colour, the hero button's arrow, external-link arrows leaning toward their direction, and a short menu entrance.

Scroll-linked motion uses `animation-timeline: view()`. Browsers without it show the final state. The children of each focus item move rather than the item itself, so in-page links land exactly below the header. `prefers-reduced-motion: reduce` removes all of it, including smooth scrolling.

## Deliberately avoided

Gradients, glass, glow, blobs, cards, pills, badges, sparkles, serif-italic accents, decorative numbering, monospace, tracked-uppercase labels, fake telemetry, fake screenshots or dashboards, rotating-word or typewriter headlines, page-wide fade-ins, parallax, and a giant footer wordmark. Live RielArt and Portal screenshots were considered as real product imagery. They were not used because the live sites could not be reached during this pass, and screenshots would go stale.

## Libraries evaluated (October 9, 2026)

- **GSAP (adopted, core only, wide screens).** It earns its place in one job: measuring the three leaders and drawing them at a single speed, with each discipline timed to its line's arrival, across a range of widths. CSS cannot measure, so fixed delays made the short middle leader finish early and the disciplines arrive out of step. Everything that was already effective stays in CSS: the clause rise (it must not wait for a script), hover and focus (CSS transitions reverse cleanly mid-way), and the scroll-linked reading aids. ScrollTrigger was not added; CSS scroll timelines already do that work. The first version loaded GSAP on every device, which cost the mobile Lighthouse score 5 points (TBT 220ms on a throttled CPU). Loading it only from 721px restored 100.
- **Lenis (not adopted).** The site is a short, document-like page whose navigation depends on in-page anchors, `scroll-padding-top` under a sticky header, and CSS scroll timelines. Smooth-scroll hijacking adds latency to keyboard and wheel scrolling, needs its own anchor and offset handling, and would have to be disabled for reduced motion anyway. Native scrolling (smooth only for in-page anchors, off under reduced motion) is the better experience here.
- **React Bits (ideas only, no code).** The repository was read through raw GitHub source. TrueFocus (hovering one word de-emphasises the rest) informed the hero's hover isolation, rebuilt in CSS with `:has()` and contrast-checked colours instead of blur. SplitText's line rise matches what the hero already did, so per-character splitting was rejected as too flashy for this brand. React was not introduced.
- **21st.dev (not reachable).** The site could not be reached from the build container, so no component from it was reviewed or used.

## Known characteristics

- Atkinson Hyperlegible Next uses a slashed zero (for example in "2026"). This is intended by the typeface and has no alternate.
- The face has no arrow glyphs, so ↗ ↓ → render from the system font.

## Architecture and maintenance

- Static HTML, CSS, and vanilla JavaScript. No framework, build step, or analytics.
- One runtime dependency: GSAP 3.15.0 core (`assets/vendor/gsap/gsap.min.js`, 72.9 KB raw / 28.3 KB gzip, unmodified, standard no-charge licence in `LICENSE.txt`). `site.js` injects it only on the homepage, only from 721px, and only when motion is allowed, so phones and reduced-motion visitors never download it. No GSAP plugins are used: the scroll-linked effects stay in CSS.
- `assets/css/site.css` (about 23 KB, down from 38 KB) is a single token-driven stylesheet. Colour tokens live on `:root` and `[data-theme="dark"]`.
- `assets/fonts/` holds one WOFF2 file and `OFL.txt`.
- New image: `logo-knockout.png` (white G for the cobalt footer). No portrait is shown on the site. `gabriel-macovei.webp` remains only as the JSON-LD Person image, and the Open Graph card is unchanged.
- All eight HTML shells share identical header, mobile menu, and footer markup, and the same `?v=20261009r1` cache version.

## Responsive breakpoints

- Above 1180px: full desktop composition.
- 1024px and up: 8rem minimum leaders and a 24px gap to each discipline.
- 960px and below: Menu button, and single-column Focus, Work, About, Writing, and Contact.
- 721–1023px: 4rem minimum leaders and a 20px gap.
- 720px and below: the disciplines become an index under the headline; GSAP is not loaded.
- 640px and below: full-width hero button, compact RielArt lockup.
- 360px and below: icon-only Menu button so the name stays on one line.

This redesign is local only. Deployment, DNS, live hosting, external services, and third-party systems were not changed.
