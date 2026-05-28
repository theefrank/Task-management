# Task list (each task is a dictionary)
tasks = []

# Function to add a task
def add_task():
    name = input("Enter task name: ")
    tasks.append({"name": name, "completed": False})
    print("Task added successfully!")

# Function to mark task as complete
def mark_complete():
    view_pending()
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to view pending tasks
def view_pending():
    print("\nPending Tasks:")
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{i+1}. {task['name']}")

# Function to view progress
def view_progress():
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])

    if total == 0:
        print("No tasks available.")
    else:
        print(f"Progress: {completed}/{total} tasks completed")

# Main function
def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            mark_complete()

        elif choice == "3":
            view_pending()

        elif choice == "4":
            view_progress()

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()