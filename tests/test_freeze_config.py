import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from freeze import REQUIRED_BUILD_ARTIFACTS, app, optimize_images


class FreezeConfigTests(unittest.TestCase):
    def test_required_freezer_configuration_present(self) -> None:
        self.assertEqual(app.config['FREEZER_DESTINATION'], 'build')
        self.assertIn('FREEZER_BASE_URL', app.config)
        self.assertTrue(app.config['FREEZER_BASE_URL'].startswith('http'))


    def test_required_artifacts_do_not_include_nonessential_js(self) -> None:
        self.assertNotIn('static/js/script.js', REQUIRED_BUILD_ARTIFACTS)
        self.assertNotIn('static/js/easter-eggs.js', REQUIRED_BUILD_ARTIFACTS)

    @patch('freeze.PILLOW_AVAILABLE', True)
    @patch('freeze.Image')
    def test_optimize_images_accepts_valid_image_folder(self, mock_image_module) -> None:
        image_object = MagicMock()
        image_object.format = 'PNG'
        mock_context = MagicMock()
        mock_context.__enter__.return_value = image_object
        mock_image_module.open.return_value = mock_context

        with tempfile.TemporaryDirectory() as tmpdir:
            image_path = Path(tmpdir) / 'sample.png'
            image_path.write_bytes(b'placeholder')
            self.assertTrue(optimize_images(Path(tmpdir)))


if __name__ == '__main__':
    unittest.main()
