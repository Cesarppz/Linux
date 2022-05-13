from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from decouple import config


CLAVE_DB = config('clave_postgres')
engine = create_engine('postgresql://postgres:{clave}@localhost/test_sqlalchemy'.format(clave=CLAVE_DB))

# Ver si la base de datos existe
if not database_exists(engine.url):
    create_database(engine.url)


Session = sessionmaker(engine)


Base = declarative_base()