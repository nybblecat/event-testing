from datetime import date

from sqlalchemy import Column, String, Integer, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship

from base import Base


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)

    pax = relationship("Pax", back_populates="event")
    groups = relationship("Group", back_populates="event")
    
    nights = relationship("Night", back_populates="event")
    tables = relationship("Table", back_populates="event")
    slots = relationship("Slot", back_populates="event")
    reservations = relationship("Reservation", back_populates="event")

    restaurants = relationship("Restaurant", back_populates="event")
    start_date = Column(Date)
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

    def create_reservation(self, group, table, slot):
        """

        :type group: object
        :type table: object
        :type slot: object
        """
        assert isinstance(group, object)
        assert isinstance(table, object)
        assert isinstance(slot, object)

        # If a reservation already exists, we can't make a new one here.
        if group.get_reservation():
            return False

        # Check for enough free seats to accommodate the group
        assert (table.get_seats_free(slot) >= len(group))

        reservation = Reservation(self, group, table, slot, 
            date(2018, 7, 26), 1, True)

        self.reservations.append(reservation)