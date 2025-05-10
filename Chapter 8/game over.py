# Start the project
import random
words = ['good','bad','ugly']
random_words = random.choice(words)

# Show the blanks of words 
display = ['_' for letter in random_words]
print(' '.join(display))
lives = 6

# Request to guess word and see if it's right or not right
while '_' in display and lives > 0:
    guessed = input('Please guess a letter \n').lower()

    if guessed not in random_words:
        lives -= 1

    for position in range(len(random_words)):
        if random_words[position] == guessed:
            display[position] = guessed
            
    print(' '.join(display))
    print(f'You have {lives} more tries!')

# Final result
if lives ==0:
    print('''
You lose!
        ''')
    print('''
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
        ''') 
else:
    print('YOU WIN !')