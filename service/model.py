# model.py
# model definition

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Boolean, Text, MetaData, ForeignKey
from sqlalchemy.orm import relation
from database import *

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id          = Column(Integer, primary_key=True)
    username    = Column(String(20))
    password    = Column(String(256))
    email       = Column(String(50))
    active      = Column(Boolean)
    activation  = Column(String(256))
    session_token = Column(String(256))
    session_timestamp = Column(Integer)
    projects = relation("Project", backref="owner")
    
    def __init__(self, username, password, email, active, activation):
        self.username = username
        self.password = password
        self.email = email
        self.active = active
        self.activation = activation

    def __repr__(self):
       return "User '{0}','{1}'".format(self.username, self.email)

class Project(Base):
    __tablename__ = 'projects'

    id          = Column(Integer, primary_key=True)
    owner_id       = Column(Integer, ForeignKey('users.id'))
    name        = Column(String(50))
    description = Column(Text)
    
    def __init__(self, owner, name, description):
        self.id = id
        self.owner = session.query(User).filter(User.id==owner).one()
        self.name = name
        self.description = description

    def __repr__(self):
       return "User '{0}'".format(self.name)

