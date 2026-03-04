import unittest
from pathlib import Path


class TemplateStructureTests(unittest.TestCase):
    def test_index_imports_macros_with_context(self) -> None:
        index_html = Path('templates/index.html').read_text(encoding='utf-8')
        self.assertIn('{% import "macros.html" as macros with context %}', index_html)

    def test_macros_file_contains_required_macros(self) -> None:
        macros_html = Path('templates/macros.html').read_text(encoding='utf-8')
        self.assertIn('{% macro render_item', macros_html)
        self.assertIn('{% macro render_skill_category', macros_html)


if __name__ == '__main__':
    unittest.main()
