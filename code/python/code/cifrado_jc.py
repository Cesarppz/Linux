#!/usr/bin/python3
KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}


def cypher(text):
    text = text.split(' ')
    box  = []

    for word in text:
        cypher_word = ''
        for letter in word:
            try:
                cypher_word += KEYS[letter]
                #cypher_word = format(ord(KEYS[letter]),'b')
                
            except KeyError:
                cypher_word += letter
                #cypher_word += format(ord(letter),'b')
        box.append(cypher_word)  #Agrego la suma de las letras cifradas a la lista para luego unirlas
    return ' '.join(box)


def descipher(text):
    #binary_numbers = [128,64,32,16,8,4,2,1]
    text = text.split(' ')
    box     = []
    #des_box = []
    #n = 8
    #split_strings = [text[index : index + n] for index in range(0, len(text), n)]
    #print(split_strings)
    # for letter in split_strings:
    #     sumatory = 0
    #     for idx , n in enumerate(letter):
    #         print(idx,n)
    #         if n == '1':
    #             sumatory += binary_numbers[idx]
            
    #     decipher_letter = chr(sumatory)
    #     print(decipher_letter)
    #     box.append(decipher_letter)
            

    
    for word in text:
        descipher_word = ''
        
        for letter in word:
            for i,j in KEYS.items():
                if letter == j:
                    descipher_word += i
            if letter not in KEYS:
                descipher_word += letter


        box.append(descipher_word)
    return ' '.join(box)


if __name__ == '__main__':
    start=input(f' B I E N V E N I D O\n\n [E]Para encriptar\n [D]Para desencriptar\n [S]Para salir ')
    start = start.lower()
    
    if start == 'd':
        text=input(f'\nColoque su texto aquí: ')
        res =descipher(text)
        print(f'\n {res}\n Con cuidado rey')
    elif start == 'e':
        text=input(f'\nColoque su texto aquí: ')
        res = cypher(text)
        print(f'\n {res}\n Aquí tienes tu mensaje secreto')
    else:
        print('Adios!...')