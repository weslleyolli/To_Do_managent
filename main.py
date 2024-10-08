def add_task(tasks, task_name):
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    print(f"Task {task_name} added.")
    return

def view_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        name_task = task["task"]
        print(f"{i}. [{status}]{name_task}")
    return

def update_name_task(tasks, index_task, new_task_name):
    index_task_adjusted = int(index_task) - 1
    if index_task_adjusted >= 0 and index_task_adjusted < len(tasks):
        tasks[index_task_adjusted]["task"] = new_task_name
        print(f"Task {index_task} updated to {new_task_name}")
    else:
        print(f"Task {index_task} not found.")
    return

def complete_task(tasks, index_task):
    index_task_adjusted = int(index_task) - 1
    tasks[index_task_adjusted]["completed"] = True
    print(f"Task {index_task} completed.")
    return

def delete_task_complete(tasks):
    for task in tasks:
        if task["completed"]:
            tasks.remove(task)
    print(f"The task completed was deleted.")
    return

tasks =  []
while True:
    print("\nMenu of to do management")
    print("1. Add task")
    print("2. View task")
    print("3. Update task")
    print("4. Complete task")
    print("5. Delete task complete")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name_task = input("Enter your task name: ")
        add_task(tasks, name_task)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        view_tasks(tasks)
        task_index = input("Enter index of task: ")
        new_task_name = input("Enter new task name: ")
        update_name_task(tasks, task_index, new_task_name)
    elif choice == "4":
        view_tasks(tasks)
        task_index = input("Enter index of task: ")
        complete_task(tasks, task_index)

    elif choice == "5":
        delete_task_complete(tasks)
        view_tasks(tasks)
    elif choice == "6":
        break

    print("Program finished")

