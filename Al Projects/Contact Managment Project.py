# Welcome message
print('Contact Management')

# Important Variables 
contacts = {}
contacts_count = 0

# While Loop
while True and contacts_count < 1000:
    choice = input('''
1- Add a contact 
2- View contact
3- Edit a contact 
4- Exit
Enter your choice: ''')

# Add a contact
    if choice == '1':
        name = input('Enter your name \n').lower()
        
        id = input('Enter your id \n')
        while not id.isdigit():
            print('Sorry, it not an ID')
            id = input('Please enter valid id \n')

        phone = input('Enter your phone number \n')
        while not phone.isdigit():
            print('Sorry, it is not number')
            phone = input('Please enter valid phone number \n')

        contacts[name] = { 
        'name': name,
        'phone': phone,
        'id': id
        }
        print(f"{name} was added successfully!")

# View a contact 
    elif choice == '2':
        if not contacts:
            print('Not found')
        else:
            print(contacts)

# Edit a contact 
    elif choice == '3':
        name_to_edit = input('Enter your name \n').lower()

        if name_to_edit in contacts:
            new_id = input('Enter your new id \n')
            while not new_id.isdigit():
                print('Sorry, it not an ID')
                new_id = input('Please enter valid new id \n')

            new_phone = input('Enter your phone number \n')
            while not new_phone.isdigit():
                print('Sorry, it is not number')
                new_phone = input('Please enter valid phone number \n')
            else:
                print('Name not found')

            contacts[name] = {
            'name': name,
            'phone': new_phone,
            'id': new_id,
            }
            print(f"{name} was added successfully!")

# Exit the project
    elif choice == '4':
        input('Click ENTER to exit: ')
        break

# Situation ( NO CHOICE )
    else:
        print('Invalid choice')
        break