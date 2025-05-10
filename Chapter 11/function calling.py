def take_order(name):
    print(f'Welcome to the restaurant! {name}')
    # input code here 
    print('Order taken successfully')
    thank_customer (name)


def thank_customer (name):
    print(f"Thank you {name} for choosing our restaurant !")

take_order(input('What is your name: '))