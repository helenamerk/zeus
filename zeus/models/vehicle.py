from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey

from zeus import db

class Vehicle(db.Model):

    id = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    # Static data
    vin = Column(String)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)

    # Smartcar access
    access_token = Column(String)
    access_expiration = Column(DateTime)
    refresh_token = Column(String)

    # Live updating
    percent_remaining = Column(Float)
    charge_status = Column(String)

    # Settings
    desired_range = Column(Integer)
