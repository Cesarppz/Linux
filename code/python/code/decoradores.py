def decorador(funcion_parametro):
    
    def funcion_interna(*arg):
        print('\nse va a realizar una operación matemática \n')
        return funcion_parametro(*arg)
    
    return funcion_interna

@decorador
def potencia(*arg):
    return pow(n,n2)

@decorador
def suma(n,n2):
    return n + n2


def resta(*arg):
    return n - n2 

def run(*arg):
    
    while True:
        option =input('\nElige una opción entre [p], [s] y [r]  ')
        if option == 'p':
            print(potencia(n,n2))
        elif option == 's':
            print(suma(n,n2))
        elif option == 'r':
            print(resta(n,n2))

if __name__ == '__main__':
    n = int(input('dame un número  ' ))
    n2 = int(input('dame un número  ' ))

    run(n,n2)



# def decorator(protected_pw):

#     def interior(password):
#         if password == 'cesar':
#             return protected_pw()
#         else :
#             print('contraseña incorrecta ')
#     return interior


# @decorator
# def protected_pw():
#     print('La contraseña es correcta')

# if __name__ == '__main__':

#     password = input('Dame una contraseña ').lower()

#     password_v = protected_pw(password)


