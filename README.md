# Codevanta Static Product Site

`codevanta.onrender.com` is deployed as a Render Static Site. That keeps the public site awake on the free tier because static hosting does not use a sleeping web service.

## Production structure

Production is built from:

- [content/site.json](content/site.json) for product copy, pricing, FAQ, bot modes, and app demo data
- [site_static/index.template.html](site_static/index.template.html) for the public marketing page
- [site_static/app.template.html](site_static/app.template.html) for the `/app/` workspace page
- [site_static/site.js](site_static/site.js) for tabs, FAQ, local registration, local login, and app hydration
- [static/css/style.css](static/css/style.css) for the visual system
- [scripts/build_static.py](scripts/build_static.py) to generate `dist/`

Build locally:

```bash
python scripts/build_static.py
```

Generated output:

- `dist/index.html`
- `dist/app/index.html`
- `dist/assets/style.css`
- `dist/assets/site.js`
- `dist/robots.txt`
- `dist/sitemap.xml`

## Registration model

The public site now includes registration and login, but it is currently a static-browser demo:

- accounts are stored in `localStorage`
- passwords are hashed in the browser before saving
- the `/app/` workspace is a local sandbox dashboard, not server-backed auth

If you want real multi-device user accounts later, the next step is adding a backend auth provider and database.

## Render deploy

[render.yaml](render.yaml) is configured for a Render Static Site:

- Runtime: `static`
- Build command: `python scripts/build_static.py`
- Publish directory: `dist`

## Content edits

To change live content:

1. Edit [content/site.json](content/site.json)
2. Push to GitHub
3. Render rebuilds the static site automatically

To verify Google Search Console later, set `google_site_verification` in [content/site.json](content/site.json), or pass `GOOGLE_SITE_VERIFICATION` during build.

## Django status

The Django project is still present in the repo, but it is not the live production path anymore. The public site is generated from the static builder instead of Django templates or Django admin.
