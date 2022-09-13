from base import create_database
import os

class Config():
    SECRET_KEY = 'My_secret_key'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587 
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'cesararturo20027@gmail.com'
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

class DeveloperConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:c20022007@localhost:5432/flask?options=-c%20search_path=flask_schema'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # __url_base = 'postgresql://postgres:c20022007@localhost:5432/flask'
    # __schema_name = 'flask_schema'

    # def start_db(self):
    #     Base, engine = create_database(self.__url_base, self.__schema_name)
    #     return Base, engine