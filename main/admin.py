from django.contrib import admin

from .models import (
    ConversionEvent,
    Feature,
    FaqItem,
    LandingPageContent,
    LandingStat,
    ProductPlan,
    ProofPoint,
    SiteVisit,
    UserProfile,
    ValueReason,
    WorkflowStep,
)


class OrderedInline(admin.TabularInline):
    extra = 0
    ordering = ("sort_order", "id")


class ProofPointInline(OrderedInline):
    model = ProofPoint


class LandingStatInline(OrderedInline):
    model = LandingStat


class FeatureInline(OrderedInline):
    model = Feature


class ValueReasonInline(OrderedInline):
    model = ValueReason


class WorkflowStepInline(OrderedInline):
    model = WorkflowStep


class ProductPlanInline(OrderedInline):
    model = ProductPlan


class FaqItemInline(OrderedInline):
    model = FaqItem


@admin.register(LandingPageContent)
class LandingPageContentAdmin(admin.ModelAdmin):
    inlines = [
        ProofPointInline,
        LandingStatInline,
        FeatureInline,
        ValueReasonInline,
        WorkflowStepInline,
        ProductPlanInline,
        FaqItemInline,
    ]
    fieldsets = (
        (
            "SEO",
            {
                "fields": ("site_name", "meta_title", "meta_description"),
            },
        ),
        (
            "Hero",
            {
                "fields": (
                    "badge_text",
                    "hero_title",
                    "hero_lead",
                    "primary_button_text",
                    "primary_button_url",
                    "secondary_button_text",
                ),
            },
        ),
        (
            "Hero card",
            {
                "fields": (
                    "hero_card_label",
                    "price_text",
                    "price_note",
                    "hero_card_copy",
                    "disclaimer",
                ),
            },
        ),
        (
            "Features section",
            {
                "fields": ("features_eyebrow", "features_heading", "features_intro"),
            },
        ),
        (
            "Value section",
            {
                "fields": ("why_eyebrow", "why_heading", "why_copy"),
            },
        ),
        (
            "Workflow section",
            {
                "fields": ("workflow_eyebrow", "workflow_heading", "workflow_intro"),
            },
        ),
        (
            "Pricing section",
            {
                "fields": ("pricing_eyebrow", "pricing_heading", "pricing_intro"),
            },
        ),
        (
            "Accounts section",
            {
                "fields": ("accounts_eyebrow", "accounts_heading", "accounts_copy"),
            },
        ),
        (
            "FAQ section",
            {
                "fields": ("faq_eyebrow", "faq_heading", "faq_intro"),
            },
        ),
        (
            "Bottom CTA",
            {
                "fields": ("cta_eyebrow", "cta_heading", "cta_copy", "cta_button_text", "footer_text"),
            },
        ),
    )

    def has_add_permission(self, request):
        if LandingPageContent.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user_email",
        "user_name",
        "focus",
        "base_purchase_status",
        "wants_pro_updates",
        "created_at",
    )
    list_filter = ("focus", "base_purchase_status", "wants_pro_updates", "created_at")
    search_fields = ("user__email", "user__username", "user__first_name", "company_name")
    autocomplete_fields = ("user",)

    @admin.display(ordering="user__email", description="Email")
    def user_email(self, obj):
        return obj.user.email

    @admin.display(ordering="user__first_name", description="Name")
    def user_name(self, obj):
        return obj.user.first_name or obj.user.username


@admin.register(SiteVisit)
class SiteVisitAdmin(admin.ModelAdmin):
    list_display = ("created_at", "path", "status_code", "user", "visitor_key", "utm_source")
    list_filter = ("status_code", "created_at", "utm_source", "utm_medium", "utm_campaign")
    search_fields = ("path", "visitor_key", "user__email", "referrer", "user_agent")
    autocomplete_fields = ("user",)
    readonly_fields = (
        "visitor_key",
        "user",
        "path",
        "method",
        "status_code",
        "referrer",
        "user_agent",
        "ip_hash",
        "utm_source",
        "utm_medium",
        "utm_campaign",
        "utm_content",
        "utm_term",
        "created_at",
    )

    def has_add_permission(self, request):
        return False


@admin.register(ConversionEvent)
class ConversionEventAdmin(admin.ModelAdmin):
    list_display = ("created_at", "event_type", "user", "path", "visitor_key")
    list_filter = ("event_type", "created_at")
    search_fields = ("user__email", "path", "visitor_key")
    autocomplete_fields = ("user",)
    readonly_fields = ("visitor_key", "user", "event_type", "path", "metadata", "created_at")

    def has_add_permission(self, request):
        return False


admin.site.site_header = "Codevanta Control"
admin.site.site_title = "Codevanta Control"
admin.site.index_title = "Site management"
