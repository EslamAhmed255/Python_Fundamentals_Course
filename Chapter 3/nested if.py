nationality = input("Are you Egyptain? (yes) or (no) \n").lower()

if nationality == "yes":
    print("Okay nice that's the first step! ")

    age = int(input("Please enter your age \n"))

    if age >= 16:
        print("Okay nice, now you can have an ID")

    else:
        print("Sorry, complete 16 and come again")
else:
    print("Sorry, this service is only available for Egyptains")