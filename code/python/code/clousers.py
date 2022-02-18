
def receptor(palabra:str) :
    assert type(palabra) == str , "Solo se puede usar cadenas de texto"
    def repetidor(multiplo:int):
        return palabra * multiplo
    return repetidor

if __name__ == '__main__':
    palabra = input('Elije la palabra ')
    try:
        multiplo = int(input('Elije la cantidad de veces que deseas que se repita la palabra '))
        funct = receptor(palabra)
        print(funct(multiplo))
    except ValueError as v:
        print(v,"Solo se puede usar numeros enteros")
   