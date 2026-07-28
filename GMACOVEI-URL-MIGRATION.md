# GMACOVEI URL Migration

Last updated: July 28, 2026

## Hosting behavior

The repository is configured for GitHub Pages through `CNAME`. Standard GitHub Pages does not interpret the `_redirects` file. Therefore:

- `_redirects` documents the desired permanent redirects for a compatible CDN or hosting layer.
- Static HTML fallback pages remain at legacy paths for GitHub Pages.
- The fallback pages use `noindex,follow`, canonicalize to RielArt, and provide a visible continuation link.
- A meta refresh improves the visitor experience but is not represented as a real HTTP 301.

## Route table

| Current route | Intended purpose | Indexability | Canonical | Redirect or fallback behavior | Sitemap |
|---|---|---|---|---|---|
| `/` | Gabriel Macovei personal professional profile | `index,follow` | `https://gmacovei.com/` | Primary page; no redirect | Included |
| `/privacy-policy/` | Personal-site privacy information | `noindex,follow` | `https://gmacovei.com/privacy-policy/` | Public static page | Excluded |
| `/terms-conditions/` | Personal-site usage terms | `noindex,follow` | `https://gmacovei.com/terms-conditions/` | Public static page | Excluded |
| `/404.html` | Not-found recovery page | `noindex,follow` | None | GitHub Pages custom 404 | Excluded |
| `/blog/` | Legacy local writing index | `noindex,follow` | `https://rielart.com/blog/` | Desired 301 in compatible hosting; static fallback and meta refresh on GitHub Pages | Excluded |
| `/blog/ai-chatbots-cut-support-costs/` | Legacy AI chatbot article route | `noindex,follow` | `https://rielart.com/blog/ai-chatbot-small-business/` | Desired 301 in compatible hosting; static fallback and meta refresh on GitHub Pages | Excluded |
| `/blog/website-costing-you-leads/` | Legacy website strategy article route | `noindex,follow` | `https://rielart.com/blog/website-costing-you-leads/` | Desired 301 in compatible hosting; static fallback and meta refresh on GitHub Pages | Excluded |
| `/blog/direct-mail-outperforms-digital-ads-toronto/` | Legacy direct-mail article route without a confirmed current one-to-one article | `noindex,follow` | `https://rielart.com/blog/` | Desired 301 to the current article library; static fallback and meta refresh on GitHub Pages | Excluded |

## Verified destinations

The RielArt article library and the first two specific article destinations were reachable during the July 28, 2026 audit. The direct-mail route has no approved one-to-one destination in the supplied repository, so it routes to the RielArt article library rather than inventing a replacement.

## Sitemap policy

Only the canonical homepage is included. Legal, 404, and legacy fallback pages remain publicly accessible but are excluded because they are `noindex` or non-content routes.

## Redirect ownership

A real HTTP 301 requires configuration in the active hosting or CDN layer. Publishing these static files alone preserves fallbacks but does not create server-level permanent redirects on standard GitHub Pages.
