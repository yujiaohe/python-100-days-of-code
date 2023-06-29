import random
from art import logo, vs
from game_data import data
from replit import clear


def compare(account_a, account_b):
    """Takes the account_a and account_b and returns the max follower account"""
    if account_a["follower_count"] > account_b["follower_count"]:
        return "a"
    elif account_a["follower_count"] < account_b["follower_count"]:
        return "b"
    else:
        return "e"


def info(data_dict):
    """Takes the account data and return format name, description and country from a data dictionary"""
    return f"{data_dict['name']}, a {data_dict['description']}, from {data_dict['country']}"


score = 0
print(logo)
account_a = random.choice(data)
continue_flag = True

while continue_flag:
    account_b = random.choice(data)
    # random choose account_b and account_b != account_a
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {info(account_a)}")
    # Below print is only for debug
    print(f"Pssst, A follower: {account_a['follower_count']}")
    print(vs)
    print(f"Against B: {info(account_b)}")
    # Below print is only for debug
    print(f"Pssst, B follower: {account_b['follower_count']}")
    decision = input(
        "Who has more followers? Type 'A' or 'B' or 'E'(equal): ").lower()
    clear()
    print(logo)
    if decision == compare(account_a, account_b):
        score += 1
        account_a = account_b
        print(f"You're right! Current score: {score}")
    else:
        continue_flag = False
        print(f"Sorry, that's wrong. Final score: {score}")
