from datetime import date

from event import Event
from base import Session, engine, Base
from pax import Pax
from group import Group
from reservation import Reservation
from restaurant import Restaurant
from table import Table
from slot import Slot
from day import Day

from datetime import date

Base.metadata.create_all(engine)

session = Session()


my_event = Event(4, 4)  # 4 nights, 4 restaurants

day1 = Day(my_event)
day2 = Day(my_event)
day3 = Day(my_event)
day4 = Day(my_event)

pax1 = Pax(my_event, "Bill", "Cosbourne", "bill@isp.net", "212-555-1234")
pax2 = Pax(my_event, "Sarah", "Smith", "ssmith@powercorp.biz", "360-455-5357")
pax3 = Pax(my_event, "Ashley", "Wayne", "testy@mctester.pro", "967-444-1212")
pax4 = Pax(my_event, "Jacques", "Orge", "jorge@bills.org", "222-967-1111")

group1 = Group(my_event, "Purple")
group2 = Group(my_event, "Green")
group3 = Group(my_event, "Blue")

rest1 = Restaurant(my_event, "Chez Pierre")
rest2 = Restaurant(my_event, "Alice Fazoolis")
rest3 = Restaurant(my_event, "Last Temptation")
rest4 = Restaurant(my_event, "Boathouse")

table_r1_t1 = Table(my_event, rest1, 4, day1)
table_r1_t2 = Table(my_event, rest1, 4, day1)
table_r1_t3 = Table(my_event, rest1, 4, day1)

table_r2_t1 = Table(my_event, rest2, 4, day1)
table_r2_t2 = Table(my_event, rest2, 4, day1)
table_r2_t3 = Table(my_event, rest2, 4, day1)

table_r3_t1 = Table(my_event, rest3, 4, day1)
table_r3_t2 = Table(my_event, rest3, 4, day1)
table_r3_t3 = Table(my_event, rest3, 4, day1)

slot_r1_s1 = Slot(my_event, rest1, day1, 90)
slot_r1_s2 = Slot(my_event, rest1, day1, 90)
slot_r1_s3 = Slot(my_event, rest1, day1, 90)

slot_r2_s1 = Slot(my_event, rest2, day1, 90)
slot_r2_s2 = Slot(my_event, rest2, day1, 90)
slot_r2_s3 = Slot(my_event, rest2, day1, 90)

slot_r3_s1 = Slot(my_event, rest3, day1, 90)
slot_r3_s2 = Slot(my_event, rest3, day1, 90)
slot_r3_s3 = Slot(my_event, rest3, day1, 90)

reservation_test = Reservation(my_event, group1, table_r1_t1, slot_r1_s1, date(2018, 7, 26), 1, True)


session.add(my_event)

session.add(day1)
session.add(day2)
session.add(day3)
session.add(day4)

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

session.add(table_r1_t1)
session.add(table_r1_t2)
session.add(table_r1_t3)

session.add(table_r2_t1)
session.add(table_r2_t2)
session.add(table_r2_t3)

session.add(table_r3_t1)
session.add(table_r3_t2)
session.add(table_r3_t3)

session.add(slot_r1_s1)
session.add(slot_r1_s2)
session.add(slot_r1_s3)

session.add(slot_r2_s1)
session.add(slot_r2_s2)
session.add(slot_r2_s3)

session.add(slot_r3_s1)
session.add(slot_r3_s2)
session.add(slot_r3_s3)

session.commit()
session.close()