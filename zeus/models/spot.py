from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey

from zeus import db

class Spot(db.Model):

    id = Column(Integer, primary_key=True)

    type = Column(String)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)
