
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

if user_choose == 4 :
    print("Goodby:)")

