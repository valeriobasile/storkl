# database.py
#
# setup database connection

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import *

engine = create_engine('mysql://{0}:{1}@{2}/storklservice'.format(
    config["mysql_username"], 
    config["mysql_password"], 
    config["mysql_host"], 
    config["mysql_database"]
), echo=True)
Session = sessionmaker(bind=engine)
session = Session()
