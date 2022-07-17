from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    username = Column(String)
    picture = Column(String)
    country = Column(String)
    bio = Column(String)
    papers = relationship('Paper', backref='authors')


class Paper(Base):
    __tablename__ = 'papers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    picture = Column(String)
    category = Column(String)
    language = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    synopsis = Column(String)

