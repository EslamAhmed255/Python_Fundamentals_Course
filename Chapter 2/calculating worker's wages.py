# Write the important variables

length = float(input("Please type length: \n"))

width = float(input("Please type width: \n"))

meter = float(input("How much for 1 meter: \n"))

# Convert variables & and get area space

length_word = (length)

width_word = (width)

total_area = (length_word * width_word)

str_total_area = str(total_area)

print("Your total area is: " + str_total_area)

# Convert variables & get the total price of the area 

price = (total_area * meter)

str_price = str(price)

print("Give the guy: $" + str_price)