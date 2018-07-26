from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Group(Base):
	__tablename__ = 'group'

	id = Column(Integer, primary_key=True)

	event_id = Column(Integer, ForeignKey('events.id'))
	event = relationship("Event", back_populates='groups')

	pax = relationship("Pax", back_populates='group', uselist=False)
	reservation = relationship("Reservation")

	name = Column(String)

	def __init__(self, event, name):
		"""

        :type event: object
        :type name: string
        """
		assert isinstance(event, object)
		self.event = event

		assert isinstance(name, str)
		self.name = name


	#def __len__(self):

	def add(self, pax):
		"""

        :type pax: object
        """
		self.pax = pax