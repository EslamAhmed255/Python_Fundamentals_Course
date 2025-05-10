# append ( To add anything to the list )
# extend ( To merge two lists in one list )
# remove ( To delete any object in the list )


# simple project 

favorite_colors = []

# first colors append 

first = input("Add the first color you like: ").lower()

favorite_colors.append(first)

# Add more colors

add_colors_question = input("Do you want to add more colors?: ").lower()

if add_colors_question == "yes":

    add = input("Add the colors you like to append: ").lower()
    favorite_colors.append(add)

elif add_colors_question == "no":
    print("Okay, as you like ")

else:
    print("invalid input")

# print the final look of favorite colors list

print(f"your favorite colors are {favorite_colors}")