import smartcar, requests

CLIENT_ID = '52e8d23b-b296-4f8b-89a0-18b64fac4b38'
CLIENT_SECRET = '13a5b398-ebf1-433f-a82f-60a5224548d8'

client = smartcar.AuthClient(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri='http://localhost:5000/callback',
    scope=[
        'read_vehicle_info',
        'read_vin',
        'read_charge',
        'read_battery',
        'control_security',
    ],
    test_mode=True
)

def smartcar_special_request(vid, access_token, endpoint):
    url = 'https://api.smartcar.com/v1.0/vehicles/' + vid + '/' + endpoint
    headers = {"Authorization": "Bearer " + access_token}
    response = requests.get(url, headers=headers)
    return response.json()

def get_battery(vid, access_token):
    return smartcar_special_request(vid, access_token, 'battery')

def get_charge(vid, access_token):
    return smartcar_special_request(vid, access_token, 'charge')

def smartcar_action_request(vid, access_token, action):
    url = 'https://api.smartcar.com/v1.0/vehicles/' + vid + '/' + endpoint
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    response = requests.post(url, headers=headers)
    payload = {"action": action}
    return response.json()

def lock(vid, access_token):
    return smartcar_action_request(vid, access_token, 'LOCK')

def unlock(vid, access_token):
    return smartcar_action_request(vid, access_token, 'UNLOCK')
