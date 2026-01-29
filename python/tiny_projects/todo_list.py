#!/usr/bin/env python3

import json


todos = {}


def save_file(data):
    with open("data.json", "w", encoding="utf-8") as write_file:
        json.dump(data, write_file, indent=4)
        
def load_file():
    with open("data.json", "r", encoding="utf-8") as read_file:
        loaded_json = json.load(read_file)
    
    return loaded_json





def add_task():
    
    global todos
    todos = load_file() or {}

    while True:
        task = input("Add a task (or type 'exit'): ")
        if task == "exit":
            save_file(todos)
            break
        
        task_id = len(todos) + 1
        todos[task_id] = task
        print("Task added ✅")

def view_all_tasks():
    
    global todos
    todos = load_file() or {}
    
    if not todos:
        print("No tasks yet.")
        return

    print("All Tasks:")
    for key, value in todos.items():
        print(f"{key} - {value}")



def delete_task():
    global todos
    todos = load_file() or {}
    view_all_tasks()
    task_id = input("Enter task number to delete: ")

    if task_id.isdigit():
        task_id = int(task_id)
        if task_id in todos:
            todos.pop(task_id)
            save_file(todos)
            print("Task deleted ✅")
        else:
            print("Task not found ❌")
    else:
        print("Invalid input ❌")




print("Hello Hamza! What can I do for you?")
print("1 - add a task | 2 - delete a task | 3 - view all tasks")

choice = input("$ ")

if choice == '1':
    add_task()
elif choice == '2':
    delete_task()
elif choice == '3':
    view_all_tasks()
else:
    print("Invalid choice")
