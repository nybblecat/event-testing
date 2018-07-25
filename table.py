from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from base import Base


class Table(Base):
    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True)

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates="tables", uselist=False)

    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))  # A table belong to one restaurant
    restaurant = relationship("Restaurant", back_populates="tables", uselist=False)

    day_id = Column(Integer, ForeignKey('days.id'))
    day = relationship("Days", back_populates="tables", uselist=False)  # Every day a new table object

    seats = Column(Integer)  # Number of seats at the table

    def __init__(self, restaurant, seats, day):
        """

        :type event: object
        :type restaurant: object
        :type seats: int
        :type day: object
        """
        assert isinstance(event, object)
        assert isinstance(restaurant, object)
        assert isinstance(seats, int)
        assert isinstance(day, object)

        self.event = event
        self.restaurant = restaurant
        self.seats = seats
        self.day = day