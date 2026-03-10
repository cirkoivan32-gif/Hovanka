from django.conf import settings
from django.db import models


class LandingPageContent(models.Model):
    site_name = models.CharField(max_length=120, default="Codevanta")
    meta_title = models.CharField(
        max_length=160,
        default="Codevanta | Base Crypto AI Program + Real User Access",
    )
    meta_description = models.CharField(
        max_length=255,
        default=(
            "Codevanta Base is the current $3 crypto AI decision-support release. "
            "Register a real account, manage access, and follow the Pro v2.0 roadmap."
        ),
    )
    badge_text = models.CharField(
        max_length=120,
        default="Base version live / $3 one-time / Pro v2.0 in development",
    )
    hero_title = models.CharField(
        max_length=180,
        default="Codevanta Base is live now. Pro v2.0 is still in development.",
    )
    hero_lead = models.TextField(
        default=(
            "The current release is a lightweight crypto AI decision-support "
            "program with live market scan, weak-setup filtering, setup scoring, "
            "and a real account dashboard for access and release tracking."
        ),
    )
    primary_button_text = models.CharField(max_length=40, default="Buy Base Version")
    primary_button_url = models.URLField(default="https://payhip.com/b/50WXH")
    secondary_button_text = models.CharField(max_length=40, default="Create Account")
    hero_card_label = models.CharField(max_length=60, default="Current release")
    price_text = models.CharField(max_length=40, default="$3")
    price_note = models.CharField(max_length=80, default="one-time base version access")
    hero_card_copy = models.TextField(
        default=(
            "Buy the base build now, keep a real account on the site, and use the "
            "dashboard to track access, release status, and Pro v2.0 updates."
        ),
    )
    disclaimer = models.TextField(
        default=(
            "Decision-support software. It does not guarantee profits and should "
            "not replace risk management or independent review."
        ),
    )
    features_eyebrow = models.CharField(max_length=60, default="Base version")
    features_heading = models.CharField(
        max_length=120,
        default="What Codevanta Base actually does",
    )
    features_intro = models.TextField(
        default=(
            "This is the real public build: a focused decision-support layer for "
            "cleaner trade review, not a fake all-in-one SaaS promise."
        ),
    )
    why_eyebrow = models.CharField(max_length=60, default="Why it matters")
    why_heading = models.CharField(
        max_length=120,
        default="Most trading damage happens before the order is even opened.",
    )
    why_copy = models.TextField(
        default=(
            "Traders usually get hurt by timing mistakes, weak conviction, or "
            "entering on noise. Codevanta is built to slow that process down and "
            "surface cleaner moments for review."
        ),
    )
    workflow_eyebrow = models.CharField(max_length=60, default="Workflow")
    workflow_heading = models.CharField(
        max_length=120,
        default="Use it in four clear steps",
    )
    workflow_intro = models.TextField(
        default=(
            "The workflow stays short: scan, score, decide, and review without "
            "burying yourself in unnecessary panels."
        ),
    )
    pricing_eyebrow = models.CharField(max_length=60, default="Product versions")
    pricing_heading = models.CharField(
        max_length=120,
        default="Base version is live now. Pro v2.0 is still in development.",
    )
    pricing_intro = models.TextField(
        default=(
            "The public release is the $3 base build. Pro v2.0 is planned as the "
            "next stronger version with broader filters and a cleaner operator workflow."
        ),
    )
    accounts_eyebrow = models.CharField(max_length=60, default="Real accounts")
    accounts_heading = models.CharField(
        max_length=120,
        default="Register once, keep your access status and release updates in one place.",
    )
    accounts_copy = models.TextField(
        default=(
            "Accounts are stored on the server with proper password hashing, staff "
            "moderation, and analytics on visits, signups, and checkout clicks."
        ),
    )
    faq_eyebrow = models.CharField(max_length=60, default="FAQ")
    faq_heading = models.CharField(
        max_length=120,
        default="Questions users usually ask before they register or buy.",
    )
    faq_intro = models.TextField(
        default="Short answers to the practical questions that matter before onboarding.",
    )
    cta_eyebrow = models.CharField(max_length=60, default="Ready to move")
    cta_heading = models.CharField(
        max_length=120,
        default="Buy the current base version for $3 and keep the Pro v2.0 roadmap separate.",
    )
    cta_copy = models.TextField(
        default=(
            "Use the current base release if you want the working build today. "
            "Use your account dashboard to follow access and future Pro updates."
        ),
    )
    cta_button_text = models.CharField(max_length=40, default="Buy Base Version")
    footer_text = models.CharField(
        max_length=255,
        default="Codevanta is built for market decision support, not guaranteed returns.",
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Landing page"
        verbose_name_plural = "Landing page"

    def __str__(self):
        return self.site_name

    @classmethod
    def get_solo(cls):
        page, created = cls.objects.get_or_create(pk=1)
        if created:
            page.seed_default_sections()
        else:
            page.seed_missing_sections()
        return page

    def seed_default_sections(self):
        self.create_default_proof_points()
        self.create_default_stats()
        self.create_default_features()
        self.create_default_value_reasons()
        self.create_default_workflow_steps()
        self.create_default_plans()
        self.create_default_faq_items()

    def seed_missing_sections(self):
        if not self.proof_points.exists():
            self.create_default_proof_points()
        if not self.stats.exists():
            self.create_default_stats()
        if not self.features.exists():
            self.create_default_features()
        if not self.value_reasons.exists():
            self.create_default_value_reasons()
        if not self.workflow_steps.exists():
            self.create_default_workflow_steps()
        if not self.plans.exists():
            self.create_default_plans()
        if not self.faq_items.exists():
            self.create_default_faq_items()

    def create_default_proof_points(self):
        ProofPoint.objects.bulk_create(
            [
                ProofPoint(page=self, sort_order=1, text="Live market scan and structure review"),
                ProofPoint(page=self, sort_order=2, text="Server-backed registration and account access"),
                ProofPoint(page=self, sort_order=3, text="Pro v2.0 roadmap tracking from one dashboard"),
            ]
        )

    def create_default_stats(self):
        LandingStat.objects.bulk_create(
            [
                LandingStat(
                    page=self,
                    sort_order=1,
                    value="$3",
                    label="Current base version price",
                ),
                LandingStat(
                    page=self,
                    sort_order=2,
                    value="EMA + RSI + ATR + VWAP",
                    label="Indicator stack behind the setup review",
                ),
                LandingStat(
                    page=self,
                    sort_order=3,
                    value="Real accounts",
                    label="Dashboard, registrations, and staff analytics in one system",
                ),
            ]
        )

    def create_default_features(self):
        Feature.objects.bulk_create(
            [
                Feature(
                    page=self,
                    sort_order=1,
                    title="Real-Time Analysis",
                    description=(
                        "Tracks live OHLCV behavior so decisions are based on the "
                        "current tape, not delayed screenshots."
                    ),
                ),
                Feature(
                    page=self,
                    sort_order=2,
                    title="Signal Filtering",
                    description=(
                        "Filters weak setups and low-quality entries before FOMO or "
                        "revenge trading takes over."
                    ),
                ),
                Feature(
                    page=self,
                    sort_order=3,
                    title="Indicator Stack",
                    description=(
                        "Combines EMA, RSI, ATR, VWAP, and volatility context to improve "
                        "trade selection."
                    ),
                ),
                Feature(
                    page=self,
                    sort_order=4,
                    title="Review Workflow",
                    description=(
                        "Helps evaluate how signals would have behaved before you push "
                        "more size or more risk."
                    ),
                ),
                Feature(
                    page=self,
                    sort_order=5,
                    title="Account Dashboard",
                    description=(
                        "Keeps account access, purchase status, and future roadmap "
                        "interest in one place."
                    ),
                ),
                Feature(
                    page=self,
                    sort_order=6,
                    title="Pro Upgrade Path",
                    description=(
                        "The roadmap stays explicit: Pro v2.0 is still in development, "
                        "not falsely presented as shipped."
                    ),
                ),
            ]
        )

    def create_default_value_reasons(self):
        ValueReason.objects.bulk_create(
            [
                ValueReason(
                    page=self,
                    sort_order=1,
                    title="Less emotional timing",
                    description="Cuts down entries triggered by hype, panic, or fast candles.",
                ),
                ValueReason(
                    page=self,
                    sort_order=2,
                    title="Cleaner review process",
                    description="Keeps attention on setups that deserve review instead of every chart move.",
                ),
                ValueReason(
                    page=self,
                    sort_order=3,
                    title="Actual company control",
                    description="Staff can now see visits, registrations, and checkout intent from one backend.",
                ),
            ]
        )

    def create_default_workflow_steps(self):
        WorkflowStep.objects.bulk_create(
            [
                WorkflowStep(
                    page=self,
                    sort_order=1,
                    number="01",
                    title="Scan the market",
                    description="Monitor live crypto behavior and let the software highlight structure worth attention.",
                ),
                WorkflowStep(
                    page=self,
                    sort_order=2,
                    number="02",
                    title="Filter the setup",
                    description="Check whether the move still has quality after momentum, volatility, and trend filters.",
                ),
                WorkflowStep(
                    page=self,
                    sort_order=3,
                    number="03",
                    title="Decide with context",
                    description="Use the signal as decision support and keep risk management in your own hands.",
                ),
                WorkflowStep(
                    page=self,
                    sort_order=4,
                    number="04",
                    title="Track access and roadmap",
                    description="Keep your account, product status, and Pro v2.0 interest in one real dashboard.",
                ),
            ]
        )

    def create_default_plans(self):
        ProductPlan.objects.bulk_create(
            [
                ProductPlan(
                    page=self,
                    sort_order=1,
                    name="Base Version",
                    badge="Current public release",
                    price="$3",
                    billing="one-time",
                    description=(
                        "This is the real working base build available now. It is not "
                        "pretending to be the future Pro release."
                    ),
                    cta_text="Buy on Payhip",
                    url=self.primary_button_url,
                    featured=True,
                    feature_list=(
                        "Real-time market scan and setup review\n"
                        "Signal filtering using EMA, RSI, ATR, and VWAP context\n"
                        "Cleaner decision-support before entry\n"
                        "Real account dashboard for access and release tracking"
                    ),
                ),
                ProductPlan(
                    page=self,
                    sort_order=2,
                    name="Pro v2.0",
                    badge="Next roadmap build",
                    price="Soon",
                    billing="in development",
                    description=(
                        "This version is not released yet. It is the planned stronger "
                        "build with broader filters, refined workflow review, and more "
                        "mature operator logic."
                    ),
                    cta_text="In Development",
                    disabled=True,
                    feature_list=(
                        "Broader multi-condition market scoring\n"
                        "Cleaner workflow review and stronger setup confirmation\n"
                        "More refined strategy modules and analysis depth\n"
                        "Status: roadmap only, not shipping yet"
                    ),
                ),
            ]
        )

    def create_default_faq_items(self):
        FaqItem.objects.bulk_create(
            [
                FaqItem(
                    page=self,
                    sort_order=1,
                    question="Is registration real now?",
                    answer=(
                        "Yes. Accounts are stored on the server with Django auth, "
                        "proper password hashing, and staff-side visibility in admin."
                    ),
                ),
                FaqItem(
                    page=self,
                    sort_order=2,
                    question="Does registration mean I already bought the product?",
                    answer=(
                        "No. Registration creates your account on the site. The Base "
                        "version is still purchased separately through Payhip."
                    ),
                ),
                FaqItem(
                    page=self,
                    sort_order=3,
                    question="Where can the company see site statistics?",
                    answer=(
                        "Staff users can open the control panel and Django admin to see "
                        "visits, registrations, checkout clicks, and recent activity."
                    ),
                ),
                FaqItem(
                    page=self,
                    sort_order=4,
                    question="What is Pro v2.0 right now?",
                    answer=(
                        "Pro v2.0 is a roadmap line in development. It is presented "
                        "separately so the live site reflects the actual product status."
                    ),
                ),
            ]
        )


class OrderedPageItem(models.Model):
    page = models.ForeignKey(LandingPageContent, on_delete=models.CASCADE)
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ["sort_order", "id"]


class ProofPoint(OrderedPageItem):
    page = models.ForeignKey(
        LandingPageContent,
        on_delete=models.CASCADE,
        related_name="proof_points",
    )
    text = models.CharField(max_length=120)

    class Meta(OrderedPageItem.Meta):
        verbose_name = "Proof point"
        verbose_name_plural = "Proof points"

    def __str__(self):
        return self.text


class LandingStat(OrderedPageItem):
    page = models.ForeignKey(
        LandingPageContent,
        on_delete=models.CASCADE,
        related_name="stats",
    )
    value = models.CharField(max_length=120)
    label = models.CharField(max_length=140)

    class Meta(OrderedPageItem.Meta):
        verbose_name = "Stat"
        verbose_name_plural = "Stats"

    def __str__(self):
        return self.value


class Feature(OrderedPageItem):
    page = models.ForeignKey(
        LandingPageContent,
        on_delete=models.CASCADE,
        related_name="features",
    )
    title = models.CharField(max_length=120)
    description = models.TextField()

    class Meta(OrderedPageItem.Meta):
        verbose_name = "Feature"
        verbose_name_plural = "Features"

    def __str__(self):
        return self.title


class ValueReason(OrderedPageItem):
    page = models.ForeignKey(
        LandingPageContent,
        on_delete=models.CASCADE,
        related_name="value_reasons",
    )
    title = models.CharField(max_length=120)
    description = models.TextField()

    class Meta(OrderedPageItem.Meta):
        verbose_name = "Value reason"
        verbose_name_plural = "Value reasons"

    def __str__(self):
        return self.title


class WorkflowStep(OrderedPageItem):
    page = models.ForeignKey(
        LandingPageContent,
        on_delete=models.CASCADE,
        related_name="workflow_steps",
    )
    number = models.CharField(max_length=12, default="01")
    title = models.CharField(max_length=120)
    description = models.TextField()

    class Meta(OrderedPageItem.Meta):
        verbose_name = "Workflow step"
        verbose_name_plural = "Workflow steps"

    def __str__(self):
        return f"{self.number} {self.title}"


class ProductPlan(OrderedPageItem):
    page = models.ForeignKey(
        LandingPageContent,
        on_delete=models.CASCADE,
        related_name="plans",
    )
    name = models.CharField(max_length=120)
    badge = models.CharField(max_length=120, blank=True)
    price = models.CharField(max_length=40)
    billing = models.CharField(max_length=60, blank=True)
    description = models.TextField(blank=True)
    cta_text = models.CharField(max_length=40, default="Open")
    url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    feature_list = models.TextField(
        help_text="One feature per line.",
        blank=True,
    )

    class Meta(OrderedPageItem.Meta):
        verbose_name = "Product plan"
        verbose_name_plural = "Product plans"

    def __str__(self):
        return self.name

    @property
    def feature_items(self):
        return [line.strip() for line in self.feature_list.splitlines() if line.strip()]


class FaqItem(OrderedPageItem):
    page = models.ForeignKey(
        LandingPageContent,
        on_delete=models.CASCADE,
        related_name="faq_items",
    )
    question = models.CharField(max_length=180)
    answer = models.TextField()

    class Meta(OrderedPageItem.Meta):
        verbose_name = "FAQ item"
        verbose_name_plural = "FAQ items"

    def __str__(self):
        return self.question


class UserProfile(models.Model):
    FOCUS_CHOICES = [
        ("Spot swing", "Spot swing"),
        ("Futures momentum", "Futures momentum"),
        ("DCA building", "DCA building"),
        ("Mixed routine", "Mixed routine"),
    ]
    PURCHASE_STATUS_CHOICES = [
        ("not_purchased", "Not purchased"),
        ("purchased", "Purchased"),
        ("granted", "Granted manually"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    company_name = models.CharField(max_length=120, blank=True)
    focus = models.CharField(
        max_length=40,
        choices=FOCUS_CHOICES,
        default="Mixed routine",
    )
    wants_pro_updates = models.BooleanField(default=True)
    base_purchase_status = models.CharField(
        max_length=20,
        choices=PURCHASE_STATUS_CHOICES,
        default="not_purchased",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.user.email or self.user.username


class SiteVisit(models.Model):
    visitor_key = models.CharField(max_length=64, db_index=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="site_visits",
    )
    path = models.CharField(max_length=255, db_index=True)
    method = models.CharField(max_length=10)
    status_code = models.PositiveSmallIntegerField()
    referrer = models.TextField(blank=True)
    user_agent = models.TextField(blank=True)
    ip_hash = models.CharField(max_length=64, blank=True, db_index=True)
    utm_source = models.CharField(max_length=120, blank=True)
    utm_medium = models.CharField(max_length=120, blank=True)
    utm_campaign = models.CharField(max_length=120, blank=True)
    utm_content = models.CharField(max_length=120, blank=True)
    utm_term = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["created_at", "path"]),
            models.Index(fields=["visitor_key", "created_at"]),
        ]

    def __str__(self):
        return f"{self.path} [{self.status_code}]"


class ConversionEvent(models.Model):
    EVENT_CHOICES = [
        ("signup", "Signup"),
        ("login", "Login"),
        ("base_checkout", "Base checkout"),
        ("pro_waitlist", "Pro waitlist"),
    ]

    visitor_key = models.CharField(max_length=64, db_index=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="conversion_events",
    )
    event_type = models.CharField(max_length=40, choices=EVENT_CHOICES, db_index=True)
    path = models.CharField(max_length=255, blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["event_type", "created_at"]),
        ]

    def __str__(self):
        return f"{self.get_event_type_display()} @ {self.created_at:%Y-%m-%d %H:%M}"
