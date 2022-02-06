from hotel.db.models import DBCustomer
from hotel.db.engine import DBSession


def read_all_customers():
    session = DBSession()
    rooms = session.query(DBCustomer).all()
    return rooms

def read_customer(customer_id: int):
    session = DBSession()
    room = session.query(DBCustomer).get(customer_id)
    return room
