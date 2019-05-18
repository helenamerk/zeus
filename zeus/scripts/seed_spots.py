from zeus import db
from zeus.models.spot import Spot, SpotType

def create_spots(count, chargers):
    spots = [Spot(type=SpotType.CHARGER.value) for i in range(chargers)]
    for spot in spots:
        db.session.add(spot)
        db.session.commit()

    spots = [Spot(type=SpotType.STANDARD.value) for i in range(count-chargers)]
    for spot in spots:
        db.session.add(spot)
        db.session.commit()

if __name__ == "__main__":
    create_spots(50, 10)
