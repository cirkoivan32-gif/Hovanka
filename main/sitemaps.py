from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import LandingPageContent


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0

    def items(self):
        LandingPageContent.get_solo()
        return ["home"]

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        return LandingPageContent.get_solo().updated_at
