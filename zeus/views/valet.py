from flask import render_template, redirect
from zeus import app, db
from zeus.models.vehicle import Vehicle
from zeus.utils.smartcar import smartcar, lock, unlock, get_battery
from zeus.utils.onesignal import notify_action
from zeus.models.spot import Spot, SpotType
from sqlalchemy import and_
from zeus.scripts.scheduler import Queue


def identify_next_car():

    q = Queue()
    q.populate_queue()
    vehicle = q.pop()
    return {
        'id': vehicle.id,
        'spot': vehicle.spot.type
    }

def check_threshold(busy_ev_spots):
    completedVehicles = []
    print('Vehicles that are busy:')
    print(busy_ev_spots)
    for spot in busy_ev_spots:
        vehicle = Vehicle.query.filter_by(id=spot.vehicle_id).first()
        vehicle = Vehicle.query.get(spot.vehicle_id)
        battery = get_battery(vehicle.id, vehicle.access_token)
        print(battery)
        if (battery.range > vehicle.desired_range):
            print(vehicle.id + ' is beyond the requested range :)')
            completedVehicles.append(vehicle)
            notify_action('CAPACITY', spot.vehicle_id)

    return completedVehicles

@app.route("/valet/login", methods=['GET'])
def valet_login_page():
    return render_template("valet_login.html")

@app.route("/valet/login", methods=['POST'])
def valet_login_verify():
    """
    Verify the valet's login credentials 
    """
    return redirect('dashboard')

@app.route("/valet/dashboard", methods=['GET'])
def valet_page():
    # if we have empty spots, bring up next vehicle from queue!
    nextCar = None
    open_ev_spots = Spot.query.filter_by(vehicle_id=None, type=2).all()
    if len(open_ev_spots) > 0:
        nextCar = identify_next_car()
    print(open_ev_spots)

    count_ev_spots = len(open_ev_spots)

    # check all current chargers if vehicle has reached requested mileage   
    busy_ev_spots = Spot.query.filter(and_(Spot.vehicle_id.isnot(None)), (Spot.type==2)).all()
    print(busy_ev_spots)

    completedVehicles = check_threshold(busy_ev_spots)
    

    return render_template("valet_dashboard.html", open_ev_spots=count_ev_spots, vehicles=completedVehicles, next_vehicle=nextCar)

@app.route("/valet/<string:vehicle_id>/unlock", methods=['POST'])
def valet_unlock(vehicle_id):
    notify_action('UNLOCK', vehicle_id)

    vehicle = Vehicle.query.get(vehicle_id)
    unlock(vehicle.id, vehicle.access_token)
    print('IMPLEMENT UNLOCKING HERE')
    # unlock vehicle id and drive
    return render_template("valet_driving.html", vehicle_id=vehicle_id)

@app.route("/valet/<string:vehicle_id>/lock", methods=['POST'])
def valet_lock(vehicle_id):
    notify_action('LOCK', vehicle_id)
    
    # unlock vehicle id and drive
    vehicle = Vehicle.query.get(vehicle_id)
    lock(vehicle.id, vehicle.access_token)

    print('TODO: Record new state (NOT CHARGING) and new parking spot in db ')

    next_vehicle=valet_next_car()

    return redirect("/valet/dashboard")

@app.route("/valet/next", methods=['GET'])
def valet_next_car():
    """
    Calculate and return the next vehicle swap to the client
    """
    nextCar = identify_next_car()
    notify_action('SELECTED', nextCar['id'])
    # calculate next car in queue
    # => proceed to flow (unlock, move, plug, lock)

    return render_template("valet_driving.html", vehicle=nextCar)
    
