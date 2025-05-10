print ('***** Welcome to iShop calculator *****')

list_items = []

prices_list = []

number_of_items = int(input('How many items do you have in the basket?: '))

if number_of_items > 0:

    print('Lets go counting them')

    for item in range(1,number_of_items + 1):

        items = input(f'What is the name of the item number {item}: ').lower()

        list_items.append(items)

        price = float(input(f'What is the price of {items}: $'))

        prices_list.append(price)

# show the items and full price

    items_list_question = input('Do you want to see all the items you have?: (yes or no) ').lower()

    if items_list_question == 'yes':

        print(list_items)

        price_question = input('Do you want to see the total price of all items?: (yes or no) ').lower()

        if price_question == 'yes':

            print(sum(prices_list))

        else:

            print('Okay, thanks for using the app')

    else:

        print('Okay, thanks for using the app')

else:

    print('Invalid choice')