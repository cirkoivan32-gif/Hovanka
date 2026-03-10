from collections import Counter
from datetime import timedelta
from urllib.parse import urlparse

from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST

from .forms import EmailAuthenticationForm, ProfileForm, RegistrationForm
from .models import ConversionEvent, LandingPageContent, SiteVisit, UserProfile
from .tracking import log_conversion_event


def build_site_url(request):
    return settings.SITE_URL or request.build_absolute_uri("/").rstrip("/")


def build_page_context(request, **extra):
    page = LandingPageContent.get_solo()
    site_url = build_site_url(request)
    context = {
        "page": page,
        "proof_points": page.proof_points.all(),
        "stats": page.stats.all(),
        "features": page.features.all(),
        "reasons": page.value_reasons.all(),
        "steps": page.workflow_steps.all(),
        "plans": page.plans.all(),
        "faq_items": page.faq_items.all(),
        "canonical_url": f"{site_url}{request.path}",
        "google_site_verification": settings.GOOGLE_SITE_VERIFICATION,
        "allow_indexing": not settings.DEBUG,
    }
    context.update(extra)
    return context


@require_GET
def home(request):
    return render(request, "home.html", build_page_context(request))


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        log_conversion_event(
            request,
            "signup",
            {
                "focus": user.profile.focus,
                "company_name": user.profile.company_name,
            },
            user=user,
        )
        messages.success(request, "Your account has been created.")
        return redirect("dashboard")

    return render(
        request,
        "auth/register.html",
        build_page_context(request, register_form=form, allow_indexing=False),
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = EmailAuthenticationForm(request.POST or None, request=request)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        log_conversion_event(request, "login", {"focus": user.profile.focus}, user=user)
        messages.success(request, "You are now signed in.")
        return redirect("dashboard")

    return render(
        request,
        "auth/login.html",
        build_page_context(request, login_form=form, allow_indexing=False),
    )


@require_GET
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You have been signed out.")
    return redirect("home")


@login_required
def dashboard(request):
    profile = request.user.profile
    wants_updates_before = profile.wants_pro_updates
    form = ProfileForm(request.POST or None, user=request.user)

    if request.method == "POST" and form.is_valid():
        form.save()
        if not wants_updates_before and request.user.profile.wants_pro_updates:
            log_conversion_event(
                request,
                "pro_waitlist",
                {"source": "dashboard_profile_form"},
                user=request.user,
            )
        messages.success(request, "Your dashboard profile was updated.")
        return redirect("dashboard")

    recent_events = request.user.conversion_events.all()[:8]
    recent_visits = request.user.site_visits.all()[:8]
    account_metrics = [
        {"value": request.user.date_joined.strftime("%d %b %Y"), "label": "Account created"},
        {"value": profile.get_base_purchase_status_display(), "label": "Base access"},
        {"value": "Enabled" if profile.wants_pro_updates else "Off", "label": "Pro updates"},
    ]

    return render(
        request,
        "dashboard.html",
        build_page_context(
            request,
            profile_form=form,
            account_metrics=account_metrics,
            recent_events=recent_events,
            recent_visits=recent_visits,
            control_panel_url="control" if request.user.is_staff else "",
            allow_indexing=False,
        ),
    )


@login_required
@require_POST
def join_pro_waitlist(request):
    profile = request.user.profile
    if not profile.wants_pro_updates:
        profile.wants_pro_updates = True
        profile.save(update_fields=["wants_pro_updates", "updated_at"])
        log_conversion_event(request, "pro_waitlist", {"source": "button"}, user=request.user)
        messages.success(request, "Pro v2.0 updates are now enabled for your account.")
    else:
        messages.info(request, "Your account is already marked for Pro v2.0 updates.")
    return redirect("dashboard")


@require_GET
def base_checkout_redirect(request):
    page = LandingPageContent.get_solo()
    log_conversion_event(
        request,
        "base_checkout",
        {"destination": page.primary_button_url},
        user=request.user if request.user.is_authenticated else None,
    )
    return redirect(page.primary_button_url)


@staff_member_required
@require_GET
def control_panel(request):
    now = timezone.now()
    last_7_days = now - timedelta(days=7)
    last_30_days = now - timedelta(days=30)

    total_visits = SiteVisit.objects.count()
    unique_visitors = SiteVisit.objects.values("visitor_key").distinct().count()
    visits_last_7_days = SiteVisit.objects.filter(created_at__gte=last_7_days).count()
    registered_users = UserProfile.objects.count()
    signups_last_30_days = UserProfile.objects.filter(created_at__gte=last_30_days).count()
    base_checkout_clicks = ConversionEvent.objects.filter(event_type="base_checkout").count()
    checkout_clicks_last_30_days = ConversionEvent.objects.filter(
        event_type="base_checkout",
        created_at__gte=last_30_days,
    ).count()
    pro_waitlist_users = UserProfile.objects.filter(wants_pro_updates=True).count()

    top_pages = (
        SiteVisit.objects.values("path")
        .annotate(total=Count("id"))
        .order_by("-total", "path")[:10]
    )

    top_sources = (
        SiteVisit.objects.exclude(utm_source="")
        .values("utm_source")
        .annotate(total=Count("id"))
        .order_by("-total", "utm_source")[:10]
    )

    referrer_counter = Counter()
    for referrer in SiteVisit.objects.exclude(referrer="").values_list("referrer", flat=True)[:500]:
        host = urlparse(referrer).netloc or referrer
        referrer_counter[host] += 1
    top_referrers = referrer_counter.most_common(10)

    recent_signups = UserProfile.objects.select_related("user")[:12]
    recent_events = ConversionEvent.objects.select_related("user")[:12]
    recent_visits = SiteVisit.objects.select_related("user")[:15]

    metrics = [
        {"value": total_visits, "label": "Total visits"},
        {"value": unique_visitors, "label": "Unique visitors"},
        {"value": visits_last_7_days, "label": "Visits, last 7 days"},
        {"value": registered_users, "label": "Registered accounts"},
        {"value": signups_last_30_days, "label": "Signups, last 30 days"},
        {"value": base_checkout_clicks, "label": "Base checkout clicks"},
        {"value": checkout_clicks_last_30_days, "label": "Checkout clicks, last 30 days"},
        {"value": pro_waitlist_users, "label": "Accounts waiting for Pro v2.0"},
    ]

    return render(
        request,
        "control.html",
        build_page_context(
            request,
            metrics=metrics,
            top_pages=top_pages,
            top_sources=top_sources,
            top_referrers=top_referrers,
            recent_signups=recent_signups,
            recent_events=recent_events,
            recent_visits=recent_visits,
            allow_indexing=False,
        ),
    )


def robots_txt(request):
    site_url = build_site_url(request)
    lines = ["User-agent: *"]
    if settings.DEBUG:
        lines.append("Disallow: /")
    else:
        lines.append("Allow: /")
    lines.append(f"Sitemap: {site_url}/sitemap.xml")
    return HttpResponse("\n".join(lines), content_type="text/plain")
