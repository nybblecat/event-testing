from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Group(Base):
	__tablename__ = 'group'

	id = Column(Integer, primary_key=True)

	event_id = Column(Integer, ForeignKey('event.id'))
	event = relationship("Event", back_populates='group')

	pax = relationship("Pax")

	name = Column(String)

	def __init__(self, event, name):
		"""

        :type event: object
        :type name: string
        """
        assert isinstance(event, object)
        self.event = event

        asset isinstance(name, str)
        self.name = name
        

	#def __len__(self):

	#def add_to_group(self, pax):