# Shruthi, make me a number guessing game

# CODE EXAMPLES FOR REFERENCE:
'''
print("THIS IS HOW YOU PRINT TEXT")

userInput = input("PROMPT USER TO ENTER INPUT> ")

# Generate A Random Number Between 0 and 13
import random
randomNumber = random.randint(0, 13)

'''
import random

print("Guess a number between 0 and 13")
print(" ")

randomNumber = random.randint(0, 13)

guess = input("Guess number here> ")
guess = int(guess) # cast as integer

if randomNumber == guess:
    print("Correct!")
elif randomNumber > guess:
    print("Guess higher")
elif randomNumber < guess:
    print("Guess lower")
else:
    print("Error guess again")
