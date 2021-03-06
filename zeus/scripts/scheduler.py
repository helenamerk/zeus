from zeus.utils.smartcar import smartcar, get_battery, get_charge
from zeus import db
from zeus.models.vehicle import Vehicle
from zeus.models.spot import Spot, SpotType
from sqlalchemy import and_

class Queue:

    def __init__(self):
        self.queue = []

    def populate_queue(self):
        result = db.session.query(Vehicle).filter(Vehicle.needs_charging == True).order_by(
            Vehicle.departure_time, Vehicle.desired_range
        )
        # for vehicle in result:
        #     print('MAKE: ', vehicle.make)
        #     print('\t departure time: ', vehicle.departure_time)
        #     print('\t desired_range: ', vehicle.desired_range)

        for vehicle in result:
            # do not add to queue if vehicle is already in a charging spot
            res = Spot.query.filter(and_(Spot.vehicle_id == vehicle.id), (Spot.type==2)).all()
            print('CREATING QUEUE')
            print(res)
            if len(res) != 1:
                self.queue.append(vehicle)

        # print(self.queue)
        # return self.queue

    def pop(self):
        if not self.queue:
            return None
        return self.queue[0]


def retrieve_charge_status(vehicle):
    pass

if __name__ == "__main__":
    q = Queue()
    q.populate_queue()
    q.pop()


"""
queue = []
queue = db.query(Vehicle WHERE needs_charging=True ORDER BY departure_time ASC)
sorted_queue = queue.sort(queue, key=lambda x: x.desired_range)
"""
