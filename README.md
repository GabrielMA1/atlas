# gmacovei.com

Static source for Gabriel Macovei's personal professional website.

## Site role

gmacovei.com explains Gabriel's professional focus, selected work, working approach, writing, and contact routes. Commercial brand, website, advertising, pricing, and project-inquiry information belongs on RielArt. Approved RielArt clients use the separate Client Portal.

## Technology

- Static HTML, CSS, and JavaScript
- Responsive light and dark themes
- No build step or runtime framework
- GitHub Pages-compatible routing and `CNAME`

## Local preview

Run a static HTTP server from the repository root. For example:

```text
python -m http.server 8000
```

Then open `http://127.0.0.1:8000/`.

## Quality checks

Run the standard-library audit:

```text
python tools/site_audit.py
```

The audit checks public routes, metadata, links, image references, structured data, indexability, legacy fallback behavior, duplicate IDs, homepage anchors, and outdated positioning.

## Deployment

The current repository is prepared for GitHub Pages. Keep `CNAME` unchanged. GitHub Pages does not process the `_redirects` file, so real HTTP 301 redirects must be configured at the active CDN or hosting layer. Static legacy fallback pages remain for GitHub Pages.

See `GMACOVEI-DEPLOYMENT-MANIFEST.txt` for the public/excluded file list and `GMACOVEI-QA-REPORT.md` for the latest validation record.
