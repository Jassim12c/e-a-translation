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
    'l': 'ل',
    'z': 'ز',
    'j': 'ج',
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

digraphs = {
    'sh': 'ش',
    'th': 'ذ',
    'ch': 'ج',
}


def change_digraphs(arg1):

    find_letter = re.compile(r'{}'.format(arg1))
    two_letters = find_letter.search(sentence)
    grouped_letters = str(two_letters.group())

    for keys, values in digraphs.items():
        if keys == grouped_letters:
            final_sen = sentence.replace(grouped_letters, digraphs[keys])
            return final_sen

sentence = input("> ")


for key, value in letters_numbers.items():
    for letter in sentence:
        if letter == key:
            x = sentence.replace(letter, value)
            sentence = x


# reshapes arabic letters to make them linked
reshaped_text = arabic_reshaper.reshape(sentence)
# reverses the sentences to 'right to left'
rev_text = reshaped_text[::-1]
print(rev_text)

print(tuple(digraphs.items())[0][0])
