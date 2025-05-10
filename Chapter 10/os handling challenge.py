import random
import os

# While loop 
while True:
    guess = int(input('Guess a number between 1 and 10: '))
    random_number = random.randint(1,10)

    # If statement
    if guess == random_number:
        print("Congratulations, You did it !")
        break
    else:
        print('Wrong guess, try again..')
        input("You guessed wrong, press any key to continue...")
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    # os.system('cls' if os.name == 'nt' else 'clear') -> Shorthand statement