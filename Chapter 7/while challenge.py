import random

right_number = random.randint(1,10)

Guess = int(input("guess a number between 1 and 10: "))

while Guess > right_number:

    print("The number is too high")

    Guess = int(input("Enter a number again: "))
    
    while Guess < right_number:

        print("The number is too low")

        Guess = int(input("Enter a number again: "))

print("Nice, you guessed the right number ")