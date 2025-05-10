import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# Books list (stores all books)
books = []

# Available list (stores only available books)
available = []


# Add book
def add_book():
    if user_choice == '1':
        clear_screen()
        isbn_enter = int(input('Enter ISBN: '))
        book_name = input('Enter book name: ').lower()
        book_author = input('Enter author name: ').lower()

        new_book = {
            'isbn': isbn_enter,
            'name': book_name,
            'author': book_author
        }

        books.append(new_book)
        available.append(new_book)

        print(f"Book '{book_name}' by '{book_author}' added to the catalog. Available: {new_book in available}")
        
        more_book = input('Do you want to add more books? (y or n): ').lower()
        if more_book == 'y':
            add_book()


# List books (now shows availability)
def list_books():
    if user_choice == '4':
        clear_screen()
        print("\n--- List of All Books ---")
        if not books:
            print("No books in the catalog yet!")
        else:
            for book in books:
                # Check if book is available
                status = "AVAILABLE" if book in available else "CHECKED OUT"
                print(f"ISBN: {book['isbn']} | Title: '{book['name']}' | Author: {book['author']} | Status: {status}")
        
        input("\nPress Enter to return to the menu...")


# Check out a book
def check_out():
    if user_choice == '2':
        clear_screen()
        isbn_check_out = int(input('Enter ISBN to check out: '))

        found_book = None
        for book in available:
            if book['isbn'] == isbn_check_out:
                found_book = book
                break
                
        if found_book:
            available.remove(found_book)
            print(f"\nBook '{found_book['name']}' by {found_book['author']} checked out successfully!")
        else:
            print("\nBook not found or already checked out!")
        
        choice = input('Do you want to check out another book: (y or n): ').lower()
        if choice == 'y':
            check_out()
        else:
            input("\nPress Enter to return to the menu...")


# Check in a book
def check_in():
    if user_choice == '3':
        clear_screen()
        isbn_check_in = int(input('Enter ISBN to check in: '))
        
        # Find the book in all books but not in available
        found_book = None
        for book in books:
            if book['isbn'] == isbn_check_in and book not in available:
                found_book = book
                break
                
        if found_book:
            available.append(found_book)
            print(f"\nBook '{found_book['name']}' by {found_book['author']} checked in successfully!")
        else:
            print("\nBook not found or already available!")

        choice = input('Do you want to check out another book: (y or n): ').lower()
        if choice == 'y':
            check_out()
        else:
            input("\nPress Enter to return to the menu...")


# Main menu loop
while True:
    clear_screen()
    print('''
    --- Library Menu ---
    1. Add book 
    2. Check out book
    3. Check in book
    4. List books
    5. Exit
    ''')
    user_choice = input('Enter your choice (1-5): ')

    if user_choice == '5':
        print("Goodbye!")
        break

    add_book()
    list_books()
    check_out()
    check_in()