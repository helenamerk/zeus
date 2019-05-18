from datetime import datetime
from flask import render_template, request, redirect, url_for, abort
from zeus import app, db
from zeus.models.user import User
from zeus.models.vehicle import Vehicle
from zeus.models.spot import Spot
from zeus.utils.smartcar import client, smartcar

@app.route("/vehicle/queue", methods=['POST'])
def queue_vehicle():
    form_data = request.form
    vehicle = Vehicle.query.get(form_data.getlist("selected_vehicle")[0])
    spot = Spot.query.get(form_data.getlist("parked_spot")[0])
    vehicle.spot = spot
    vehicle.desired_range = form_data.getlist("desired_range")[0]
    db.session.add(vehicle)
    db.session.add(spot)
    db.session.commit()
    return redirect("/vehicle/{}".format(vehicle.id))

@app.route('/vehicle/<vehicle_id>', methods=['GET'])
def vehicle(vehicle_id):
    print("C")
    return ""
