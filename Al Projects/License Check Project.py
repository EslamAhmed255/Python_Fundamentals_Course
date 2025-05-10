print("Welcome to license check app")

age = int(input("Please enter your age \n"))

license = input("Do you have a license? (Yes) or (No) \n").lower()

if age >= 18 and license == "yes":
    print("Okay nice, you can drive")

elif age < 18 or license == "no":
    print("Sorry, you can't drive")

else:
    print("Please enter valid information")