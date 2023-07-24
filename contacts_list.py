import json
import os

CONTACT_FILE = "contact.json"

def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r') as f:
            return json.load(f)
    else:
        return []

def save_contacts(contacts):
    with open(CONTACT_FILE, 'w') as f:
        json.dump(contacts, f)

def add_contact(name, email):
    contacts = load_contacts()
    new_contact = {"name": name, "email": email}
    contacts.append(new_contact)
    save_contacts(contacts)

def delete_contact(name):
    contacts = load_contacts()
    contacts = [contact for contact in contacts if contact["name"] != name]
    save_contacts(contacts)

def list_contacts():
    contacts = load_contacts()
    for contact in contacts:
        print(f"Name: {contact['name']}, Email: {contact['email']}")

def search_contact(name):
    contacts = load_contacts()
    for contact in contacts:
        if contact["name"] == name:
            print(f"Name: {contact['name']}, Email: {contact['email']}")
            return
    print("Contact not found.")

if __name__ == "__main___":
    while True:
        print("\nContact List Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. List Contacts")
        print("4. Search Contact")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            name = input("Enter contact name:")
            email = input("Enter contact email:")
            add_contact(name, email)
            print("Contact added!")
        elif choice == 2:
            name = input("Enter contact's name to delete: ")
            delete_contact(name)
            print("Contact deleted!")
        elif choice == 3:
            print("Contacts:")
            list_contacts()
        elif choice == 4:
            name = input("Enter contact name to search: ")
            search_contact(name)
        elif choice == 5:
            print("Exiting the program.")
            break
        else: 
            print("Invalid choice. Please try again.")