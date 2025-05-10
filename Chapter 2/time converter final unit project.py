time = int(input("Enter the duration in seconds: \n"))

minutes = time // 60

seconds = time & 60

hours = minutes // 60

print(f"The duration is: {hours} hours , {minutes} minutes , and {seconds} seconds.")