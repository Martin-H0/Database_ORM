# models/reservation.py
from database.generic_mapper import GenericMapper

class ReservationMapper(GenericMapper):
    def __init__(self, db):
        super().__init__(db, "reservation")
        # Cizí klíč: customer_id -> customer

    def create(self, data: dict):
        if "customer_id" in data:
            if not self._check_id_exists("customer", data["customer_id"]):
                raise ValueError(f"customer_id={data['customer_id']} neexistuje v 'customer'!")
        return super().create(data)

    def update(self, record_id: int, data: dict):
        if not self._check_id_exists(self.table_name, record_id):
            raise ValueError(f"reservation.id={record_id} neexistuje!")

        if "customer_id" in data:
            if not self._check_id_exists("customer", data["customer_id"]):
                raise ValueError(f"customer_id={data['customer_id']} neexistuje!")
        return super().update(record_id, data)

    def delete(self, record_id: int):
        if not self._check_id_exists(self.table_name, record_id):
            raise ValueError(f"reservation.id={record_id} neexistuje!")
        return super().delete(record_id)
