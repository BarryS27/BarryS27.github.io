import unittest
from pathlib import Path


class BuildPipelineTests(unittest.TestCase):
    def test_scss_wrapper_removed(self) -> None:
        self.assertFalse(Path('scss.py').exists())

    def test_styles_uses_single_main_import(self) -> None:
        styles = Path('static/css/styles.scss').read_text(encoding='utf-8')
        self.assertIn('@import "main";', styles)
        self.assertNotIn('node_modules', styles)
        self.assertNotIn('ui/src/scss/main', styles)


if __name__ == '__main__':
    unittest.main()
