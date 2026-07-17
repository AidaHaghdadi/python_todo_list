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


user_selection = None
while user_selection != 8 :
    show_menu()
    try:
        user_selection = int(input("Enter your selection :"))
    except ValueError:
        print("Invalid Input!")
        continue
    else:
        print("Invalid Choice Number!")