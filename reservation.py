from sqlalchemy import Column, String, Integer, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship, backref

from base import Base


class Reservation(Base):
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True)

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates="reservations")

    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship("Group", back_populates="reservation", uselist=False)

    table_id = Column(Integer, ForeignKey('table.id'))
    table = relationship("Table")

    slot_id = Column(Integer, ForeignKey('slot.id'))
    slot = relationship("Slot")

    created_on = Column(Date)
    created_by = Column(Integer)
    active = Column(Boolean)

    def __init__(self, event, group, table, slot, created_on, created_by, active):
        """

        :type event: object
        :type pax: object
        :type table: object
        :type slot: object
        :type created_on: date
        :type created_by: bool
        """
        self.event = event
        self.group = group
        self.table = table
        self.slot = slot
        self.created_on = created_on
        self.created_by = created_by

