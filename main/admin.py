from django.contrib import admin

from .models import Feature, LandingPageContent, LandingStat, ProofPoint, ValueReason, WorkflowStep


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


@admin.register(LandingPageContent)
class LandingPageContentAdmin(admin.ModelAdmin):
    inlines = [
        ProofPointInline,
        LandingStatInline,
        FeatureInline,
        ValueReasonInline,
        WorkflowStepInline,
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
            "Offer card",
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


admin.site.site_header = "Crypto AI Admin"
admin.site.site_title = "Crypto AI Admin"
admin.site.index_title = "Landing page management"
