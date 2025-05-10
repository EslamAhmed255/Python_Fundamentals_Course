import random 

# Rock Asci
rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

# Paper Asci
paper = ('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')

# Scissors Asci
scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

# User choice 

print('Welcome to rock, paper, scissors')

Confirm = input('Press Enter to continue or type (help) for the rules \n').lower()

if Confirm == 'help':

    print('''
                            *****RULES*****
                1) You choose and the computer chooses
                2) Rock smashes Scissors -> Rock wins
                3) Scissors cut paper -> Scissors win
                4) Paper covers rock -> Paper wins
''')
    
user = input('Type your choice (rock, paper or scissors) \n').lower()

if user not in ["rock","paper","scissors"]:

    print("Invalid choice")

else:

    if user == 'rock':

        print(f'You choose {rock}')

    elif user == 'paper':

        print(f'Your choose {paper}')

    elif user == 'scissors':

        print(f'You choose {scissors}')

    else:

        print('Invalid choice')

# Computer choice

computer_choice = random.choice(['rock','paper','scissors'])

if computer_choice == 'rock':

    print(f'Computer choose {rock}')

elif computer_choice == 'paper':

    print(f'Computer choose {paper}')

elif computer_choice == 'scissors':

    print(f'Computer choose {scissors}')

# Win & Lose situations

if user == computer_choice:

    print(f'you choose {user} and computer choose {computer_choice} it is a tie !')

elif user == 'rock' and computer_choice == 'scissors':

    print (f'Good job {user} beats {computer_choice}')

elif user == 'paper' and computer_choice == 'rock':

    print (f'Good job {user} beats {computer_choice}')

elif user == 'scissors' and computer_choice == 'paper':

    print (f'Good job {user} beats {computer_choice}')

else:

    print(f'Sorry you lose, {computer_choice} beats {user}')