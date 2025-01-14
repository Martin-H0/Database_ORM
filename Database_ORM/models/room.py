# models/room.py
from database.generic_mapper import GenericMapper

class RoomMapper(GenericMapper):
    def __init__(self):
        super().__init__( "room")
        # Nemáme FK, jen PK

    def update(self, record_id: int, data: dict):
        if not self._check_id_exists(self.table_name, record_id):
            raise ValueError(f"room.id={record_id} neexistuje!")
        return super().update(record_id, data)

    def delete(self, record_id: int):
        if not self._check_id_exists(self.table_name, record_id):
            raise ValueError(f"room.id={record_id} neexistuje!")
        return super().delete(record_id)
