# Clear screen function
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Calculate function
def calculate(item_number, item_price):
    return item_number * item_price

# Main function
while True:
    clear_screen()
    print('Welcome to the shopping cart calculator!')

    # User inputs
    user_budget = float(input('Enter your spending budget: '))
    user_item = input('Enter the item you want to buy: ').lower()
    item_number = int(input(f'how many {user_item}s do you want to buy: '))
    item_price = float(input(f'Enter the price for {user_item}: '))
    total_cost = calculate(item_number, item_price)                                                

    # Display results
    if total_cost > user_budget:
        print('Warning: You are over budget')
    else:
        print('Successful purchase!, enjoy your item')

    # Ask user if they want to continue
    if input ('Do you want to continue?: ( y or n ): ').lower() != 'y':
        break