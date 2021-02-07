letters_numbers = {
    'w': 'و',
    'e': 'ي',
    'r': 'ر',
    't': 'ت',
    'y': 'ي',
    'i': 'ي',
    'o': 'و',
    'a': 'ا',
    's': 'س',
    'd': 'د',
    'f': 'ف',
    'g': 'ج',
    'h': 'ه',
    'k': 'ك',
    'l': 'ل',
    'z': 'ز',
    'b': 'ب',
    'n': 'ن',
    'm': 'م',
    '2': 'ئ',
    '3': 'ع',
    '3`': 'غ',
    '4': 'ذ',
    '5': 'خ',
    '6': 'ط',
    '6`': 'ظ',
    '7': 'ح',
    '8': 'ق',
    '9': 'ص',
    '9`': 'ض'
}

sentence = input("> ")

for key, value in letters_numbers.items():
    for letter in sentence:
        if letter == key:
            x = sentence.replace(letter, value)
            sentence = x
print(sentence)
