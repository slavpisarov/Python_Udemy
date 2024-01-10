import random

print("I'm thinking of a number between 1 and 100.")
choice = input("Choose difficulty level. Type 'easy' or 'hard' : ")

attempts: 0
if choice == 'easy':
    attempts = 10
else:
    attempts = 5