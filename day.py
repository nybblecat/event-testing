from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship, backref

from base import Base


class Day(Base):
    __tablename__ = 'day'

    id = Column(Integer, primary_key=True)

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates="days")

    date = Column(Date)

    def __init__(self, event):
        """

        :type event: object
        """
        assert isinstance(event, object)

        self.event = event
