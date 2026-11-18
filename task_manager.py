
class TaskManager:

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        if not title.strip():
            raise ValueError("Task title cannot be empty.")

        task = {
            "id": self.next_id,
            "title": title.strip(),
            "completed": False
        }

        self.tasks.append(task)
        self.next_id += 1
        return task

    def display_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        if not isinstance(task_id, int):
            return False

        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    return False

                task["completed"] = True
                return True

        return False

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return True
        return False
