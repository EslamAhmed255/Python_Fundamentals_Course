list1 = [ ["Apples", "Bananas"] , ["Milk", "Water"] ]

print(list1)

press = input("Press enter to change the content \n")

if press in press:

    print("Here's the updated list")

    list1.append(['Coffe', 'Milk', 'Tea'])

    list1.remove(["Milk", "Water"])

    list1.append([1, 2, 3])

    list1[0].insert(0,"Oranges")

    list1[0].append("Kiwis")
    
    print(list1)