# Project variables
import random
words = ['good','bad','ugly']
random_word = random.choice(words)
lives = 6
display = []
guessed_letters = []

# Display
for letter in random_word:
  display.append('_')
print(' '.join(display))

# Hangman stages
stages = [
        """
          _____
         |     |
         |
         |
         |
         |
        _|_
        """,
        """
          _____
         |     |
         |     O
         |
         |
         |
        _|_
        """,
        """
          _____
         |     |
         |     O
         |     |
         |
         |
        _|_
        """,
        """
          _____
         |     |
         |     O
         |    /|
         |
         |
        _|_
        """,
        """
          _____
         |     |
         |     O
         |    /|\\
         |
         |
        _|_
        """,
        """
          _____
         |     |
         |     O
         |    /|\\
         |    /
         |
        _|_
        """,
        """
          _____
         |     |
         |     O
         |    /|\\
         |    / \\
         |
        _|_
        """
]

# Take guess from user
print(stages[0])
while '_' in display and lives > 0:
    guessed = input('Please guess a letter: ').lower()

# If it's the same guessed letter
    if guessed in guessed_letters:
        print('You already guessed that, Try again.')
        print(f'You have {lives} more tries')
        continue
    guessed_letters.append(guessed)

# If it's not right 
    if guessed not in random_word:
        lives -= 1
        print(stages[6 - lives])

    else:
        for position in range(len(random_word)):
            if random_word[position] == guessed:
              display[position] = guessed
    
    print(' '.join(display))
    print(f'You have {lives} more tries!')

# Game over messages
if lives == 0:
  print(f"Game over! The word was: {random_word}")

else:
  print("Congratulations! You won!")