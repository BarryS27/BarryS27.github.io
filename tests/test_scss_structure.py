import unittest
from pathlib import Path


class ScssStructureTests(unittest.TestCase):
    def test_styles_uses_flat_core_and_vendor_ui_import(self) -> None:
        styles = Path('static/css/styles.scss').read_text(encoding='utf-8')
        self.assertIn('@import "core";', styles)
        self.assertIn('@import "ui/src/scss/main";', styles)

    def test_flat_core_exists_and_legacy_dirs_removed(self) -> None:
        self.assertTrue(Path('static/css/_core.scss').exists())
        self.assertFalse(Path('static/css/common').exists())
        self.assertFalse(Path('static/css/@barrys27').exists())


if __name__ == '__main__':
    unittest.main()
