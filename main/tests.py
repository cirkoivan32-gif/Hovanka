from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from .models import LandingPageContent


class HomePageTests(TestCase):
    def test_home_page_returns_success(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Crypto AI")

    def test_home_page_creates_default_content(self):
        self.assertEqual(LandingPageContent.objects.count(), 0)

        self.client.get(reverse("home"))

        page = LandingPageContent.objects.get()
        self.assertEqual(page.proof_points.count(), 3)
        self.assertEqual(page.stats.count(), 3)
        self.assertEqual(page.features.count(), 6)
        self.assertEqual(page.value_reasons.count(), 3)
        self.assertEqual(page.workflow_steps.count(), 3)

    def test_robots_and_sitemap_are_available(self):
        robots_response = self.client.get(reverse("robots-txt"))
        sitemap_response = self.client.get(reverse("sitemap"))

        self.assertEqual(robots_response.status_code, 200)
        self.assertContains(robots_response, "Sitemap:")
        expected_rule = "Disallow: /" if settings.DEBUG else "Allow: /"
        self.assertContains(robots_response, expected_rule)
        self.assertEqual(sitemap_response.status_code, 200)
        self.assertContains(sitemap_response, "urlset")
