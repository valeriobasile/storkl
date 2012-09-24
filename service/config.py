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
   
# MySQL connetcion data (CHANGE THEM to suit your needs)
"mysql_username"        : "storklservice",
"mysql_password"        : "storklservice",
"mysql_host"            : "localhost",
"mysql_database"        : "storklservice",
}

