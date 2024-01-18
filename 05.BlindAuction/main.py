import os
from art import logo

print(logo)
bids = {}
finished = False

while not finished:
    name = input("What's your name? ")
    price = int(input("What's your bid? "))
    bids[name] = price

    more_bids = input("Are there any other bidders? yes/no ")

    if more_bids == 'no':
        finished = True
    elif more_bids == "yes":
        os.system('clear')

highest_bid = 0
winner = ""

for key in bids:
    money = bids[key]
    if(money > highest_bid):
        highest_bid = money
        winner = key

print(f"The winner is {winner} with a bid of ${highest_bid}")