import json
from main import morse_to_english, english_to_morse


def test_morse_to_english():
    # Test cases for Morse to English conversion
    assert morse_to_english('.- -... -.-.') == 'ABC'
    assert morse_to_english('.... . .-.. .-.. ---') == 'HELLO'
    assert morse_to_english('... --- ...') == 'SOS'

def test_english_to_morse():
    # Test cases for English to Morse conversion
    assert english_to_morse('ABC') == '.- -... -.-. '
    assert english_to_morse('HELLO') == '.... . .-.. .-.. --- '
    assert english_to_morse('SOS') == '... --- ... '

def test_invalid_input():
    # Test cases for invalid input
    assert morse_to_english('.____.') == ''  # Invalid Morse code
    assert english_to_morse('ㄱㄴㄷ') == ''  # Invalid English text

if __name__ == '__main__':
    # Run the test cases
    test_morse_to_english()
    test_english_to_morse()
    test_invalid_input()
    print("All tests passed successfully!")
