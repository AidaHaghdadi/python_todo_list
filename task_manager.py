class TaskManager:
    def __init__ (self):
        self.tasks = []

    # Add task function
    def add_task(self, task):
        self.tasks.append(task)