# service.py
# StorKl Webservice, views

import web
import simplejson as json
from pymongo import Connection
import bcrypt
import base64
import time
import os
import smtplib

# TODO move to configuration file
config = dict()
config["smtp_server"] = "localhost"
config["activation_sender"] = "Storkl <valerio@storkl.net>"
config["activation_subject"] = "Welcome to StorkL"
config["activation_body"] = """Your activation is one click away.
    The activation code is {0}"""

connection = Connection()
db = connection.storkl

urls = (
    '/auth',        'auth',
    '/register',    'register',
    '/activate',    'activate',
    '/',            'dashboard',
    '/dashboard',   'dashboard',
    '/projects',    'projects',
    '/involvement', 'involvement',
    '/p/(.*)',        'project',
    '/p/(.*)/(.*)',   'task',
    '/trust',       'trust',
)

def activation_email(recipient, activation):
    email = """From: {0}
To: {1}
Subject: {2}

{3}""".format(config["activation_sender"], 
    recipient, config["activation_subject"], 
    config["activation_body"].format(activation))
    
    server = smtplib.SMTP(config["smtp_server"])
    server.sendmail(config["activation_sender"], [recipient], email)
    server.quit()

# POST: username, password, email
# return: -
class register:
    def POST(self):
        i = web.input()
        
        errors = []
        if db.users.find({"email":i.email}).count() > 0:
            errors.append("there is already a registered user with this email")
        if db.users.find({"username":i.username}).count() > 0:
            errors.append("username already in use")
        
        if len(errors) == 0:
            activation = base64.b64encode(os.urandom(16))
            response = {
                "success":True,
                "response":{}
            }
            db.users.insert({
                "username":i.username,
                "email":i.email,
                "password":bcrypt.hashpw(i.password, bcrypt.gensalt()),
                "activation":activation,
                "active":False,
            })
            activation_email(i.email,activation)
        else:
            response = {
                "success":False,
                "errors":errors
            }
            
        web.header('Content-Type', 'application/json')
        return json.dumps(response)

# POST: activation token
# return: -
class activate:
    def POST(self):
        i = web.input()
        
        errors = []
        if db.users.find({"activation":i.activation}).count() == 0:
            errors.append("invalid activation code")
        else:
            user = db.users.find_one({"activation":i.activation})
            
        if len(errors) == 0:
            response = {
                "success":True,
                "response":{}
            }
            user["active"]=True
            db.users.save(user)
        else:
            response = {
                "success":False,
                "errors":errors
            }
            
        web.header('Content-Type', 'application/json')
        return json.dumps(response)


# POST: username, password
# return: session id
class auth:
    def POST(self):
        i = web.input()
        
        errors = []
        if db.users.find({"username":i.username}).count() == 0:
            errors.append("username not found")
        else:
            user = db.users.find_one({"username":i.username})
            hashed = bcrypt.hashpw(i.password, bcrypt.gensalt())
            print user["active"]
            if bcrypt.hashpw(i.password, hashed) != hashed:
                errors.append("incorrect password")
            if not user["active"]:
                errors.append("user not active")
                
        if len(errors) == 0:
            session = base64.b64encode(os.urandom(16))
            timestamp = time.time()
            response = {
                "success":True,
                "response":{
                    "session":session,
                    "timestamp":timestamp,
                }
            }
            db.sessions.insert({
                "user":user["username"],
                "session":session,
                "timestamp":timestamp,
            })
        else:
            response = {
                "success":False,
                "errors":errors
            }
            
        web.header('Content-Type', 'application/json')
        return json.dumps(response)
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
