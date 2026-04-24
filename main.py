tasks = []

while True:
    print("\nTo-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Added!")

    elif choice == "2":
        for i, t in enumerate(tasks, 1):
            print(i, t)

    elif choice == "3":
        break
