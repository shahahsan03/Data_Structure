# Add a new contact.
# List all contacts.
# Search for a contact by name.
# Delete a contact by name.

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class ContactBookView:
    def __init__(self):
        self.items = []

    def add_contact(self, name, number):
        contact = Contact(name,number)
        self.items.append(contact)
        
    def list_contacts(self):
        for contact in self.items:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def search_contact(self, name):
        found = False
        for contact in self.items:
            if name == contact.name:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")
                found= True
        if not found:
            print('No Records Found')

    def delete_contact(self, name):
        for item in self.items:
            if name == item.name:
                print(f'Deleted the contact of {item.name}')
                self.items.remove(item)
            else:
                print('No Records Found')
    
    
if __name__ == "__main__":
    contact = ContactBookView()
    contact.add_contact('Ahsan', '03253190838')
    contact.add_contact('Wasi', '03245956121')
    contact.list_contacts()
    print()
    contact.search_contact('Ahsan')
    print()
    contact.delete_contact('Ahsan')
    contact.list_contacts()