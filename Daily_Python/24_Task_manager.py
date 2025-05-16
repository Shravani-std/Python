tasks = []

def display_menu():
    print("\n=== Task Manager ===")
    print("1. Add Task" \
          "\n2. View Tasks" \
          "\n3. Complete Task" \
          "\n4. Delete Task" \
          "\n0. Exit")

def addTask():
    title = input("\nEnter Task Title: ")
    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added successfully!")

def viewTask():
    if not tasks:
        print("No tasks found.")
        return
    print("\n=== My Tasks ===")
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else " "
        print(f"{i + 1}. [{status}] {task['title']}")

def completeTask():
    viewTask()
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number that is completed: "))
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return
        task_to_complete = tasks[task_number - 1]
        task_to_complete["completed"] = True
        print(f"Task '{task_to_complete['title']}' marked as completed!")
    except ValueError:
        print("Please enter a valid number.")

def deleteTask():
    viewTask()
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to delete: "))
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return
        deleted_task = tasks.pop(task_number - 1)
        print(f"Task '{deleted_task['title']}' deleted successfully!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (0-4): ")
        if choice == "1":
            addTask()
        elif choice == "2":
            viewTask()
        elif choice == "3":
            completeTask()
        elif choice == "4":
            deleteTask()
        elif choice == "0":
            print("Goodbye...")
            break
        else:
            print("Invalid choice.")

main()
