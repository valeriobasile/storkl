# model.py
# model definition

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Boolean, MetaData, ForeignKey
from sqlalchemy.orm import relation
from database import *

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    username = Column(String(100), primary_key=True)
    password = Column(String(100))
    email = Column(String(100))
    active = Column(Boolean)
    activation = Column(String(256))

    def __init__(self, username, password, email, active, activation):
        self.username = username
        self.password = password
        self.email = email
        self.active = active
        self.activation = activation

    def __repr__(self):
       return "User '{0}','{1}'".format(self.username, self.email)


class UserSession(Base):
    __tablename__ = 'user_sessions'

    user_id = Column(String(100), ForeignKey('users.username'))
    user = relation(User)
    session_token = Column(String(256), primary_key=True)
    timestamp = Column(Integer)

    def __init__(self, username, session_token, timestamp):
        self.user = session.query(User).filter(User.username==username).one()
        self.session_token = session_token
        self.timestamp = int(timestamp)


