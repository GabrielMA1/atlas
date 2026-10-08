# GMACOVEI Personal-Site Design Notes

Updated: October 8, 2026

## Why the site was redesigned again

The September system was competent but read as a template. Every section used the same eyebrow, H2 and right-hand intro. The page alternated navy, light and blue bands in a familiar SaaS rhythm. A condensed grotesk was paired with a serif-italic "human accent". Decorative plates stood in for the work. The RielArt relationship was also explained six times: the hero route line, the hero button, the work chapter, the About paragraph, a dedicated Business band, and Contact.

## Concept: plainly put

Gabriel's proposition is clarity: systems people can understand, work that is documented, and accounts the business owns. The site should feel like the clearest brief you have been handed across a desk. Every decision below follows from that.

1. **One colour field.** The cobalt of the G mark (`#0b3bcf`, sampled from the logo's median tone) is used flat and at full strength for the hero, Contact, and footer. Everything between is paper and ink. There are no gradients, and blue is not used as a tint everywhere.
2. **One typeface built for clarity.** Atkinson Hyperlegible Next (SIL OFL, self-hosted, variable 200–800, 34 KB) was designed so that no two letters can be confused. It suits someone whose principles are "keep systems understandable" and "make information clearer", and it looks nothing like the Inter/Instrument/Geist family that most templates use. Hierarchy comes only from size and weight. There are no italics, no second family, and no tracked uppercase.
3. **Outcome first, discipline second.** The three headline clauses lead the Focus section in large cobalt type ("Look better online."), and the discipline name ("Digital Presence") sits beneath as a label. A visitor reads the promise in the hero and then sees each part of it explained.
4. **The desk line.** The portrait is cropped 4:5 so that the front edge of Gabriel's desk ends exactly where the cobalt field ends and the page begins. It is a composition specific to this photograph, with no frame or ornament.
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
- **Hero:** a cobalt field. The name and focus phrase come first, then the four-line headline, the summary, one white button, and the RielArt route. The headline is sized in container-query units (`min(5.75rem, 11.6cqi, 9svh)`), so it is always exactly four lines at any width and never pushes the hero past a short viewport. The portrait sits on the field's bottom edge in two columns down to 721px. Below that it follows the statement and runs edge to edge on phones.
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

The lowest computed contrast for any visible text is 5.61:1 in light and 5.95:1 in dark.

## Motion

Only state changes are animated: nav underline, button colour, the arrow on the hero button, and a short menu entrance. Nothing animates on scroll. `prefers-reduced-motion: reduce` removes all of it and smooth scrolling.

## Deliberately avoided

Gradients, glass, glow, blobs, cards, pills, badges, sparkles, serif-italic accents, decorative numbering, monospace, tracked-uppercase labels, fake telemetry, fake screenshots or dashboards, scroll-triggered reveals, and a giant footer wordmark. Live RielArt and Portal screenshots were considered as real product imagery. They were not used because the live sites could not be reached during this pass, and screenshots would go stale.

## Known characteristics

- Atkinson Hyperlegible Next uses a slashed zero (for example in "2026"). This is intended by the typeface and has no alternate.
- The face has no arrow glyphs, so ↗ ↓ → render from the system font.

## Architecture and maintenance

- Static HTML, CSS, and vanilla JavaScript. No framework, build step, analytics, or runtime dependency.
- `assets/css/site.css` (about 23 KB, down from 38 KB) is a single token-driven stylesheet. Colour tokens live on `:root` and `[data-theme="dark"]`.
- `assets/fonts/` holds one WOFF2 file and `OFL.txt`.
- New images: `gabriel-macovei-portrait.webp` (640 × 800 crop of the original portrait) and `logo-knockout.png` (white G for the cobalt footer).
- All eight HTML shells share identical header, mobile menu, and footer markup, and the same `?v=20261008r1` cache version.

## Responsive breakpoints

- Above 1180px: full desktop composition.
- 961–1180px: wider portrait column.
- 960px and below: Menu button, and single-column Focus, Work, About, Writing, and Contact. The hero keeps two columns.
- 720px and below: single-column hero. The portrait follows the statement at 4:3.4 and still lands on the field's edge.
- 640px and below: full-width hero button, edge-to-edge portrait, compact RielArt lockup.
- 360px and below: icon-only Menu button so the name stays on one line.

This redesign is local only. Deployment, DNS, live hosting, external services, and third-party systems were not changed.
