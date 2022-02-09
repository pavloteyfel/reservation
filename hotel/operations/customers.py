from typing import Dict, Optional

from pydantic import BaseModel
from hotel.db.db_interface import DBInterface

from hotel.operations.interface import DataInterface, DictStrAny


class CustomerCreateData(BaseModel):
    first_name: str
    last_name: str
    email_address: str


class CustomerUpdateData(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email_address: Optional[str]


def read_all_customers(customer_interface: DataInterface) -> list[DictStrAny]:
    return customer_interface.read_all()


def read_customer(customer_id: int, customer_interface: DBInterface) -> DictStrAny:
    return customer_interface.read_by_id(customer_id)


def create_customer(data: CustomerCreateData, customer_interface: DataInterface) -> DictStrAny:
    return customer_interface.create(data)


def update_customer(customer_id: int, data: CustomerUpdateData, customer_interface: DataInterface):
    return customer_interface.update(customer_id, data)
