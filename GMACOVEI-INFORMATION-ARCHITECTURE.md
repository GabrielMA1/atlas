# GMACOVEI Information Architecture

Last updated: October 8, 2026

## Primary navigation

The desktop and mobile navigation use the same structure:

1. Work — `/#work`
2. About — `/#about`
3. Writing — `/#writing`
4. Contact — `/#contact`
5. RielArt ↗ — `https://rielart.com`

The logo and Gabriel Macovei wordmark link to `/`, so "Home" is not repeated in primary navigation.

## Homepage section hierarchy

### 1. Hero

- Section ID: `home`
- H1: I help businesses look better online, reach more people, and work smarter.
- Primary action: Explore my work → `#work`
- RielArt route: inline link in the sentence "Brand, website, and online advertising projects belong at RielArt ↗" → `https://rielart.com`
- Purpose: Establish identity, positioning, location, and the commercial route without making the personal site a service page.
- Notes: from 721px, three links beside the headline clauses go to `#digital-presence`, `#advertising-management`, and `#practical-systems` (the focus items).
- Portrait: none. The photo was removed from the site in October 2026.

### 2. Professional focus

- Section ID: `focus`
- H2: What I work across.
- Cards:
  - Digital Presence
  - Advertising Management
  - Practical Systems
- Purpose: Describe capability areas rather than packages.

Business IT, cloud tools, integrations, automation, workflows, and practical AI remain supporting details beneath Practical Systems. Advertising Management is limited to focused Google Search or Meta advertising, with commercial inquiries routed to RielArt.

### 3. Selected work

- Section ID: `work`
- H2: Businesses, products, and systems I have helped shape.
- Items:
  - RielArt — Business (H3)
  - RielArt Client Portal — Product, nested inside the RielArt entry (H4)
- Purpose: Show accurate, labelled work without fabricating clients or case studies.

### 4. About and working approach

- Section ID: `about`
- H2: A practical approach to digital work.
- Components:
  - Two-paragraph biography
  - Four working principles
  - Compact skills list
- Purpose: Consolidate the former About, Skills, Industries, and Outcomes sections into a personal professional profile.

### 5. Writing

- Section ID: `writing`
- H2: Notes on digital work and practical technology.
- Current article set:
  - Website Builder vs WordPress: Which Approach Fits Your Business?
  - 3 Brand Identity Mistakes That Kill Credibility
  - How Small Businesses Can Implement AI Chatbots Without Code
- Purpose: Present a balanced sample of current writing hosted on RielArt.

### 6. Contact

- Section ID: `contact`
- H2: Choose the right way to connect.
- Routes:
  - Business project → RielArt project inquiry
  - Professional connection → LinkedIn
  - Direct email → `hello@gmacovei.com`
- Purpose: Send each visitor to the correct destination without adding a form.

### 7. Footer

- Concise personal description
- Explore: Work, About, Writing, Contact
- Connect: LinkedIn ↗, RielArt ↗, Client Portal ↗, hello@gmacovei.com
- Legal: Privacy, Terms
- Decorative GMACOVEI wordmark, hidden from assistive technology
- The same footer is used on every HTML route

## Secondary routes

### Privacy Policy

- Route: `/privacy-policy/`
- Purpose: Explain local theme storage, absence of an inquiry form and analytics, and third-party links.
- Indexability: `noindex,follow`

### Terms & Conditions

- Route: `/terms-conditions/`
- Purpose: Explain the informational nature of the personal site and third-party links.
- Indexability: `noindex,follow`

### 404

- Route: `/404.html`
- Purpose: Help visitors recover to the homepage.
- Indexability: `noindex,follow`

### Legacy writing fallbacks

- `/blog/`
- `/blog/ai-chatbots-cut-support-costs/`
- `/blog/website-costing-you-leads/`
- `/blog/direct-mail-outperforms-digital-ads-toronto/`

These remain accessible static fallbacks for GitHub Pages, use `noindex,follow`, identify the destination clearly, and link to the correct RielArt URL. They are not included in the sitemap.

## Heading rules

- Exactly one H1 per public HTML document.
- Homepage H2 headings identify major sections.
- H3 headings identify focus areas, RielArt, the "How I work" and "Skills in practice" groups, articles, and contact routes.
- H4 headings identify the Client Portal (inside RielArt) and the four working principles inside "How I work".
- Section eyebrows were removed in October 2026; headings carry the structure.

## Link behavior

- Homepage anchor links remain in the same tab.
- External websites may open in a new tab with `rel="noopener noreferrer"`.
- `mailto:` links remain in the same browsing context and do not use `target="_blank"`.
- External meaning is shown through the visible `↗` cue where useful.
