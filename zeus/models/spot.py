from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey

from zeus import db
from enum import Enum

class Spot(db.Model):

    id = Column(Integer, primary_key=True)

    type = Column(Integer)
    vehicle_id = Column(String, ForeignKey('vehicle.id'), nullable=True)

class SpotType(Enum):
    STANDARD = 1
    CHARGER = 2
