import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id          = db.Column(db.Integer, primary_key= True)
    name        = db.Column(db.String(50), nullable=False, unique=True)
    email       = db.Column(db.String(50), unique=True)
    password    = db.Column(db.String(102), nullable=False)
    comment     = db.relationship('Comment')
    created_at  = db.Column(db.DateTime(), default=datetime.datetime.now())

    def __init__(self, name, password, email):
        self.name = name
        self.email = email
        self.password = self.__encrip_password(password)
    
    def __encrip_password(self, password):
        password = generate_password_hash(password)
        return password

    
    def verify_password(self, password):
        return check_password_hash(self.password, password)

class Comment(db.Model):
    __tablename__ = 'comments'

    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment     = db.Column(db.Text())
    created_at  = db.Column(db.DateTime(), default=datetime.datetime.now())

    def __init__(self,user_id,comment):
        self.user_id = user_id
        self.comment = comment
