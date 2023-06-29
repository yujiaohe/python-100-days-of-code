from replit import clear
from art import logo

print(logo)
print("Welcome to the sercret auction program.")
continue_flag = True
bids = {}
while continue_flag:
  name = input("What is your name?: ")
  price = int(input("What's your bid?: $"))
  bids[name] = price
  decision = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
  if decision == "no":
    continue_flag = False
    winner = ""
    winner_bid = 0
    for name_key in bids:
      if bids[name_key] > winner_bid:
        winner = name_key
        winner_bid = bids[winner]
    print(f"The winner is {winner} with a bid of ${winner_bid}")
  else:
    clear()