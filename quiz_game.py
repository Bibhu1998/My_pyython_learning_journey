print("Welcome the quiz game!")
game_start = input("Do you want to play this Game? ")

if game_start.lower() == 'no':
    quit()
    print("No hard feelings! Visit Again")

print("Let's start the game")
score = 0

answer = input("What does CPU stands for: ")
if answer.lower() == 'central processing unit':
    print("Correct")
    score += 1
else:
    print("Incorrect! Try agin")

answer = input("Who is the PM of India: ")
if answer.lower() == 'narendra modi':
    print("Correct")
    score += 1
else:
    print("Incorrect! Try agin")

answer = input("Who is the CM of Odisha: ")
if answer.lower() == 'narendra modi':
    print("Correct")
    score += 1
else:
    print("Incorrect! Try agin")

answer = input("What does GPU stands for: ")
if answer.lower() == 'narendra modi':
    print("Correct")
    score += 1
else:
    print("Incorrect! Try agin")

answer = input("What does RAM stands for: ")
if answer.lower() == 'narendra modi':
    print("Correct")
    score += 1
else:
    print("Incorrect! Try agin")

if score>=4:
    print("You've got "+str(score)+" out of 5. Excellent, keep it up!")
    print("You've secured "+str((score/5)*100)+"%")
else:
    print("You've got "+str(score)+" out of 5. You need to work on your GK!")
    print("You've secured "+str((score/5)*100)+"%")

