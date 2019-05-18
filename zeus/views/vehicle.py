from datetime import datetime
from flask import render_template, request, redirect, url_for, abort
from zeus import app, db
from zeus.models.user import User
from zeus.models.vehicle import Vehicle
from zeus.models.spot import Spot
from zeus.utils.smartcar import client, smartcar
from datetime import datetime

@app.route("/vehicle/queue", methods=['POST'])
def queue_vehicle():
    form_data = request.form
    vehicle = Vehicle.query.get(form_data.getlist("selected_vehicle")[0])
    spot = Spot.query.get(form_data.getlist("parked_spot")[0])
    vehicle.spot = spot
    vehicle.desired_range = form_data.getlist("desired_range")[0]
    parsed = datetime.strptime(form_data['departure_time'], "%I:%M %p")
    vehicle.departure_time = parsed
    db.session.add(vehicle)
    db.session.add(spot)
    db.session.commit()
    return redirect("/vehicle/{}".format(vehicle.id))

@app.route('/vehicle/<vehicle_id>', methods=['GET'])
def vehicle(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id).refresh()
    return render_template("vehicle.html", vehicle=vehicle)
