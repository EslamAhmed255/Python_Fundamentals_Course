import random 

print("Welcome to 'whose wallet' ")

print("You will give me a list of names, and i will pick one to pay for the dinner")

list = input("If you are ready, enter the names separated by a comma \n").lower()

listed_names = list.split(", ")

pick = random.choice(listed_names)

print(f"Please ask {pick} to pay for the dinner today")