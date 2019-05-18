from flask import Flask
app = Flask(__name__)

#This is a weird circular dependency but the docs told me to do it :/
#http://flask.pocoo.org/docs/1.0/patterns/packages/#simple-packages
import zeus.views
