from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship, backref

from base import Base


class Night(Base):
    __tablename__ = 'night'

    id = Column(Integer, primary_key=True)

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates="nights")

    date = Column(Date) # Simplified date handling as we handle only a few consecutive nights.
                        # Each night has its own restaurant tables and time slots.

    def __init__(self, event):
        """

        :type event: object
        """
        assert isinstance(event, object)

        self.event = event
