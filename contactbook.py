class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        self.contacts.append(contact)
        print("Contact added successfully!\n")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.\n")
        else:
            print(f"{'Index':<6}{'Name':<20}{'Phone':<15}{'Email':<30}{'Address'}")
            print("-" * 75)
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i:<6}{contact['Name']:<20}{contact['Phone']:<15}{contact['Email']:<30}{contact['Address']}")
            print()

    def update_contact(self):
        if not self.contacts:
            print("No contacts found.\n")
            return

        try:
            index = int(input("Enter the index of the contact to update: ")) - 1
            if index < 0 or index >= len(self.contacts):
                raise IndexError
            selected_contact = self.contacts[index]

            print("Leave a field blank to keep the current value.")
            name = input(f"Enter new Name (current: {selected_contact['Name']}): ") or selected_contact['Name']
            phone = input(f"Enter new Phone (current: {selected_contact['Phone']}): ") or selected_contact['Phone']
            email = input(f"Enter new Email (current: {selected_contact['Email']}): ") or selected_contact['Email']
            address = input(f"Enter new Address (current: {selected_contact['Address']}): ") or selected_contact['Address']

            self.contacts[index] = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            print("Contact updated successfully!\n")
        except (ValueError, IndexError):
            print("Invalid index. Please try again.\n")

    def delete_contact(self):
        if not self.contacts:
            print("No contacts found.\n")
            return

        try:
            index = int(input("Enter the index of the contact to delete: ")) - 1
            if index < 0 or index >= len(self.contacts):
                raise IndexError
            deleted_contact = self.contacts.pop(index)
            print(f"Contact {deleted_contact['Name']} deleted successfully!\n")
        except (ValueError, IndexError):
            print("Invalid index. Please try again.\n")

    def search_contact(self):
        search_term = input("Enter the name or phone number to search: ").lower()

        results = [
            contact for contact in self.contacts
            if search_term in contact['Name'].lower() or search_term == contact['Phone']
        ]

        if results:
            print(f"{'Name':<20}{'Phone':<15}{'Email':<30}{'Address'}")
            print("-" * 75)
            for contact in results:
                print(f"{contact['Name']:<20}{contact['Phone']:<15}{contact['Email']:<30}{contact['Address']}")
            print()
        else:
            print("No matching contacts found.\n")

    def run(self):
        while True:
            print("1. Add Contact")
            print("2. Display Contacts")
            print("3. Update Contact")
            print("4. Delete Contact")
            print("5. Search Contact")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.display_contacts()
            elif choice == "3":
                self.update_contact()
            elif choice == "4":
                self.delete_contact()
            elif choice == "5":
                self.search_contact()
            elif choice == "6":
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    app = ContactBook()
    app.run()
