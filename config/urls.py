from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from main.sitemaps import StaticViewSitemap
from main.views import robots_txt


sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("robots.txt", robots_txt, name="robots-txt"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("", include("main.urls")),
]
