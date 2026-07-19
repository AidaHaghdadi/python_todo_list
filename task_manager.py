class TaskManager:
    def __init__ (self):
        self.tasks = []

    # Add task function
    def add_task(self, task):
        self.tasks.append(task)

    # Show list of tasks function
    def show_tasks(self):
        return self.tasks
    
    # Edit task function
    def edit_task(self, task_number, new_title, new_description):
        if 1<= task_number <= len(self.tasks):
            task_for_edit = self.tasks[task_number - 1]
            if new_title:
                task_for_edit.title = new_title
            if new_description:
                task_for_edit.description = new_description
            return True
        else:
            return False