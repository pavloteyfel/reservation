from fastapi import APIRouter
from hotel.operations.bookings import (
    BookingCreateData,
    read_all_bookings,
    read_booking,
    create_booking,
    delete_booking,
)

router = APIRouter()


@router.get("/bookings")
def api_read_all_bookings():
    return read_all_bookings()


@router.get("/bookings/{booking_id}")
def api_read_booking(booking_id: int):
    return read_booking(booking_id)


@router.post("/bookings")
def api_create_booking(booking: BookingCreateData):
    return create_booking(booking)


@router.delete("/bookings/{booking_id}")
def api_delete_booking(booking_id: int):
    return delete_booking(booking_id)

