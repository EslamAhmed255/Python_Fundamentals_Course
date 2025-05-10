names = input('Enter the first name and the last name of your friends by comma: ').split(', ')

abbreviated_names = []

for name in names:

    name_parts = name.split()
    
    print(name_parts)

    first_name = name_parts[0]

    last_name = name_parts[1]

    # Shortcut names 

    first_initial = first_name[0]

    last_initial = last_name[1]

    abbreviation = first_initial + '.' + last_initial + '.'

    abbreviated_names.append(abbreviation)

print('Abbreviated_Names')

for x in abbreviated_names:

    print(x)