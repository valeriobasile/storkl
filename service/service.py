# service.py
# StorKl Webservice, views

import web
import simplejson as json
import bcrypt
import base64
import time
import os
import smtplib
from config import *
from model import *
from database import *

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
    #server.sendmail(config["activation_sender"], [recipient], email)
    print(email)
    server.quit()

# User registration
#
# POST: username, password, email
# return: -
class register:
    def POST(self):
        i = web.input()
        
        errors = []
        if session.query(User).filter(User.email==i.email).count() > 0:
            errors.append("there is already a registered user with this email")
        if session.query(User).filter(User.username==i.username).count() > 0:
            errors.append("username already in use")
        
        if len(errors) == 0:
            activation = base64.b64encode(os.urandom(16))
            response = {
                "success":True,
                "response":{}
            }
            # create User object
            user = User(
                username = i.username, 
                password = bcrypt.hashpw(i.password, bcrypt.gensalt()),
                email = i.email, 
                active = False,
                activation = activation,
            )
            session.add(user)
            session.commit()

            activation_email(i.email,activation)
        else:
            response = {
                "success":False,
                "errors":errors
            }
            
        web.header('Content-Type', 'application/json')
        return json.dumps(response)

# user activation
#
# POST: activation token
# return: -
class activate:
    def POST(self):
        i = web.input()
        
        errors = []
        user_query = session.query(User).filter(User.activation==i.activation)
        if user_query.count() == 0:
            errors.append("invalid activation code")
        else:
            user = user_query.one()
            
        if len(errors) == 0:
            response = {
                "success":True,
                "response":{}
            }
            user.active=True
            session.commit()
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
        user_query = session.query(User).filter(User.username==i.username)
        if user_query.count() == 0:
            errors.append("username not found")
        else:
            user = user_query.one()
            print bcrypt.hashpw(i.password, user.password),user.password
            if bcrypt.hashpw(i.password, user.password) != user.password:
                errors.append("incorrect password")
            elif not user.active:
                errors.append("user not active")
                
        if len(errors) == 0:
            session_token = base64.b64encode(os.urandom(16))
            timestamp = time.time()
            response = {
                "success":True,
                "response":{
                    "session":session_token,
                    "timestamp":timestamp,
                }
            }
            user_session = UserSession(
                username = i.username, 
                session_token = session_token,
                timestamp = timestamp,
            )
            session.add(user_session)
            session.commit()
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
