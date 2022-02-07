from typing import Any
from hotel.db.models import Base, to_dict
from hotel.db.engine import DBSession


class DataObject:
    dict[str, Any]


class DBInterface:
    def __init__(self, db_class: type[Base]):
        self.db_class = db_class

    def read_by_id(self, id: int) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)
        return to_dict(result)

    def read_all(self) -> list[DataObject]:
        session = DBSession()
        results = session.query(self.db_class).all()
        return [to_dict(result) for result in results]

    def create(self, data: DataObject) -> DataObject:
        session = DBSession()
        result = self.db_class(**data)
        session.add(result)
        session.commit()
        return to_dict(result)

    def update(self, id: int, data: DataObject) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)
        for key, value in data.items():
            setattr(result, key, value)
        session.commit()
        return to_dict(result)

    def delete(self, id: int) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)
        result.delete()
        session.commit()
        return to_dict(result)
