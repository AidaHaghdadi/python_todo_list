class TaskManager:
    def __init__ (self):
        self.tasks = []

    # Add task function
    def add_task(self, task):
        self.tasks.append(task)

    # Show list of tasks function
    def show_tasks(self):
        return self.tasks