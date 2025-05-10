import random

# Print functions

print("Welcome to Coin Guessing Game")

print("Choose a method to toss the coin:")

print("""
1. Using random.random()
2. Using random.randint()
""")

# User choice

choice = input("Enter your choice ( 1 or 2 ) \n")

# If statements on user choice

if choice == "1":
    random_number = random.random()

    if random_number >= 0.5:
        computer_result = "head"

    else:
        computer_result = "tail"

elif choice == "2":
    if random.randint(0,1) == 0:
        computer_result = "head"

    else:
        computer_result = "tail"

else:
    print("Invalid choice")

# head or tail choice work

sign = input("Enter your guess ( Head or Tail ) \n").lower()

if sign == computer_result:
    print("Nice, you win! ")

else:
    print("Sorry, you lose")

print(f"The computer choice was {computer_result}")