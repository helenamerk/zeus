import requests
import json

action_map = {
    'LOCK': 'Your vehicle was sent a lock request.',
    'UNLOCK': 'Your vehicle was sent an unlock request',
    'TIGHT_TIME':'Heads up! You may not receive a full charge today.',
    'SELECTED':'Your car just got queued up!',
    'CAPACITY': 'Your car is at or past requested capacity.',
    'OTHER':'ALERT :)',
}

def notify_action(action, vehicleId):
    message = action_map[action]
    header = {"Content-Type": "application/json; charset=utf-8",
            "Authorization": "Basic ZDNjYzhkMWItOTRjMi00ZDQyLTlmMzEtYmJlYWE3N2I3NTlh"}

    payload = {"app_id": "5c739c73-c07c-419d-8b7e-792d15849bd5",
           "filters": [
			  	{"field": "tag", "key": "vehicleId", "relation": "=", "value": vehicleId}
			],
            "contents": {"en": message}}
    
    req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
    print('--------------------')
    print(req.status_code, req.reason)