# Codevanta Django Site

`codevanta.onrender.com` is now intended to run as a Django web service, not as a static demo. The site includes:

- real account registration and login with Django auth
- a user dashboard at `/app/`
- a staff control panel at `/control/`
- Django admin at `/admin/`
- visit tracking, signup tracking, and base checkout click tracking

## Main routes

- `/` public landing page
- `/accounts/register/` real account registration
- `/accounts/login/` sign in
- `/app/` user dashboard
- `/ops/` staff analytics dashboard
- `/admin/` admin area
- `/checkout/base/` tracked redirect to the Payhip base product

## Local run

```bash
python manage.py migrate
python manage.py runserver
```

## Render deploy

`render.yaml` is configured for:

- a Python web service named `codevanta`
- a PostgreSQL database named `codevanta-db`
- `bash build.sh`
- `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`

The build script:

```bash
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py ensure_admin
```

## Required environment variables

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=False`
- `DJANGO_SECURE_SSL_REDIRECT=False` for Render health checks, unless you explicitly re-enable it
- `DATABASE_URL`
- `DJANGO_SUPERUSER_USERNAME`
- `DJANGO_SUPERUSER_EMAIL`
- `DJANGO_SUPERUSER_PASSWORD`

`RENDER_EXTERNAL_HOSTNAME` is provided by Render and is already used to populate `ALLOWED_HOSTS` automatically.

## Statistics and management

Where to manage the site:

- content, users, purchase status, and logs: `/admin/`
- summarized site statistics: `/ops/`

What is tracked:

- page visits
- unique visitors by visitor cookie
- recent signups
- checkout clicks for the base product
- Pro v2.0 waitlist interest

## Product positioning

The landing page reflects the actual product state:

- Base Version is the real public release for `$3`
- Pro v2.0 is still in development
- registration creates a site account, but purchase still happens separately through Payhip

## Legacy files

The older static-site builder files are still in the repository for reference, but the intended production path is now the Django app.
