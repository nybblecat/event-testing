from event import Event
from base import Session, engine, Base
from pax import Pax
from group import Group
from reservation import Reservation
from restaurant import Restaurant
from table import Table
from slot import Slot
from night import Night

Base.metadata.create_all(engine)

session = Session()

group = session.query(Group).filter(Group.id == 2).one()
user = session.query(Pax).filter(Pax.id == 4).one()

print (user)

reservation = group.get_reservation()

table = reservation.get_table()
slot = reservation.get_slot()

print (str(table.num_seats_free(slot)))

user.group_join(group)

session.commit()

print (user)

#print (str(len(group)))

print (str(len(group)))

print (str(table.num_seats_free(slot)))

print (*group.get_pax(), sep='\n')

session.close()