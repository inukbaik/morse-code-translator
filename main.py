import json


def morse_to_english(morse_code):
    with open('data.json', 'r') as file:
        morse_code_dict = json.load(file)
        morse_code = morse_code.split(' ')
        english = ''
        for code in morse_code:
            if code in morse_code:
                english += morse_code_dict[code]
            else:
                english += ' '
    return english


def english_to_morse(english):
    with open('data.json', 'r') as file:
        morse_code_dict = json.load(file)
        english = english.upper()
        morse_code = ''
        for letter in english:
            if letter == ' ':
                morse_code += ' '
            else:
                for key, value in morse_code_dict.items():
                    if value == letter:
                        morse_code += key + ' '
    return morse_code


select = input('Enter 1 for Morse to English, Enter 2 for English to Morse: ')

if select == '1':
    morse_code = input('Enter Morse Code: ')
    print(morse_to_english(morse_code))
elif select == '2':
    english = input('Enter English: ')
    print(english_to_morse(english))
