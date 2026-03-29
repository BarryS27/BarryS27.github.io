import unittest
from pathlib import Path


class ScssStructureTests(unittest.TestCase):
    def test_styles_has_main_import(self) -> None:
        styles = Path('static/css/styles.scss').read_text(encoding='utf-8')
        self.assertIn('@import "main";', styles)


if __name__ == '__main__':
    unittest.main()
