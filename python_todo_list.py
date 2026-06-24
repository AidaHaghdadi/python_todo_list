
tasks = []

user_choose = None
while user_choose != 4 :
    print("\nMenu:")
    print("1-Add Task")
    print("2-Show Tasks")
    print("3-Delete Task")
    print("4-Exit\n")

    try :
        user_choose = int(input("Enter your choose:"))
    except ValueError :
        print("Invalid input!")
        continue
    
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
            try :
                task_number_for_delete = int(input("\nEnter task number to delete :"))
                if 1 <= task_number_for_delete <= len(tasks) :
                    task_number_for_delete -= 1
                    tasks.pop(task_number_for_delete)
                    print("Task deleted!\n")
                    if tasks :
                        print("New tasks list :")
                        for index, task in enumerate(tasks):
                            print(f"{index + 1}. {task}")
                    if not tasks:
                        print("No tasks found!")
                else :
                    print("Invalid task number!")
            except ValueError :
                print("Please enter a number!")
        else : 
            print("No tasks found!")

    elif user_choose == 4 :
        print("Goodbye :)") 

    else:
        print("Invalid choice!")