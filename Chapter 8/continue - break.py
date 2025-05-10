# Continue 
for i in range(5):
    if i == 2:
        continue
    print(i)

print('----------------------------')

for x in range(11):
    if x % 2 != 0:
        continue
    print(x)

print('----------------------------')

# Break
for y in range(6):
    if y == 6:
        print('I have to exit now')
        break
    print(y)