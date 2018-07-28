from datetime import date

from event import Event
from base import Session, engine, Base
from pax import Pax
from group import Group
from reservation import Reservation
from restaurant import Restaurant
from table import Table
from slot import Slot
from night import Night

from datetime import date

Base.metadata.create_all(engine)

session = Session()


my_event = Event(4, 4)  # 4 nights, 4 restaurants

night1 = Night(my_event)
night2 = Night(my_event)
night3 = Night(my_event)
night4 = Night(my_event)

pax1 = Pax(my_event, "Bill", "Cosbourne", "bill@isp.net", "212-555-1234")
pax2 = Pax(my_event, "Sarah", "Smith", "ssmith@powercorp.biz", "360-455-5357")
pax3 = Pax(my_event, "Ashley", "Wayne", "testy@mctester.pro", "967-444-1212")
pax4 = Pax(my_event, "Jacques", "Orge", "jorge@bills.org", "222-967-1111")

group1 = Group(my_event, "Purple")
group2 = Group(my_event, "Green")
group3 = Group(my_event, "Blue")

rest1 = Restaurant(my_event, "Stonecutters")
rest2 = Restaurant(my_event, "Alice Fazoolis")
rest3 = Restaurant(my_event, "Last Temptation")

tables_r1 = [
	Table(my_event, rest1, 4, night1),
	Table(my_event, rest1, 4, night1),
	Table(my_event, rest1, 4, night1)
]

tables_r2 = [
	Table(my_event, rest2, 4, night1),
	Table(my_event, rest2, 4, night1),
	Table(my_event, rest2, 4, night1)
]

tables_r3 = [
	Table(my_event, rest3, 4, night1),
	Table(my_event, rest3, 4, night1),
	Table(my_event, rest3, 4, night1)
]

slots_r1 = [
	Slot(my_event, rest1, night1, 90),
	Slot(my_event, rest1, night1, 90),
	Slot(my_event, rest1, night1, 90)
]

slots_r2 = [
	Slot(my_event, rest2, night1, 90),
	Slot(my_event, rest2, night1, 90),
	Slot(my_event, rest2, night1, 90)
]

slots_r3 = [
	Slot(my_event, rest3, night1, 90),
	Slot(my_event, rest3, night1, 90),
	Slot(my_event, rest3, night1, 90)
]

reservation_test = Reservation(my_event, group1, tables_r1[0], slots_r1[0], date(2018, 7, 26), 1, True)


session.add(my_event)

session.add(night1)
session.add(night2)
session.add(night3)
session.add(night4)

session.add(pax1)
session.add(pax2)
session.add(pax3)
session.add(pax4)

session.add(group1)
session.add(group2)
session.add(group3)

session.add(rest1)
session.add(rest2)
session.add(rest3)

for table in tables_r1:
	session.add(table)

for table in tables_r2:	
	session.add(table)

for table in tables_r3:
	session.add(table)

for slot in slots_r1:
	session.add(slot)

for slot in slots_r2:
	session.add(slot)

for slot in slots_r3:
	session.add(slot)

session.commit()
session.close()