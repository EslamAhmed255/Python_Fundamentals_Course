print("Welcome to password guess application")

guess = int(input("Please write the write number ( The one it is correct guess ) \n"))

number = 7

if guess == number:
    print("You have guessed the right number, GOOD JOB!")
    
else:
    print(f"you guessed {guess} but the right number is {number}")