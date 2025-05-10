life = 6 # Global variable

def life_lose():
    global life
    life -= 1 # Local variable
    print(f'you have {life} tries')

life_lose()