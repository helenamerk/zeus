from flask import render_template
from zeus import app

@app.route("/valet/login", methods=['GET'])
def valet_login_page():
    return render_template("valet_login.html")

@app.route("/valet/login", methods=['POST'])
def valet_login_verify():
    """
    Verify the valet's login credentials
    """
    pass

@app.route("/valet/dashboard", methods=['GET'])
def valet_page():
    return render_template("valet.html")
