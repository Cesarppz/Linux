from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import CreateSchema
from sqlalchemy_utils import database_exists, create_database


def create_database(url_base, schema_name):
    Base = declarative_base()
    Base.metadata.schema = schema_name

    engine = create_engine(url_base)

    if not engine.dialect.has_schema(engine, schema_name):
        engine.execute(CreateSchema(schema_name))

    if not database_exists(engine.url):
        create_database(engine.url)

    return Base, engine

    