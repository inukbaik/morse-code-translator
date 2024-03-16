import json


def create_reverse_dict(original_dict):
    reverse_dict = {}
    for key, value in original_dict.items():
        reverse_dict[value] = key
    return reverse_dict


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
        reverse_dict = create_reverse_dict(morse_code_dict)
        english = english.upper()
        morse_code = ''
        for letter in english:
            if letter == ' ':
                morse_code += ' '
            elif letter in reverse_dict:
                morse_code += reverse_dict[letter] + ' '
    return morse_code


def main():
    try:
        select = input('Enter 1 for Morse to English, Enter 2 for English to Morse: ')
        if select not in ['1', '2']:
            raise ValueError('Invalid Input. Please enter 1 or 2')

        if select == '1':
            morse_code = input('Enter Morse Code: ')
            print(morse_to_english(morse_code))
        elif select == '2':
            english = input('Enter English: ')
            print(english_to_morse(english))
    except ValueError as ve:
        print(ve)

if __name__ == '__main__':
    main()