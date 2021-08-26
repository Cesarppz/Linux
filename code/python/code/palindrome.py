from typing import Dict, List, Tuple


def is_palindrome(string:str) -> bool:
    string = string.replace(' ', '').lower()
    return string == string[::-1]


if __name__ == '__main__':
    response: str = input('Ingrese la palabra que desea varificar si es un palindromo ')
    respuesta: bool =is_palindrome(response)
    if respuesta == True:
        print('La palabra es un palindromo')
    else :
        print('La palabra no es un palindromo')