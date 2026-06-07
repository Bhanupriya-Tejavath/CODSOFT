tasks = []

def show_menu():
    print("\n" + "=" * 40)
    print("        CodSoft To-Do List")
    print("=" * 40)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if not tasks:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        print(f"Task '{new_task}' added successfully!")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                remove_index = int(input("Enter task number to remove: "))
                removed_task = tasks.pop(remove_index - 1)
                print(f"Task '{removed_task}' removed successfully!")

            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting To-Do List Application.")
        break

    else:
        print("Invalid choice. Please try again.")

        
