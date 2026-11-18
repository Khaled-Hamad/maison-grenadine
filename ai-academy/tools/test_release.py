#!/usr/bin/env python3
"""Focused release checks for complete, navigable and honestly initialised teaching kits."""

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import posixpath
import sys
import unittest
from urllib.parse import unquote, urljoin, urlsplit
from zipfile import ZipFile

import fitz
from lxml import etree, html
from openpyxl import load_workbook
from pptx import Presentation
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
R = "http://schemas.openxmlformats.org/package/2006/relationships"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
COMMON = {"slides.pptx", "guide.docx", "workbook.xlsx", "guide.pdf", "slides.pdf",
          "guide.md", "practice.csv", "roadmap.csv", "process.svg", "process.pdf",
          "process.png", "process.excalidraw"}
PROJECT = {"architecture.svg", "architecture.pdf", "architecture.png", "architecture.excalidraw",
           "design.svg", "design.pdf", "design.png", "acceptance-tests.csv"}


class ReleaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = json.loads((ROOT / "course-map.json").read_text())["items"]

    def test_requested_coverage_and_real_files(self):
        self.assertEqual(len(self.items), 32)
        weeks = [i for i in self.items if i["kind"] == "week"]
        self.assertEqual([x["week"] for x in weeks], list(range(1, 25)))
        self.assertEqual(sum(x["hours"] for x in weeks), 144)
        self.assertEqual(sum(x["kind"] == "project" for x in self.items), 6)
        for item in self.items:
            with self.subTest(kit=item["id"]):
                directory = ROOT / "kits" / item["id"]
                expected = COMMON | (PROJECT if item["kind"] == "project" else set())
                for name in expected:
                    self.assertGreater((directory / name).stat().st_size, 50)
                with ZipFile(directory / f"{item['id']}-kit.zip") as archive:
                    self.assertIsNone(archive.testzip())
                    self.assertEqual({Path(p).name for p in archive.namelist()}, expected)
                with (directory / "roadmap.csv").open(encoding="utf-8-sig") as source:
                    rows = list(csv.DictReader(source))
                self.assertAlmostEqual(sum(float(r["Planned hours"]) for r in rows), item["hours"])
                if item["id"] == "blueprint":
                    self.assertEqual(len(rows), 24)

    def test_html_links_fragments_and_heading_structure(self):
        pages = [ROOT / "index.html", *sorted((ROOT / "pages").glob("*.html"))]
        self.assertEqual(len(pages), 33)
        trees = {page.resolve(): html.fromstring(page.read_text()) for page in pages}
        for page, tree in trees.items():
            with self.subTest(page=page.name):
                self.assertEqual(len(tree.xpath("//main")), 1)
                self.assertEqual(len(tree.xpath("//h1")), 1)
                ids = tree.xpath("//*[@id]/@id")
                self.assertEqual(len(ids), len(set(ids)))
                for link in tree.xpath("//*[@href]/@href | //*[@src]/@src"):
                    parsed = urlsplit(link)
                    if parsed.scheme or parsed.netloc:
                        continue
                    target = (page.parent / unquote(parsed.path)).resolve() if parsed.path else page
                    self.assertTrue(target.is_relative_to(ROOT), f"{page.name}: escaping link {link}")
                    self.assertTrue(target.exists(), f"{page.name}: missing {link}")
                    if parsed.fragment and target.suffix == ".html":
                        target_tree = trees.get(target)
                        if target_tree is None:
                            target_tree = html.fromstring(target.read_text())
                        self.assertIn(unquote(parsed.fragment), target_tree.xpath("//*[@id]/@id"), f"{page.name}: {link}")

    def test_office_packages_and_real_brand_header(self):
        for item in self.items:
            directory = ROOT / "kits" / item["id"]
            for name in ["slides.pptx", "guide.docx", "workbook.xlsx"]:
                with self.subTest(kit=item["id"], office=name), ZipFile(directory / name) as package:
                    self.assertIsNone(package.testzip())
                    names = set(package.namelist())
                    for part in names:
                        if part.endswith((".xml", ".rels")):
                            tree = etree.fromstring(package.read(part))
                            if part.endswith(".rels"):
                                parent = "" if part == "_rels/.rels" else posixpath.dirname(posixpath.dirname(part))
                                for relation in tree:
                                    if relation.get("TargetMode") == "External":
                                        continue
                                    target = unquote(urlsplit(relation.get("Target")).path)
                                    resolved = target.lstrip("/") if target.startswith("/") else posixpath.normpath(posixpath.join(parent, target))
                                    self.assertIn(resolved, names, f"{item['id']}:{part} -> {resolved}")
                    if name == "guide.docx":
                        self.assertIn("word/brandHeader.xml", names)
                        document = etree.fromstring(package.read("word/document.xml"))
                        self.assertEqual(document.find(f".//{{{W}}}pgSz").get(f"{{{W}}}w"), "11906")
                        self.assertTrue(document.findall(f".//{{{W}}}tbl"))
                        self.assertIn(b"Segoe UI", package.read("word/styles.xml"))
                    if name == "slides.pptx":
                        root_relationships = etree.fromstring(package.read("_rels/.rels"))
                        self.assertFalse(any(relation.get("Type").endswith("classificationlabels") for relation in root_relationships))
                        self.assertFalse(any(path.startswith("docMetadata/") for path in names))
            presentation = Presentation(directory / "slides.pptx")
            self.assertGreaterEqual(len(presentation.slides), 15)
            self.assertTrue(all(slide.has_notes_slide for slide in presentation.slides))
            self.assertLessEqual(len(presentation.slide_layouts), 2)

    def test_workbooks_start_unassessed_and_numeric_examples_reconcile(self):
        for item in self.items:
            wb = load_workbook(ROOT / "kits" / item["id"] / "workbook.xlsx", data_only=True)
            with self.subTest(kit=item["id"]):
                self.assertEqual(wb["Rubric"]["C10"].value, "Not assessed")
                self.assertEqual(wb["Rubric"]["C11"].value, "Not assessed")
                self.assertTrue(all(wb["Safety gates"].cell(r, 2).value == "Pending" for r in range(5, 10)))
                self.assertTrue(all(wb["Safety gates"].cell(r, 3).value is None for r in range(5, 10)))
                self.assertTrue(all(wb["Lab log"].cell(r, 5).value == "Unrun" for r in range(5, wb["Lab log"].max_row+1)))
                self.assertEqual(wb["Budget"]["F13"].value, "Unpriced items remain")
                if item.get("week") == 3:
                    self.assertAlmostEqual(wb["Metrics"]["D5"].value, 8/26)
                    self.assertEqual(wb["Metrics"]["D11"].value, 290)
                    self.assertEqual(wb["Metrics"]["D12"].value, 1000)
                if item.get("week") == 9:
                    self.assertEqual(wb["Cleaned example"]["F16"].value, 265)
                    self.assertEqual(wb["Cleaned example"]["F17"].value, -40)
                    self.assertIsNone(wb["Cleaned example"]["F7"].value)
                if item.get("week") == 10:
                    self.assertAlmostEqual(wb["Analysis"]["E10"].value, .0675)
                if "Capstone rubric" in wb:
                    self.assertEqual(wb["Capstone rubric"]["D12"].value, "Not assessed")
            wb.close()

    def test_pdf_text_and_content_bounds(self):
        for item in self.items:
            for name in ["guide.pdf", "slides.pdf"]:
                with self.subTest(kit=item["id"], pdf=name), fitz.open(ROOT / "kits" / item["id"] / name) as pdf:
                    self.assertGreaterEqual(len(pdf), 3)
                    self.assertGreater(sum(len(p.get_text()) for p in pdf), 2000)
                    for page in pdf:
                        for block in page.get_text("dict")["blocks"]:
                            for line in block.get("lines", []):
                                for span in line["spans"]:
                                    x0, y0, x1, y1 = span["bbox"]
                                    self.assertGreaterEqual(x0, -2)
                                    self.assertGreaterEqual(y0, -2)
                                    self.assertLessEqual(x1, page.rect.width+2, (item["id"], name, span["text"]))
                                    self.assertLessEqual(y1, page.rect.height+2)
                                    self.assertNotIn("\ufffd", span["text"])

    def test_inventory_and_offline_bundle(self):
        inventory = json.loads((ROOT / "resource-inventory.json").read_text())
        self.assertEqual(len(inventory), 432)
        for record in inventory:
            path = ROOT / record["file"]
            self.assertEqual(path.stat().st_size, record["bytes"])
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), record["sha256"])
        with ZipFile(ROOT / "downloads/ai-academy-complete.zip") as archive:
            self.assertIsNone(archive.testzip())
            names = archive.namelist()
            self.assertIn("ai-academy/index.html", names)
            self.assertIn("ai-academy/README.md", names)
            for item in self.items:
                self.assertIn(f"ai-academy/kits/{item['id']}/{item['id']}-kit.zip", names)
            self.assertFalse(any("/private-input/" in name or name.endswith((".potx", ".potm")) or "Brand.zip" in name for name in names))
            self.assertFalse(any("/.build/" in name or "/node_modules/" in name for name in names))


def browser_checks(base):
    evidence = ROOT / ".build"
    evidence.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            context = browser.new_context(viewport={"width": 1440, "height": 1100}, accept_downloads=True)
            page = context.new_page()
            errors = []
            requests = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.on("request", lambda request: requests.append(request.url))
            page.goto(urljoin(base, "index.html"))
            page.wait_for_load_state("networkidle")
            assert page.locator("[data-lesson]:visible").count() == 24
            page.screenshot(path=str(evidence / "website-desktop.png"), full_page=False)
            page.locator("#phase-filter").select_option("0")
            assert page.locator("[data-lesson]:visible").count() == 4
            page.locator("#course-search").fill("no-such-topic-84813")
            assert page.locator("#no-lessons").is_visible()
            page.locator("#reset-course").click()
            assert page.locator("[data-lesson]:visible").count() == 24
            page.locator("#phase-0").screenshot(path=str(evidence / "website-course-map.png"))
            page.locator('[data-review="week-01"]').click()
            assert page.locator("#review-count").inner_text() == "1 / 24"
            page.reload()
            page.wait_for_load_state("networkidle")
            assert page.locator('[data-review="week-01"]').get_attribute("aria-pressed") == "true"
            with page.expect_download() as exported:
                page.locator("#export-progress").click()
            rows = list(csv.reader(io.StringIO(Path(exported.value.path()).read_text(encoding="utf-8-sig"))))
            assert len(rows) == 25 and rows[1][2] == "Reviewed"
            page.locator("#kind-filter").select_option("project")
            assert page.locator("[data-resource]:visible").count() == 6
            page.locator("#library-search").fill("voice")
            assert page.locator("[data-resource]:visible").count() == 1
            page.locator("#kind-filter").select_option("all")
            page.locator("#library-search").fill("")
            with page.expect_download() as downloaded:
                page.locator('a[href="kits/week-01/week-01-kit.zip"]').click()
            with ZipFile(downloaded.value.path()) as kit:
                assert "week-01/guide.docx" in kit.namelist()
            for file in sorted((ROOT / "pages").glob("*.html")):
                page.goto(urljoin(base, f"pages/{file.name}"))
                page.wait_for_load_state("networkidle")
                assert page.locator("main h1").count() == 1, file.name
                assert page.evaluate("document.documentElement.scrollWidth <= innerWidth+1"), file.name
            assert not errors, errors
            if base.startswith("file:"):
                assert not any(url.startswith(("http:", "https:")) for url in requests), requests
            page.set_viewport_size({"width": 390, "height": 844})
            page.goto(urljoin(base, "index.html"))
            page.wait_for_load_state("networkidle")
            assert page.evaluate("document.documentElement.scrollWidth <= innerWidth+1")
            page.locator(".menu-toggle").click()
            assert page.locator("#primary-nav").is_visible()
            page.locator("#primary-nav").get_by_role("link", name="Projects").click()
            assert page.locator(".menu-toggle").get_attribute("aria-expanded") == "false"
            page.goto(urljoin(base, "index.html"))
            page.wait_for_load_state("networkidle")
            page.screenshot(path=str(evidence / "website-mobile.png"), full_page=False)
            page.goto(urljoin(base, "pages/week-07.html"))
            page.wait_for_load_state("networkidle")
            assert page.evaluate("document.documentElement.scrollWidth <= innerWidth+1")
            page.screenshot(path=str(evidence / "website-mobile-lesson.png"), full_page=False)
            context.close()
            blocked = browser.new_context()
            blocked.add_init_script('Object.defineProperty(window,"localStorage",{get(){throw new DOMException("Storage blocked","SecurityError")}})')
            page = blocked.new_page()
            page.goto(urljoin(base, "index.html"))
            page.wait_for_load_state("networkidle")
            assert "session only" in page.locator("#storage-notice").inner_text()
            page.locator('[data-review="week-01"]').click()
            assert page.locator("#review-count").inner_text() == "1 / 24"
            blocked.close()
            plain = browser.new_context(java_script_enabled=False, viewport={"width": 390, "height": 844})
            page = plain.new_page()
            page.goto(urljoin(base, "index.html"))
            assert page.locator("[data-lesson]:visible").count() == 24
            assert page.locator("#primary-nav").is_visible()
            assert page.locator("#course-search").is_hidden()
            plain.close()
        finally:
            browser.close()
    print("Browser: filtering, local reviews, export, downloads, 32 detail pages, mobile, blocked storage and no-JS routes passed.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-browser", action="store_true")
    parser.add_argument("--base-url", default=ROOT.as_uri()+"/")
    args = parser.parse_args()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ReleaseTests))
    if not result.wasSuccessful():
        return 1
    if not args.skip_browser:
        browser_checks(args.base_url)
    return 0


if __name__ == "__main__":
    sys.exit(main())
