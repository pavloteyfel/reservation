
from hotel.db.models import DBRoom
from hotel.db.engine import DBSession


@app.get("/rooms")
def real_all_rooms():
    session = DBSession()
    rooms = session.query(DBRoom).all()
    return rooms
