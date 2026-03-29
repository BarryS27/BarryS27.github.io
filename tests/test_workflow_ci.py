import unittest
from pathlib import Path


class WorkflowCITests(unittest.TestCase):
    def test_workflow_triggers_include_push_schedule_and_manual(self) -> None:
        workflow = Path('.github/workflows/deploy.yml').read_text(encoding='utf-8')
        self.assertIn('push:', workflow)
        self.assertIn('schedule:', workflow)
        self.assertIn("cron: '0 0 * * 0'", workflow)
        self.assertIn('workflow_dispatch:', workflow)

    def test_workflow_uses_direct_curl_sass_and_auto_commit(self) -> None:
        workflow = Path('.github/workflows/deploy.yml').read_text(encoding='utf-8')
        self.assertIn('curl -L https://unpkg.com/@barrys27/ui/src/scss/main.scss -o static/css/main.scss', workflow)
        self.assertIn('sudo snap install dart-sass', workflow)
        self.assertIn('dart-sass static/css/styles.scss static/css/styles.css --no-source-map', workflow)
        self.assertIn('stefanzweifel/git-auto-commit-action@v5', workflow)
        self.assertIn('build/static/css/styles.css is missing or empty', workflow)


if __name__ == '__main__':
    unittest.main()
