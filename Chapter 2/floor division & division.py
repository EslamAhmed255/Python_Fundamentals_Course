# Division: /
# Floor division: //

total_numbers = input("Please type the number of minutes: \n")

int_minutes = int(total_numbers)

hours = int_minutes // 60

minutes = int_minutes % 60

print("this course is: " + str(hours) + " Hours " + str(minutes) + " Minutes " )