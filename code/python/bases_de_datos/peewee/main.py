import peewee


data_base = peewee.MySQLDatabase('test',
                                host='localhost',
                                port=3306,
                                user='root',
                                password='Cesar20022007#')