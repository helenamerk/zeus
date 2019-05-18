import smartcar

from zeus.lib.util import memoized

@memoized
def client():
    CLIENT_ID = '52e8d23b-b296-4f8b-89a0-18b64fac4b38'
    CLIENT_SECRET = '13a5b398-ebf1-433f-a82f-60a5224548d8'

    return smartcar.AuthClient(
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

