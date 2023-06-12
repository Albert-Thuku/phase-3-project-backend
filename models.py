from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref, sessionmaker, declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine('sqlite:///project.db', connect_args={'check_same_thread':False})

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    password = Column(String(8))

    destinations = association_proxy('users_destinations', 'destinations', creator=lambda ds: Users_Destinations(destinations=ds))
    users_destinations = relationship('Users_Destinations',back_populates='user', cascade='all, delete-orphan')

class Destinations(Base):
    __tablename__ = 'destinations'
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    image = Column(String())
    description = Column(String())
    category = Column(String())
    location = Column(String())
    visit_url = Column(String())

    users = association_proxy('users_destinations', 'users', creator=lambda us: Users_Destinations(users=us))
    users_destinations = relationship('Users_Destinations',back_populates='destination', cascade='all, delete-orphan')

class Users_Destinations(Base):
    __tablename__='users_destinations'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    destination_id = Column(Integer(), ForeignKey('destinations.id'))

    user = relationship('Users', back_populates='users_destinations')
    destination = relationship('Destinations', back_populates='users_destinations')

Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()