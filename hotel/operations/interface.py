from typing import Protocol

from pydantic.typing import DictStrAny


class DataInterface(Protocol):
    def read_by_id(self, id: int) -> DictStrAny:
        ...

    def read_all(self) -> list[DictStrAny]:
        ...

    def create(self, data: DictStrAny) -> DictStrAny:
        ...

    def update(self, id: int, data: DictStrAny) -> DictStrAny:
        ...

    def delete(self, id: int) -> DictStrAny:
        ...
