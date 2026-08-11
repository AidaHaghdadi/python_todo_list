# Python To-Do List

A simple command-line To-Do List application built with Python and Object-Oriented Programming (OOP).

## Features

* Add new tasks
* Display all tasks
* Edit tasks
* Search tasks by title
* Complete tasks
* Delete tasks with confirmation
* Change task priority by moving tasks
* Add optional task descriptions
* Save tasks automatically using JSON
* Load saved tasks when the application starts
* Keep task completion status after restarting the program

## Project Structure

```text
python_todo_list/
│
├── main.py
├── task.py
├── task_manager.py
├── storage.py
├── tasks.json
└── README.md
```

## How It Works

The application uses Python objects to manage tasks during runtime.

Before saving tasks, each `Task` object is converted into a dictionary using the `to_dict()` method. The dictionaries are then stored in a JSON file using Python's built-in `json` module.

When the application starts, the JSON data is loaded using `json.load()`. The dictionaries are then converted back into `Task` objects using the `from_dict()` method.

```text
Task Object
    ↓
to_dict()
    ↓
Dictionary
    ↓
json.dump()
    ↓
tasks.json
```

When loading:

```text
tasks.json
    ↓
json.load()
    ↓
Dictionary
    ↓
from_dict()
    ↓
Task Object
```

## Technologies

* Python
* Object-Oriented Programming (OOP)
* JSON
* Git & GitHub

## How to Run

Clone the repository and run:

```bash
python main.py
```

The application will automatically load previously saved tasks from `tasks.json`.


## Author

Aida Haghdadi
