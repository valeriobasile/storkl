# config.py
# StorkL configuration file

config = {

# SMTP server (user to send email confirmation/activation)
"smtp_server"           : "localhost",

"activation_sender"     : "Storkl <valerio@storkl.net>",

"activation_subject"    : "Welcome to StorkL",

"activation_body" : 

"""Your activation is one click away.
The activation code is {0}""",
   
#  
"db_sqlite"             : "storkl.db",
}

