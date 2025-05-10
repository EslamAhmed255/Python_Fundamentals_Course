import random

words = ['office','panda','cabin','ginger']

random_word = random.choice(words)

guessed = input('Write the letter that you guessed \n').lower()

for letter in random_word:

    if letter == guessed:

        print('Right')

    else:

        print('Wrong')