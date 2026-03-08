# Crypto AI Landing Page

Minimal Django landing page for selling Crypto AI and deploying it to Render on a public `*.onrender.com` domain.

## Local run

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000` and manage the site through `http://127.0.0.1:8000/admin/`.

## Environment variables

Copy `.env.example` into your preferred local env workflow, or set variables manually:

- `DJANGO_SECRET_KEY`: required when `DJANGO_DEBUG=False`
- `DJANGO_DEBUG`: `True` locally, `False` on Render
- `DJANGO_ALLOWED_HOSTS`: optional comma-separated extra hosts
- `DJANGO_CSRF_TRUSTED_ORIGINS`: optional comma-separated origins with scheme
- `DJANGO_SITE_URL`: canonical public URL such as `https://crypto-ai-site.onrender.com`
- `GOOGLE_SITE_VERIFICATION`: optional Search Console verification token
- `DJANGO_SUPERUSER_USERNAME`: optional env-based admin username
- `DJANGO_SUPERUSER_EMAIL`: optional env-based admin email
- `DJANGO_SUPERUSER_PASSWORD`: optional env-based admin password
- `DATABASE_URL`: optional if you later attach PostgreSQL or another supported database

`RENDER_EXTERNAL_HOSTNAME` is injected automatically by Render and is used to extend `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, and `SITE_URL`.

## Render deploy

Manual dashboard setup:

- Runtime: `Python 3`
- Build command: `bash build.sh`
- Start command: `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`
- Plan: `Free`
- Env vars:
  - `DJANGO_SECRET_KEY`
  - `DJANGO_DEBUG=False`
  - `DJANGO_SITE_URL=https://your-service.onrender.com`
  - optional `DJANGO_SUPERUSER_USERNAME`
  - optional `DJANGO_SUPERUSER_EMAIL`
  - optional `DJANGO_SUPERUSER_PASSWORD`

Or deploy with the included `render.yaml` blueprint.

Important for a public Google-indexed site: Render's Free web services spin down after 15 minutes of inactivity, and while they are spun down Render automatically responds to `/robots.txt` with a disallow-all response. Free web services are fine for testing, but they are not a strong production SEO choice.

Render web services must bind to `0.0.0.0`, which is why the included start command explicitly uses `--bind 0.0.0.0:$PORT`.

## Google indexing

After deploy:

- Keep `DJANGO_DEBUG=False`
- Confirm `robots.txt` and `sitemap.xml` are reachable on the public domain
- Add the site in Google Search Console
- Submit `https://your-domain/sitemap.xml` in Search Console
- Add `GOOGLE_SITE_VERIFICATION` if Google asks for a meta-tag verification token
- If SEO matters, avoid a host or plan that serves a temporary disallow-all `robots.txt` while the site is asleep

## Content management

The landing page content is editable through Django admin.

- Log in at `/admin/`
- Edit the single `Landing page` record and its inline sections
- For persistent production edits, prefer Postgres via `DATABASE_URL`
- If you choose Render's Free Postgres, remember that Render documents a 30-day expiration for that database

Important: a free Render web service does not give you a persistent disk, so SQLite is not a safe long-term choice for editable production content.

## Production checks

Run these before shipping:

```bash
python manage.py collectstatic --no-input
python manage.py check
python manage.py check --deploy
```
