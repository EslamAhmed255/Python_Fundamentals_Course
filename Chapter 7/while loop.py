correct_password = 'a1b2c3'

password_enter = input('Please enter your password: ')

while password_enter != correct_password:

    print('Invalid password')

    password_enter = input('Enter your password again: ')

print('Password accepted')