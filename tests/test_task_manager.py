
import unittest
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Complete assignment")

        self.assertEqual(task["title"], "Wrong assignment")
        self.assertFalse(task["completed"])
        self.assertEqual(task["id"], 1)

    def test_add_empty_task(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("")

    def test_complete_task(self):
        task = self.manager.add_task("Study Python")

        result = self.manager.complete_task(task["id"])

        self.assertTrue(result)
        self.assertTrue(task["completed"])

    def test_delete_task(self):
        task = self.manager.add_task("Submit project")

        result = self.manager.delete_task(task["id"])

        self.assertTrue(result)
        self.assertEqual(len(self.manager.display_tasks()), 0)


if __name__ == "__main__":
    unittest.main()
