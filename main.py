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


user_task = TaskManager()
user_selection = None
while user_selection != 8 :
    show_menu()
    try:
        user_selection = int(input("Enter your selection :"))
    except ValueError:
        print("Invalid Input!")
        continue
    
    # Add book
    if user_selection == 1:
        task_title = input("Enter your task :").capitalize()
        task_description = input("Enter description (optional): ").capitalize

        task = Task(task_title, task_description)
        user_task.add_task(task)
        print("Task added!")

    elif user_selection == 8:
        print("Exit Program.")

    else:
        print("Invalid Choice Number!")