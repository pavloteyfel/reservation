from hotel.db.models import DBRoom, to_dict
from hotel.db.engine import DBSession


def read_all_rooms():
    session = DBSession()
    rooms = session.query(DBRoom).all()
    return [to_dict(room) for room in rooms]

def read_room(room_id: int):
    session = DBSession()
    room = session.query(DBRoom).get(room_id)
    return to_dict(room)
