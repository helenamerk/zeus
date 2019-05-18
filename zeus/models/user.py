from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey

from zeus import db

class User(db.Model):
    id = Column(Integer, primary_key=True)

    # Login credentials
    name = Column(String)
    password_hash = Column(String)

    # Profile settings
    today_departure = Column(DateTime)
    default_departure = Column(DateTime)
    billing_token = Column(String)
