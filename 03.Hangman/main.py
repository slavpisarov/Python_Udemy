import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6;

display = ['_'] * word_length

print(logo)
print(display)

while "_" in display and lives >= 0:
  correct = False
  guess = input("Guess a letter:").lower()

  if guess in display:
    print('You already guessed that letter')
  else:
    for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
          correct=True
          display[position] = letter
  
    if correct is False:
      print(stages[lives])
      print(f'Letter "{guess}" is not in the word, you loose a life.')
      lives -= 1
      
  print(display)

if lives<0:
  print(f"You lost.The correct words is: {chosen_word}")
else:
  print("You won!")