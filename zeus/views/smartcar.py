import requests

from flask import Flask, request, jsonify, render_template
from zeus import app
from zeus.lib.smartcar import client


@app.route('/auth', methods=['GET'])
def auth():
    auth_url = client().get_auth_url()
    return render_template('connect_car.html', auth_url=auth_url)

def extended_sdk(vid, access_token, endpoint):
    url = 'https://api.smartcar.com/v1.0/vehicles/' + vid + '/' + endpoint
    headers = {"Authorization": "Bearer " + access_token}
    response = requests.get(url, headers=headers)

    return response.text


def init_vehicle_data(access):
    access_token = access['access_token']
    response = smartcar.get_vehicle_ids(access_token)
    vid = response['vehicles'][0]
    vehicle = smartcar.Vehicle(vid, access_token)

    charge = extended_sdk(vid, access_token, 'charge')
    battery = extended_sdk(vid, access_token, 'battery')

    info = vehicle.info()

    return {'vid': vid, 'info': info, 'charge': charge, 'battery': battery}

@app.route('/callback', methods=['GET'])
def callback():
    code = request.args.get('code')
    access = client.exchange_code(code)

    ##
    status = init_vehicle_data(access)

    # TODO: add vid to user db
    # TODO: store vid, info, charge, battery in vehicle db

    # Respond with a success status to browser
    return jsonify(status)
