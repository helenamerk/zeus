from datetime import datetime
from flask import render_template, request, redirect, url_for, abort
from zeus import app, db
from zeus.models.user import User

@app.route("/user/login", methods=['GET'])
def login_page():
    return render_template("user_login.html")

def verify_password(user, password):
    if not user or not user.verify_password(password):
        return False
    return True

@app.route("/user/login", methods=['POST'])
def login_verify():
    """
    Verify the user's login credentials
    """
    username = request.form.getlist("username")[0]
    password = request.form.getlist("password")[0]
    user = User.query.filter_by(username = username).first()
    if not verify_password(user, password):
        abort(403)
    return redirect(url_for("user_page", user_id=user.id))

@app.route("/user/signup", methods=['GET'])
def signup_page():
    return render_template("user_signup.html")

@app.route("/user", methods=['POST'])
def create_user():
    form_data = request.form
    new_user = User(username=form_data.getlist("username")[0], password=form_data.getlist("password")[0])
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("user_page", user_id=new_user.id))

@app.route("/user/<int:user_id>", methods=['GET'])
def user_page(user_id):
    return render_template("user.html", user_id=user_id)

@app.route("/user/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    pass
