

def repeating(text):
    #text.replace(' ','')
    text = list(text)
    letter = []
    idx = [] 
    for k,i in enumerate(text):
        number_repetition = text.count(i)
        if number_repetition == 1:
            letter.append(i)
            idx.append(k)
    
    if letter:
        return letter[0],idx[0]
    else:
        print('Todas las letras se repiten')


if __name__ == '__main__':
    text = input(f'Dame un string  ')
    letter,idx = repeating(text)
    print(f'La primera letra que no se repite es \'{letter}\' y se encuentra en el índice {idx}')








# def first_not_repeating_char(char_sequence):
#     seen_letters = {}

#     for idx, letter in enumerate(char_sequence):
#         if letter not in seen_letters:
#             seen_letters[letter] = (idx, 1)
#         else:
#             seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

#     final_letters = []
#     for key, value in seen_letters.iteritems():
#         if value[1] == 1:
#             final_letters.append( (key, value[0]) )

#     not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

#     if not_repeated_letters:
#         return not_repeated_letters[0][0]
#     else:
#         return '_'


# if __name__ == '__main__':
#     char_sequence = str(raw_input('Escribe una secuencia de caracteres: '))

#     result = first_not_repeating_char(char_sequence)

#     if result == '_':
#         print('Todos los caracteres se repiten.')
#     else:
#         print('El primer caracter no repetido es: {}'.format(result))