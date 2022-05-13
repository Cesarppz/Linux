#! /home/cesarppz/anaconda3/envs/ia/bin/python3
from datetime import datetime

from base import Base, Session, engine
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import exists
from sqlalchemy.sql.expression import and_


class User(Base):
    __tablename__ = 'users'

    id         = Column(Integer(), primary_key=True)
    username   = Column(String(50), nullable=False, unique=True)
    email      = Column(String(50), unique=True)
    password   = Column(String(20),nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
    courses    = relationship('Course', backref='user')


    def __init__(self,username,email,password,id=None,created_at=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at

    def __str__(self) -> str:
        return f'User Name: {self.username}, Email: {self.email}'


class Course(Base):
    __tablename__ = 'courses'

    id      = Column(Integer(), primary_key= True)
    title   = Column(Text(), nullable=False)
    user_id = Column(ForeignKey('users.id'))

    def __init__(self, title, user_id=None):
        self.title = title
        self.user_id = user_id

    
    def __str__(self):
        return self.title


if __name__ == '__main__':

    session = Session()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    new_users = [User('user1','prueba@gmail.com','password1'),
                 User('user2','prueba2@gmail.com','password2'),
                 User('user3','prueba3@gmail.com','password3'),
                 User('user4','prueba4@gmail.com','password4'),
                 User('user5','prueba5@gmail.com','password5'),
                 User('user6','prueba6@gmail.com','password6')]

    # Add if not exist
    for user in new_users:
        if not session.query(exists().where(User.username==user.username)).scalar():
            session.add(user)
            session.commit()

    new_courses = [
        Course('Curso de Pyhton',2),
        Course('Curso de Pandas para python',4),
        Course('Curso de Pandas para python',6)

    ]

    for course in new_courses:
        if not session.query(exists().where(and_(Course.user_id==course.user_id, Course.title==course.title))).scalar():
            session.add(course)
            session.commit()


    # Otra manera de add un curso
    # user8 = User('user8','prueba8@gmail.com','password8')
    # user8.courses.append(Course('Curso de Java',user8.id))
    # session.add(user8)
    # session.commit()

    #Select 
    # users = session.query(User).filter(
    #     User.id >= 2
    # )

    users = session.query(User).all()

    for user in users:
        if user.courses:
            for course in user.courses:
                print(user,'Curso:',course.title)

    courses = session.query(Course).all()
    for course in courses:
        print(course, course.user.username)



    # Joins

    #Inner
    users = session.query(User).join(
        Course #, User.id == Course.user.id 
    )
    

    #Left 
    users = session.query(User).outerjoin(
        Course
    )

    
    print('Joins')
    for user in users:
        print(user)

