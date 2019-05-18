from sqlalchemy import Boolean, Column, Integer, Float, String, DateTime, ForeignKey

from zeus import db
from zeus.utils.smartcar import (
    client, AccessTokens, maybe_get_fresh_access_tokens,
    get_battery, get_charge, ChargingState
)

class Vehicle(db.Model):

    id = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    spot = db.relationship('Spot', uselist=False, backref='vehicle', lazy=True)

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
    range = Column(Float)
    charge_state = Column(Integer)
    is_plugged_in = Column(Boolean)


    # Settings
    desired_range = Column(Integer)
    departure_time = Column(DateTime)

    def is_queued(self):
        return self.spot is not null and not self.is_plugged_in

    def is_charging(self):
        return self.spot is not null and self.is_plugged_in

    def access_tokens(self):
        return AccessTokens(
            token=self.access_token,
            expiration=self.access_expiration,
            refresh=self.refresh_token
        )

    def refresh(self):
        access_tokens = maybe_get_fresh_access_tokens(self.access_tokens())
        battery = get_battery(self.id, access_tokens.token)
        charge = get_charge(self.id, access_tokens.token)

        self.access_token = access_tokens.token
        self.access_expiration = access_tokens.expiration
        self.refresh_token = access_tokens.refresh

        self.percent_remaining = battery.percent_remaining
        self.range = battery.range
        self.charge_state = charge.state.value
        self.is_plugged_in = charge.is_plugged_in
        db.session.add(self)
        db.session.commit()
        return self

    def charging_description(self):
        if self.charge_state == ChargingState.FULLY_CHARGED.value:
            return "Fully Charged"
        if self.charge_state == ChargingState.CHARGING.value:
            return "Charging"
        if self.charge_state == ChargingState.NOT_CHARGING.value:
            return "Not Charging"
        return "Possible Error"

