from art import logo,vs
from game_data import data
import random
import os


def format_data(c):
    return f"{c["name"]}, a {c["description"]}, from {c["country"]} "

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

print(logo)
score = 0
game_continue = True
compareB = random.choice(data)

while game_continue:
    compareA = compareB
    compareB = random.choice(data)
    while compareA == compareB:
        compareB = random.choice(data)

    print(f"Compare A: {format_data(compareA)}")
    print(vs)
    print(f"Against B: {format_data(compareB)}")

    guess = input("Who has more followers? 'A'/'B' :").lower()

    a_followers = compareA["follower_count"]
    b_followers = compareB["follower_count"]

    is_correct = check_answer(guess ,a_followers, b_followers)

    os.system('clear')

    if is_correct:
        score +=1
        print(f"You are correct!Currect score: {score}")
    else:
        game_continue = False
        print(f"Incorrect. Final score: {score}")