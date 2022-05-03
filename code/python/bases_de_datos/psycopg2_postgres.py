import psycopg2
from decouple import config
import traceback

DROP_TABLE = """ DROP TABLE IF EXISTS test_table"""   #Borrar tabla

#Crear tabla
USER_TABLE = """ CREATE TABLE test_table(            
    id SERIAL,
    user_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""   
QUERY_INSERT = """INSERT INTO test_table (user_name,email,password) VALUES(%s,%s,%s)"""  #Query para insertar los datos 
QUERY = """SELECT * FROM test_table WHERE lower(user_name) LIKE 'c%' """

if __name__ == '__main__':
    try:
        connect = psycopg2.Connect("dbname='nombre' user='user_name' password='clave' host='localhost'")
        
        with connect.cursor() as cursor:
            # Drop table if exist
            #cursor.execute(DROP_TABLE)
            
            #Create table
            try:
                cursor.execute(USER_TABLE)

            except psycopg2.OperationalError as err:
                pass
            
            #Insert
            values = [
                ('Carlos','carlos@gmailcom','clave123'),
                ('Javier','javier2002@gmailcom','clave23')
                ]
            #cursor.execute(QUERY_INSERT,values)  #Para ingresar un valor. Puedo ingresar varios con ciclo For
            cursor.executemany(QUERY_INSERT,values) #Para ejecutar varios a la vez

            connect.commit() #Al alterar la base de datos tengo que hacer un commit

            #QUERYS
            rows = cursor.execute(QUERY)  #Me da el number de registros
            for register in cursor.fetchall():
                print(register)
            

    except pymysql.err.OperationalError as err:
        print('Error in the conexion')
        print(err)

    finally:
        connect.close()
        print('successful connection')