import yaml 

__config = None

def config():
    global __config

    if not __config:
        with open('config.yaml','r') as f:   #Abro el archivo .yaml que hice, para no tener que leerlo a disco cada vez que lo llame
            __config = yaml.safe_load(f)     #Lo leo y lo inicializo a una variable
        
    return __config     # En caso de que la variable _config ya etuviera inicializada , es decir ya lo hubiera leido, solo paso el valor de la variable, que es un diccionario con la info del arichivo .yaml
