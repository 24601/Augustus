from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
from scripts.check_site import check_site  # noqa: E402


SITE_URL = "https://24601.github.io"
BASE_URL = "/Augustus"


class SiteCheckTests(unittest.TestCase):
    def make_site(self) -> Path:
        tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(tempdir.cleanup)
        site = Path(tempdir.name)
        (site / "assets").mkdir()
        (site / "assets/social.png").write_bytes(b"not an image, but a rendered asset")
        (site / "assets/site.css").write_text("body {}", encoding="utf-8")
        self.write_page(site, "index.html", "Home", "home", '<a href="#detail">Details</a><p id="detail">Here</p>')
        self.write_page(site, "ecosystem.html", "Ecosystem", "ecosystem", '<a href="/Augustus/assets/site.css">CSS</a>')
        self.write_page(site, "examples.html", "Examples", "examples", "")
        (site / "robots.txt").write_text("User-agent: *\nSitemap: https://24601.github.io/Augustus/sitemap.xml\n", encoding="utf-8")
        (site / "sitemap.xml").write_text(
            '<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            "<url><loc>https://24601.github.io/Augustus/</loc></url>"
            "<url><loc>https://24601.github.io/Augustus/ecosystem.html</loc></url>"
            "<url><loc>https://24601.github.io/Augustus/examples.html</loc></url>"
            "</urlset>",
            encoding="utf-8",
        )
        return site

    def write_page(self, site: Path, name: str, title: str, heading: str, body: str) -> None:
        canonical_path = "/" if name == "index.html" else f"/{name}"
        page = f"""<!doctype html>
<html><head><title>{title}</title>
<link rel="canonical" href="https://24601.github.io/Augustus{canonical_path}">
<meta name="description" content="{title} description">
<meta property="og:image" content="https://24601.github.io/Augustus/assets/social.png">
</head><body><main><h1>{heading}</h1>{body}</main></body></html>"""
        (site / name).write_text(page, encoding="utf-8")

    def codes(self, site: Path) -> set[str]:
        return {issue.code for issue in check_site(site, SITE_URL, BASE_URL)}

    def test_complete_rendered_site_passes_without_fetching_external_links(self) -> None:
        site = self.make_site()
        index = site / "index.html"
        index.write_text(index.read_text(encoding="utf-8").replace("</main>", '<a href="https://example.test/no-fetch">External</a><script src="//cdn.example.test/site.js"></script></main>'), encoding="utf-8")
        self.assertEqual([], check_site(site, SITE_URL, BASE_URL))

    def test_page_semantics_are_structural_not_copy_based(self) -> None:
        site = self.make_site()
        page = site / "index.html"
        page.write_text(page.read_text(encoding="utf-8").replace("<title>Home</title>", "<title> </title>").replace("<h1>home</h1>", "<h2>home</h2>"), encoding="utf-8")
        self.assertEqual({"h1", "title"}, self.codes(site))

    def test_canonical_must_include_the_github_pages_basepath(self) -> None:
        site = self.make_site()
        page = site / "ecosystem.html"
        page.write_text(page.read_text(encoding="utf-8").replace("https://24601.github.io/Augustus/ecosystem.html", "https://24601.github.io/ecosystem.html"), encoding="utf-8")
        self.assertEqual({"canonical"}, self.codes(site))

    def test_internal_assets_and_fragments_must_resolve(self) -> None:
        site = self.make_site()
        page = site / "ecosystem.html"
        page.write_text(page.read_text(encoding="utf-8").replace("assets/site.css", "assets/missing.css").replace("</main>", '<a href="/Augustus/#missing">Broken fragment</a></main>'), encoding="utf-8")
        self.assertEqual({"fragment", "internal-path"}, self.codes(site))

    def test_percent_encoded_fragments_resolve_to_decoded_ids(self) -> None:
        site = self.make_site()
        page = site / "index.html"
        page.write_text(page.read_text().replace('href="#detail"', 'href="#%64etail"'))
        self.assertEqual([], check_site(site, SITE_URL, BASE_URL))

    def test_public_pages_cannot_silently_add_noindex_directives(self) -> None:
        for name, content in (("robots", "noindex,follow"), ("Googlebot", "NONE"), ("bingbot", "noindex")):
            with self.subTest(name=name, content=content):
                site = self.make_site()
                page = site / "index.html"
                page.write_text(page.read_text().replace("</head>", f'<meta name="{name}" content="{content}"></head>'))
                self.assertEqual({"noindex"}, self.codes(site))

    def test_root_relative_internal_paths_must_keep_the_project_basepath(self) -> None:
        site = self.make_site()
        page = site / "ecosystem.html"
        page.write_text(page.read_text(encoding="utf-8").replace("/Augustus/assets/site.css", "/assets/site.css"), encoding="utf-8")
        self.assertEqual({"basepath"}, self.codes(site))

    def test_duplicate_ids_are_reported_before_fragment_links_become_ambiguous(self) -> None:
        site = self.make_site()
        page = site / "index.html"
        page.write_text(page.read_text(encoding="utf-8").replace('id="detail"', 'id="detail">First</p><p id="detail"'), encoding="utf-8")
        self.assertEqual({"duplicate-id"}, self.codes(site))

    def test_sitemap_and_robots_are_part_of_the_generated_site_contract(self) -> None:
        site = self.make_site()
        (site / "sitemap.xml").write_text("<urlset><url><loc>https://24601.github.io/</loc></url>", encoding="utf-8")
        (site / "robots.txt").write_text("User-agent: *\n", encoding="utf-8")
        self.assertEqual({"robots", "sitemap"}, self.codes(site))

    def test_sitemap_locations_must_resolve_to_canonical_generated_pages(self) -> None:
        site = self.make_site()
        sitemap = site / "sitemap.xml"
        sitemap.write_text(sitemap.read_text(encoding="utf-8").replace("ecosystem.html", "missing.html"), encoding="utf-8")
        self.assertEqual({"sitemap-pages", "sitemap-url"}, self.codes(site))


if __name__ == "__main__":
    unittest.main()
