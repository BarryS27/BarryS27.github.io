import unittest
from pathlib import Path
from unittest.mock import patch

from scss import compile_scss


class BuildPipelineTests(unittest.TestCase):
    def test_browserslist_file_present(self) -> None:
        content = Path('.browserslistrc').read_text(encoding='utf-8')
        self.assertIn('last 2 versions', content)

    @patch('scss.ensure_dart_sass')
    @patch('scss.ensure_lightningcss')
    @patch('scss.subprocess.run')
    def test_compile_scss_uses_binary_pipeline(self, mock_run, mock_lightning, mock_sass) -> None:
        mock_sass.return_value = Path('/tmp/sass')
        mock_lightning.return_value = Path('/tmp/lightningcss')

        self.assertTrue(compile_scss())
        self.assertEqual(mock_run.call_count, 2)

    @patch('scss.ensure_dart_sass', side_effect=RuntimeError('boom'))
    def test_compile_scss_handles_provision_failure(self, _mock_sass) -> None:
        self.assertFalse(compile_scss())

    def test_scss_pipeline_has_no_node_paths(self) -> None:
        pipeline = Path('scss.py').read_text(encoding='utf-8')
        self.assertNotIn('node_modules', pipeline)
        self.assertNotIn('npm', pipeline)

    def test_scss_pipeline_includes_vendor_load_path(self) -> None:
        pipeline = Path('scss.py').read_text(encoding='utf-8')
        self.assertIn('"vendor"', pipeline)


if __name__ == '__main__':
    unittest.main()
