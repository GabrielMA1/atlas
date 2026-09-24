#!/usr/bin/env python3
"""Audit the static gmacovei.com source using Python's standard library."""

from __future__ import annotations

import argparse
import html
import json
import re
import struct
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
from xml.etree import ElementTree


REQUIRED_ROUTES = {
    "/": "index.html",
    "/privacy-policy/": "privacy-policy/index.html",
    "/terms-conditions/": "terms-conditions/index.html",
    "/404.html": "404.html",
    "/blog/": "blog/index.html",
    "/blog/ai-chatbots-cut-support-costs/": "blog/ai-chatbots-cut-support-costs/index.html",
    "/blog/website-costing-you-leads/": "blog/website-costing-you-leads/index.html",
    "/blog/direct-mail-outperforms-digital-ads-toronto/": "blog/direct-mail-outperforms-digital-ads-toronto/index.html",
}

LEGACY_CANONICALS = {
    "/blog/": "https://rielart.com/blog/",
    "/blog/ai-chatbots-cut-support-costs/": "https://rielart.com/blog/ai-chatbot-small-business/",
    "/blog/website-costing-you-leads/": "https://rielart.com/blog/website-costing-you-leads/",
    "/blog/direct-mail-outperforms-digital-ads-toronto/": "https://rielart.com/blog/",
}

NOINDEX_ROUTES = set(REQUIRED_ROUTES) - {"/"}

OUTDATED_PUBLIC_COPY = (
    "Digital Strategist & AI Expert",
    "AI Expert",
    "build, automate & grow",
    "AI & Automation",
    "Explore AI & Automation",
    "digital strategy, IT systems, and practical AI",
    "Brand · Web · AI systems",
    "Brand, web, and AI systems",
    "RielArt is where client projects live",
    "Typical outcomes",
    "Who I help and how",
    "Let’s build something useful together",
    "liquid-glass",
    "founder-led",
    "2027",
    "I turn complex digital work into clear, usable systems.",
)

APPROVED_FOCUS_AREAS = (
    "Digital Presence",
    "Advertising Management",
    "Practical Systems",
)

APPROVED_FOCUS_PHRASE = "Digital Presence · Advertising Management · Practical Systems"

APPROVED_TITLE = (
    "Gabriel Macovei | Digital Presence, Advertising Management & Practical Systems"
)

APPROVED_DESCRIPTION = (
    "Gabriel Macovei is a digital professional focused on digital "
    "presence, advertising management, business technology, automation, and practical systems."
)

APPROVED_KNOWS_ABOUT = {
    "Digital presence",
    "Website strategy",
    "Advertising management",
    "Google Ads",
    "Meta advertising",
    "Business IT",
    "Cloud tools",
    "Automation",
    "Integrations",
    "Practical artificial intelligence",
}

OUTDATED_FOCUS_HEADINGS = (
    "Digital strategy",
    "IT systems",
    "Automation and practical AI",
)

APPROVED_HERO_HEADLINE = (
    "I help businesses look better online, reach more people, and work smarter."
)

APPROVED_NAV_ORDER = (
    "/#work",
    "/#about",
    "/#writing",
    "/#contact",
)

REMOVED_CAPABILITY_DISCLAIMER = (
    "These are professional capability areas, not public service packages."
)

REQUIRED_EXCLUSIONS = (
    "README.md",
    "REDESIGN-NOTES.md",
    "QA-REPORT.md",
    "GMACOVEI-STRATEGY.md",
    "GMACOVEI-INFORMATION-ARCHITECTURE.md",
    "GMACOVEI-COPY-MAP.md",
    "GMACOVEI-URL-MIGRATION.md",
    "GMACOVEI-IMPLEMENTATION-LOG.md",
    "GMACOVEI-QA-REPORT.md",
    "GMACOVEI-DEPLOYMENT-MANIFEST.txt",
    "tools",
    "images/gabriel-macovei.jpg",
    "images/rielart-preview.jpg",
)


class PageParser(HTMLParser):
    """Collect the page information needed by the audit."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.in_title = False
        self.h1_count = 0
        self.ids: list[str] = []
        self.anchors: list[dict[str, str]] = []
        self.resources: list[tuple[str, str]] = []
        self.images: list[dict[str, str]] = []
        self.canonical = ""
        self.description = ""
        self.robots = ""
        self.refresh = ""
        self.json_ld: list[str] = []
        self.in_json_ld = False
        self.json_ld_parts: list[str] = []
        self.meta_properties: dict[str, str] = {}
        self.meta_names: dict[str, str] = {}

    @staticmethod
    def attrs_dict(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
        return {name.lower(): value or "" for name, value in attrs}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        data = self.attrs_dict(attrs)

        if tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.h1_count += 1

        if "id" in data:
            self.ids.append(data["id"])

        if tag == "a" and "href" in data:
            self.anchors.append(data)

        if tag == "img":
            self.images.append(data)
            if data.get("src"):
                self.resources.append(("image", data["src"]))

        if tag == "script":
            script_type = data.get("type", "").lower()
            if script_type == "application/ld+json":
                self.in_json_ld = True
                self.json_ld_parts = []
            elif data.get("src"):
                self.resources.append(("script", data["src"]))

        if tag == "link":
            rel_tokens = set(data.get("rel", "").lower().split())
            href = data.get("href", "")
            if "canonical" in rel_tokens:
                self.canonical = href
            elif href and rel_tokens.intersection({"stylesheet", "icon", "apple-touch-icon"}):
                self.resources.append(("link", href))

        if tag == "meta":
            name = data.get("name", "").lower()
            prop = data.get("property", "").lower()
            http_equiv = data.get("http-equiv", "").lower()
            content = data.get("content", "").strip()
            if name == "description":
                self.description = content
            elif name == "robots":
                self.robots = content.lower().replace(" ", "")
            elif http_equiv == "refresh":
                self.refresh = content
            if name:
                self.meta_names[name] = content
            if prop:
                self.meta_properties[prop] = content

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self.in_title = False
        elif tag == "script" and self.in_json_ld:
            self.json_ld.append("".join(self.json_ld_parts).strip())
            self.in_json_ld = False
            self.json_ld_parts = []

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if self.in_json_ld:
            self.json_ld_parts.append(data)

    @property
    def title(self) -> str:
        return " ".join("".join(self.title_parts).split())


def route_for(path: Path, root: Path) -> str:
    rel = path.relative_to(root).as_posix()
    if rel == "index.html":
        return "/"
    if rel == "404.html":
        return "/404.html"
    if rel.endswith("/index.html"):
        return f"/{rel[:-10]}"
    return f"/{rel}"


def file_for_url(url_path: str, root: Path, current: Path) -> Path:
    parsed = urlparse(url_path)
    clean_path = unquote(parsed.path)
    if clean_path.startswith("/"):
        candidate = root / clean_path.lstrip("/")
    else:
        candidate = current.parent / clean_path
    if clean_path.endswith("/") or candidate.is_dir():
        candidate = candidate / "index.html"
    return candidate.resolve()


def is_external(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} or value.startswith("//")


def image_dimensions(path: Path) -> tuple[int, int] | None:
    """Read common raster dimensions without third-party packages."""
    try:
        data = path.read_bytes()
    except OSError:
        return None

    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        return struct.unpack(">II", data[16:24])

    if data.startswith(b"\xff\xd8"):
        offset = 2
        while offset + 9 < len(data):
            if data[offset] != 0xFF:
                offset += 1
                continue
            marker = data[offset + 1]
            offset += 2
            if marker in {0xD8, 0xD9}:
                continue
            if offset + 2 > len(data):
                break
            length = struct.unpack(">H", data[offset:offset + 2])[0]
            if marker in {
                0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF,
            } and offset + 7 <= len(data):
                height, width = struct.unpack(">HH", data[offset + 3:offset + 7])
                return width, height
            offset += max(length, 2)

    if data.startswith(b"RIFF") and data[8:12] == b"WEBP" and len(data) >= 30:
        chunk = data[12:16]
        if chunk == b"VP8X":
            width = 1 + int.from_bytes(data[24:27], "little")
            height = 1 + int.from_bytes(data[27:30], "little")
            return width, height
        if chunk == b"VP8 " and len(data) >= 30 and data[23:26] == b"\x9d\x01\x2a":
            width, height = struct.unpack("<HH", data[26:30])
            return width & 0x3FFF, height & 0x3FFF
        if chunk == b"VP8L" and len(data) >= 25 and data[20] == 0x2F:
            bits = int.from_bytes(data[21:25], "little")
            width = (bits & 0x3FFF) + 1
            height = ((bits >> 14) & 0x3FFF) + 1
            return width, height

    return None


def parse_pages(root: Path, errors: list[str]) -> dict[str, tuple[Path, PageParser, str]]:
    pages: dict[str, tuple[Path, PageParser, str]] = {}
    for html_path in sorted(root.rglob("*.html")):
        if ".git" in html_path.parts:
            continue
        source = html_path.read_text(encoding="utf-8")
        parser = PageParser()
        try:
            parser.feed(source)
        except Exception as exc:  # HTMLParser is tolerant; unexpected errors are significant.
            errors.append(f"{html_path.relative_to(root)}: HTML parse error: {exc}")
        pages[route_for(html_path, root)] = (html_path, parser, source)
    return pages


def check_required_routes(root: Path, errors: list[str]) -> None:
    for route, relative in REQUIRED_ROUTES.items():
        if not (root / relative).is_file():
            errors.append(f"Missing required route {route} ({relative})")


def check_page_metadata(
    pages: dict[str, tuple[Path, PageParser, str]],
    errors: list[str],
) -> None:
    for route, (path, page, _) in pages.items():
        label = path.as_posix()
        if not page.title:
            errors.append(f"{label}: missing title")
        if not page.description:
            errors.append(f"{label}: missing meta description")
        if page.h1_count != 1:
            errors.append(f"{label}: expected one H1, found {page.h1_count}")
        duplicates = [value for value, count in Counter(page.ids).items() if count > 1]
        if duplicates:
            errors.append(f"{label}: duplicate IDs: {', '.join(duplicates)}")

        if route == "/404.html":
            if page.robots != "noindex,follow":
                errors.append(f"{label}: 404 must use noindex,follow")
            continue

        if not page.canonical:
            errors.append(f"{label}: missing canonical")

        if route == "/":
            if page.robots != "index,follow":
                errors.append(f"{label}: homepage must use index,follow")
            if page.canonical != "https://gmacovei.com/":
                errors.append(f"{label}: incorrect homepage canonical {page.canonical!r}")
        elif route in NOINDEX_ROUTES and page.robots != "noindex,follow":
            errors.append(f"{label}: route must use noindex,follow")

        if route in LEGACY_CANONICALS:
            expected = LEGACY_CANONICALS[route]
            if page.canonical != expected:
                errors.append(f"{label}: legacy canonical should be {expected}")
            if expected not in page.refresh:
                errors.append(f"{label}: meta refresh does not match canonical")
            if not any(anchor.get("href") == expected for anchor in page.anchors):
                errors.append(f"{label}: missing visible Continue to RielArt link")


def check_links_and_assets(
    root: Path,
    pages: dict[str, tuple[Path, PageParser, str]],
    errors: list[str],
) -> None:
    root_resolved = root.resolve()
    for route, (path, page, _) in pages.items():
        label = path.relative_to(root).as_posix()
        for anchor in page.anchors:
            href = anchor.get("href", "").strip()
            if not href:
                errors.append(f"{label}: anchor with empty href")
                continue
            if href.startswith(("mailto:", "tel:")):
                if anchor.get("target", "").lower() == "_blank":
                    errors.append(f"{label}: mail or telephone link must not use target=_blank ({href})")
                continue
            if href.startswith(("javascript:", "data:")):
                errors.append(f"{label}: unsafe or non-navigable anchor ({href})")
                continue
            if is_external(href):
                if anchor.get("target", "").lower() == "_blank":
                    rel_tokens = set(anchor.get("rel", "").lower().split())
                    if not {"noopener", "noreferrer"}.issubset(rel_tokens):
                        errors.append(f"{label}: target=_blank missing noopener noreferrer ({href})")
                continue

            parsed = urlparse(href)
            target = file_for_url(href, root, path)
            try:
                target.relative_to(root_resolved)
            except ValueError:
                errors.append(f"{label}: internal link escapes the site root ({href})")
                continue
            if not target.is_file():
                errors.append(f"{label}: broken internal link ({href})")
                continue
            if parsed.fragment and target.suffix.lower() == ".html":
                target_route = route_for(target, root)
                target_page = pages.get(target_route)
                if target_page and parsed.fragment not in target_page[1].ids:
                    errors.append(f"{label}: broken anchor #{parsed.fragment} in {href}")

        for kind, value in page.resources:
            if not value or is_external(value) or value.startswith("data:"):
                continue
            target = file_for_url(value, root, path)
            if not target.is_file():
                errors.append(f"{label}: missing {kind} asset ({value})")


def check_images(
    root: Path,
    pages: dict[str, tuple[Path, PageParser, str]],
    errors: list[str],
) -> None:
    for _, (path, page, _) in pages.items():
        label = path.relative_to(root).as_posix()
        for image in page.images:
            if "alt" not in image:
                errors.append(f"{label}: image missing alt attribute ({image.get('src', '')})")
            src = image.get("src", "")
            if not src or is_external(src):
                continue
            target = file_for_url(src, root, path)
            dimensions = image_dimensions(target)
            width = image.get("width", "")
            height = image.get("height", "")
            if not width or not height:
                errors.append(f"{label}: image missing width or height ({src})")
                continue
            if dimensions and width.isdigit() and height.isdigit():
                declared_ratio = int(width) / max(int(height), 1)
                actual_ratio = dimensions[0] / max(dimensions[1], 1)
                if abs(declared_ratio - actual_ratio) > 0.01:
                    errors.append(
                        f"{label}: declared image ratio {width}x{height} does not match "
                        f"{dimensions[0]}x{dimensions[1]} ({src})"
                    )

    homepage = pages.get("/")
    if homepage:
        og_image = homepage[1].meta_properties.get("og:image", "")
        if og_image:
            target = file_for_url(og_image, root, homepage[0])
            dimensions = image_dimensions(target)
            if dimensions != (1200, 630):
                errors.append(f"Homepage Open Graph image must be 1200x630, found {dimensions}")


def check_json_ld(
    pages: dict[str, tuple[Path, PageParser, str]],
    errors: list[str],
) -> None:
    homepage = pages.get("/")
    if not homepage:
        return
    page = homepage[1]
    if not page.json_ld:
        errors.append("Homepage: missing JSON-LD")
        return

    parsed_blocks = []
    for block in page.json_ld:
        try:
            parsed_blocks.append(json.loads(block))
        except json.JSONDecodeError as exc:
            errors.append(f"Homepage: invalid JSON-LD: {exc}")

    types: set[str] = set()
    for block in parsed_blocks:
        nodes = block.get("@graph", [block]) if isinstance(block, dict) else []
        for node in nodes:
            if isinstance(node, dict):
                node_type = node.get("@type")
                if isinstance(node_type, str):
                    types.add(node_type)
                elif isinstance(node_type, list):
                    types.update(str(value) for value in node_type)

    required_types = {"Person", "WebSite", "Organization"}
    missing = required_types - types
    if missing:
        errors.append(f"Homepage: JSON-LD missing types: {', '.join(sorted(missing))}")


def check_approved_positioning(
    pages: dict[str, tuple[Path, PageParser, str]],
    errors: list[str],
) -> None:
    homepage = pages.get("/")
    if not homepage:
        return

    _, page, source = homepage
    visible_text = " ".join(
        html.unescape(re.sub(r"<[^>]+>", " ", source)).split()
    )

    if APPROVED_FOCUS_PHRASE not in visible_text:
        errors.append(
            f"Homepage: missing approved focus phrase {APPROVED_FOCUS_PHRASE!r}"
        )

    for area in APPROVED_FOCUS_AREAS:
        heading_pattern = rf"<h3>\s*{re.escape(area)}\s*</h3>"
        if not re.search(heading_pattern, source, flags=re.I):
            errors.append(f"Homepage: missing approved focus heading {area!r}")

    for heading in OUTDATED_FOCUS_HEADINGS:
        heading_pattern = rf"<h3>\s*{re.escape(heading)}\s*</h3>"
        if re.search(heading_pattern, source, flags=re.I):
            errors.append(f"Homepage: outdated primary focus heading {heading!r}")

    if page.title != APPROVED_TITLE:
        errors.append(f"Homepage: title does not match approved positioning: {page.title!r}")
    if page.description != APPROVED_DESCRIPTION:
        errors.append("Homepage: meta description does not match approved positioning")
    if page.meta_properties.get("og:title") != APPROVED_TITLE:
        errors.append("Homepage: Open Graph title does not match approved positioning")
    if page.meta_properties.get("og:description") != APPROVED_DESCRIPTION:
        errors.append("Homepage: Open Graph description does not match approved positioning")
    if page.meta_names.get("twitter:title") != APPROVED_TITLE:
        errors.append("Homepage: X title does not match approved positioning")
    if page.meta_names.get("twitter:description") != APPROVED_DESCRIPTION:
        errors.append("Homepage: X description does not match approved positioning")

    person_nodes: list[dict[str, object]] = []
    for block in page.json_ld:
        try:
            parsed = json.loads(block)
        except json.JSONDecodeError:
            continue
        nodes = parsed.get("@graph", [parsed]) if isinstance(parsed, dict) else []
        person_nodes.extend(
            node
            for node in nodes
            if isinstance(node, dict) and node.get("@type") == "Person"
        )

    if len(person_nodes) != 1:
        errors.append(f"Homepage: expected one Person schema node, found {len(person_nodes)}")
    else:
        person = person_nodes[0]
        if person.get("jobTitle") != "Digital Professional":
            errors.append("Homepage: Person jobTitle must be 'Digital Professional'")
        knows_about = person.get("knowsAbout")
        actual = set(knows_about) if isinstance(knows_about, list) else set()
        if actual != APPROVED_KNOWS_ABOUT:
            errors.append(
                "Homepage: Person knowsAbout does not match approved focus vocabulary"
            )

    inquiry_url = "https://rielart.com/contact/#project-inquiry"
    if not any(anchor.get("href") == inquiry_url for anchor in page.anchors):
        errors.append("Homepage: RielArt commercial inquiry route changed or is missing")


def check_refinement_requirements(
    pages: dict[str, tuple[Path, PageParser, str]],
    root: Path,
    errors: list[str],
) -> None:
    homepage = pages.get("/")
    if not homepage:
        return

    _, _, homepage_source = homepage
    homepage_text = " ".join(
        html.unescape(re.sub(r"<[^>]+>", " ", homepage_source)).split()
    )

    if APPROVED_HERO_HEADLINE not in homepage_text:
        errors.append("Homepage: approved refined hero headline is missing")
    if REMOVED_CAPABILITY_DISCLAIMER in homepage_text:
        errors.append("Homepage: removed capability disclaimer is still visible")

    portrait_match = re.search(
        r'<figure\s+class="[^"]*\bportrait\b[^"]*"[^>]*>(.*?)</figure>',
        homepage_source,
        flags=re.I | re.S,
    )
    if not portrait_match:
        errors.append("Homepage: portrait figure is missing")
    elif re.search(r"<figcaption\b", portrait_match.group(1), flags=re.I):
        errors.append("Homepage: portrait caption wrapper must be removed")

    if len(re.findall(r'class="work-action"', homepage_source)) != 2:
        errors.append("Homepage: expected two structural Selected Work action regions")

    nav_patterns = {
        "desktop": r'<nav\s+class="desktop-nav"[^>]*>(.*?)</nav>',
        "mobile": r'<nav\s+aria-label="Mobile navigation"[^>]*>(.*?)</nav>',
    }
    for route, (path, _, source) in pages.items():
        label = path.relative_to(root).as_posix()
        for nav_name, pattern in nav_patterns.items():
            match = re.search(pattern, source, flags=re.I | re.S)
            if not match:
                errors.append(f"{label}: missing {nav_name} navigation")
                continue
            hrefs = re.findall(r'href="([^"]+)"', match.group(1), flags=re.I)
            internal_order = tuple(href for href in hrefs if href.startswith("/#"))
            if internal_order != APPROVED_NAV_ORDER:
                errors.append(
                    f"{label}: {nav_name} navigation order should be "
                    "Work, About, Writing, Contact"
                )

        if 'class="footer-wordmark" aria-hidden="true"' not in source:
            errors.append(f"{label}: decorative footer wordmark must remain aria-hidden")


def check_shared_assets(
    pages: dict[str, tuple[Path, PageParser, str]],
    root: Path,
    errors: list[str],
) -> None:
    """Keep every shell on one cache version, self-hosted fonts, and a pre-paint JS flag."""
    versions: set[str] = set()
    for _, (path, _, source) in pages.items():
        label = path.relative_to(root).as_posix()
        found = set(re.findall(r'/assets/(?:css/site\.css|js/site\.js)\?v=([\w-]+)', source))
        if len(found) != 1:
            errors.append(f"{label}: shared CSS and JavaScript must use one cache version, found {sorted(found)}")
        versions.update(found)
        if 'document.documentElement.classList.add("js")' not in source:
            errors.append(f"{label}: inline head script must set the js class before first paint")
        if re.search(r"fonts\.(?:googleapis|gstatic)\.com|use\.typekit", source):
            errors.append(f"{label}: external font service referenced")
    if len(versions) > 1:
        errors.append(f"Shared asset cache versions differ across pages: {sorted(versions)}")

    css_path = root / "assets/css/site.css"
    css = css_path.read_text(encoding="utf-8") if css_path.is_file() else ""
    for font in re.findall(r'url\("(/assets/fonts/[^"]+)"\)', css):
        if not (root / font.lstrip("/")).is_file():
            errors.append(f"assets/css/site.css: missing font file {font}")
    if not (root / "assets/fonts/OFL.txt").is_file():
        errors.append("assets/fonts/OFL.txt: font licence file is missing")


def check_sitemap(
    root: Path,
    pages: dict[str, tuple[Path, PageParser, str]],
    errors: list[str],
) -> None:
    sitemap_path = root / "sitemap.xml"
    if not sitemap_path.is_file():
        errors.append("Missing sitemap.xml")
        return
    try:
        tree = ElementTree.parse(sitemap_path)
    except ElementTree.ParseError as exc:
        errors.append(f"sitemap.xml: XML parse error: {exc}")
        return

    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    actual = {
        element.text.strip()
        for element in tree.findall(".//sm:loc", namespace)
        if element.text
    }
    expected = {
        page.canonical
        for route, (_, page, _) in pages.items()
        if route != "/404.html"
        and page.robots == "index,follow"
        and page.canonical.startswith("https://gmacovei.com/")
    }
    if actual != expected:
        errors.append(
            "sitemap.xml parity mismatch: "
            f"expected {sorted(expected)}, found {sorted(actual)}"
        )


def check_outdated_copy(
    pages: dict[str, tuple[Path, PageParser, str]],
    root: Path,
    errors: list[str],
) -> None:
    public_sources = [(path, source) for path, _, source in pages.values()]
    for relative in ("assets/css/site.css", "assets/js/site.js"):
        path = root / relative
        if path.is_file():
            public_sources.append((path, path.read_text(encoding="utf-8")))

    for path, source in public_sources:
        source_lower = source.lower()
        for phrase in OUTDATED_PUBLIC_COPY:
            if phrase.lower() in source_lower:
                errors.append(f"{path.relative_to(root).as_posix()}: outdated public copy {phrase!r}")


def check_deployment_exclusions(root: Path, errors: list[str]) -> None:
    config_path = root / "_config.yml"
    if not config_path.is_file():
        errors.append("Missing _config.yml deployment exclusions")
        return
    config = config_path.read_text(encoding="utf-8")
    for item in REQUIRED_EXCLUSIONS:
        if item not in config:
            errors.append(f"_config.yml: missing exclusion for {item}")


def check_css(root: Path, errors: list[str]) -> None:
    css_path = root / "assets/css/site.css"
    if not css_path.is_file():
        errors.append("Missing assets/css/site.css")
        return
    css = css_path.read_text(encoding="utf-8")
    without_comments = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    if without_comments.count("{") != without_comments.count("}"):
        errors.append("assets/css/site.css: unbalanced braces")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root (defaults to the parent of tools/)",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []

    check_required_routes(root, errors)
    pages = parse_pages(root, errors)
    check_page_metadata(pages, errors)
    check_links_and_assets(root, pages, errors)
    check_images(root, pages, errors)
    check_json_ld(pages, errors)
    check_approved_positioning(pages, errors)
    check_refinement_requirements(pages, root, errors)
    check_shared_assets(pages, root, errors)
    check_sitemap(root, pages, errors)
    check_outdated_copy(pages, root, errors)
    check_deployment_exclusions(root, errors)
    check_css(root, errors)

    css_bytes = (root / "assets/css/site.css").stat().st_size
    js_bytes = (root / "assets/js/site.js").stat().st_size
    print(f"Audited {len(pages)} HTML pages.")
    print(f"CSS: {css_bytes:,} bytes")
    print(f"JavaScript: {js_bytes:,} bytes")
    font_bytes = sum(path.stat().st_size for path in (root / "assets/fonts").glob("*.woff2"))
    print(f"Fonts: {font_bytes:,} bytes")

    if errors:
        print(f"\nFAIL - {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nPASS - static site audit completed with no findings.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
