from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from passlib.apps import custom_app_context as pwd_context

from zeus import db

class User(db.Model):
    id = Column(Integer, primary_key=True)

    # Login credentials
    username = Column(String, index=True)
    password_hash = Column(String)
    vehicles = db.relationship('Vehicle', backref='user', lazy=True)

    # Profile settings
    billing_token = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password_hash = User.hash_password(password)

    @staticmethod
    def hash_password(password):
        return pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

