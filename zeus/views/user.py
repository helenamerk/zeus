from flask import render_template
from zeus import app

@app.route("/user/<int:user_id>")
def show_user_page(user_id):
    return render_template("user.html", user_id=user_id)

