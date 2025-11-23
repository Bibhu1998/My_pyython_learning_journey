import random

options = ['rock','paper','scissors']

user_win = 0
opponent_win = 0

while True:
    user_input = input("Type Rock/Paper/Scissors and Q for quit: ").lower()
    if user_input == 'q':
        # print("Choose the correct option.")
        break
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    opponent_input = options[random_number]
    print("Oponent picked",opponent_input+'.')

    if user_input == 'rock' and opponent_input == 'cissors':
        user_win += 1
        print("You won!")
    elif user_input == 'cissors' and opponent_input == 'paper':
        user_win += 1
        print("You won!")
    elif user_input == 'paper' and opponent_input == 'rock':
        user_win += 1
        print("You won!")
    else:
        print('You lost!')
        opponent_win += 1

print("You win",user_win,"times.")
print("Opponent win",opponent_win,"times.")

