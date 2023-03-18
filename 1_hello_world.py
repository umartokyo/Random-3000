# Mar 18 / 2023

word = 'hello world'

alphabet = " abcdefghijklmnopqrstuvwxyz,.'?!"
input_word = word.lower()
output_word = ''

for search in input_word:
    for letter in alphabet:
        print(output_word + letter)
        if letter == search:
            output_word += letter
            break
