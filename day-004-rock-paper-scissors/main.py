rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Sissors."))
computer = random.randint(0, 2)
map = [rock, paper, scissors]

if user > 3 or user < 0:
    print("You typed an invalid number, you lose!")
else:
    print(map[user])
    print("Computer chose:")
    print(map[computer])
    delta = user - computer
    if delta == 1 or delta == -2:
        print("You win!")
    elif delta == -1 or delta == 2:
        print("You lose")
    else:
        print("It's a draw")
