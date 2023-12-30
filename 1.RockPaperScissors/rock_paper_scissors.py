import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock, paper, scissors]

user_choice = int(input('Type 0 for rock, 1 for paper, 2 for scissors: \n'))

if user_choice >= 3 or user_choice < 0:
  print("Plese, enter only valid numbers")

else:
  print(f'You chose: {list[user_choice]}')
  
  random_choice = random.randint(0, 2)
  
  print(f'Computer chose: {list[random_choice]}')
  
  if user_choice == 0:
    if random_choice == 0:
      print('Draw')
    elif random_choice == 1:
      print('You lost')
    elif random_choice == 2:
      print('You win!')
  elif user_choice == 1:
    if random_choice == 0:
      print('You win!')
    elif random_choice == 1:
      print('Draw')
    elif random_choice == 2:
      print('You lost')
  elif user_choice == 2:
   if random_choice == 0:
    print('You lost')
   elif random_choice == 1:
    print('You win!')
   elif random_choice == 2:
    print('Draw')