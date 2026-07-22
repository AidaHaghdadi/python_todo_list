from task import Task
from task_manager import TaskManager

def show_menu():
    print("\nMenu:")
    print("1-Add Task")
    print("2-Show Tasks")
    print("3-Edit Task")
    print("4-Search Task")
    print("5-Complete Task")
    print("6-Move Task")
    print("7-Delete Task")
    print("8-Exit")

def print_tasks(tasks):
    result = user_task.show_tasks()

    if result:
        print("\nTask List:")
        for index, task in enumerate(result):
            print(f"{index + 1}. {task}")
        return True
    else:
        print("Task list is empty!")
        return False

user_task = TaskManager()
user_selection = None
while user_selection != 8 :
    show_menu()
    try:
        user_selection = int(input("Enter your selection :"))
    except ValueError:
        print("Invalid Input!")
        continue
    
    # Add task
    if user_selection == 1:
        while True:
            task_title = input("Enter your task: ").strip()
            if task_title:
                task_title = task_title.capitalize()
                break
            print("Task title cannot be empty!")

        task_description = input("Enter description (optional): ").capitalize()

        task = Task(task_title, task_description)
        user_task.add_task(task)
        print("Task added!")

    # Show task
    elif user_selection == 2:
        print_tasks(user_task.tasks)
        
    # Edit task
    elif user_selection == 3:
        if user_task.tasks :
            print_tasks(user_task.tasks)
            try:
                task_number = int(input("Enter the number of task that you want to edit:"))
            except ValueError:
                print("Invalid Input!")
                continue

            new_title = input("New title (leave blank to keep current):").capitalize()
            new_description = input("New description (leave blank to keep current):").capitalize()

            result = user_task.edit_task(task_number, new_title, new_description)
            if result == True:
                print("Task updated successfully.")

            else:
                print("Invalid Choice Number!")
        else:
            print("Task list is empty!")

    # Search task
    elif user_selection == 4:
        if user_task.tasks:
            task_title = input("Enter your task title :").capitalize()
            result = user_task.search_task(task_title)

            if result:
                print_tasks(result)
            else:
                print("No task fount!")
        else:
            print("Task list is empty!")

    # Complete task
    elif user_selection == 5:
        if user_task.tasks:
            print_tasks(user_task.tasks)
            try:
                comp_task = int(input("Enter the number of task that you complete:"))
            except ValueError:
                print("Invalid input!")
            
            result = user_task.complete_task(comp_task)
            if result == True:
                print("The status of task changed.")
            else:
                print("Invalid number choice!")
        else:
            print("Task list is empty!")

    elif user_selection == 7:
        if user_task.tasks:
            print_tasks(user_task.tasks)
            try:
                del_task_num = int(input("Enter the number of task that you want to delete:"))
            except ValueError:
                print("Invalid input!")
            
            result = user_task.delete_task(del_task_num)
            if result == True:
                print("Task deleted.")
            elif result == False:
                print("Operation cancelled.")
            elif result == "Invalid answer":
                print("Invalid answer! please choice 'y' or 'n'")
            else:
                print("Invalid choice number!")

        else:
            print
    elif user_selection == 8:
        print("Exit Program.")

    else:
        print("Invalid Choice Number!")