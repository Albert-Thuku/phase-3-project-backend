from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref, sessionmaker, declarative_base

engine = create_engine('sqlite:///project.db')

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    password = Column(String(8))

    destinations = relationship('Destinations', backref = backref('user'), cascade = 'all, delete-orphan')

class Destinations(Base):
    __tablename__ = 'destinations'
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    image = Column(String())
    description = Column(String())
    location = Column(String())
    visit_url = Column(String())
    interested = Column(Boolean())
    user_id = Column(Integer(), ForeignKey('users.id'))

Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()