from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Float, String, DateTime

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)

    # Login credentials
    name = Column(String)
    password_hash = Column(String)

    # Profile settings
    today_departure = Column(DateTime)
    default_departure = Column(DateTime)
    billing_token = Column(String)

class Vehicle(Base)
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True)

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
