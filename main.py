import arabic_reshaper
import re

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
    'g': 'ق',
    'h': 'ه',
    'k': 'ك',
    'c': 'ك',
    'l': 'ل',
    'z': 'ز',
    'j': 'ج',
    'b': 'ب',
    'n': 'ن',
    'm': 'م',
    '2': 'ئ',
    '3': 'ع',
    '4': 'ذ',
    '5': 'خ',
    '6': 'ط',
    '7': 'ح',
    '8': 'ق',
    '9': 'ص',
    '9`': 'ض'
}

digraphs = {
    'sh': 'ش',
    'th': 'ذ',
    'ch': 'ج',
    '6`': 'ظ',
    '3`': 'غ',
}


def change_digraphs(sen):
    for key in digraphs.keys():
        find_letter = re.compile(r'{}'.format(key))
        two_letters = find_letter.findall(sen)
        grouped_letters = two_letters

        for keys, values in digraphs.items():
            for di in grouped_letters:
                if keys == di:
                    sen = sen.replace(di, digraphs[keys])

    for key, value in letters_numbers.items():
        for letter in sen:
            if letter == key:
                x = sen.replace(letter, value)
                sen = x
    # reshapes arabic letters to make them linked
    reshaped_text = arabic_reshaper.reshape(sen)
    # reverses the sentences to 'right to left'
    rev_text = reshaped_text[::-1]
    return rev_text


sentence = input("> ")

print(change_digraphs(sentence))
