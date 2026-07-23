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
    
    # Search task function
    def search_task(self, task_title):
        result = []

        for task in self.tasks:
            if task_title == task.title:
                result.append(task)
        return result
    
    # Complete task function
    def complete_task(self, comp_task):
        if 1<= comp_task <= len(self.tasks):
            task_for_comp = self.tasks[comp_task - 1]

            if task_for_comp.is_completed:
                return "Already complete"

            task_for_comp.is_completed = True
            return True

        else:
            return False

    # Move task function for change priority
    def move_task(self, task1, task2):
        if not (1 <= task1 <= len(self.tasks)):
            return "Invalid task1"
        if not (1 <= task2 <= len(self.tasks)):
            return "Invalid task2"
        if task1 == task2:
            return "same"

        self.tasks[task1 - 1], self.tasks[task2 - 1] = self.tasks[task2 - 1], self.tasks[task1 - 1]
        return True
            
    # Delete task function 
    def delete_task(self, del_task_num):
        if 1<= del_task_num <= len(self.tasks):
            ask = input("Are you sure for delete this task (y/n):").lower()
            if ask == "y" :
                self.tasks.pop(del_task_num - 1)
                return True
            elif ask == "n":
                return False
            else :
                return "Invalid answer"
        return "Invalid number"

