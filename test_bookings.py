import unittest
from hotel.operations.bookings import BookingCreateData, DataObject, InvalidDateError, create_booking


class DataInterfaceStub:
    def read_by_id(self, id: int) -> DataObject:
        raise NotImplementedError()

    def read_all(self) -> list[DataObject]:
        raise NotImplementedError()
        ...

    def create(self, data: DataObject) -> DataObject:
        raise NotImplementedError()
        ...

    def update(self, id: int, data: DataObject) -> DataObject:
        raise NotImplementedError()
        ...

    def delete(self, id: int) -> DataObject:
        raise NotImplementedError()
        ...


class RoomInterface(DataInterfaceStub):
    def read_by_id(self, id: int) -> DataObject:
        return {"id": id, "number": "101", "size": 10, "price": 150_00}


class BookingInterface(DataInterfaceStub):
    def create(self, data: DataObject) -> DataObject:
        booking = dict(data)
        booking["id"] = 1
        return booking


class TestBooking(unittest.TestCase):

    def test_price_one_day(self):
        booking_data = BookingCreateData(
            room_id=1,
            customer_id=1,
            from_date="2021-12-24",
            to_date="2021-12-25",
        )
        booking = create_booking(
            booking_data, BookingInterface(), RoomInterface())
        self.assertEqual(booking["price"], 150_00)

    def test_date_error(self):
        booking_data = BookingCreateData(
            room_id=1,
            customer_id=1,
            from_date="2021-12-24",
            to_date="2021-12-24",
        )
        self.assertRaises(InvalidDateError, create_booking,
                          booking_data, BookingInterface(), RoomInterface())


if __name__ == "__main__":
    unittest.main()
