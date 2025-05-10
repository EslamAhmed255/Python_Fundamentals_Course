sentence = input('Enter a sentence: ').lower()

words = sentence.split()

reversed_words = words[::-1]

print(' '.join(reversed_words))