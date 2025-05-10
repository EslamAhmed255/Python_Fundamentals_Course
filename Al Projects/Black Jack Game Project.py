# Import modules
import time
import os
import random

# Clear screen function
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Game welcome screen
def welcome_screen():
    print('Starting game......')
    time.sleep(3)
    clear_screen()
    print('Welcome to Black Jack game')
    print('''
.------..------..------..------..------.
|B.--. ||L.--. ||A.--. ||C.--. ||K.--. |
| :(): || :/\: || (\/) || :/\: || :/\: |
| ()() || (__) || :\/: || :\/: || :\/: |
| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'
.------..------..------..------.        
|J.--. ||A.--. ||C.--. ||K.--. |        
| :(): || (\/) || :/\: || :/\: |        
| ()() || :\/: || :\/: || :\/: |        
| '--'J|| '--'A|| '--'C|| '--'K|        
`------'`------'`------'`------'        
''')

# Cards list and values
cards_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'ace', 'queen', 'king', 'jack'] * 4

card_values = {
    'ace': 11,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'jack': 10,
    'queen': 10,
    'king': 10,
}

# Cards value function
def card_value(card):
    if card in ['jack', 'queen', 'king']:
        return 10
    elif card == 'ace':
        return 11
    else:
        return int(card)

# Total calculator with ace handling
def calculate_total(hand):
    total = sum([card_value(card) for card in hand])
    aces = hand.count('ace')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# Main game function
def main_function():
    random.shuffle(cards_list)

    player_hand = []
    dealer_hand = []

    for i in range(2):
        player_hand.append(cards_list.pop())
        dealer_hand.append(cards_list.pop())

    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)

    print(f"Player's cards: {player_hand}, and current total: {player_total}")
    print(f"Dealer's cards: {dealer_hand}, and current total: {dealer_total}")

    # Immediate Blackjack cases
    if player_total == 21 and dealer_total == 21:
        print("Both got Blackjack! It's a tie!")
        return player_hand, dealer_hand
    elif dealer_total == 21:
        print("Dealer got Blackjack! You lose!")
        return player_hand, dealer_hand
    elif player_total == 21:
        print("Blackjack! You win!")
        return player_hand, dealer_hand

    # Player's turn
    while player_total < 21:
        action = input("Do you want to hit or stand? ").lower()
        if action == 'hit':
            player_hand.append(cards_list.pop())
            player_total = calculate_total(player_hand)
            print(f"Player's cards: {player_hand}, and current total: {player_total}")
        elif action == 'stand':
            break

    if player_total > 21:
        print(f"Player's total exceeded 21. You lose!")
        return player_hand, dealer_hand

    # Dealer's turn
    while dealer_total < 17:
        dealer_hand.append(cards_list.pop())
        dealer_total = calculate_total(dealer_hand)
        print(f"Dealer's cards: {dealer_hand}, and current total: {dealer_total}")
        time.sleep(1)

    # Final outcome
    if dealer_total > 21:
        print(f"Dealer's total exceeded 21. You win!")
    elif player_total > dealer_total:
        print("Congratulations! You win!")
    elif player_total < dealer_total:
        print("Sorry, dealer wins!")
    else:
        print("It's a tie!")

    return player_hand, dealer_hand

# Start the game loop
while True:
    welcome_screen()
    main_function()
    new_game = input('Do you want to play again?: ').lower()
    if new_game != 'y': 
        break
print('Thanks for playing the game')