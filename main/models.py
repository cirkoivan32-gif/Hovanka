from django.db import models


class LandingPageContent(models.Model):
    site_name = models.CharField(max_length=120, default="Crypto AI")
    meta_title = models.CharField(
        max_length=160,
        default="Crypto AI | Real-Time Crypto Market Signal Support",
    )
    meta_description = models.CharField(
        max_length=255,
        default=(
            "Crypto AI scans market structure in real time, filters weak setups, "
            "and helps traders focus on higher-quality crypto entries."
        ),
    )
    badge_text = models.CharField(max_length=80, default="Launch access / $3")
    hero_title = models.CharField(
        max_length=180,
        default="Crypto AI finds cleaner setups before emotion takes over.",
    )
    hero_lead = models.TextField(
        default=(
            "Watch the market in real time, filter weak entries, and focus on "
            "moves that deserve attention instead of chasing candles."
        ),
    )
    primary_button_text = models.CharField(max_length=40, default="Buy Now")
    primary_button_url = models.URLField(default="https://payhip.com/b/50WXH")
    secondary_button_text = models.CharField(max_length=40, default="See Features")
    hero_card_label = models.CharField(max_length=60, default="Launch package")
    price_text = models.CharField(max_length=40, default="$3")
    price_note = models.CharField(max_length=80, default="one-time launch access")
    hero_card_copy = models.TextField(
        default=(
            "Get access to the launch version now and use it as a decision-support "
            "layer before making crypto entries."
        ),
    )
    disclaimer = models.TextField(
        default=(
            "Decision-support software. It does not guarantee profits and should "
            "not replace risk management."
        ),
    )
    features_eyebrow = models.CharField(max_length=60, default="Core features")
    features_heading = models.CharField(
        max_length=120,
        default="What Crypto AI actually does",
    )
    features_intro = models.TextField(
        default=(
            "Built to reduce emotional entries and turn noisy market behavior into "
            "cleaner, more readable decision support."
        ),
    )
    why_eyebrow = models.CharField(max_length=60, default="Why it matters")
    why_heading = models.CharField(
        max_length=120,
        default="Most losses start before the trade is even opened.",
    )
    why_copy = models.TextField(
        default=(
            "Traders usually get hurt by timing mistakes, weak conviction, or "
            "entering on noise. Crypto AI is built to slow that process down and "
            "surface better moments for review."
        ),
    )
    workflow_eyebrow = models.CharField(max_length=60, default="Simple workflow")
    workflow_heading = models.CharField(max_length=120, default="Use it in three clear steps")
    workflow_intro = models.TextField(
        default=(
            "The workflow stays simple so you can move from market scan to action "
            "without getting buried in unnecessary complexity."
        ),
    )
    cta_eyebrow = models.CharField(max_length=60, default="Ready to test it")
    cta_heading = models.CharField(
        max_length=120,
        default="Get Crypto AI for the $3 launch price.",
    )
    cta_copy = models.TextField(
        default=(
            "Early access is intentionally priced low so you can test the launch "
            "version before the future PRO upgrade expands the feature set."
        ),
    )
    cta_button_text = models.CharField(max_length=40, default="Buy on Payhip")
    footer_text = models.CharField(
        max_length=255,
        default="Crypto AI is built for market decision support, not guaranteed returns.",
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

    def create_default_proof_points(self):
        ProofPoint.objects.bulk_create(
            [
                ProofPoint(page=self, sort_order=1, text="Live market structure snapshots"),
                ProofPoint(page=self, sort_order=2, text="Signal filtering before you enter"),
                ProofPoint(page=self, sort_order=3, text="Paper-trade style review logic"),
            ]
        )

    def create_default_stats(self):
        LandingStat.objects.bulk_create(
            [
                LandingStat(
                    page=self,
                    sort_order=1,
                    value="EMA + RSI + ATR + VWAP",
                    label="Indicator stack behind the signal review",
                ),
                LandingStat(
                    page=self,
                    sort_order=2,
                    value="Weak setups out",
                    label="Focus on fewer, better market moments",
                ),
                LandingStat(
                    page=self,
                    sort_order=3,
                    value="PRO version soon",
                    label="Planned expansion with deeper strategy and news-aware logic",
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
                        "Tracks live OHLCV behavior so decisions are based on the current tape, "
                        "not on delayed screenshots."
                    ),
                ),
                Feature(
                    page=self,
                    sort_order=2,
                    title="Signal Filtering",
                    description=(
                        "Filters weak setups and low-quality entries before FOMO or revenge "
                        "trading takes over."
                    ),
                ),
                Feature(
                    page=self,
                    sort_order=3,
                    title="Indicator Stack",
                    description=(
                        "Combines EMA, RSI, ATR, VWAP, and volatility context to improve the "
                        "quality of trade selection."
                    ),
                ),
                Feature(
                    page=self,
                    sort_order=4,
                    title="Paper Trade Review",
                    description=(
                        "Helps evaluate how signals would have behaved without forcing you to "
                        "risk capital first."
                    ),
                ),
                Feature(
                    page=self,
                    sort_order=5,
                    title="Adaptive Learning",
                    description=(
                        "Built to evolve as new market data arrives so the model can improve "
                        "with fresh conditions."
                    ),
                ),
                Feature(
                    page=self,
                    sort_order=6,
                    title="PRO Upgrade Path",
                    description=(
                        "A future PRO version can expand into additional strategies, stronger AI "
                        "logic, and news-aware analysis."
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
                    description="Cuts down entries triggered by hype, panic, or fast-moving candles.",
                ),
                ValueReason(
                    page=self,
                    sort_order=2,
                    title="Cleaner market focus",
                    description="Keeps attention on setups that deserve review instead of every chart move.",
                ),
                ValueReason(
                    page=self,
                    sort_order=3,
                    title="Faster decision support",
                    description="Turns multiple indicators into one readable decision layer.",
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
                    title="Act with context",
                    description="Use the signal as decision support and keep risk management in your own hands.",
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
