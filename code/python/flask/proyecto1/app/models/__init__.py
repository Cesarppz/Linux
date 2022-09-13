from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy import create_engine



engine = create_engine('postgresql://postgres:c20022007@localhost:5432/api')
engine.execute("CREATE SCHEMA IF NOT EXISTS users;") #create db
#engine.execute("USE users;") # select new db


meta = MetaData(schema='users')
db = SQLAlchemy(metadata=meta)
