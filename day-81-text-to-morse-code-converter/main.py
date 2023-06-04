from art import logo

# from https://gist.github.com/mohayonao/094c71af14fe4791c5dd
morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

print("Welcome to Text to Morse Code Converter!")
print(logo)

continue_flag = True
while continue_flag:
    text = input("Input your text that need to convert to Morse Code:\n").lower()
    result = ""
    for char in text:
        result += morse_code.get(char, char)
    print(f"Morse Code is:\n{result}")
    while True:
        flag = input("Continue? input 'Yes' or 'No': ").lower()
        if flag == "no":
            continue_flag = False
            break
        elif flag == "yes":
            break
        else:  # invalid input, try again
            print("Invalid input, please try again!")




