from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base #Tener absceso a las funcionalidades de orm
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:Cesar20022007#@localhost/newspapers')
#mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
#engine.execute("CREATE DATABASE newspaper") #Para crear la base de datos 
engine.execute("USE newspapers") #Para usar la base de datos 

Session = sessionmaker(bind=engine) 

Base = declarative_base()       #Crear la sesion base 

