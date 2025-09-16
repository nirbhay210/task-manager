import json
import os

#----------------STATE--------------

TASKS_FILE = "tasks.json"
tasks = []
next_id = 1


#--------------HELPERS-------------

def _load_tasks():
    print("load task")

def _save_tasks():
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def _find_task_index_by_id(task_id: int) -> int:
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            return i
    return -1



#--------------CRUD----------------


def add_task() -> None:
    global next_id
    title = input("Enter task title: ").strip()
    if not title:
        print("title can not be Empty")
        return
    description = input("Enter task description: ").strip()
    status = input(("Enter status (press Enter for 'pending'): ")).strip() or "pending"

    record = {
        "id": next_id,
        "title": title,
        "description": description,
        "status": status,
    }
    tasks.append(record)
    _save_tasks()
    print(f"task #{next_id} added: {title} [{status}]")
    next_id += 1



def view_tasks() -> None:
    if not tasks:
        print("\nNo tasks found.\n")
        return
    print("\nCureent Tasks")
    print(f"{'ID':<5}{'Title':<20}{'Status':<12}{'Description'}")
    print("-" * 60)
    for task in tasks:
        print(f"{task['id']:<5}{task['title']:<20}{task['status']:<12}{task['description']}")
    print()


def update_task() -> None:
    try:
        task_id = int(input("Enter task ID to update: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    idx = _find_task_index_by_id(task_id)
    if idx == -1:
        print(f"No task found with ID {task_id}")
        return
    task = tasks[idx]
    print(f"\nUpdating Task {task_id}. Press Enter to keep old value.\n")

    new_title = input(f"Title [{task['title']}]: ").strip()
    if new_title:
        task["title"] = new_title
    
    new_desc = input(f"Description [{task['description']}]: ").strip()
    if new_desc:
        task["description"] = new_desc
    
    new_status = input(f"Status [{task['status']}]: ").strip()
    if new_status:
        task["status"] = new_status

    tasks[idx] = task
    _save_tasks()
    print(f"Task {task_id} updated.\n")

def delete_task():
    print("[TODO]")


#--------------Menu----------------

def print_menu():
    print("-------Task Manager------- ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("q. Quit")
    

#--------------Router----------------

def handle_choice(choice: str):
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice =="3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "q":
        _save_tasks()
        print("Goodbye! ")
        exit()
    else:
        print("Invalid choice. ")
    


#---------------- MAIN -----------------


def main():
    _load_tasks()
    while True:
        print_menu()
        choice = input("choose an option: ").strip()
        handle_choice(choice)

if __name__ == "__main__":
    main()