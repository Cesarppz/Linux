from queries import QUERY_INSERT, QUERY, QUERY_SELECT_ID, QUERY_UPDATE, QUERY_DELETE
import os

def terminal_clear(function):

    def wrapper(connect, cursor):
        os.system('clear')  #Ejecuro el comando clear en terminal
        function(connect, cursor)
        input('')
        os.system('clear')
    
    wrapper.__doc__ = function.__doc__
    return wrapper


def user_exists(function):

    def wrapper(connect, cursor):

        id_user = input('Ingrese el ID del usuario que quiere eliminar ').strip()
        try:
            int(id_user)

            cursor.execute(QUERY_SELECT_ID,(id_user,))
            user = cursor.fetchone()

            if user:
                function(id_user, connect, cursor)
            else:
                print('>>> No se encuentra un usuario con ese ID')

        except ValueError:
            print('>>> Valor inválido')

    wrapper.__doc__ = function.__doc__

    return wrapper

@terminal_clear
def list_users(connect, cursor):
    '''D) Listar los usuarios'''

    cursor.execute(QUERY)

    for id, user_name, email in cursor.fetchall():
        print(f'id: {id}, User Name: {user_name}, Email: {email}')


@terminal_clear
@user_exists
def remove_user(id_user, connect, cursor):
    '''B) Borrar usuario'''
    
    cursor.execute(QUERY_DELETE, (id_user,))
    connect.commit()
    print('>>> Usuario eliminado exitosamente')


@terminal_clear
@user_exists         
def update_user(id_user, connect, cursor):
    '''C) Actualizar usuario'''

    user_name = input('Ingrese el nuevo user_name del usuario ').strip()
    email = input('Ingrese el nuevo Email del usuario ').strip()
    password = input('Ingrese la nueva contraseña del usuario ').strip()
    new_values = (user_name, email, password, id_user)

    cursor.execute(QUERY_UPDATE, new_values)
    connect.commit()

    print('>>> Usuario actualizado exitosamente')
            

@terminal_clear
def create_user( connect, cursor):
    '''\nA) Crear usuario'''

    user_name = input('Ingrese el nombre del usuario ').strip()
    email = input('Ingrese el corre del usuario ').strip()
    password = input('Ingrese la contraseña del usuario ').strip()

    value = (user_name, email, password)
    print(value)
    print('\n Usuario creado exitosamente')

    try:
        cursor.execute(QUERY_INSERT,value)
        connect.commit()

    except Exception as e:
        print('>>> Error al ingresar el usuario')
        print(e)



def default(*args):
    print('\n>>> Opción no válida !\n')
    


options = {
    'a': create_user,
    'b': remove_user,
    'c': update_user,
    'd': list_users
    }