#!/usr/bin/env python3
"""Verify the static inputs and generated output required by the site."""

from __future__ import annotations

import argparse
import re
import sys
from xml.etree import ElementTree
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


REQUIRED_ANCHORS = {
    "top",
    "main",
    "products",
    "artwork",
    "about",
    "free-coloring-page",
}
REQUIRED_LINKS = {
    "https://amzn.to/4xuR1cS",
    "https://payhip.com/b/3DBeF",
    "https://payhip.com/LittleWonderPaperCo",
    "https://classful.com/product/non-editable-version-community-helpers-vocabulary/",
    "https://classful.com/littlewonderpaperco/",
    "mailto:hello@littlewonderpaperco.works",
}
REQUIRED_FILES = {
    "index.html",
    "styles.css",
    "CNAME",
    "robots.txt",
    "_config.yml",
    "assets/downloads/free-capybara-astronaut-us-letter.pdf",
    "assets/downloads/free-capybara-astronaut-a4.pdf",
}


class ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[str] = []
        self.anchors: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        for attribute in ("href", "src"):
            value = attributes.get(attribute)
            if value:
                self.references.append(value)
        srcset = attributes.get("srcset")
        if srcset:
            self.references.extend(
                candidate.strip().split()[0]
                for candidate in srcset.split(",")
                if candidate.strip()
            )
        element_id = attributes.get("id")
        if element_id:
            self.anchors.add(element_id)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def check_pdf(path: Path, expected_box: tuple[str, str]) -> list[str]:
    errors: list[str] = []
    data = path.read_bytes()
    if not data.startswith(b"%PDF-"):
        return [f"{path}: does not start with a PDF signature"]
    if len(re.findall(rb"/Type\s*/Page(?:\s|/|$)", data)) != 1:
        errors.append(f"{path}: expected exactly one page")
    if expected_box[0].encode() not in data or expected_box[1].encode() not in data:
        errors.append(f"{path}: expected page dimensions were not found")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", type=Path, default=Path("."))
    parser.add_argument("--source", type=Path)
    args = parser.parse_args()
    site = args.site
    source = args.source or site
    errors: list[str] = []

    for relative_path in REQUIRED_FILES:
        if not (source / relative_path).is_file():
            errors.append(f"missing required file: {relative_path}")

    index = site / "index.html"
    if not index.is_file():
        errors.append("cannot inspect references because index.html is missing")
    else:
        document = index.read_text(encoding="utf-8")
        parsed = ReferenceParser()
        parsed.feed(document)
        missing_anchors = REQUIRED_ANCHORS - parsed.anchors
        if missing_anchors:
            errors.append(f"missing required anchors: {', '.join(sorted(missing_anchors))}")
        missing_links = REQUIRED_LINKS - set(parsed.references)
        if missing_links:
            errors.append(f"missing required links: {', '.join(sorted(missing_links))}")
        for reference in parsed.references:
            parsed_url = urlsplit(reference)
            if not reference or parsed_url.scheme or parsed_url.netloc:
                continue
            local_path = (parsed_url.path or reference).lstrip("/")
            if parsed_url.fragment and not parsed_url.path:
                if parsed_url.fragment not in parsed.anchors:
                    errors.append(f"unresolved local fragment in index.html: #{parsed_url.fragment}")
                continue
            target = site / local_path
            if not target.is_file():
                errors.append(f"unresolved local reference in index.html: {reference}")
            elif parsed_url.fragment and target.suffix.lower() in {".html", ".htm"}:
                target_parser = ReferenceParser()
                target_parser.feed(target.read_text(encoding="utf-8"))
                if parsed_url.fragment not in target_parser.anchors:
                    errors.append(f"unresolved local fragment in index.html: {reference}")

    for relative_path, dimensions in (
        ("assets/downloads/free-capybara-astronaut-us-letter.pdf", ("612", "792")),
        ("assets/downloads/free-capybara-astronaut-a4.pdf", ("595.2756", "841.8898")),
    ):
        path = site / relative_path
        if path.is_file():
            errors.extend(check_pdf(path, dimensions))

    sitemap = site / "sitemap.xml"
    if not sitemap.is_file():
        errors.append("generated sitemap.xml is missing")
    else:
        try:
            sitemap_root = ElementTree.parse(sitemap).getroot()
            sitemap_locations = {
                element.text
                for element in sitemap_root.iter()
                if element.tag.rsplit("}", 1)[-1] == "loc"
            }
        except ElementTree.ParseError as error:
            errors.append(f"sitemap.xml is not valid XML: {error}")
            sitemap_locations = set()
        if "https://www.littlewonderpaperco.works/" not in sitemap_locations:
            errors.append("sitemap.xml does not contain the canonical homepage")

    robots = site / "robots.txt"
    if not robots.is_file():
        errors.append("generated robots.txt is missing")
    else:
        robots_text = robots.read_text(encoding="utf-8")
        expected_sitemap = "Sitemap: https://www.littlewonderpaperco.works/sitemap.xml"
        if expected_sitemap not in robots_text:
            errors.append("robots.txt does not reference the canonical sitemap")

    if errors:
        for error in errors:
            fail(error)
        return 1
    print("Site verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
