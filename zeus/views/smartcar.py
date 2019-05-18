import smartcar
import requests

from flask import Flask, request, jsonify
from zeus import app

CLIENT_ID = '52e8d23b-b296-4f8b-89a0-18b64fac4b38'
CLIENT_SECRET = '13a5b398-ebf1-433f-a82f-60a5224548d8'

client = smartcar.AuthClient(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri='http://localhost:5000/callback',
    scope=[
        'read_vehicle_info',
        'control_security',
        'read_charge',
        'read_battery',
    ]
)

@app.route('/auth', methods=['GET'])
def auth():
    auth_url = client.get_auth_url()
    return '''
        <h1>Get Started with Zeus ⚡!</h1>
        <h2>Optimizing EV charging queues.</h2>
        <a href={auth_url}>
          <button>Connect Car</button>
        </a>
    '''

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

    # Respond with a success status to browser
    return jsonify(status)
