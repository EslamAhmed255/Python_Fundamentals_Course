import string
import random

print(string.ascii_lowercase)

print(string.ascii_uppercase)

print(string.digits)

print(string.punctuation)

# Random.choices

random_5 = random.choices(string.ascii_letters, k=5)

print(random_5)