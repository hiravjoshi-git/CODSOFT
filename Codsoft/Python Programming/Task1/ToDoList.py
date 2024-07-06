import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. [{status}] {task['title']} - {task['description']}")

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append({"title": title, "description": description, "completed": False})
    save_tasks(tasks)
    print("Task added successfully.")

def update_task(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["title"] = input("Enter new task title: ")
        tasks[task_index]["description"] = input("Enter new task description: ")
        save_tasks(tasks)
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def complete_task(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update an existing task")
        print("4. Mark a task as completed")
        print("5. Delete a task")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
