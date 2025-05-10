total_seconds = input("Type the time in Seconds: \n")

# Convert type

str_seconds = int(total_seconds)

minutes = str_seconds // 60

hours = minutes // 60

# Convert for print function

print("Your time in Minutes = " + str(minutes) + " Minutes " + "& total Hours = " + str(hours))