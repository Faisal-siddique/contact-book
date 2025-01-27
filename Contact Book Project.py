
contact = {}

'''Contact Book in python:- 

1. Add new contact
2. Search contact
3. Display contacts
4. Edit contact
5. Delete contact
6. Exit
   Enter your choice'''

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print(f"{key}\t\t{contact[key]}")

def my_function():
    display_contact()

while True:
    choice = int(input("1. Add new contact \n 2.Search contact \n 3.Display contact \n 4.Edit contact \n 5.Delete Contact \n 6.Exit \n   Enter your choice"))
    if choice == 1:
        name = input("enter the contact name ")
        phone = input("enter the mobile number")
        contact[name] = phone
        print("Contact Added Sucess")

    elif choice == 2:
        search_name = input("enter the contact name ")
        if search_name in contact:
            print(search_name, "'s contact number is ", contact[search_name])
        else:
            print("Name is not found in contact book")

    elif choice == 3:
       print(choice)
       if not contact:
           print("empty contact book")
       else:
           display_contact () 

    elif choice == 4:
       edit_contact = input("Enter the contact to be edited ")
       if edit_contact in contact:
           phone = input("enter mobile number")
           contact[edit_contact]=phone     
           print("contact updated")
           display_contact()
       else:
           print ("Name is not found in contact book")
    elif choice == 5:
        del_contact = input("Enter the contact to be deleted")
        if del_contact in contact:
            confirm =input("Do you want to delete this contact y/n? ")
            if confirm =='y' or confirm =='Y':
                contact.pop(del_contact)
            my_function()
        else:
            break 
    
        
