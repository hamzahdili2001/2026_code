#!/usr/bin/env python3

import json
import os



DATA_FILE = "data.json"

# LOAD TASKS FROM JSON FILE
def load_file():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    return {}


# SAVE TASKS TO JSON FILE
def save_file(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# VIEW ALL TASKS
def view_all_tasks(todos):

    if not todos:
        print("No tasks yet.")
        return

    print("\nAll Tasks:")
    for key, value in todos.items():
        print(f"{key} - {value}")
    print() #empty line

# ADD NEW TASK
def add_task(todos):
    while True:
        task = input("Add a task (or type 'exit'): ")
        if task.lower() == "exit":
            save_file(todos)
            break
        
        # Generate a new unique ID
        task_id = str(max([int(k) for k in todos.keys()], default=0) + 1)
        todos[task_id] = task
        print("Task added ✅")



# DELETE A TASK
def delete_task(todos):
    view_all_tasks(todos)
    task_id = input("Enter task number to delete: ")

    if task_id in todos:
        todos.pop(task_id)
        save_file(todos)
        print("Task deleted ✅")
    else:
        print("Task not found ❌")



# MAIN LOOP
def main():

    todos = load_file()
    
    print("Hello Hamza! What can I do for you?")
    print("# (1 or add) => Add a task\n# (2 or delete) => Delete a task\n# (3 or view) => View all tasks\n# (4 or exit) => Exit\n")


    while True:
        choice = input("$ ").strip()
        if choice == "1" or choice == "add":
            add_task(todos)
        elif choice == "2" or choice == "delete":
            delete_task(todos)
        elif choice == "3" or choice == "view":
            view_all_tasks(todos)
        elif choice == "4" or choice == "exit":
            save_file(todos)
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice ❌")

if __name__ == "__main__":
    main()

