from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

from base import Base


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)

    pax = relationship("Pax", backref="events")
    reservations = relationship("Reservation", backref="events")

    restaurants = relationship("Restaurant", backref="events")
    tables = relationship("Table", backlog="events")

    slots = relationships("Slot", backref="events")
    days = relationship("Days", backref="events")

    num_nights = Column(Integer)
    num_restaurants = Column(Integer)
    active = Column(Boolean)

    def __init__(self, num_nights, num_restaurants):
        """

        :type num_nights: int
        :type num_restaurants: int
        """
        assert isinstance(num_nights, int)
        self.num_nights = num_nights

        assert isinstance(num_restaurants, int)
        self.num_restaurants = num_restaurants
