import random

top_of_number = input("Type a Number: ")

if top_of_number.isdigit():
    top_of_number = int(top_of_number)
    
    if top_of_number <= 0:
        print("Enter a valid number whic is greater than 0 next time! Bye!")
        quit()
else:
    print("Type a valid number next time!")
    quit()

random_number = random.randint(0, top_of_number)

guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a valid number!")
        continue
    
    if user_guess == random_number:
        print("You guessed it correct!")
        break
    else:
        print("Wrong guess! Try your luck again.")
        continue
print("You got it in",guesses,"guesses.")
 
