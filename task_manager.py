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



#--------------CRUD----------------


def add_task():
    print("[TODO]")
def view_tasks():
    print("[TODO]")
def update_task():
    print("[TODO]")
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