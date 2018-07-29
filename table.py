from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

#from base import Base
#below imports & queries will need to be moved to a separate file

from base import Session, engine, Base
from reservation import Reservation


class Table(Base):
    __tablename__ = 'table'

    id = Column(Integer, primary_key=True)

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates="tables", uselist=False)

    # These tables belong to the restaurant
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))  # A table belong to one restaurant
    restaurant = relationship("Restaurant", back_populates="tables", uselist=False)

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

    def num_seats_free(self, slot):
        """

        :type slot: object
        """
        # Ensure table and slot occur on the same night of the event
        assert (slot.night_id == self.night_id)

        Base.metadata.create_all(engine)
        session = Session()
        # Get every reservation 
        my_reservations = session.query(Reservation).\
            filter(Reservation.table_id == self.id).\
            filter(Reservation.slot_id == slot.id).\
            all()

        pax_sum = sum(len(group) for group in my_reservations)

        session.close()

        return self.num_seats - pax_sum