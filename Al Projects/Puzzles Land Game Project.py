print("""
      
██████╗░░█████╗░███╗░░██╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔════╝██╔══██╗
██║░░██║███████║██╔██╗██║██║░░██╗░█████╗░░██████╔╝
██║░░██║██╔══██║██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗
██████╔╝██║░░██║██║░╚███║╚██████╔╝███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝
      
Welcome to my island!
""")

doors = input("""There are two doors in front of you. 🟥 a red door & 🟦 blue door 
which one you open? \n""").lower()

if doors == "blue":

    print(""""oops! you chose the crocodile door 🐊🐊🐊,
    game over!""")

elif doors == "red":

    print("Great! now you entered a room. and you found three boxes: ◻️  white, ⬛ black, 🟩 green" )

    box = input("Which one do you choose? \n").lower()

    if box == "red":
        print("oops! you opened a box filled of snakes 🐍🐍🐍")

    elif box == ("black"):
        print("oops! you opened a box filled of spiders 🕸️🕸️🕸️")

    elif box == ("green"):
        print("Good job! you found the treasure 🌟")

    else:
        print("Invalid choice! ❌")

else:
    print("Invalid choice! ❌")