# Simple To-Do List Application (CLI)

tasks = []  # list to store tasks

def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print("Task added successfully.")

def delete_task():
    show_tasks()
    if tasks:
        try:
            task_no = int(input("\nEnter task number to delete: "))
            removed_task = tasks.pop(task_no - 1)
            print(f"Removed task: {removed_task}")
        except (ValueError, IndexError):
            print("Invalid task number.")

def main():
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
