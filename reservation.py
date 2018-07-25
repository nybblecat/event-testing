from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

from base import Base


class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates='reservations', uselist=False)

    pax_id = Column(Integer, ForeignKey('pax.id'))
    pax = relationship("Pax", back_populates="reservations", uselist=False)

    table_id = Column(Integer, ForeignKey('tables.id'))
    table = relationship("Table", back_populates="reservations", uselist=False)

    slot_id = Column(Integer, ForeignKey('slots.id'))
    slot = relationship("Slots", back_populates="reservations", uselist=False)

    created_on = Column(Date)
    created_by = Column(Integer)
    active = Column(Boolean)

    def __init__(self, event, pax, table, slot, created_on, created_by, active):
        """

        :type event: object
        :type pax: object
        :type table: object
        :type slot: object
        :type created_on: date
        :type created_by: int
        """
        self.event = event
        self.pax = pax
        self.table = table
        self.slot = slot
        self.created_on = created_on
        self.created_by = created_by

