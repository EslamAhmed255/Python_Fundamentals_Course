# Project Variables
import string
alphabet = string.ascii_lowercase
word = input('Please type a word: ').lower()
encrypted_word = ''

# For Loop
for letter in word:
    if letter in alphabet:
        original_position = alphabet.index(letter)
        new_position = (original_position + 2) % 26
        encrypted_word += alphabet[new_position]

# Print The Final Result
print(f'Here is the Encrypted word: {encrypted_word}')