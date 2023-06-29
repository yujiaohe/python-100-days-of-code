#Number Guessing Game Objectives:

# Include an ASCII art logo. http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
# https://listmoz.com/#B42c6zkDx43YWVPCJNkJ

# Learning notes: set easy, hard attempts as global constant to manage them easily

from art import logo
import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
num = random.randint(1, 100)
# debug print the answer
print(f"Pssst, the correct answer is {num}")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
while level not in ['easy', 'hard']:
    print("Invalid input.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if level == "easy":
    attempts = EASY_LEVEL_ATTEMPTS
elif level == "hard":
    attempts = HARD_LEVEL_ATTEMPTS

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > num:
        print("Too high.")
    elif guess < num:
        print("Too low.")
    else:
        print(f"You got it! The answer was {num}.")
        break
    attempts -= 1
    if attempts == 0:
        print("You've run out of guesses, you lose.")
    else:
        print("Guess again.")
