# Import modules
import time
import os


# Clear screen function
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# Welcome screen
print('''
      
Welcome to Currency conversion app

||====================================================================||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||
||\\$//        ~         '------========--------'                \\$//||
||<< /        /$\              // ____ \\                         \ >>||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
||<<|        \\ //           || <||  >\  ||                        |>>||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||''')

print('_____________________________________________________________________________')


# Available currencies function
def show_available_currencies():    
    print('''
USD = 1.0
EUR = 0.93
EGP = 50
RMB = 7.24
''')
show_available_currencies()


# Currency conversion function
def currency_conversion_process():
    currency_choice = input('Choose a currency to convert from: ').upper()

    if currency_choice in ['USD', 'EUR', 'EGP', 'RMB']:
        while True:
            user_amount = input('Enter the amount: ').strip()
            
            if not user_amount:
                print('Invalid choice! Amount cannot be empty.')
                continue
                
            deposit_confirmation = input(f"You enter {user_amount} {currency_choice}, Do you want to confirm ( Y / N ): ").upper()
            if deposit_confirmation == 'N':
                continue

            if deposit_confirmation == 'Y':
                currency_convert = input('Choose a currency to convert to: ').upper()
                
                if currency_convert not in ['USD', 'EUR', 'EGP', 'RMB']:
                    print('Invalid target currency')
                    continue
                clear_screen()
                
                conversation_rate = {
                    'USD': 1.0,
                    'EUR': 0.93,
                    'EGP': 50,
                    'RMB': 7.24
                }
                
                print('Analyzing your request..')
                time.sleep(1.5)

                print(f'Checking for {currency_choice} best rates available.. Please wait')
                time.sleep(1.5)

                print(f'Get a discount price for {currency_convert}.. Please wait')
                time.sleep(1.5)

                final_result = float(user_amount) * (conversation_rate[currency_convert] / conversation_rate[currency_choice])
                print(f"{user_amount} {currency_choice} = {final_result} {currency_convert}")
                break

        print('Thanks for using our app')

    else:
        print('Invalid choice')


# Start the project
currency_conversion_process()