import random
from password_characters import letters,numbers,symbols

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for char in range(1, nr_letters + 1):
  password += random.choice(letters)
  
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
  
for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)

password_list = list(password)
random.shuffle(password_list)
password = "".join(password_list)

print(f"Your password is: {password}")