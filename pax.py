from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

from base import Base


class Pax(Base):
    __tablename__ = 'pax'

    id = Column(Integer, primary_key=True)

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates="pax", uselist=False)

    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship("Group", back_populates="pax", uselist=False)

    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)
    active = Column(Boolean)

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
        self.active = True

    def __str__(self):
        return 'ID {0}: {1} {2} - {3} - Group: {4}'.format(self.id, self.first_name, self.last_name, self.email, self.group_id)

    def group_join(self, group):
        """

        :type group: object
        """
        assert isinstance(group, object)
        self.group_id = group.id

    def group_clear(self):
        self.group_id = None