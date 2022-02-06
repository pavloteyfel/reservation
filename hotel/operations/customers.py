from hotel.db.models import DBCustomer, to_dict
from hotel.db.engine import DBSession
from pydantic import BaseModel
from typing import Optional


class CustomerCreateData(BaseModel):
    first_name: str
    last_name: str
    email_address: str

class CustomerUpdateData(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email_address: Optional[str]


def read_all_customers():
    session = DBSession()
    customers = session.query(DBCustomer).all()
    return [to_dict(customer) for customer in customers]


def read_customer(customer_id: int):
    session = DBSession()
    customer = session.query(DBCustomer).get(customer_id)
    return to_dict(customer) 


def create_customer(data: CustomerCreateData):
    session = DBSession()
    customer = DBCustomer(**data.dict())
    session.add(customer)
    session.commit()
    return to_dict(customer)

def update_customer(customer_id: int, data: CustomerUpdateData):
    session = DBSession()
    customer = session.query(DBCustomer).get(customer_id)
    for key, value in data.dict(exclude_none=True).items():
        setattr(customer, key, value)
    session.commit()
    return to_dict(customer)