from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from base import Base


class Table(Base):
    __tablename__ = 'table'

    id = Column(Integer, primary_key=True)

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates="tables")

    # These tables belong to the restaurant
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))  # A table belong to one restaurant
    restaurant = relationship("Restaurant", back_populates="tables")

    # Every night a new restaurant table object
    night_id = Column(Integer, ForeignKey('night.id'))
    night = relationship("Night", uselist=False)  

    # Total number of seats available at this table
    num_seats = Column(Integer)

    def __init__(self, event, restaurant, num_seats, night):
        """

        :type event: object
        :type restaurant: object
        :type num_seats: int
        :type night: object
        """
        assert isinstance(event, object)
        assert isinstance(restaurant, object)
        assert isinstance(num_seats, int)
        assert isinstance(night, object)

        self.event = event
        self.restaurant = restaurant
        self.num_seats = num_seats
        self.night = night
