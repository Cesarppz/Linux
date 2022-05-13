from sqlite3 import connect
import psycopg2

from queries import USER_TABLE
from aux_funtions import options, default
from decouple import config


def initialize_db():
    try:
        clave_db = config('clave_postgres')
        connect = psycopg2.connect("postgresql://postgres:{clave}@localhost/test".format(clave=clave_db))
        
        cursor =  connect.cursor()
            # Drop table if exist
            #cursor.execute(DROP_TABLE)
            
            #Create table
        try:
            cursor.execute(USER_TABLE)
        except psycopg2.errors.DuplicateTable as err:
            pass
        connect.commit()

        return connect, cursor 

    except psycopg2.OperationalError as err:
        print('Error in the conexion')
        print(err)
    
    except Exception as err_e:
        print('Error en el porgrama ')
        print(err_e)
    


def main():
    connect, cursor = initialize_db()

    while True:
        for function in options.values():
            print(function.__doc__)
        print('Insert "quit" to exit')

        option = input('\nSelecione una opción válida: ').lower().strip()

        if option == 'quit' or option == 'q':
            connect.close()
            break 
        # Ejecutar funcion
        function = options.get(option, default)
        function(connect, cursor)

    cursor.close()
    connect.close()


if __name__ == '__main__':
    main()