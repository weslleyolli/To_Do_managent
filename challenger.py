def save_contact_in_schedule(contacts, name_contact):
    contact = {"contact": name_contact, "favorite": False}
    contacts.append(contact)
    print(f"Contact {name_contact} saved in schedule!")
    return

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for i, contact in enumerate(contacts, start=1):
        favorite = "✓" if contact["favorite"] else " "
        name_contact = contact["contact"]
        print(f"{i}. [{favorite}] {name_contact}")
    return

def edit_contact(contacts, index_contact, new_contact_name):
    try:
        index_contact_adjusted = int(index_contact) - 1
        if 0 <= index_contact_adjusted < len(contacts):
            contacts[index_contact_adjusted]["contact"] = new_contact_name
            print(f"Contact {new_contact_name} edited!")
        else:
            print(f"Contact {index_contact} not found!")
    except ValueError:
        print("Invalid index. Please enter a valid number.")
    return

def delete_contact(contacts, index_contact):
    try:
        index_contact_adjusted = int(index_contact) - 1
        if 0 <= index_contact_adjusted < len(contacts):
            removed_contact = contacts.pop(index_contact_adjusted)
            print(f"Contact {removed_contact['contact']} deleted!")
        else:
            print(f"Contact {index_contact} not found!")
    except ValueError:
        print("Invalid index. Please enter a valid number.")
    return

def favorite_contact(contacts, index_contact):
    try:
        index_contact_adjusted = int(index_contact) - 1
        if 0 <= index_contact_adjusted < len(contacts):
            contacts[index_contact_adjusted]["favorite"] = True
            print(f"Contact {contacts[index_contact_adjusted]['contact']} added to favorites.")
        else:
            print(f"Contact {index_contact} not found!")
    except ValueError:
        print("Invalid index. Please enter a valid number.")
    return

contacts = []
while True:
    print("\nMenu of schedule")
    print("1. Save contact")
    print("2. Edit contact")
    print("3. Delete contact")
    print("4. Save as favorite")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name_contact = input("Enter name of your contact: ")
        save_contact_in_schedule(contacts, name_contact)
    elif choice == "2":
        view_contacts(contacts)
        contact_index = input("Enter index of contact to edit: ")
        new_contact_name = input("Enter new contact name: ")
        edit_contact(contacts, contact_index, new_contact_name)
    elif choice == "3":
        view_contacts(contacts)
        contact_index = input("Enter index of contact to delete: ")
        delete_contact(contacts, contact_index)
    elif choice == "4":
        view_contacts(contacts)
        contact_index = input("Enter index of contact to favorite: ")
        favorite_contact(contacts, contact_index)
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please select a valid option.")
