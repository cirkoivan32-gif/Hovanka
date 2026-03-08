from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from .models import LandingPageContent


def home(request):
    page = LandingPageContent.get_solo()
    site_url = settings.SITE_URL or request.build_absolute_uri("/").rstrip("/")

    return render(
        request,
        "home.html",
        {
            "page": page,
            "proof_points": page.proof_points.all(),
            "stats": page.stats.all(),
            "features": page.features.all(),
            "reasons": page.value_reasons.all(),
            "steps": page.workflow_steps.all(),
            "canonical_url": f"{site_url}{request.path}",
            "google_site_verification": settings.GOOGLE_SITE_VERIFICATION,
            "allow_indexing": not settings.DEBUG,
        },
    )


def robots_txt(request):
    site_url = settings.SITE_URL or request.build_absolute_uri("/").rstrip("/")
    lines = ["User-agent: *"]
    if settings.DEBUG:
        lines.append("Disallow: /")
    else:
        lines.append("Allow: /")
    lines.append(f"Sitemap: {site_url}/sitemap.xml")
    return HttpResponse("\n".join(lines), content_type="text/plain")
