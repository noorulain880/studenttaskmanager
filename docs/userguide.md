# Student Task Manager – User Guide

## 1. Introduction

Student Task Manager is a simple Python console application that helps students manage their daily tasks. Users can add, view, complete, and delete tasks.

## 2. Requirements

- Python 3 installed on your computer.
- Git (optional, for cloning the repository).

## 3. Starting the Application

Open the project folder in VS Code or Command Prompt.

Run the following command:

```bash
python main.py
```

The application menu will appear.

## 4. Using the Application

### Add Task
- Select option `1`.
- Enter your task title.
- The application creates a task with a unique ID.

### Display Tasks
- Select option `2`.
- All available tasks and their status will be displayed.
- Tasks can have Pending or Completed status.

### Complete Task
- Select option `3`.
- Enter the task ID.
- The application marks the selected task as completed.

### Delete Task
- Select option `4`.
- Enter the task ID.
- The selected task will be deleted.

### Exit
- Select option `5` to close the application.

## 5. Error Handling

- Empty task titles are not accepted.
- Invalid task IDs are handled with an error message.
- Non-numeric task IDs are rejected.

## 6. Running Tests

To run automated tests, execute:

```bash
python -m unittest discover -s tests -v
```

The tests verify adding, completing, and deleting tasks, along with empty-title validation.

## 7. Important Note

Tasks are stored in memory. They are not permanently saved after the application closes.