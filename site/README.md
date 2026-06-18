# site/ — the browsable CivStack library

A self-contained static site generated from `skills/` and `docs/`. **No server, no build
tools, no network, no JavaScript frameworks** — just HTML/CSS and a little vanilla JS.

## Use it (three ways, all offline)

1. **Just open it.** Double-click `site/index.html`. The search index is inlined, so it
   works straight from `file://`.
2. **Serve it locally:**
   ```bash
   python3 -m http.server -d site 8000   # then visit http://localhost:8000
   ```
3. **Host it for others (GitHub Pages):** in your repo settings, set Pages to serve the
   `/site` folder (or copy `site/` to any static host — Netlify, S3, nginx). Nothing else
   to configure.

## What's inside

- `index.html` — search + filter over all skills (by text, category, operating system).
- `skills/<path>/index.html` — one rendered page per skill, mirroring `skills/`.
- `docs/*.html` — the reference docs rendered.
- `data.js`, `assets/style.css`, `assets/app.js` — inlined catalog and assets.

## Regenerate

The site is generated; don't hand-edit it. After changing skills or docs:

```bash
python3 tools/build_site.py        # rebuild just the site
# or
bash tools/build.sh                # regenerate library + verify + site + vault mirror
```
