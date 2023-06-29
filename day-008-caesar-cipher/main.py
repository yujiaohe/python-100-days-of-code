import art

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount = len(alphabet) - shift_amount
    for letter in start_text:
        #What happens if the user enters a number/symbol/space?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")


print(art.logo)
continue_flag = True
while continue_flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #What if the user enters a shift that is greater than the number of letters in the alphabet? e.g: 45
    #Hint: Think about how you can use the modulus (%).
    shift %= len(alphabet)
    #Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
    caesar(text, shift, direction)
    decision = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if decision == 'no':
        continue_flag = False
        print("Goodbye")
