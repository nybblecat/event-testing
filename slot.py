from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from base import Base


class Slot(Base):
    __tablename__ = 'slots'

    id = Column(Integer, primary_key=True)

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates="slots", uselist=False)

    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))  # Each restaurant has its own time slots
    restaurant = relationship("Restaurant", back_populates="slots", uselist=False)

    day_id = Column(Integer, ForeignKey('days.id'))  # Each time slot occurs on a single day
    day = relationship("Day", back_populates="slots", uselist=False)

    length = Column(Integer)  # Length of time of slot in minutes

    def __init__(self, event, restaurant, day, length):
        """

        :type event: object
        :type restaurant: object
        :type day: object
        :type length: object
        """
        assert isinstance(event, object)
        assert isinstance(restaurant, object)
        assert isinstance(day, object)
        assert isinstance(length, int)

        self.event = event
        self.restaurant = restaurant
        self.day = day
        self.length = length
