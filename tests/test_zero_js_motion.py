import unittest
from pathlib import Path


class ZeroJsMotionTests(unittest.TestCase):
    def test_template_has_no_nonessential_js_bundles(self) -> None:
        index_html = Path('templates/index.html').read_text(encoding='utf-8')
        self.assertNotIn("js/script.js", index_html)
        self.assertNotIn("js/easter-eggs.js", index_html)

    def test_motion_is_css_only(self) -> None:
        core_scss = Path('static/css/_core.scss').read_text(encoding='utf-8')
        self.assertIn('scroll-behavior: smooth;', core_scss)
        self.assertNotIn('&.in-view', core_scss)

    def test_nonessential_js_files_removed(self) -> None:
        self.assertFalse(Path('static/js/script.js').exists())
        self.assertFalse(Path('static/js/easter-eggs.js').exists())


if __name__ == '__main__':
    unittest.main()
