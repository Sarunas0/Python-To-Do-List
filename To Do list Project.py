# Function to add a task to the list
def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

# Function to edit a task in the list
def edit_task():
    display_tasks()
    task_number = int(input("Enter the task number to edit: ")) - 1
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if 0 <= task_number < len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_number] = new_task + "\n"
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task edited successfully.")
    else:
        print("Invalid task number.")

# Function to delete a task from the list
def delete_task():
    display_tasks()
    task_number = int(input("Enter the task number to delete: ")) - 1
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if 0 <= task_number < len(tasks):
        del tasks[task_number]
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

# Function to display all tasks
def display_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("No tasks found.")

# Main function
def main():
    while True:
        print("\n===== Todo List Application =====")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            edit_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

