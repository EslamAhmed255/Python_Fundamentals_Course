# Challenge: Give the user more than one try until type the right guessed word 

import random

words = ['good','bad','ugly']

random_word = random.choice(words)

# Show the blanks of guessed answer

display = []

for letter in random_word:

    display.append('_')

print(display)

# Request guess 

while '_' in display:

    guessed = input('Please guess a letter: ').lower()

# If right replace the blank 

    for position in range(len(random_word)):

        if random_word[position] == guessed:

            display[position] = guessed

    print(display)

print('''
        
*******
YOU WIN
*******

''')