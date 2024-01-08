import random
import os
from art import logo

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return("DRAW")
    elif computer_score == 0:
        return "You lose, opponent has Blackjack"
    elif user_score == 0:
        return "BLACKJACK ! You win !"
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "You win, opponent went over"
    elif user_score > computer_score:
        return " YOU WIN"
    else:
        return "You lose."

def play_game():

    print(logo)

    user_cards =[]
    computer_cards =[]
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)
        print(f"User cards: {user_cards} , user score : {user_score}")
        print(f"Comp first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            another_card = input("Do you want another card: y/n ? ")
            if another_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    computer_looses = computer_score < calc_score(user_cards)
    while computer_score != 0 and computer_score < 17 and computer_looses:
        computer_cards.append(deal_card())
        computer_score = calc_score(computer_cards)
        computer_looses = computer_score < calc_score(user_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's hand: {computer_cards}, computer score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack: y/n ?") == "y":
    os.system('clear')
    play_game()