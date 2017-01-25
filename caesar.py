def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter = letter.lower()
    return alphabet.find(letter)

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    position = alphabet_position(char)
    if char.isupper():
        if char.lower() in alphabet:
            position += rot
            position = position % 26
            return alphabet[position].upper() #addon
        else:
            return char
    else:
        if char in alphabet:
            position += rot
            position = position % 26
            return alphabet[position] #addon
        else:
            return char

def encrypt(text, rot):
    result = ''
    for letter in text:
        result += rotate_character(letter, rot)
    return result
