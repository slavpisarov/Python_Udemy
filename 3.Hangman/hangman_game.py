import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ['elephant', 'jaguar', 'kangaroo', 'zebra', 'chimpanzee', 'giraffe', 'rhinoceros', 'hippopotamus', 'platypus', 'koala', 'orangutan', 'crocodile', 'penguin', 'cheetah', 'lemur', 'ostrich', 'armadillo', 'meerkat', 'toucan', 'gorilla', 'hyena', 'parrot', 'quokka', 'gibbon', 'iguana', 'wombat', 'otter', 'puffin', 'koala', 'sloth', 'capybara', 'puffin', 'cobra', 'lemur', 'aardvark', 'mongoose', 'tapir', 'vulture', 'cormorant', 'axolotl']


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
  print("You lost")
else:
  print("You won!")