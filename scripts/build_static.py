import json
import os
import shutil
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CONTENT_PATH = ROOT / "content" / "site.json"
TEMPLATE_PATH = ROOT / "site_static" / "index.template.html"
SOURCE_CSS_PATH = ROOT / "static" / "css" / "style.css"
DIST_DIR = ROOT / "dist"
DIST_ASSETS_DIR = DIST_DIR / "assets"


def load_content():
    content = json.loads(CONTENT_PATH.read_text(encoding="utf-8"))
    if os.getenv("SITE_URL"):
        content["site_url"] = os.environ["SITE_URL"].rstrip("/")
    if os.getenv("GOOGLE_SITE_VERIFICATION"):
        content["google_site_verification"] = os.environ["GOOGLE_SITE_VERIFICATION"].strip()
    return content


def render_list_items(items):
    return "\n".join(f"                            <li>{escape(item)}</li>" for item in items)


def render_stats_grid(stats):
    parts = []
    for stat in stats:
        parts.append(
            "\n".join(
                [
                    "                        <article class=\"stat-card\">",
                    f"                            <p class=\"stat-value\">{escape(stat['value'])}</p>",
                    f"                            <p class=\"stat-label\">{escape(stat['label'])}</p>",
                    "                        </article>",
                ]
            )
        )
    return "\n".join(parts)


def render_check_list(stats):
    return "\n".join(
        f"                        <li>{escape(stat['value'])}</li>" for stat in stats
    )


def render_feature_cards(features):
    parts = []
    for index, feature in enumerate(features, start=1):
        parts.append(
            "\n".join(
                [
                    "                            <article class=\"feature-card\">",
                    f"                                <span class=\"feature-index\">{index:02d}</span>",
                    f"                                <h3>{escape(feature['title'])}</h3>",
                    f"                                <p>{escape(feature['description'])}</p>",
                    "                            </article>",
                ]
            )
        )
    return "\n".join(parts)


def render_reason_cards(reasons):
    parts = []
    for reason in reasons:
        parts.append(
            "\n".join(
                [
                    "                            <article class=\"value-card\">",
                    f"                                <h3>{escape(reason['title'])}</h3>",
                    f"                                <p>{escape(reason['description'])}</p>",
                    "                            </article>",
                ]
            )
        )
    return "\n".join(parts)


def render_step_cards(steps):
    parts = []
    for step in steps:
        parts.append(
            "\n".join(
                [
                    "                            <article class=\"step-card\">",
                    f"                                <p class=\"step-number\">{escape(step['number'])}</p>",
                    f"                                <h3>{escape(step['title'])}</h3>",
                    f"                                <p>{escape(step['description'])}</p>",
                    "                            </article>",
                ]
            )
        )
    return "\n".join(parts)


def render_template(content):
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    replacements = {
        "__SITE_NAME__": escape(content["site_name"]),
        "__SITE_URL__": escape(content["site_url"]),
        "__CANONICAL_URL__": escape(f"{content['site_url']}/"),
        "__META_TITLE__": escape(content["meta_title"]),
        "__META_DESCRIPTION__": escape(content["meta_description"]),
        "__GOOGLE_SITE_VERIFICATION__": (
            f'    <meta name="google-site-verification" content="{escape(content["google_site_verification"])}">\n'
            if content.get("google_site_verification")
            else ""
        ),
        "__BADGE_TEXT__": escape(content["badge_text"]),
        "__HERO_TITLE__": escape(content["hero_title"]),
        "__HERO_LEAD__": escape(content["hero_lead"]),
        "__PRIMARY_BUTTON_TEXT__": escape(content["primary_button_text"]),
        "__PRIMARY_BUTTON_URL__": escape(content["primary_button_url"]),
        "__SECONDARY_BUTTON_TEXT__": escape(content["secondary_button_text"]),
        "__HERO_CARD_LABEL__": escape(content["hero_card_label"]),
        "__PRICE_TEXT__": escape(content["price_text"]),
        "__PRICE_NOTE__": escape(content["price_note"]),
        "__HERO_CARD_COPY__": escape(content["hero_card_copy"]),
        "__DISCLAIMER__": escape(content["disclaimer"]),
        "__FEATURES_EYEBROW__": escape(content["features_eyebrow"]),
        "__FEATURES_HEADING__": escape(content["features_heading"]),
        "__FEATURES_INTRO__": escape(content["features_intro"]),
        "__WHY_EYEBROW__": escape(content["why_eyebrow"]),
        "__WHY_HEADING__": escape(content["why_heading"]),
        "__WHY_COPY__": escape(content["why_copy"]),
        "__WORKFLOW_EYEBROW__": escape(content["workflow_eyebrow"]),
        "__WORKFLOW_HEADING__": escape(content["workflow_heading"]),
        "__WORKFLOW_INTRO__": escape(content["workflow_intro"]),
        "__CTA_EYEBROW__": escape(content["cta_eyebrow"]),
        "__CTA_HEADING__": escape(content["cta_heading"]),
        "__CTA_COPY__": escape(content["cta_copy"]),
        "__CTA_BUTTON_TEXT__": escape(content["cta_button_text"]),
        "__FOOTER_TEXT__": escape(content["footer_text"]),
        "__PROOF_POINTS__": render_list_items(content["proof_points"]),
        "__STATS_GRID__": render_stats_grid(content["stats"]),
        "__CHECK_LIST__": render_check_list(content["stats"]),
        "__FEATURE_CARDS__": render_feature_cards(content["features"]),
        "__REASON_CARDS__": render_reason_cards(content["reasons"]),
        "__STEP_CARDS__": render_step_cards(content["steps"]),
    }
    for key, value in replacements.items():
        template = template.replace(key, value)
    return template


def build():
    content = load_content()
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE_CSS_PATH, DIST_ASSETS_DIR / "style.css")
    (DIST_DIR / "index.html").write_text(render_template(content), encoding="utf-8")
    (DIST_DIR / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {content['site_url']}/sitemap.xml\n",
        encoding="utf-8",
    )
    (DIST_DIR / "sitemap.xml").write_text(
        "\n".join(
            [
                '<?xml version="1.0" encoding="UTF-8"?>',
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
                "  <url>",
                f"    <loc>{escape(content['site_url'])}/</loc>",
                "  </url>",
                "</urlset>",
                "",
            ]
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    build()
