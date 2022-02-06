from hotel.db.models import DBBooking, DBRoom, to_dict
from hotel.db.engine import DBSession
from pydantic import BaseModel
from typing import Optional
from datetime import date


class InvalidDateError(Exception):
    ...


class BookingCreateData(BaseModel):
    room_id: int
    customer_id: int
    to_date: date


class CustomerUpdateData(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email_address: Optional[str]


def read_all_bookings():
    session = DBSession()
    bookings = session.query(DBBooking).all()
    return [to_dict(booking) for booking in bookings]


def read_booking(booking_id: int):
    session = DBSession()
    booking = session.query(DBBooking).get(booking_id)
    return to_dict(booking)


def create_booking(data: BookingCreateData):
    session = DBSession()
    room = session.query(DBRoom).get(data.room_id)
    days = (data.to_date - data.from_date).days
    if days <= 0:
        raise InvalidDateError("Invalid dates.")
    booking_dict = data.dict()
    booking_dict["price"] = room.price * days
    booking = DBBooking(**booking_dict)
    session.add(booking)
    session.commit()
    return to_dict(booking)


def delete_booking(booking_id: int):
    session = DBSession()
    booking = session.query(DBBooking).get(booking_id)
    booking.delete()
    session.commit()
    return to_dict(booking)
