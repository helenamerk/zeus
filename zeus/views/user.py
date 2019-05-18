from datetime import datetime
from flask import render_template, request, redirect, url_for, abort
from zeus import app, db
from zeus.models.user import User
from zeus.models.vehicle import Vehicle
from zeus.utils.smartcar import client, smartcar, get_battery, get_charge

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
    user = User.query.get(user_id)
    return render_template("user.html",
        vehicles=user.vehicles,
        auth_url=client.get_auth_url(state=user_id)
    )

@app.route("/user/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    pass


@app.route('/callback', methods=['GET'])
def callback():
    """
    Used on Smartcar OAuth redirect
    """
    code = request.args.get('code')
    user_id = request.args.get('state')
    access = client.exchange_code(code)
    access_token = access['access_token']

    vehicles = smartcar.get_vehicle_ids(access_token)['vehicles']
    vid = vehicles[0]

    info = smartcar.Vehicle(vid, access_token).info()
    vin = smartcar.Vehicle(vid, access_token).vin()

    battery = get_battery(vid, access_token)
    charge = get_charge(vid, access_token)

    new_vehicle = Vehicle(
        id=vid,
        user_id=user_id,
        vin=vin,
        make=info['make'],
        model=info['model'],
        year=info['year'],
        access_token=access['access_token'],
        access_expiration=access['expiration'],
        refresh_token=access['refresh_token'],
        percent_remaining=battery.percent_remaining,
        range=battery.range,
        charge_state=charge.state.value,
        is_plugged_in=charge.is_plugged_in
    )

    db.session.add(new_vehicle)
    db.session.commit()

    return redirect(url_for("user_page", user_id=user_id))
