from datetime import date
from typing import Optional

from pydantic import BaseModel

from hotel.operations.interface import DataInterface, DictStrAny


class InvalidDateError(Exception):
    ...


class BookingCreateData(BaseModel):
    room_id: int
    customer_id: int
    to_date: date
    from_date: date


class CustomerUpdateData(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email_address: Optional[str]


def read_all_bookings(booking_interface: DataInterface) -> list[DictStrAny]:
    return booking_interface.read_all()


def read_booking(booking_id: int,
                 booking_interface: DataInterface) -> DictStrAny:
    return booking_interface.read_by_id(booking_id)


def create_booking(data: BookingCreateData, booking_interface: DataInterface,
                   room_interface: DataInterface) -> DictStrAny:
    room = room_interface.read_by_id(data.room_id)
    days = (data.to_date - data.from_date).days
    if days <= 0:
        raise InvalidDateError("Invalid dates.")
    booking_dict = data.dict()
    booking_dict["price"] = room["price"] * days
    return booking_interface.create(booking_dict)


def delete_booking(booking_id: int,
                   booking_interface: DataInterface) -> DictStrAny:
    return booking_interface.delete(booking_id)
