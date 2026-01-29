#!/usr/bin/env python3

import json
import os



DATA_FILE = "contact_data.json"

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


# VIEW ALL CONTACTS
def view_all_contacts(contacts):

    if not contacts:
        print("No contact yet.")
        return

    print("\nAll Contact:")
    for name, number in contacts.items():
        print(f"{name} - {number}")
    print() #empty line

# ADD NEW CONTACT
def add_contact(contacts):
    
    while True:
        name = input("Add a name (or press Enter to stop): ").strip()
        if not name:
            break
        number = input(f"Add number for {name}: ").strip()
        if not number:
            print("Number cannot be empty ❌")
            continue
        contacts[name] = number
        print(f"Contact '{name}' added ✅")
    save_file(contacts)




# DELETE A TASK
def delete_contact(contacts):
    view_all_contacts(contacts)
    contact_name = input("Enter contact name to delete: ").strip()
    if contact_name in contacts:
        contacts.pop(contact_name)
        save_file(contacts)
        print(f"Contact '{contact_name}' deleted ✅")
    else:
        print("Contact not found ❌")



# SEARCH CONTACT
def search_contact(contacts):
    
    query = input("Enter name to search: ").strip().lower()
    results = {name: number for name, number in contacts.items() if query in name.lower()}
    if results:
        print("\nSearch Results:")
        for name, number in results.items():
            print(f"{name} - {number}")
    else:
        print("No contacts found ❌")
    print()

# MAIN LOOP
def main():

    contacts = load_file()
    
    print("Hello Hamza! What can I do for you?")
    print("# (1 or add) => Add a Contact")
    print("# (2 or delete) => Delete a Contact")
    print("# (3 or view) => View all Contacts")
    print("# (4 or search) => Search Contact")
    print("# (5 or exit) => Exit\n")


    while True:
        choice = input("$ ").strip().lower()
        if choice in ("1", "add"):
            add_contact(contacts)
        elif choice in ("2", "delete"):
            delete_contact(contacts)
        elif choice in ("3", "view"):
            view_all_contacts(contacts)
        elif choice in ("4", "search"):
            search_contact(contacts)
        elif choice in ("5", "exit"):
            save_file(contacts)
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice ❌")

if __name__ == "__main__":
    main()