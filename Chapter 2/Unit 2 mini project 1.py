# Write the important variables 

length = float ( input ( "Please type length: "))

width = float ( input ( "Please type width: " ))

meter = float ( input ( "How much for 1 meter: " ))

# Get the total space of the area

total_area = ( length * width )

str_total_area = str ( total_area )

print( "Your total area is: " + str_total_area )

# Get the total price of the area 

float_total_price = int ( total_area )

float_total_price = ( total_area * meter )

str_total_price = str ( float_total_price )

print( "Give the guy: $" + str_total_price )