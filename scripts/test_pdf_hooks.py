"""Regression checks for product scoping and printable content preservation."""

from types import SimpleNamespace
import unittest

from bs4 import BeautifulSoup

import pdf_hooks


def page(path):
    return SimpleNamespace(file=SimpleNamespace(src_uri=path), meta={})


class PdfHooksTest(unittest.TestCase):
    def test_only_navigation_pages_are_exported(self):
        selected = page("guides/color-kit-grande/assembly.md")
        pdf_hooks.on_nav(SimpleNamespace(pages=[selected]))
        for item, expected in [
            (selected, True),
            (page("guides/esp32-color-kit-grande.md"), False),
            (page("guides/color-kit-grande/assembly.de.md"), False),
            (page("guides/esp32-s3-pendrive.md"), False),
        ]:
            pdf_hooks.on_page_markdown("text", item)
            self.assertEqual(item.meta["pdf"], expected)

    def test_assembly_keeps_header_row_and_every_step(self):
        item = page("guides/color-kit-grande/assembly.md")
        item.meta["pdf"] = True
        html = "<table><thead><tr><th>First step</th></tr></thead><tbody>"
        html += "".join(f"<tr><td>Instruction {i}</td></tr>" for i in range(1, 19))
        result = BeautifulSoup(pdf_hooks.on_page_content(html + "</tbody></table>", item), "html.parser")
        self.assertEqual(len(result.select(".pdf-step")), 19)
        self.assertIn("First step", result.get_text())
        for i in range(1, 19):
            self.assertIn(f"Instruction {i}", result.get_text())

    def test_troubleshooting_preserves_long_rows(self):
        item = page("guides/color-kit-grande/troubleshooting.md")
        item.meta["pdf"] = True
        instructions = "Long diagnostic instructions. " * 200
        html = f"<table><tbody><tr><td>Symptom</td><td>{instructions}</td></tr></tbody></table>"
        result = BeautifulSoup(pdf_hooks.on_page_content(html, item), "html.parser")
        self.assertIsNone(result.find("table"))
        self.assertIn(instructions, result.get_text())

    def test_video_query_parameters_are_preserved(self):
        item = page("guides/color-kit-grande/video-tutorials.md")
        item.meta["pdf"] = True
        html = '<iframe src="https://www.youtube.com/embed/example?si=token"></iframe>'
        result = BeautifulSoup(pdf_hooks.on_page_content(html, item), "html.parser")
        self.assertEqual(result.a["href"], "https://www.youtube.com/watch?v=example&si=token")
        self.assertIsNone(result.find("iframe"))

    def test_mkdocs_video_markup_becomes_a_link(self):
        item = page("guides/esp32-s3-pendrive.md")
        item.meta["pdf"] = True
        html = '<img alt="type:video" src="../../img/demo.mp4">'
        result = BeautifulSoup(pdf_hooks.on_page_content(html, item), "html.parser")
        self.assertEqual(result.a["href"], "../../img/demo.mp4")
        self.assertIsNone(result.find("img"))


if __name__ == "__main__":
    unittest.main()
