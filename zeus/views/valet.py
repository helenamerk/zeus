from flask import render_template, redirect
from zeus import app

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


    ### 
    # Valet dashboard should contain actions on top, and data on the bottom. 
    # Data: stats about the day, ie #s of vehs in each state
    # Actions: 
        # Button(s) to move vehicle out of charging spot
        # Button to start valet_next_car() process
    ###

    return render_template("valet_dashboard.html", vehicles=[{'spot': '123'}, {'spot': '222'}])

@app.route("/valet/next", methods=['GET'])
def valet_next_car():
    # calculate next car in queue
    # => proceed to flow (unlock, move, plug, lock)
    """
    Calculate and return the next vehicle swap to the client
    """
    pass
