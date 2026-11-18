
from task_manager import TaskManager

manager = TaskManager()

while True:
    print("\n===== STUDENT TASK MANAGER =====")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task title: ")
        try:
            task = manager.add_task(title)
            print("Task added successfully! ID:", task["id"])
        except ValueError as error:
            print(error)

    elif choice == "2":
        tasks = manager.display_tasks()

        if not tasks:
            print("No tasks available.")
        else:
            for task in tasks:
                status = "Completed" if task["completed"] else "Pending"
                print(
                    task["id"], "-", task["title"],
                    "-", status
                )

    elif choice == "3":
        try:
            task_id = int(input("Enter task ID: "))
            if manager.complete_task(task_id):
                print("Task completed successfully!")
            else:
                print("Invalid task ID.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        try:
            task_id = int(input("Enter task ID: "))

            if manager.delete_task(task_id):
                print("Task deleted successfully!")
            else:
                print("Task ID not found. No task was deleted.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
