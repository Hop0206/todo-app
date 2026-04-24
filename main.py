# 📝 To-Do List Application

# This list will store tasks temporarily (in memory)
tasks = []


def show_menu():
    print("\n====================")
    print("📝 TO-DO LIST MENU")
    print("====================")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Exit")
    print("====================")


def add_task():
    task = input("Enter a new task: ")
    if task.strip() == "":
        print("⚠️ Task cannot be empty!")
    else:
        tasks.append(task)
        print(f"✅ Task added: {task}")


def view_tasks():
    if len(tasks) == 0:
        print("📭 No tasks yet.")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def delete_task():
    if len(tasks) == 0:
        print("📭 No tasks to delete.")
        return

    view_tasks()
    try:
        number = int(input("Enter task number to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"🗑️ Deleted: {removed}")
        else:
            print("⚠️ Invalid number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please select 1-4.")


# Run the program
if __name__ == "__main__":
    main()
