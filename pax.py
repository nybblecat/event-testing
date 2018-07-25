from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

from base import Base


class Pax(Base):
    __tablename__ = 'pax'

    id = Column(Integer, primary_key=True)

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates='pax', uselist=False)

    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)
    active = Column(Boolean)

    reservation = relationship("Reservation", backpopulates="pax", uselist=False)

    def __init__(self, event, first_name, last_name, email, phone):
        """

        :type event: object
        :type first_name: string
        :type last_name: string
        :type email: string
        :type phone: string
        """
        self.event = event
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

