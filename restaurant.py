from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from base import Base


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates="restaurants", uselist=False)

    tables = relationship("Table", back_populates="restaurant")
    slots = relationship("Slot", back_populates="restaurant")

    name = Column(String)
    address_line1 = Column(String)
    address_line2 = Column(String)
    #phone = Column (String)
    website_url = Column(String)
    map_url = Column(String)
    
    def __init__(self, event, name):
        #, address_line1, address_line2,
        #website_url, map_url
        
        """
        :type event: event object
        :type name: string or unicode characters as name of restaurant
        """
        assert isinstance(event, object)
        self.event = event
        
        assert not (not isinstance(name, str) and not isinstance(name, bytes))
        self.name = name

    def __str__(self):
        return 'ID {0}: {1} {2} - Total tables: {3}'.format(self.id, self.name, self.phone, self.tables)
