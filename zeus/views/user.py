from flask import render_template
from zeus import app

@app.route("/user/login", methods=['GET'])
def login_page():
    return render_template("user_login.html")

@app.route("/user/login", methods=['POST'])
def login_verify():
    """
    Verify the user's login credentials
    """
    pass

@app.route("/user/signup", methods=['GET'])
def signup_page():
    return render_template("user_signup.html")

@app.route("/user", methods=['POST'])
def create_user(user_id):
    pass

@app.route("/user/<int:user_id>", methods=['GET'])
def user_page(user_id):
    return render_template("user.html", user_id=user_id)

@app.route("/user/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    pass
