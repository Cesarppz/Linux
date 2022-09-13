class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:c20022007@localhost:5432/api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:c20022007@localhost:5432/api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'test':TestConfig,
    'development': DevelopmentConfig
}