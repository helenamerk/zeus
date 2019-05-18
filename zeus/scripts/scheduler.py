from zeus.utils.smartcar import smartcar, get_battery, get_charge
from zeus import db
from zeus.models.vehicle import Vehicle
from zeus.models.spot import Spot, SpotType

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
            self.queue.append(vehicle)

        # print(self.queue)
        # return self.queue

    def pop(self):
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
