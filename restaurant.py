from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from base import Base


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates="restaurants", uselist=False)

    tables = relationship("Table", back_populates="restaurants")
    slots = relationship("Slot", back_populate="restaurants")

    name = Column(String)
    address_line1 = Column(String)
    address_line2 = Column(String)
    url = Column(String)
    map = Column(String)
    
    def __init__(self, event, name):
        """
        :type event: event object
        :type name: string or unicode characters as name of restaurant
        """
        assert isinstance(event, object)
        assert not (not isinstance(name, str) and not isinstance(name, bytes))
        self.event = event
        self.name = name
        self.tables = tables
        self.slots = slots

