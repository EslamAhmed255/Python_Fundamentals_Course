import random
import string

print('Welcome to password generator app')

length = int(input('Enter to total number of characters in the password: '))

num_letters = int(input('Enter the number of letters in the password: '))

num_numbers = int(input('Enter the numbers of number in the password: '))

num_symbols = int(input('Enter the symbols in the password: '))

if length != (num_letters + num_numbers + num_symbols):

    print('Invalid input')

else:

    letters = string.ascii_letters

    numbers = string.digits

    symbols = string.punctuation

    password_chars = ( random.choices ( letters, k = num_letters ) ) + ( random.choices ( numbers, k = num_numbers ) ) + ( random.choices ( symbols, k = num_symbols ) )

    random.shuffle(password_chars)

    password = (password_chars)

    print(''.join(password))