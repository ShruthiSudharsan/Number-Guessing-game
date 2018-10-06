# Random Number Guessing Game by Shruthi Sudharsan- a rockstar coding student
# at theCoderSchool in Flower Mound, TX

import random

print("guess.py")
print("Copyleft 2018, Shruthi Sudharsan")
print("")
print("Guess a number between 0 and 13")
print("")

randomNumber = random.randint(0, 13)
guess = False

while guess != randomNumber:
    # PROMPT USER
    guess = input("Guess number here> ")
    guess = int(guess) # cast as integer
    # DETERMINE OUTCOME
    if randomNumber == guess:
        print("Correct!")
    elif randomNumber > guess:
        print("Guess higher")
    elif randomNumber < guess:
        print("Guess lower")
    else:
        print("Error guess again")
