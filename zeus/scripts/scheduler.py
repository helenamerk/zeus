from zeus.utils.smartcar import smartcar
from zeus import db
from zeus.models.vehicle import Vehicle
from zeus.models.spot import Spot, SpotType

def main():
    for vehicle in db.session.query(Vehicle).filter(Vehicle.spot.has(type=SpotType.CHARGER.value)):
        print(vehicle)

if __name__ == "__main__":
    main();
