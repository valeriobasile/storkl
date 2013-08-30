from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restful
from sqlalchemy import create_engine
import os
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
api = restful.Api(app)

# create database
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storkl.db')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


from app import views, models

if __name__ == '__main__':
    app.run(debug=True)
