
tasks = []

user_choose = None
while user_choose != 4 :
    print("\nMenu:")
    print("1-Add Task")
    print("2-Show Tasks")
    print("3-Delete Task")
    print("4-Exit\n")

    user_choose = int(input("Enter your choose:"))

    if user_choose == 1 :
        user_task = input("Enter your task :")
        tasks.append(user_task)
        print("Task added!\n")

    elif user_choose == 2 :
        if len(tasks) == 0:
            print("No tasks found!")
        else :    
            print("\nTasks list :")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
    
    elif user_choose == 3 :
        if len(tasks) != 0 :
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            task_number_for_delete = int(input("\nEnter task number to delete :"))
            task_number_for_delete -= 1
            tasks.pop(task_number_for_delete)
            print("Task deleted!\n")
            print("New tasks list :")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
        else : 
            print("No tasks list found!")

if user_choose == 4 :
    print("Goodby:)")