print('*** WELCOME TO MULTIPLICATION TABLE ***')

number = int(input('Enter a number: '))

for i in range(1,11):

    result = number * i

    print(f'{number} x {i} = {result}')
    