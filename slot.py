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

    night_id = Column(Integer, ForeignKey('night.id'))  # Time slots are one night only
    night = relationship("Night")

    slot_length = Column(Integer)  # Length of time of slot in minutes

    def __init__(self, event, restaurant, night, length):
        """

        :type event: object
        :type restaurant: object
        :type night: object
        :type length: int (minutes)
        """
        assert isinstance(event, object)
        assert isinstance(restaurant, object)
        assert isinstance(night, object)
        assert isinstance(length, int)

        self.event = event
        self.restaurant = restaurant
        self.night = night
        self.slot_length = length
