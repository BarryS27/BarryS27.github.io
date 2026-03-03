import json
import os
import tempfile
import unittest
from pathlib import Path

from app import PORTFOLIO_DATA, app, is_development_mode, load_portfolio_data


class PortfolioDataTests(unittest.TestCase):
    def test_portfolio_data_has_template_keys(self) -> None:
        required_keys = {"profile", "about", "now", "skills", "awards", "projects", "seo"}
        self.assertTrue(required_keys.issubset(PORTFOLIO_DATA.keys()))

        self.assertIn("title", PORTFOLIO_DATA["profile"])
        self.assertIn("location", PORTFOLIO_DATA["profile"])

        for interest in PORTFOLIO_DATA["about"]["interests"]:
            self.assertTrue({"label", "icon", "color"}.issubset(interest.keys()))

        for category in PORTFOLIO_DATA["skills"]:
            self.assertTrue({"category", "items"}.issubset(category.keys()))

        for project in PORTFOLIO_DATA["projects"]:
            self.assertTrue({"title", "description", "link"}.issubset(project.keys()))

    def test_load_portfolio_data_from_json_file(self) -> None:
        payload = {"profile": {"title": "T", "location": "L"}, "about": {}, "now": {}, "skills": [], "awards": [], "projects": []}
        with tempfile.TemporaryDirectory() as tmpdir:
            data_file = Path(tmpdir) / "data.json"
            data_file.write_text(json.dumps(payload), encoding="utf-8")
            loaded = load_portfolio_data(data_file)
        self.assertEqual(loaded["profile"]["title"], "T")

    def test_home_route_renders(self) -> None:
        client = app.test_client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        body = response.get_data(as_text=True)
        self.assertIn(PORTFOLIO_DATA["profile"]["title"], body)
        self.assertIn(PORTFOLIO_DATA["seo"]["description"], body)

    def test_development_mode_flag(self) -> None:
        original = os.environ.get("FLASK_ENV")
        try:
            os.environ["FLASK_ENV"] = "development"
            self.assertTrue(is_development_mode())
            os.environ["FLASK_ENV"] = "production"
            self.assertFalse(is_development_mode())
        finally:
            if original is None:
                os.environ.pop("FLASK_ENV", None)
            else:
                os.environ["FLASK_ENV"] = original


if __name__ == "__main__":
    unittest.main()
