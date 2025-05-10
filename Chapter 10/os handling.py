import os
print(os.name)
print('Hello')
print('Hello')
print('Hello')

input('\nPress any key to clear the screen...')

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

input('\nPress any key to exit...')