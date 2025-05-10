# Upper() and Lower() function

# area = input("Choose an area: (Cairo) or (Tanta) or (Alexandria) \n").lower()

# if area == "cairo":
#     print("You chose Cairo")

# elif area == "tanta":
#     print("Tanta is nice")

# elif area == "alexandria":
#     print("Feels like summer!")

# else:
#     print(f"sorry, {area} is not on our list")


# if shortcut

area = input("Choose and area: (Cairo) or (Giza) or (Alexandria) \n").lower()

if area == "cairo" or area == "giza" or area == "alexandria":
    print(f"Good, {area} is on our list")

else:
    print(f"Sorry, {area} is not on our list")