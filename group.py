from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Group(Base):
	__tablename__ = 'group'

	id = Column(Integer, primary_key=True)

	event_id = Column(Integer, ForeignKey('events.id'))
	event = relationship("Event", back_populates='groups')

	# Each pax can only belong to one group
	pax = relationship("Pax", back_populates='group', uselist=False)

	# Each group can only have one reservation
	reservation = relationship("Reservation", back_populates="group", uselist=False)

	# Assign some handy name so others can find their friends' group
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

	def add_pax(self, pax):
		"""

        :type pax: object
        """
		assert isinstance(pax, object)
		self.pax.append(pax)

	def get_reservation(self):
		# Returns False if there is no reservation related to this group
		return self.reservation