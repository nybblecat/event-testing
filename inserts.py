from datetime import date

from event import Event
from base import Session, engine, Base
from pax import Pax
from reservation import Reservation
from restaurant import Restaurant
from table import Table
from slot import Slot
from day import Day

Base.metadata.create_all(engine)

session = Session()

my_event = Event(4, 4)  # 4 nights, 4 restaurants

pax1 = Pax(my_event, "Bill", "Cosbourne", "bill@isp.net", "212-555-1234")
pax2 = Pax(my_event, "Sarah", "Smith", "ssmith@powercorp.biz", "360-455-5357")
pax3 = Pax(my_event, "Ashley", "Wayne", "testy@mctester.pro", "967-444-1212")
pax4 = Pax(my_event, "Jacques", "Orge", "jorge@bills.org", "222-967-1111")

rest1 = Restaurant(myevent, "Chez Pierre")
rest2 = Restaurant(myevent, "Alice Fazoolis")
rest3 = Restaurant(myevent, "Last Temptation")
rest4 = Restaurant(myevent, "Boathouse")


