from random import randint

def check_answer(user_choice,computer_choce, attempts ):
    if user_choice < computer_choce:
        print("Too low.")
        return attempts - 1
    elif user_choice > computer_choce:
        print("Too high.")
        return attempts - 1
    else:
        print("Correct! You Win!")
    
def game():
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose difficulty level. Type 'easy' or 'hard' : ")

    attempts: 0
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5

    computer_choce = randint(0,100)

    guess = 0;
    while guess != computer_choce :
        print(f"You have {attempts} attempts to guess the number.")
        guess = int(input("Make a guess: "))

        attempts = check_answer(guess, computer_choce, attempts)

        if(attempts == 0):
            print("You are out of turns, you loose.")
            return

game()