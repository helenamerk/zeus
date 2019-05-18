from zeus import app, db
from flask import render_template, request, redirect, url_for, abort
from zeus.models.vehicle import Vehicle
from zeus.models.spot import Spot
from datetime import datetime

@app.route("/vehicle/queue", methods=['POST'])
def update_vehicle():
    form_data = request.form
    vid = form_data['selected_vehicle']

    vehicle = db.session.query(Vehicle).filter_by(id=vid).first()
    vehicle.desired_range = form_data['desired_range'] 

    parsed = datetime.strptime(form_data['departure_time'], "%I:%M %p") 
    vehicle.departure_time = parsed
    db.session.commit()

    spot_id = form_data['parked_spot']
    spot = db.session.query(Spot).filter_by(id=spot_id).first()
    spot.vehicle_id = vid;
    db.session.commit()

    return "done"

