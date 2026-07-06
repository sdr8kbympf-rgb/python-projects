# This is a dictionary to store all contacts - name is the key, number is the value

Contacts = {}
print("Welcome to your Contact Book!")

#The function below adds a new contact to the dictionary
def add_contact(name, number):
    Contacts[name] = number # stores the number using the name as the key
    print(f"{name} has been added. ")

#The function below shows every contact in the dictionary
def view_contacts():
    if len(Contacts) == 0: #len() counts how many contacts exist
        print("There are no contacts. ")
    else:
        for name, number in Contacts.items(): #.items() gives us both key and value
            print(f"{name}: {number}")

#This function searches for one specific contact by name
def search_contact(name):
    if name in Contacts: # checks for the name in the dictionary
        print(f"{name}: {Contacts[name]}")
    else:
        print(f"{name} not found. ")

# This function deletes a function from your dictionary
def delete_contact(name):
    if name in Contacts:
        del Contacts[name]
        print(f"{name} has been removed. ")
    else:
        print(f"{name} not found. ")

#  This function will keep the application running until i press 5 to stop it

while True:
    # \n creates a blank line to make the menu easier to read
    print("\n What would you like to do? ")
    print("1. Add Contact")
    print("2. View all Contacts" )
    print("3. Search Contact" )
    print("4. Delete Contact" )
    print("5. Exit" )

    choice = input("Enter your choice (1-5): ") # stores whatever the user types

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ") # phone numbers stays as strings - no math required
        add_contact(name, number)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        name = input("Enter name: ")
        search_contact(name)
    elif choice == "4":
        name = input("Enter name ")
        delete_contact(name)
    elif choice == "5":
        print("Sayonara! ")
        break # Break will exit the while true loop
    else:
        print("Invalid choice. ")

        
