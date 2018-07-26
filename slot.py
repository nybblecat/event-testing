from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from base import Base


class Slot(Base):
    __tablename__ = 'slot'

    id = Column(Integer, primary_key=True)

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates="slots")

    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))  # Each restaurant has its own time slots
    restaurant = relationship("Restaurant", back_populates="slots")

    day_id = Column(Integer, ForeignKey('day.id'))  # Each time slot occurs on a single day
    day = relationship("Day")

    length = Column(Integer)  # Length of time of slot in minutes

    def __init__(self, event, restaurant, day, length):
        """

        :type event: object
        :type restaurant: object
        :type day: object
        :type length: int (minutes)
        """
        assert isinstance(event, object)
        assert isinstance(restaurant, object)
        assert isinstance(day, object)
        assert isinstance(length, int)

        self.event = event
        self.restaurant = restaurant
        self.day = day
        self.length = length
