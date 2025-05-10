print("Welcome to place the rabbit")

list = [
    ['☁','☁','☁'],
    ['☁','☁','☁'],
    ['☁','☁','☁']
]

# input function

print("Where we should put the rabbit? 🐇")

question = int(input("Please choose a row and column: "))

# First row

if question == 11:

    list[0][0] = "🐇"

    print("Success..")

    print(*list,sep='\n')

elif question == 12:

    list[0][1] = "🐇"

    print("Success..")

    print(*list,sep='\n')

elif question == 13:

    list[0][2] = "🐇"
    
    print("Success..")

    print(*list,sep='\n')

# Second row

if question == 21:

    list[1][0] = "🐇"

    print("Success..")

    print(*list,sep='\n')

elif question == 22:

    list[1][1] = "🐇"

    print("Success..")

    print(*list,sep='\n')

elif question == 23:

    list[1][2] = "🐇"

    print("Success..")

    print(*list,sep='\n')

# Third row

if question == 31:

    list[2][0] = "🐇"

    print("Success..")

    print(*list,sep='\n')

elif question == 32:

    list[2][1] = "🐇"

    print("Success..")

    print(*list,sep='\n')

elif question == 33:
    list[2][2] = "🐇"

    print("Success..")

    print(*list,sep= '\n')