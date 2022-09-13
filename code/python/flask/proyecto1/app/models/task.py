from . import db
from sqlalchemy.event import listen
from sqlalchemy import asc, desc

class Task(db.Model):
    __tablename__ = 'tasks'

    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(50), nullable=False)
    text        = db.Column(db.Text, nullable=False)
    deadline    = db.Column(db.DateTime(), nullable=False)
    created_at  = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    def __str__(self):
        return self.title

    
    def serialize(self):
        return {
            'id':self.id,
            'title':self.title,
            'Description':self.text,
            'deadline':self.deadline
        }

    
    @classmethod
    def new(cls, title, text, deadline):
        return Task(title=title, text=text, deadline=deadline)

    
    @classmethod
    def get_by_page(cls, page:int, order:str, per_page: int = 10):
        sort = asc(Task.id) if order == 'asc' else desc(Task.id)

        return Task.query.order_by(sort).paginate(page, per_page).items


    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True

        except:
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False


















# def insert_task(*args, **kwargs):
#     db.session.add(
#         Task(title='Title 1', text='Description 1', deadline='2019-12-12 12:00:00'), 

#     )

#     db.session.commit()

# listen(Task.__table__, 'after_create', insert_task)
