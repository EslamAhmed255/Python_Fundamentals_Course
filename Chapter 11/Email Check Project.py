# Import module
import time

# Get user email input
def get_email():
    email = input('Please enter your email: ')
    return email

# Validate email format
def check_email(email):
    return '@' in email and '.' in email

# Main validation loop
while True:
    email = get_email()
    
    print('Checking...')
    time.sleep(1.5)
    
    print('Validating email address...')
    time.sleep(1.5)     

    if check_email(email):
        print('Email is valid')
        break
    
    else:
        print('Email is not valid')
        again = input('Do you want to try again? (y / n): ')
        
        if again != 'y':
            break