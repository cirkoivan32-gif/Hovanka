from .models import SiteVisit
from .tracking import get_or_create_visitor_key, hash_ip_address, set_visitor_cookie


class VisitTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        visitor_key, created = get_or_create_visitor_key(request)
        request.visitor_key = visitor_key
        request.visitor_cookie_created = created

        response = self.get_response(request)

        if self.should_track(request, response):
            SiteVisit.objects.create(
                visitor_key=visitor_key,
                user=request.user if getattr(request, "user", None) and request.user.is_authenticated else None,
                path=request.path,
                method=request.method,
                status_code=response.status_code,
                referrer=request.META.get("HTTP_REFERER", "")[:1000],
                user_agent=request.META.get("HTTP_USER_AGENT", "")[:1000],
                ip_hash=hash_ip_address(request),
                utm_source=request.GET.get("utm_source", "")[:120],
                utm_medium=request.GET.get("utm_medium", "")[:120],
                utm_campaign=request.GET.get("utm_campaign", "")[:120],
                utm_content=request.GET.get("utm_content", "")[:120],
                utm_term=request.GET.get("utm_term", "")[:120],
            )

        if created:
            set_visitor_cookie(response, visitor_key)

        return response

    def should_track(self, request, response):
        if request.method != "GET":
            return False
        if request.path.startswith("/static/"):
            return False
        if request.path.startswith("/admin/jsi18n/"):
            return False
        if request.path.startswith("/favicon"):
            return False
        content_type = response.headers.get("Content-Type", "")
        if "text/html" not in content_type and request.path not in {"/robots.txt", "/sitemap.xml"}:
            return False
        return response.status_code < 500
