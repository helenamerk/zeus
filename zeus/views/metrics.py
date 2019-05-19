from datetime import datetime
from flask import render_template, request, redirect, url_for, abort
from zeus import app, db
from zeus.models.user import User
from zeus.models.vehicle import Vehicle
from zeus.models.spot import Spot
from zeus.utils.smartcar import client, smartcar
from datetime import datetime

@app.route("/metrics", methods=['GET'])
def metrics_dashboard():
    return render_template("metrics.html")
