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

QUERY = """SELECT id, user_name, email FROM test_table """

QUERY_SELECT_ID =  """SELECT id FROM test_table WHERE id = %s"""

QUERY_UPDATE = """UPDATE test_table SET user_name = %s, email = %s, password = %s WHERE id = %s"""

QUERY_DELETE = """DELETE FROM test_table WHERE id = %s"""
