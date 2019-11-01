#!/usr/bin/python3
import sys, os

# To include the application's path in the Python search path
sys.path.insert(0,"/var/www/NotionApp/")

# Construct a Flask instance "app" via actual package's __init__.py
from NotionApp import app as application