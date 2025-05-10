# Personal project on Nested If

print("Welcome to Beni suef map app")

ask = input("Do you want to take the Metro, or Taxi, or Uber? \n").lower()

if ask == "metro":

    print("Sorry, there's no metro in Beni Suef")
    
elif ask == "uber":

    print("What!? i think you're not from Beni Suef, there's no uber here")

elif ask == "taxi":

    print("okay good, that's the right choice")

    pay = input("How you want to pay for the taxi? Visa, or Cash, or Wallet? \n").lower()

    if pay == "visa":
        print("i am sure that you is not from Beni Suef, there's no visa here with taxi")

    elif pay == "wallet":
        print("Sometimes it will be an option and sometimes no")

    elif pay == "cash":
        print("Nice, now you understand how it's going on here")

    else:
        print("Invalid choice")

else:
    print("Invalid choice")