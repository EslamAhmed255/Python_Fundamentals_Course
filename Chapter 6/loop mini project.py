travel_list = input('Enter the eames of the countries separated by a comma: ').split(', ')

for country in travel_list:

    print(f'\n{country}\n')

    visited = input(f'Have you ever visited {country} before? (yes or no) \n').lower()

    if visited == 'yes':
        
        print('I hope you enjoyed there')

    else:

        print('I hope you to visit this country')
    
    print('------------')

input('press enter to exit....')