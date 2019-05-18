from zeus.utils.smartcar import smartcar, get_battery, get_charge
from zeus import db
from zeus.models.vehicle import Vehicle
from zeus.models.spot import Spot, SpotType

def get_vehicles_in_chargers():
    return [vehicle for vehicle in db.session.query(Vehicle).filter(Vehicle.spot.has(type=SpotType.CHARGER.value))]

def retrieve_charge_status(vehicle):
    pass

if __name__ == "__main__":
    print(get_vehicles_in_chargers())
