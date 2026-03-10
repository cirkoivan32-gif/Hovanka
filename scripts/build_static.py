import hashlib
import json
import os
import shutil
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CONTENT_PATH = ROOT / "content" / "site.json"
INDEX_TEMPLATE_PATH = ROOT / "site_static" / "index.template.html"
APP_TEMPLATE_PATH = ROOT / "site_static" / "app.template.html"
SOURCE_CSS_PATH = ROOT / "static" / "css" / "style.css"
SOURCE_JS_PATH = ROOT / "site_static" / "site.js"
DIST_DIR = ROOT / "dist"
DIST_APP_DIR = DIST_DIR / "app"
DIST_ASSETS_DIR = DIST_DIR / "assets"


def load_content():
    content = json.loads(CONTENT_PATH.read_text(encoding="utf-8"))
    if os.getenv("SITE_URL"):
        content["site_url"] = os.environ["SITE_URL"].rstrip("/")
    if os.getenv("GOOGLE_SITE_VERIFICATION"):
        content["google_site_verification"] = os.environ["GOOGLE_SITE_VERIFICATION"].strip()
    return content


def hash_file(path):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return digest[:12]


def render_nav_links(items):
    return "\n".join(
        f'                    <a href="{escape(item["href"])}">{escape(item["label"])}</a>'
        for item in items
    )


def render_metric_cards(items):
    parts = []
    for item in items:
        parts.append(
            "\n".join(
                [
                    '                        <article class="metric-card reveal">',
                    f'                            <p class="metric-value">{escape(item["value"])}</p>',
                    f'                            <p class="metric-label">{escape(item["label"])}</p>',
                    "                        </article>",
                ]
            )
        )
    return "\n".join(parts)


def render_list(items, css_class="", indent=""):
    class_attr = f' class="{css_class}"' if css_class else ""
    return "\n".join(f"{indent}<li{class_attr}>{escape(item)}</li>" for item in items)


def render_console_checks(items):
    return "\n".join(
        f'                                <li><span></span>{escape(item)}</li>' for item in items
    )


def render_tags(tags):
    return "".join(f'<span class="tag">{escape(tag)}</span>' for tag in tags)


def render_bot_tabs(items):
    parts = []
    for index, item in enumerate(items):
        active = " is-active" if index == 0 else ""
        parts.append(
            "\n".join(
                [
                    f'                        <button class="bot-tab{active}" type="button" data-bot-target="{escape(item["slug"])}">',
                    f'                            <span>{escape(item["label"])}</span>',
                    f'                            <small>{escape(item["stat"])}</small>',
                    "                        </button>",
                ]
            )
        )
    return "\n".join(parts)


def render_bot_panels(items):
    parts = []
    for index, item in enumerate(items):
        active = " is-active" if index == 0 else ""
        bullets = render_list(item["bullets"], indent="                                ")
        parts.append(
            "\n".join(
                [
                    f'                    <article class="bot-panel{active}" data-bot-panel="{escape(item["slug"])}">',
                    '                        <div class="bot-panel-header">',
                    "                            <div>",
                    f'                                <p class="mini-eyebrow">{escape(item["label"])}</p>',
                    f'                                <h3>{escape(item["title"])}</h3>',
                    "                            </div>",
                    f'                            <div class="tag-row">{render_tags(item["tags"])}</div>',
                    "                        </div>",
                    f'                        <p class="bot-summary">{escape(item["summary"])}</p>',
                    '                        <div class="bot-stat-line">',
                    f'                            <span>{escape(item["stat"])}</span>',
                    "                            <span>Designed for controlled deployment</span>",
                    "                        </div>",
                    '                        <ul class="bot-list">',
                    bullets,
                    "                        </ul>",
                    "                    </article>",
                ]
            )
        )
    return "\n".join(parts)


def render_advantages(items):
    parts = []
    for item in items:
        parts.append(
            "\n".join(
                [
                    '                        <article class="advantage-card reveal">',
                    f'                            <h3>{escape(item["title"])}</h3>',
                    f'                            <p>{escape(item["copy"])}</p>',
                    "                        </article>",
                ]
            )
        )
    return "\n".join(parts)


def render_workflow(items):
    parts = []
    for item in items:
        parts.append(
            "\n".join(
                [
                    '                        <article class="workflow-card reveal">',
                    f'                            <p class="workflow-step">{escape(item["step"])}</p>',
                    f'                            <h3>{escape(item["title"])}</h3>',
                    f'                            <p>{escape(item["copy"])}</p>',
                    "                        </article>",
                ]
            )
        )
    return "\n".join(parts)


def render_comparison_rows(items):
    parts = []
    for item in items:
        parts.append(
            "\n".join(
                [
                    "                                <tr>",
                    f'                                    <th scope="row">{escape(item["label"])}</th>',
                    f'                                    <td>{escape(item["codevanta"])}</td>',
                    f'                                    <td>{escape(item["manual"])}</td>',
                    f'                                    <td>{escape(item["basic"])}</td>',
                    "                                </tr>",
                ]
            )
        )
    return "\n".join(parts)


def render_connectors(items):
    return "\n".join(
        f'                        <li class="connector-chip reveal">{escape(item)}</li>' for item in items
    )


def render_quotes(items):
    parts = []
    for item in items:
        parts.append(
            "\n".join(
                [
                    '                        <article class="quote-card reveal">',
                    f'                            <p class="quote-mark">“{escape(item["quote"])}”</p>',
                    '                            <div class="quote-meta">',
                    f'                                <strong>{escape(item["name"])}</strong>',
                    f'                                <span>{escape(item["role"])}</span>',
                    "                            </div>",
                    "                        </article>",
                ]
            )
        )
    return "\n".join(parts)


def render_plan_cards(items):
    parts = []
    for index, item in enumerate(items):
        highlight = " is-featured" if index == 1 else ""
        features = render_list(item["features"], indent="                                ")
        parts.append(
            "\n".join(
                [
                    f'                        <article class="plan-card{highlight} reveal">',
                    f'                            <p class="plan-badge">{escape(item["badge"])}</p>',
                    f'                            <h3>{escape(item["name"])}</h3>',
                    '                            <div class="plan-price">',
                    f'                                <span>{escape(item["price"])}</span>',
                    f'                                <small>{escape(item["billing"])}</small>',
                    "                            </div>",
                    '                            <ul class="plan-list">',
                    features,
                    "                            </ul>",
                    f'                            <button class="btn {"btn-primary" if index == 1 else "btn-secondary"} js-open-register" type="button" data-plan="{escape(item["name"])}">{escape(item["cta"])}</button>',
                    "                        </article>",
                ]
            )
        )
    return "\n".join(parts)


def render_faq(items):
    parts = []
    for index, item in enumerate(items):
        expanded = "true" if index == 0 else "false"
        active = " is-open" if index == 0 else ""
        parts.append(
            "\n".join(
                [
                    f'                        <article class="faq-item{active} reveal">',
                    f'                            <button class="faq-trigger" type="button" aria-expanded="{expanded}">',
                    f'                                <span>{escape(item["question"])}</span>',
                    "                                <span class=\"faq-plus\"></span>",
                    "                            </button>",
                    f'                            <div class="faq-answer"><p>{escape(item["answer"])}</p></div>',
                    "                        </article>",
                ]
            )
        )
    return "\n".join(parts)


def render_register_benefits(items):
    return "\n".join(
        f'                        <li><span></span>{escape(item)}</li>' for item in items
    )


def render_app_stats(items):
    parts = []
    for item in items:
        parts.append(
            "\n".join(
                [
                    '                    <article class="app-stat reveal">',
                    f'                        <p class="metric-value">{escape(item["value"])}</p>',
                    f'                        <p class="metric-label">{escape(item["label"])}</p>',
                    "                    </article>",
                ]
            )
        )
    return "\n".join(parts)


def render_watchlist_rows(items):
    parts = []
    for item in items:
        parts.append(
            "\n".join(
                [
                    "                                <tr>",
                    f'                                    <td>{escape(item["pair"])}</td>',
                    f'                                    <td>{escape(item["setup"])}</td>',
                    f'                                    <td>{escape(item["score"])}</td>',
                    f'                                    <td><span class="state-pill">{escape(item["state"])}</span></td>',
                    "                                </tr>",
                ]
            )
        )
    return "\n".join(parts)


def render_activity(items):
    return "\n".join(f"                            <li>{escape(item)}</li>" for item in items)


def render_template(template_path, replacements):
    template = template_path.read_text(encoding="utf-8")
    for key, value in replacements.items():
        template = template.replace(key, value)
    return template


def build():
    content = load_content()
    site_json = json.dumps(content, ensure_ascii=False).replace("</", "<\\/")
    style_version = hash_file(SOURCE_CSS_PATH)
    script_version = hash_file(SOURCE_JS_PATH)

    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)

    DIST_ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    DIST_APP_DIR.mkdir(parents=True, exist_ok=True)

    shutil.copy2(SOURCE_CSS_PATH, DIST_ASSETS_DIR / "style.css")
    shutil.copy2(SOURCE_JS_PATH, DIST_ASSETS_DIR / "site.js")

    common = {
        "__BRAND__": escape(content["brand"]),
        "__SITE_NAME__": escape(content["site_name"]),
        "__SITE_URL__": escape(content["site_url"]),
        "__META_TITLE__": escape(content["meta_title"]),
        "__META_DESCRIPTION__": escape(content["meta_description"]),
        "__GOOGLE_SITE_VERIFICATION__": (
            f'    <meta name="google-site-verification" content="{escape(content["google_site_verification"])}">\n'
            if content.get("google_site_verification")
            else ""
        ),
        "__NAV_LINKS__": render_nav_links(content["nav_links"]),
        "__FOOTER_TEXT__": escape(content["footer_text"]),
        "__SITE_DATA_JSON__": site_json,
        "__STYLE_URL__": f"/assets/style.css?v={style_version}",
        "__SCRIPT_URL__": f"/assets/site.js?v={script_version}",
    }

    index_replacements = {
        **common,
        "__CANONICAL_URL__": escape(f"{content['site_url']}/"),
        "__HERO_BADGE__": escape(content["hero_badge"]),
        "__HERO_TITLE__": escape(content["hero_title"]),
        "__HERO_LEAD__": escape(content["hero_lead"]),
        "__HERO_PRIMARY_TEXT__": escape(content["hero_primary_text"]),
        "__HERO_SECONDARY_TEXT__": escape(content["hero_secondary_text"]),
        "__HERO_STATUS__": escape(content["hero_status"]),
        "__HERO_CONSOLE_TITLE__": escape(content["hero_console_title"]),
        "__HERO_CONSOLE_COPY__": escape(content["hero_console_copy"]),
        "__HERO_METRICS__": render_metric_cards(content["hero_metrics"]),
        "__HERO_POINTS__": render_list(content["hero_points"], indent="                        "),
        "__CONSOLE_PAIR__": escape(content["hero_console"]["pair"]),
        "__CONSOLE_SIGNAL_SCORE__": escape(content["hero_console"]["signal_score"]),
        "__CONSOLE_MARKET_MODE__": escape(content["hero_console"]["market_mode"]),
        "__CONSOLE_RISK_BAND__": escape(content["hero_console"]["risk_band"]),
        "__CONSOLE_BOT_NAME__": escape(content["hero_console"]["bot_name"]),
        "__CONSOLE_BOT_STATE__": escape(content["hero_console"]["bot_state"]),
        "__CONSOLE_CHECKPOINTS__": render_console_checks(content["hero_console"]["checkpoints"]),
        "__BOTS_EYEBROW__": escape(content["section_labels"]["bots_eyebrow"]),
        "__BOTS_HEADING__": escape(content["section_labels"]["bots_heading"]),
        "__BOTS_INTRO__": escape(content["section_labels"]["bots_intro"]),
        "__BOT_TABS__": render_bot_tabs(content["bot_profiles"]),
        "__BOT_PANELS__": render_bot_panels(content["bot_profiles"]),
        "__ADVANTAGES_EYEBROW__": escape(content["section_labels"]["advantages_eyebrow"]),
        "__ADVANTAGES_HEADING__": escape(content["section_labels"]["advantages_heading"]),
        "__ADVANTAGES_INTRO__": escape(content["section_labels"]["advantages_intro"]),
        "__ADVANTAGE_CARDS__": render_advantages(content["advantages"]),
        "__WORKFLOW_EYEBROW__": escape(content["section_labels"]["workflow_eyebrow"]),
        "__WORKFLOW_HEADING__": escape(content["section_labels"]["workflow_heading"]),
        "__WORKFLOW_INTRO__": escape(content["section_labels"]["workflow_intro"]),
        "__WORKFLOW_CARDS__": render_workflow(content["workflow_steps"]),
        "__COMPARISON_EYEBROW__": escape(content["section_labels"]["comparison_eyebrow"]),
        "__COMPARISON_HEADING__": escape(content["section_labels"]["comparison_heading"]),
        "__COMPARISON_INTRO__": escape(content["section_labels"]["comparison_intro"]),
        "__COMPARISON_ROWS__": render_comparison_rows(content["comparison_rows"]),
        "__CONNECTORS_EYEBROW__": escape(content["section_labels"]["connectors_eyebrow"]),
        "__CONNECTORS_HEADING__": escape(content["section_labels"]["connectors_heading"]),
        "__CONNECTORS_INTRO__": escape(content["section_labels"]["connectors_intro"]),
        "__CONNECTOR_CHIPS__": render_connectors(content["connectors"]),
        "__QUOTES_EYEBROW__": escape(content["section_labels"]["quotes_eyebrow"]),
        "__QUOTES_HEADING__": escape(content["section_labels"]["quotes_heading"]),
        "__QUOTES_INTRO__": escape(content["section_labels"]["quotes_intro"]),
        "__QUOTE_CARDS__": render_quotes(content["quotes"]),
        "__PLANS_EYEBROW__": escape(content["section_labels"]["plans_eyebrow"]),
        "__PLANS_HEADING__": escape(content["section_labels"]["plans_heading"]),
        "__PLANS_INTRO__": escape(content["section_labels"]["plans_intro"]),
        "__PLAN_CARDS__": render_plan_cards(content["plans"]),
        "__FAQ_EYEBROW__": escape(content["section_labels"]["faq_eyebrow"]),
        "__FAQ_HEADING__": escape(content["section_labels"]["faq_heading"]),
        "__FAQ_INTRO__": escape(content["section_labels"]["faq_intro"]),
        "__FAQ_ITEMS__": render_faq(content["faq"]),
        "__CTA_EYEBROW__": escape(content["section_labels"]["cta_eyebrow"]),
        "__CTA_HEADING__": escape(content["section_labels"]["cta_heading"]),
        "__CTA_COPY__": escape(content["section_labels"]["cta_copy"]),
        "__CTA_PRIMARY_TEXT__": escape(content["cta_primary_text"]),
        "__CTA_SECONDARY_TEXT__": escape(content["cta_secondary_text"]),
        "__REGISTER_TITLE__": escape(content["register"]["title"]),
        "__REGISTER_COPY__": escape(content["register"]["copy"]),
        "__REGISTER_BENEFITS__": render_register_benefits(content["register"]["benefits"]),
        "__LOGIN_TITLE__": escape(content["login"]["title"]),
        "__LOGIN_COPY__": escape(content["login"]["copy"]),
        "__LOGIN_HELP__": escape(content["login"]["help"]),
    }

    app_replacements = {
        **common,
        "__CANONICAL_URL__": escape(f"{content['site_url']}/app/"),
        "__APP_EYEBROW__": escape(content["app"]["eyebrow"]),
        "__APP_TITLE__": escape(content["app"]["title"]),
        "__APP_COPY__": escape(content["app"]["copy"]),
        "__APP_STATS__": render_app_stats(content["app"]["stats"]),
        "__WATCHLIST_ROWS__": render_watchlist_rows(content["app"]["watchlist"]),
        "__APP_ACTIVITY__": render_activity(content["app"]["activity"]),
    }

    (DIST_DIR / "index.html").write_text(
        render_template(INDEX_TEMPLATE_PATH, index_replacements),
        encoding="utf-8",
    )
    (DIST_APP_DIR / "index.html").write_text(
        render_template(APP_TEMPLATE_PATH, app_replacements),
        encoding="utf-8",
    )
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
