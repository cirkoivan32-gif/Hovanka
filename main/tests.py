from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import ConversionEvent, LandingPageContent, SiteVisit


User = get_user_model()


class HomePageTests(TestCase):
    def test_home_page_returns_success(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Codevanta")

    def test_home_page_creates_default_content(self):
        self.assertEqual(LandingPageContent.objects.count(), 0)

        self.client.get(reverse("home"))

        page = LandingPageContent.objects.get()
        self.assertEqual(page.proof_points.count(), 3)
        self.assertEqual(page.stats.count(), 3)
        self.assertEqual(page.features.count(), 6)
        self.assertEqual(page.value_reasons.count(), 3)
        self.assertEqual(page.workflow_steps.count(), 4)
        self.assertEqual(page.plans.count(), 2)
        self.assertEqual(page.faq_items.count(), 4)

    def test_visit_tracking_runs_on_home_page(self):
        self.client.get(reverse("home"))

        visit = SiteVisit.objects.get()
        self.assertEqual(visit.path, "/")
        self.assertEqual(visit.status_code, 200)

    def test_robots_and_sitemap_are_available(self):
        robots_response = self.client.get(reverse("robots-txt"))
        sitemap_response = self.client.get(reverse("sitemap"))

        self.assertEqual(robots_response.status_code, 200)
        self.assertContains(robots_response, "Sitemap:")
        expected_rule = "Disallow: /" if settings.DEBUG else "Allow: /"
        self.assertContains(robots_response, expected_rule)
        self.assertEqual(sitemap_response.status_code, 200)
        self.assertContains(sitemap_response, "urlset")


class AuthenticationFlowTests(TestCase):
    def test_register_creates_real_user_and_profile(self):
        response = self.client.post(
            reverse("register"),
            {
                "full_name": "Ivan Cirko",
                "email": "ivan@example.com",
                "company_name": "Codevanta",
                "focus": "Mixed routine",
                "wants_pro_updates": "on",
                "password1": "StrongPass123",
                "password2": "StrongPass123",
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("dashboard"))
        user = User.objects.get(username="ivan@example.com")
        self.assertEqual(user.first_name, "Ivan Cirko")
        self.assertEqual(user.profile.company_name, "Codevanta")
        self.assertTrue(user.profile.wants_pro_updates)
        self.assertTrue(ConversionEvent.objects.filter(event_type="signup").exists())

    def test_login_and_dashboard_require_real_auth(self):
        user = User.objects.create_user(
            username="user@example.com",
            email="user@example.com",
            password="StrongPass123",
            first_name="Real User",
        )
        user.profile.focus = "Spot swing"
        user.profile.save()

        dashboard_response = self.client.get(reverse("dashboard"))
        self.assertEqual(dashboard_response.status_code, 302)

        response = self.client.post(
            reverse("login"),
            {
                "email": "user@example.com",
                "password": "StrongPass123",
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("dashboard"))
        self.assertContains(response, "Real User")
        self.assertTrue(ConversionEvent.objects.filter(event_type="login").exists())

    def test_checkout_redirect_logs_conversion(self):
        response = self.client.get(reverse("base-checkout"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "https://payhip.com/b/50WXH")
        self.assertTrue(ConversionEvent.objects.filter(event_type="base_checkout").exists())


class StaffControlTests(TestCase):
    def test_control_panel_requires_staff(self):
        user = User.objects.create_user(
            username="plain@example.com",
            email="plain@example.com",
            password="StrongPass123",
        )
        self.client.force_login(user)

        response = self.client.get(reverse("control"))

        self.assertEqual(response.status_code, 302)

    def test_staff_can_open_control_panel(self):
        staff = User.objects.create_superuser(
            username="admin@example.com",
            email="admin@example.com",
            password="StrongPass123",
        )
        self.client.force_login(staff)

        response = self.client.get(reverse("control"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "control.html")
        self.assertContains(response, "Control panel")
