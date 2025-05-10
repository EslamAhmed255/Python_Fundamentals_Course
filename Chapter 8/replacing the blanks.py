import random

words = ['good','bad','ugly']

random_word = random.choice(words)

# Show the blanks of guessed answer

display = []

for letter in random_word:

    display.append('_')

# Request guess from user

guessed = input('Type the guessed letter \n').lower()

# If it's right replace the blank

for position in range(len(random_word)):

    if random_word[position] == guessed:

        display[position] = guessed

print(display)

print(random_word)