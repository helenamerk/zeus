from flask import render_template, redirect
from zeus import app
from zeus.models.vehicle import Vehicle
from zeus.utils.smartcar import smartcar

def identify_next_car():
    return {'id': '123123123', 'spot': '1101'}

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
    # TODO: 
    # get all ev spots
    # while spot == empty, ==> valet_next_car()
    #
    # elseif status >= threshold, make unlock button available
    # 
    # proceed to flow (unplug, unlock, move, lock) ==> leaves us with a vacant spot
    #
    # valet_next_car()
    emptySpots = []
    
    ### 
    # Valet dashboard should contain actions on top, and data on the bottom. 
    # Data: stats about the day, ie #s of vehs in each state
    # Actions: 
        # Button(s) to move vehicle out of charging spot
        # Button to start valet_next_car() process
    ###
    completedVehicles = []
    completedVehicles.append({'id': '12345', 'spot': '123'})
    completedVehicles.append({'id': '12346', 'spot': '222'})

    if len(emptySpots) > 0:
        nextCar = identify_next_car()

    return render_template("valet_dashboard.html", vehicles=completedVehicles, next_vehicle=nextCar)

@app.route("/valet/<int:vehicle_id>/unlock", methods=['POST'])
def valet_unlock(vehicle_id):
    # vehicle = Vehicle.query.get(vehicle_id)
    # smartcar.unlock(vehicle.id, vehicle.access_token)
    print('IMPLEMENT UNLOCKING HERE')
    # unlock vehicle id and drive
    return render_template("valet_driving.html", vehicle_id=vehicle_id)

@app.route("/valet/<int:vehicle_id>/lock", methods=['POST'])
def valet_lock(vehicle_id):
    # unlock vehicle id and drive
    # vehicle = Vehicle.query.get(vehicle_id)
    # smartcar.lock(vehicle.id, vehicle.access_token)

    print('IMPLEMENT LOCKING HERE')
    print('Record new state (NOT CHARGING) and new parking spot in db ')

    next_vehicle=valet_next_car()

    return redirect("/valet/dashboard")

@app.route("/valet/next", methods=['GET'])
def valet_next_car():
    """
    Calculate and return the next vehicle swap to the client
    """
    # calculate next car in queue
    # => proceed to flow (unlock, move, plug, lock)

    return render_template("valet_driving.html", vehicle=identify_next_car())
    
