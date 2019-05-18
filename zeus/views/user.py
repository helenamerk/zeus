from datetime import datetime
from flask import render_template, request, redirect, url_for
from zeus import app, db
from zeus.models.user import User

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
def create_user():
    data = request.get_json(force=True)
    data["today_departure"] = datetime.fromtimestamp(data["today_departure"])
    data["default_departure"] = datetime.fromtimestamp(data["default_departure"])
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("user_page", user_id=new_user.id))

@app.route("/user/<int:user_id>", methods=['GET'])
def user_page(user_id):
    return render_template("user.html", user_id=user_id)

@app.route("/user/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    pass
