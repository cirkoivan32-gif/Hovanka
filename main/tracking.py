import hashlib
import secrets

from django.conf import settings

from .models import ConversionEvent


VISITOR_COOKIE_NAME = "codevanta_vid"


def get_or_create_visitor_key(request):
    visitor_key = request.COOKIES.get(VISITOR_COOKIE_NAME, "").strip()
    created = False
    if not visitor_key:
        visitor_key = secrets.token_urlsafe(24)
        created = True
    return visitor_key, created


def set_visitor_cookie(response, visitor_key):
    response.set_cookie(
        VISITOR_COOKIE_NAME,
        visitor_key,
        max_age=60 * 60 * 24 * 365,
        secure=not settings.DEBUG,
        samesite="Lax",
    )


def hash_ip_address(request):
    raw_ip = request.META.get("HTTP_X_FORWARDED_FOR", "").split(",")[0].strip()
    if not raw_ip:
        raw_ip = request.META.get("REMOTE_ADDR", "").strip()
    if not raw_ip:
        return ""
    payload = f"{settings.SECRET_KEY}:{raw_ip}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def log_conversion_event(request, event_type, metadata=None, user=None):
    visitor_key, _ = get_or_create_visitor_key(request)
    return ConversionEvent.objects.create(
        visitor_key=visitor_key,
        user=user if user and user.is_authenticated else getattr(request, "user", None)
        if getattr(request, "user", None) and request.user.is_authenticated
        else None,
        event_type=event_type,
        path=request.path,
        metadata=metadata or {},
    )
