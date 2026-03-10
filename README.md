# Crypto AI Landing Page

Static landing page build for Render Static Sites. Static sites do not sleep after inactivity, so this is the production path for `codevanta.onrender.com`.

## Static production

Production now builds from:

- [content/site.json](content/site.json) for text, links, and SEO values
- [site_static/index.template.html](site_static/index.template.html) for layout
- [static/css/style.css](static/css/style.css) for styling
- [scripts/build_static.py](scripts/build_static.py) to generate `dist/`

Build locally:

```bash
python scripts/build_static.py
```

Generated files land in `dist/`:

- `dist/index.html`
- `dist/robots.txt`
- `dist/sitemap.xml`
- `dist/assets/style.css`

## Render deploy

The included [render.yaml](render.yaml) is now configured for a Render Static Site:

- Runtime: `static`
- Build command: `python scripts/build_static.py`
- Publish directory: `dist`

Static Sites do not use Django, Gunicorn, or a database in production, so there is no sleep/wake delay on free hosting.

## Content changes

To change live content:

1. Edit [content/site.json](content/site.json)
2. Push to GitHub
3. Render rebuilds the static site automatically

To verify Google Search Console later, set `google_site_verification` in [content/site.json](content/site.json), or pass `GOOGLE_SITE_VERIFICATION` during build.

## Local Django

The Django project is still in the repo, but it is no longer the production deployment path. That means:

- `/admin/` is not part of the live static site
- content is managed through Git instead of Django admin
- the Django code can still be used locally if you want to keep it as a draft/back-office project
