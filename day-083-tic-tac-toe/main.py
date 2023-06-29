import random
from art import logo


def show_grid(grid):
    for index in range(len(grid)):
        if (index+1) % 3 == 0:
            print(f" {grid[index]} ")
        else:
            print(f" {grid[index]} ", end="|")

        if index == 2 or index == 5:
            print("-----------")

    print("Available location:")
    for index in range(len(grid)):
        value = index if grid[index] == ' ' else ' '
        if (index+1) % 3 == 0:
            print(f" {value} ")
        else:
            print(f" {value} ", end="|")

        if index == 2 or index == 5:
            print("-----------")


def check_winter(grid):
    if grid[:3] in [['X']*3, ['O']*3]:
        return True, grid[0]
    elif grid[3:6] in [['X']*3, ['O']*3]:
        return True, grid[3]
    elif grid[6:9] in [['X']*3, ['O']*3]:
        return True, grid[6]
    elif grid[::3] in [['X']*3, ['O']*3]:
        return True, grid[0]
    elif grid[1::3] in [['X']*3, ['O']*3]:
        return True, grid[1]
    elif grid[2::3] in [['X']*3, ['O']*3]:
        return True, grid[2]
    elif grid[::4] in [['X']*3, ['O']*3]:
        return True, grid[0]
    elif grid[2::2][:3] in [['X']*3, ['O']*3]:
        return True, grid[2]
    else:
        return False, 'NA'


current_grid = [' ']*9
player_flag = True
print("Welcome to Tic Tac Toe")
print(logo)
player = input("Start the game and chose the player. 'X' or 'O'? 'X' play first. ").upper()
while player_flag:
    if player == 'X' or player == 'O':
        player_flag = False
    else:
        print("Incorrect input, please try again!")
        player = input("Start the game and chose the player. 'X' or 'O'? 'X' play first. ").upper()

opps = 'O'
# X player go first
if player == 'O':
    opps = 'X'
    random_index = random.randint(0, len(current_grid) - 1)
    while current_grid[random_index] != ' ':
        random_index = random.randint(0, len(current_grid) - 1)
    current_grid[random_index] = opps

continue_flag = True
while continue_flag:
    show_grid(current_grid)
    checked = int(input(f"[{player}] Your turn, please chose available location from 0 to 8: "))
    while current_grid[checked] != ' ':
        print("Incorrect input, please try again!")
        checked = int(input(f"[{player}] Your turn, please chose available location from 0 to 8: "))
    current_grid[checked] = player

    random_index = random.randint(0, len(current_grid) - 1)
    while current_grid[random_index].strip() in ['X', 'O']:
        random_index = random.randint(0, len(current_grid) - 1)
    current_grid[random_index] = opps

    game_result, winner = check_winter(current_grid)
    if game_result:
        continue_flag = False
        show_grid(current_grid)
        if winner == player:
            print("Game over, you win!")
        else:
            print("Game over, you lose!")





