# Student Task Manager

A simple console-based Student Task Manager developed using Python. This project demonstrates Python programming, object-oriented programming, Git, GitHub, branching, pull requests, automated testing, and GitHub Actions.

**Project status:** Completed

## Features

- Add new tasks with unique IDs.
- Display all tasks.
- Mark tasks as completed.
- Delete tasks.
- Validate empty task titles.
- Handle invalid user input.
- Automated unit testing using Python unittest.
- GitHub Actions workflow for automatic testing.

## Technologies Used

- Python
- Git
- GitHub
- GitHub Actions
- Python unittest

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/noorulain880/studenttaskmanager.git
   ```

2. Open the project folder:

   ```bash
   cd studenttaskmanager
   ```

3. Make sure Python is installed.

## How to Run

Run the application using:

```bash
python main.py
```

Follow the menu displayed in the terminal:

1. Add Task
2. Display Tasks
3. Complete Task
4. Delete Task
5. Exit

## Running Automated Tests

Run the unit tests using:

```bash
python -m unittest discover -s tests -v
```

The tests check task creation, empty task validation, task completion, and task deletion.

## GitHub Actions

GitHub Actions automatically runs the unit tests when code is pushed to the `main` branch or when a pull request targets `main`.

## Project Structure

```text
studenttaskmanager/
│
├── main.py
├── task_manager.py
├── tests/
│   └── test_task_manager.py
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── docs/
│   └── userguide.md
├── README.md
├── LABREPORT.md
└── LICENSE
```

## Author

Student Task Manager – Python and GitHub Assignment