from sqlalchemy import Column, Integer , String , Float , Text
from base import Base


class Article(Base):
    __tablename__= 'Newspaper'
    
    id        = Column(String(200),primary_key=True)
    body      = Column(Text())
    title     = Column(String(100))
    url       = Column(String(255),unique=True)
    host      = Column(String(60))
    num_title = Column(Integer)
    num_body  = Column(Integer)
    uid_site  = Column(String(60))
    

    def __init__(self,uid,body,title,url,host,num_title,num_body,uid_site):
        self.id=uid
        self.body=body
        self.title=title
        self.url=url
        self.host=host
        self.num_title=num_title
        self.num_body=num_body
        self.uid_site=uid_site