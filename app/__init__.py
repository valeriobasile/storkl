from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

# read configuration
app.config.from_object('config')

# create database
db = SQLAlchemy(app)

from app import views, models

if __name__ == '__main__':
    app.run(debug=True)
