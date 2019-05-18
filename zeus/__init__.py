from flask import Flask
app = Flask(__name__)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('./static', filename)

#This is a weird circular dependency but the docs told me to do it :/
#http://flask.pocoo.org/docs/1.0/patterns/packages/#simple-packages
import zeus.views
