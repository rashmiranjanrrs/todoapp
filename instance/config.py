# Initialize your database here and it shld only return an instance
# of the database

import os

SQLALCHEMY_DATABASE_URI = 'mysql://root:passwor@localhost/root'
                           #mysql://username:password@server/database_name
SQLALCHEMY_TRACK_MODIFICATIONS = True
