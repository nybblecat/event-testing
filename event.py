from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from base import Base


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)

    pax = relationship("Pax", back_populates="event", uselist=False)
    groups = relationship("Group", back_populates="event", uselist=False)
    reservations = relationship("Reservation", back_populates="event", uselist=False)

    restaurants = relationship("Restaurant", back_populates="event", uselist=False)
    tables = relationship("Table", back_populates="event", uselist=False)

    slots = relationship("Slot", back_populates="event", uselist=False)
    days = relationship("Day", back_populates="event", uselist=False)

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
