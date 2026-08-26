# GMACOVEI Personal-Site Design Notes

Updated: August 26, 2026

## Art direction

The site now uses a portrait-led, brand-aware visual system built from warm stone, paper, ink, deep navy, and GMACOVEI blue. The design is personal and composed, with editorial pacing but without a newsroom, dashboard, or technical-instrument aesthetic.

The central visual idea comes from the GMACOVEI G: an open, stepped aperture appears in the portrait crop, selected-work imagery, and the RielArt relationship panel. It is used sparingly as a recognizable structural cue rather than a decorative effect.

## Composition

- The portrait anchors the desktop hero on the left and remains part of the narrative on smaller screens.
- The approved name, focus line, headline, professional summary, RielArt route, and two actions form the hero copy on the right.
- Professional Focus is one continuous navy field with staggered content and strong horizontal rules, not three numbered cards.
- Selected Work uses two alternating full-width chapters for RielArt and the Client Portal.
- About, principles, skills, writing, and contact use open layout, rules, and controlled spacing instead of repeated rounded containers.
- RielArt has a dedicated relationship panel that explains why commercial work lives there.

## Personal specificity

The design is tied to first-party material already in the repository:

- Gabriel Macovei's existing office portrait
- the GMACOVEI G monogram and live wordmark
- the related RielArt dimensional R mark
- the exact approved professional focus and headline
- the real relationship between this personal profile, RielArt, and the RielArt Client Portal
- real writing, contact, legal, and legacy destinations

No fabricated projects, awards, testimonials, employer claims, metrics, or platform capabilities were added.

## What was intentionally removed

- Numbered focus, principle, and contact systems
- Fake portal status, progress, phase, security, and dashboard UI
- Universal reveal animations and IntersectionObserver choreography
- Repeated rounded cards, skill pills, decorative halos, backdrop blur, and hover lift
- Oversized footer wordmark treatment
- Technical telemetry, architecture-diagram, command-line, or control-panel styling
- Generic AI imagery, glow, glassmorphism, neon, gradients, and futuristic motifs
- Agency-style pricing, packages, inquiry forms, and commercial service sprawl

## Type, color, and motion

The site uses a humanist system-sans stack headed by Aptos and Segoe UI, with no font download or variable-weight dependency. Light mode is warm and paper-like; dark mode is a deliberate ink-and-navy composition rather than a simple inversion. Blue is reserved for identity, hierarchy, links, and focus.

Motion is limited to short interface state changes and smooth anchor navigation. The reduced-motion media query removes transitions and animations and disables smooth scrolling.

## Responsive behavior

- Above 1100px: complete desktop navigation and a two-column portrait/copy hero.
- 861–1100px: compact header controls and a two-column hero sized for tablet/compact desktop.
- 860px and below: single-column hero, copy before portrait, stacked work chapters, and simplified section layouts.
- 620px and below: full-width primary actions and single-column contact routes.
- 360px and below: tighter type/spacing while retaining the complete name, headline, actions, and portrait; the header brand cap is wide enough to keep Gabriel Macovei visible at 320px.

The JavaScript-enhanced mobile menu is only activated when JavaScript is available. Without JavaScript, the primary navigation remains visible and horizontally scrollable instead of disappearing.

## Social preview

The Open Graph image was regenerated with the built-in image-generation tool, then converted to an optimized 1200 x 630 JPEG. It uses the current exact positioning line, the portrait, the warm-stone/navy palette, and the open-frame visual cue. The stale strategist/IT/founder descriptor is no longer embedded in the social card.

## Architecture and maintenance

The site remains static HTML, CSS, and vanilla JavaScript. No framework, build system, font service, analytics library, animation library, or third-party runtime was introduced. All eight HTML shells use the same `?v=20260901final1` CSS and JavaScript cache version so the redesign is not mixed with previously cached assets.

This redesign is local only. Deployment, DNS, live hosting, repositories outside this clone, external services, and third-party systems were not changed.
