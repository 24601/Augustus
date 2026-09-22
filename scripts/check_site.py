#!/usr/bin/env python3
"""Validate rendered Pages structure without network requests.

Checks HTML links/assets, common robots meta directives, canonical/sitemap
URLs, and the project robots file's sitemap declaration. Does not decode images,
parse CSS URLs, inspect HTTP headers, or validate origin-level crawler policy.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
import posixpath
import re
import sys
from typing import Iterable
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET


DEFAULT_SITE_URL = "https://24601.github.io"
DEFAULT_BASE_URL = "/Augustus"
REQUIRED_PAGES = ("index.html", "ecosystem.html", "examples.html")


@dataclass(frozen=True)
class Issue:
    path: Path
    code: str
    detail: str

    def __str__(self) -> str:
        return f"{self.path}: {self.code}: {self.detail}"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_count = 0
        self.title_text: list[str] = []
        self._in_title = False
        self.main_count = 0
        self.h1_count = 0
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()
        self.canonicals: list[str] = []
        self.descriptions: list[str] = []
        self.og_images: list[str] = []
        self.indexing_blocks: list[str] = []
        self.references: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_by_name = {name.lower(): value or "" for name, value in attrs}
        lowered = tag.lower()
        if lowered == "title":
            self.title_count += 1
            self._in_title = True
        elif lowered == "main":
            self.main_count += 1
        elif lowered == "h1":
            self.h1_count += 1
        if "id" in attrs_by_name:
            element_id = attrs_by_name["id"]
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)
        if lowered == "link" and "canonical" in attrs_by_name.get("rel", "").lower().split():
            self.canonicals.append(attrs_by_name.get("href", ""))
        if lowered == "meta":
            if attrs_by_name.get("name", "").lower() == "description":
                self.descriptions.append(attrs_by_name.get("content", ""))
            if attrs_by_name.get("property", "").lower() == "og:image":
                self.og_images.append(attrs_by_name.get("content", ""))
            if attrs_by_name.get("name", "").lower() in {"robots", "googlebot", "bingbot"}:
                directives = set(re.split(r"[\s,]+", attrs_by_name.get("content", "").lower()))
                if directives.intersection({"noindex", "none"}):
                    self.indexing_blocks.append(attrs_by_name.get("content", ""))
        for attribute in ("href", "src", "poster", "action"):
            value = attrs_by_name.get(attribute)
            if value and not (lowered == "link" and attribute == "href" and "canonical" in attrs_by_name.get("rel", "").lower().split()):
                self.references.append((attribute, value))
        if attrs_by_name.get("srcset"):
            for candidate in attrs_by_name["srcset"].split(","):
                url = candidate.strip().split(maxsplit=1)[0] if candidate.strip() else ""
                if url:
                    self.references.append(("srcset", url))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_text.append(data)


def normalize_base_url(base_url: str) -> str:
    base_url = "/" + base_url.strip("/") if base_url.strip("/") else ""
    return base_url


def site_path_for_page(page: Path) -> str:
    value = page.as_posix()
    if value == "index.html":
        return "/"
    if value.endswith("/index.html"):
        return "/" + value.removesuffix("index.html")
    return "/" + value


def expected_url(site_url: str, base_url: str, page: Path) -> str:
    return site_url.rstrip("/") + base_url + site_path_for_page(page)


def is_ignorable_reference(value: str) -> bool:
    return not value or value.lower().startswith(("mailto:", "tel:", "data:", "javascript:"))


def page_target(site_dir: Path, current: Path, url_path: str, base_url: str) -> Path | None:
    path = unquote(url_path)
    if path.startswith("/"):
        if base_url and not (path == base_url or path.startswith(base_url + "/")):
            return None
        relative = path[len(base_url):].lstrip("/") if base_url else path.lstrip("/")
        target = site_dir / relative
    else:
        target = current.parent / path
    target = Path(posixpath.normpath(str(target)))
    if target == site_dir or str(url_path).endswith("/"):
        target /= "index.html"
    elif not target.suffix and target.is_dir():
        target /= "index.html"
    return target


def resolve_reference(
    site_dir: Path,
    current: Path,
    reference: str,
    site_url: str,
    base_url: str,
) -> tuple[Path | None, str | None]:
    """Return the local target and fragment; external URLs return (None, None)."""
    parsed = urlsplit(reference)
    if not parsed.path and not parsed.netloc and not parsed.scheme:
        return current, unquote(parsed.fragment) or None
    if parsed.scheme and parsed.scheme not in {"http", "https"}:
        return None, None
    if parsed.scheme in {"http", "https"} or parsed.netloc:
        absolute = urlsplit(urljoin(site_url.rstrip("/") + "/", reference))
        origin = f"{absolute.scheme}://{absolute.netloc}"
        if origin != site_url.rstrip("/"):
            return None, None
        return page_target(site_dir, current, absolute.path or "/", base_url), unquote(absolute.fragment) or None
    return page_target(site_dir, current, parsed.path or "", base_url), unquote(parsed.fragment) or None


def validate_html_pages(site_dir: Path, site_url: str, base_url: str) -> list[Issue]:
    issues: list[Issue] = []
    parsed_pages: dict[Path, PageParser] = {}
    html_pages = sorted(site_dir.rglob("*.html"))
    for path in html_pages:
        relative = path.relative_to(site_dir)
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8"))
        parser.close()
        parsed_pages[path.resolve()] = parser
        if parser.title_count != 1 or not "".join(parser.title_text).strip():
            issues.append(Issue(relative, "title", "expected one non-empty <title>"))
        expected = expected_url(site_url, base_url, relative)
        if parser.canonicals != [expected]:
            issues.append(Issue(relative, "canonical", f"expected {expected!r}, found {parser.canonicals!r}"))
        if len(parser.descriptions) != 1 or not parser.descriptions[0].strip():
            issues.append(Issue(relative, "description", "expected one non-empty meta description"))
        if len(parser.og_images) != 1 or not parser.og_images[0].strip():
            issues.append(Issue(relative, "og-image", "expected one non-empty og:image"))
        for directive in parser.indexing_blocks:
            issues.append(Issue(relative, "noindex", f"public page blocks indexing: {directive}"))
        if parser.main_count != 1:
            issues.append(Issue(relative, "main", f"expected one <main>, found {parser.main_count}"))
        if parser.h1_count != 1:
            issues.append(Issue(relative, "h1", f"expected one <h1>, found {parser.h1_count}"))
        for element_id in sorted(parser.duplicate_ids):
            issues.append(Issue(relative, "duplicate-id", f"duplicate id: {element_id}"))

    for current, parser in parsed_pages.items():
        relative = current.relative_to(site_dir)
        for attribute, reference in parser.references + [("og:image", item) for item in parser.og_images]:
            if is_ignorable_reference(reference):
                continue
            target, fragment = resolve_reference(site_dir, current, reference, site_url, base_url)
            if target is None:
                parsed = urlsplit(reference)
                absolute = urlsplit(urljoin(site_url.rstrip("/") + "/", reference))
                is_same_origin = f"{absolute.scheme}://{absolute.netloc}" == site_url.rstrip("/")
                if (reference.startswith("/") and not reference.startswith("//")) or is_same_origin:
                    issues.append(Issue(relative, "basepath", f"{attribute} escapes {base_url or '/'}: {reference}"))
                continue
            try:
                target.relative_to(site_dir)
            except ValueError:
                issues.append(Issue(relative, "internal-path", f"{attribute} escapes the site: {reference}"))
                continue
            if not target.is_file():
                issues.append(Issue(relative, "internal-path", f"missing {attribute} target: {reference}"))
                continue
            if fragment:
                target_parser = parsed_pages.get(target.resolve())
                if target_parser is None:
                    issues.append(Issue(relative, "fragment", f"fragment target is not HTML: {reference}"))
                elif fragment not in target_parser.ids:
                    issues.append(Issue(relative, "fragment", f"missing fragment #{fragment}: {reference}"))
    return issues


def validate_sitemap(site_dir: Path, site_url: str, base_url: str) -> list[Issue]:
    path = site_dir / "sitemap.xml"
    issues: list[Issue] = []
    if not path.is_file():
        return [Issue(Path("sitemap.xml"), "sitemap", "missing sitemap.xml")]
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as error:
        return [Issue(Path("sitemap.xml"), "sitemap", f"invalid XML: {error}")]
    if root.tag.rsplit("}", 1)[-1] != "urlset":
        return [Issue(Path("sitemap.xml"), "sitemap", "root element must be urlset")]
    locations = [element.text.strip() for element in root.iter() if element.tag.rsplit("}", 1)[-1] == "loc" and element.text]
    if not locations:
        issues.append(Issue(Path("sitemap.xml"), "sitemap", "contains no URL locations"))
    expected_pages = {expected_url(site_url, base_url, Path(page)) for page in REQUIRED_PAGES}
    for location in locations:
        parsed = urlsplit(location)
        if parsed.query or parsed.fragment:
            issues.append(Issue(Path("sitemap.xml"), "sitemap-url", f"must not contain a query or fragment: {location}"))
            continue
        if f"{parsed.scheme}://{parsed.netloc}" != site_url.rstrip("/") or not (
            parsed.path == base_url or parsed.path.startswith(base_url + "/")
        ):
            issues.append(Issue(Path("sitemap.xml"), "sitemap-url", f"not a Pages URL: {location}"))
            continue
        target = page_target(site_dir, site_dir / "index.html", parsed.path, base_url)
        if target is None or not target.is_file() or target.suffix != ".html":
            issues.append(Issue(Path("sitemap.xml"), "sitemap-url", f"does not resolve to a generated page: {location}"))
            continue
        expected = expected_url(site_url, base_url, target.relative_to(site_dir))
        if location != expected:
            issues.append(Issue(Path("sitemap.xml"), "sitemap-url", f"not the canonical page URL: {location}"))
    missing = expected_pages.difference(locations)
    if missing:
        issues.append(Issue(Path("sitemap.xml"), "sitemap-pages", f"missing required URLs: {', '.join(sorted(missing))}"))
    return issues


def validate_robots(site_dir: Path, site_url: str, base_url: str) -> list[Issue]:
    path = site_dir / "robots.txt"
    if not path.is_file():
        return [Issue(Path("robots.txt"), "robots", "missing robots.txt")]
    expected = site_url.rstrip("/") + base_url + "/sitemap.xml"
    for line in path.read_text(encoding="utf-8").splitlines():
        name, separator, value = line.partition(":")
        if separator and name.strip().lower() == "sitemap" and value.strip() == expected:
            return []
    return [Issue(Path("robots.txt"), "robots", f"missing Sitemap: {expected}")]


def check_site(site_dir: Path, site_url: str = DEFAULT_SITE_URL, base_url: str = DEFAULT_BASE_URL) -> list[Issue]:
    site_dir = site_dir.resolve()
    base_url = normalize_base_url(base_url)
    if not site_dir.is_dir():
        return [Issue(site_dir, "site", "generated site directory does not exist")]
    issues: list[Issue] = []
    for page in REQUIRED_PAGES:
        if not (site_dir / page).is_file():
            issues.append(Issue(Path(page), "page", "required generated page is missing"))
    if not issues:
        issues.extend(validate_html_pages(site_dir, site_url, base_url))
    issues.extend(validate_sitemap(site_dir, site_url, base_url))
    issues.extend(validate_robots(site_dir, site_url, base_url))
    return issues


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site_dir", type=Path, help="Jekyll destination directory")
    parser.add_argument("--site-url", default=DEFAULT_SITE_URL)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    args = parser.parse_args(argv)
    issues = check_site(args.site_dir, args.site_url, args.base_url)
    if issues:
        print("Rendered-site validation failed:", file=sys.stderr)
        for issue in issues:
            print(f"  {issue}", file=sys.stderr)
        return 1
    print(f"Rendered-site validation passed for {args.site_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
