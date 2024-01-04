from alphabet import alphabet

def caesar(start_text,shift_num,shift_direction):
    end_text=""
    if shift_direction == "decode":
        shift_num *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_num
            new_letter = alphabet[new_position]
            end_text += new_letter
        else:
            end_text += char
    print(f"The {shift_direction}d word is {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(text,shift,direction)

    result = input("Do you want to go again? yes/no ")
    if result == 'no':
        should_continue = False
        print('Goodbye')
