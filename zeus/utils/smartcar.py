from enum import Enum
from collections import namedtuple

import requests
import smartcar

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

class ChargingState(Enum):
    FULLY_CHARGED = 1
    CHARGING = 2
    NOT_CHARGING = 3

ChargingStatus = namedtuple('ChargingStatus', ['state', 'is_plugged_in'])
BatteryStatus = namedtuple('BatteryStatus', ['range', 'percent_remaining'])
AccessTokens = namedtuple('AccessTokens', ['token', 'expiration', 'refresh'])

def smartcar_special_request(vid, access_token, endpoint):
    url = 'https://api.smartcar.com/v1.0/vehicles/' + vid + '/' + endpoint
    headers = {"Authorization": "Bearer " + access_token}
    response = requests.get(url, headers=headers)
    return response.json()

def get_battery(vid, access_token):
    response = smartcar_special_request(vid, access_token, 'battery')
    print(response)
    return BatteryStatus(range=response['range'], percent_remaining=response['percentRemaining'])

def get_charge(vid, access_token):
    response = smartcar_special_request(vid, access_token, 'charge')
    return ChargingStatus(state=ChargingState[response['state']], is_plugged_in=response['isPluggedIn'])

def smartcar_action_request(vid, access_token, action):
    url = 'https://api.smartcar.com/v1.0/vehicles/' + vid + '/security'
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    response = requests.post(url, headers=headers)
    payload = {"action": action}
    return response.json()

def lock(vid, access_token):
    return smartcar_action_request(vid, access_token, 'LOCK')

def unlock(vid, access_token):
    return smartcar_action_request(vid, access_token, 'UNLOCK')

def maybe_get_fresh_access_tokens(access_tokens):
    if smartcar.is_expired(access_tokens.expiration):
        new_access = client.exchange_refresh_token(access_tokens.refresh)
        return AccessTokens(
            token=new_access['access_token'],
            expiration=new_access['expiration'],
            refresh=new_access['refresh_token']
        )
    else:
        return access_tokens
