# models/reservation_room.py
from database.generic_mapper import GenericMapper

class ReservationRoomMapper(GenericMapper):
    def __init__(self):
        super().__init__("reservation_room")
        # FK: reservation_id -> reservation, room_id -> room

    def create(self, data: dict):
        if "reservation_id" in data:
            if not self._check_id_exists("reservation", data["reservation_id"]):
                raise ValueError(f"reservation_id={data['reservation_id']} neexistuje!")
        if "room_id" in data:
            if not self._check_id_exists("room", data["room_id"]):
                raise ValueError(f"room_id={data['room_id']} neexistuje!")
        return super().create(data)

    def update(self, record_id: int, data: dict):
        if not self._check_id_exists(self.table_name, record_id):
            raise ValueError(f"reservation_room.id={record_id} neexistuje!")

        if "reservation_id" in data:
            if not self._check_id_exists("reservation", data["reservation_id"]):
                raise ValueError(f"reservation_id={data['reservation_id']} neexistuje!")
        if "room_id" in data:
            if not self._check_id_exists("room", data["room_id"]):
                raise ValueError(f"room_id={data['room_id']} neexistuje!")
        return super().update(record_id, data)

    def delete(self, record_id: int):
        if not self._check_id_exists(self.table_name, record_id):
            raise ValueError(f"reservation_room.id={record_id} neexistuje!")
        return super().delete(record_id)
