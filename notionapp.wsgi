#!/usr/bin/python3
activate_this = '/var/www/NotionApp/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys, os

# To include the application's path in the Python search path
sys.path.insert(0,"/var/www/NotionApp/")

# Construct a Flask instance "app" via actual package's __init__.py
from NotionApp import app as application
app.debug = True
