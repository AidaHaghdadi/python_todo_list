import json
from task import Task

def save_tasks(tasks):
    tasks_data = [task.to_dict() for task in tasks]

    with open("tasks.json", "w") as file:
        json.dump(tasks_data, file)
    
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks_data = json.load(file)

        tasks = [Task.from_dict(data) for data in tasks_data]
        return tasks

    except FileNotFoundError:
        return []