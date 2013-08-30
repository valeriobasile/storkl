from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restful
from sqlalchemy import create_engine
import os


app = Flask(__name__)
api = restful.Api(app)

# create database
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storkl.db')
db = SQLAlchemy(app)
engine = create_engine(SQLALCHEMY_DATABASE_URI)

from app import views, models

if __name__ == '__main__':
    app.run(debug=True)
