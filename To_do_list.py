# To-Do List Application

todo_list = []
def show_menu():
    print("\nTo-Do List Menu:\n1. View Tasks \n2. Add Task"+
    "\n3. Mark Task as Done \n4. Delete Task \n5. Exit")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, 1):
            status = "✅" if task['done'] else "❌"
            print(f"{i}. [{status}] {task['task']}")

def add_task():
    task = input("Enter the task: ")
    todo_list.append({'task': task, 'done': False})
    print("Task added successfully.")

def mark_done():
    view_tasks()
    try:
        task_number = int(input("Enter task number to mark as done: "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1]['done'] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(todo_list):
            removed = todo_list.pop(task_number - 1)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please select from 1 to 5.")
