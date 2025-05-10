# Important lists 

your_library = []

your_wishlist = []

# Your library

owned1 = input("Enter the name of a book you own: ").lower()

your_library.append(owned1)

owned1 = input("Enter the name of another book you own (or pres 'Enter' to skip): ").lower()

if owned1:
    
    your_library.append(owned1)

print(f"Now your library contains {your_library}")

# Your wishlist

wish1 = input("Enter the name of a book you wish to have in the future: ").lower()

your_wishlist.append(wish1)

wish1 = input("Enter the name of another book you wish to have in the future ( Or press to skip ): ").lower()

if wish1:
    
    your_wishlist.append(wish1)

print(f"Now your wishlist contains {your_wishlist}")

# Wishlist already owned

updated_wishlist1 = input("Enter another name of the book from your wishlist you've got ( Or press enter to skip ): ").lower()

if updated_wishlist1 in your_wishlist:

    your_library.append(updated_wishlist1)

    your_wishlist.remove(updated_wishlist1)

print(f"Updated library contains {your_library}")

print(f"Updated wishlist contains {your_wishlist}")
    
# Book donations

donate1 = input("Enter the name of a book from your library you wish to donate in the future (Or press enter to skip): ").lower()

if donate1 in your_library:

    your_library.remove(donate1)

print(f"Your final library after donation contains: {your_library}")

print("    THANK YOU FOR USING THE APP    ")