# models/payment.py
from database.generic_mapper import GenericMapper

class PaymentMapper(GenericMapper):
    def __init__(self, db):
        super().__init__(db, "payment")
        # FK: reservation_id -> reservation

    def create(self, data: dict):
        if "reservation_id" in data:
            if not self._check_id_exists("reservation", data["reservation_id"]):
                raise ValueError(f"reservation_id={data['reservation_id']} neexistuje!")
        return super().create(data)

    def update(self, record_id: int, data: dict):
        if not self._check_id_exists(self.table_name, record_id):
            raise ValueError(f"payment.id={record_id} neexistuje!")

        if "reservation_id" in data:
            if not self._check_id_exists("reservation", data["reservation_id"]):
                raise ValueError(f"reservation_id={data['reservation_id']} neexistuje!")
        return super().update(record_id, data)

    def delete(self, record_id: int):
        if not self._check_id_exists(self.table_name, record_id):
            raise ValueError(f"payment.id={record_id} neexistuje!")
        return super().delete(record_id)
