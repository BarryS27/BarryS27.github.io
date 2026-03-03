import unittest
from pathlib import Path


class WorkflowCITests(unittest.TestCase):
    def test_workflow_has_schedule_and_manual_trigger(self) -> None:
        workflow = Path('.github/workflows/deploy.yml').read_text(encoding='utf-8')
        self.assertIn('schedule:', workflow)
        self.assertIn("cron: '0 0 * * 0'", workflow)
        self.assertIn('workflow_dispatch:', workflow)

    def test_workflow_vendors_package_without_node(self) -> None:
        workflow = Path('.github/workflows/deploy.yml').read_text(encoding='utf-8')
        self.assertIn('https://registry.npmjs.org/@barrys27%2fui/latest', workflow)
        self.assertIn('vendor/@barrys27/ui', workflow)
        self.assertNotIn('setup-node', workflow)
        self.assertNotIn('npm install', workflow)


if __name__ == '__main__':
    unittest.main()
