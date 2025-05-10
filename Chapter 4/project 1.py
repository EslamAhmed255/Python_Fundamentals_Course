import random

# Put your basic variables

user_input = int(input("Please enter 4-digit PIN code: \n"))
pc_input = random.randint(1000, 9999)

# Put the if statements functions

if len(str(user_input)) != 4:
    print("Please enter 4-digits number")

elif user_input == pc_input:
    print(f"Nice! the number you puted is: {user_input} and it's the same to {pc_input}")

elif user_input != pc_input:
    print(f"Sorry, the number you puted: {user_input} is not the same to {pc_input}")

else:
    print("Invalid choice")