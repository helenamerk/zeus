from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/db.sqlite"
db = SQLAlchemy(app)


#This is a weird circular dependency but the docs told me to do it :/
#http://flask.pocoo.org/docs/1.0/patterns/packages/#simple-packages
import zeus.views
