#!/usr/bin/env python3
"""Dependency-free structural, content, and internal-link checks for the static site."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
IGNORED = {ROOT / "account" / "index 2.html"}
SPECIAL_FILES = {"googleee2e63c7386ab57f.html"}
CANONICAL_EXEMPT = {
    "account/index.html",
    "sms-consent.html",
    "sms-opt-in-evidence.html",
    "sms-privacy.html",
    "sms-terms.html",
}
FORBIDDEN_PUBLIC_COPY = re.compile(
    r"\b(?:AI|startup|beta|pilot|pharmacy)\b|OpenAI|Claude", re.IGNORECASE
)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.in_title = False
        self.h1_count = 0
        self.lang = ""
        self.meta: list[dict[str, str]] = []
        self.links: list[str] = []
        self.images: list[dict[str, str]] = []
        self.ids: list[str] = []
        self.labels_for: set[str] = set()
        self.controls: list[tuple[str, dict[str, str]]] = []
        self.visible_text: list[str] = []
        self.hidden_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): (value or "") for key, value in attrs}
        if tag == "html":
            self.lang = values.get("lang", "")
        if tag == "title":
            self.in_title = True
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta":
            self.meta.append(values)
        if tag == "a" and values.get("href"):
            self.links.append(values["href"])
        if tag == "link" and values.get("href"):
            self.links.append(values["href"])
        if tag == "script" and values.get("src"):
            self.links.append(values["src"])
        if tag == "img":
            self.images.append(values)
            if values.get("src"):
                self.links.append(values["src"])
        if values.get("id"):
            self.ids.append(values["id"])
        if tag == "label" and values.get("for"):
            self.labels_for.add(values["for"])
        if tag in {"input", "select", "textarea"}:
            self.controls.append((tag, values))
        if tag in {"script", "style"}:
            self.hidden_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        if tag in {"script", "style"} and self.hidden_depth:
            self.hidden_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        if not self.hidden_depth and data.strip():
            self.visible_text.append(data.strip())


def local_target(source: Path, href: str) -> Path | None:
    split = urlsplit(href)
    if split.scheme or split.netloc or href.startswith(("mailto:", "tel:", "sms:", "#")):
        return None
    raw_path = unquote(split.path)
    if not raw_path:
        return None
    target = ROOT / raw_path.lstrip("/") if raw_path.startswith("/") else source.parent / raw_path
    if raw_path.endswith("/") or target.is_dir():
        target /= "index.html"
    return target.resolve()


def meta_content(page: PageParser, *, name: str | None = None, prop: str | None = None) -> str:
    for item in page.meta:
        if name and item.get("name", "").lower() == name.lower():
            return item.get("content", "").strip()
        if prop and item.get("property", "").lower() == prop.lower():
            return item.get("content", "").strip()
    return ""


def main() -> int:
    errors: list[str] = []
    html_files = sorted(
        path for path in ROOT.rglob("*.html")
        if path not in IGNORED and ".git" not in path.parts
    )

    for path in html_files:
        relative = path.relative_to(ROOT).as_posix()
        if relative in SPECIAL_FILES:
            continue
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8"))
        noindex = "noindex" in meta_content(parser, name="robots").lower()

        if parser.lang.lower() != "en":
            errors.append(f"{relative}: missing html lang=en")
        if not parser.title.strip():
            errors.append(f"{relative}: missing title")
        if not meta_content(parser, name="viewport"):
            errors.append(f"{relative}: missing viewport meta")
        if parser.h1_count != 1:
            errors.append(f"{relative}: expected one h1, found {parser.h1_count}")
        duplicate_ids = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
        if duplicate_ids:
            errors.append(f"{relative}: duplicate ids {', '.join(duplicate_ids)}")
        if relative not in CANONICAL_EXEMPT and not any(
            item.get("rel", "").lower() == "canonical" for item in parser.meta
        ):
            # Canonicals are link elements; checked in the source below.
            if 'rel="canonical"' not in path.read_text(encoding="utf-8"):
                errors.append(f"{relative}: missing canonical link")
        if not noindex and relative not in CANONICAL_EXEMPT and not meta_content(parser, name="description"):
            errors.append(f"{relative}: missing meta description")
        for image in parser.images:
            if "alt" not in image:
                errors.append(f"{relative}: image missing alt attribute ({image.get('src', 'unknown')})")
        for tag, control in parser.controls:
            if (
                control.get("type", "").lower() in {"hidden", "submit", "button"}
                or control.get("aria-hidden", "").lower() == "true"
            ):
                continue
            control_id = control.get("id", "")
            if not control_id or (control_id not in parser.labels_for and not control.get("aria-label")):
                errors.append(f"{relative}: unlabeled {tag} ({control.get('name', control_id or 'unknown')})")
        for href in parser.links:
            target = local_target(path, href)
            if target and not target.exists():
                errors.append(f"{relative}: broken internal reference {href}")

        if not noindex and relative not in CANONICAL_EXEMPT:
            visible_copy = " ".join(parser.visible_text)
            match = FORBIDDEN_PUBLIC_COPY.search(visible_copy)
            if match:
                errors.append(f"{relative}: prohibited public wording {match.group(0)!r}")

    sitemap_path = ROOT / "sitemap.xml"
    sitemap_root = ET.parse(sitemap_path).getroot()
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_urls = [node.text or "" for node in sitemap_root.findall("s:url/s:loc", namespace)]
    if len(sitemap_urls) != len(set(sitemap_urls)):
        errors.append("sitemap.xml: duplicate URLs")
    for url in sitemap_urls:
        split = urlsplit(url)
        if split.scheme != "https" or split.netloc != "perrysoftwarellc.com":
            errors.append(f"sitemap.xml: unexpected host or scheme {url}")
            continue
        target = ROOT / (split.path.lstrip("/") or "index.html")
        if split.path.endswith("/") and split.path != "/":
            target /= "index.html"
        if not target.exists():
            errors.append(f"sitemap.xml: missing local target {url}")
    if any("thank-you.html" in url for url in sitemap_urls):
        errors.append("sitemap.xml: noindex thank-you page must not be listed")

    if errors:
        print(f"Site validation failed with {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Site validation passed: {len(html_files) - len(SPECIAL_FILES)} HTML pages, {len(sitemap_urls)} indexed URLs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
