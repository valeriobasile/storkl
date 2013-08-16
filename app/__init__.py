from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# read configuration
app.config.from_object('config')

# create database
db = SQLAlchemy(app)

from app import views, models


