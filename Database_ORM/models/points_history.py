# models/points_history.py
from database.generic_mapper import GenericMapper

class PointsHistoryMapper(GenericMapper):
    def __init__(self, db):
        super().__init__(db, "points_history")
        # Cizí klíč: customer_id -> customer

    def create(self, data: dict):
        if "customer_id" in data:
            if not self._check_id_exists("customer", data["customer_id"]):
                raise ValueError(f"customer_id={data['customer_id']} neexistuje v tabulce 'customer'!")
        return super().create(data)

    def update(self, record_id: int, data: dict):
        # Ověř PK
        if not self._check_id_exists(self.table_name, record_id):
            raise ValueError(f"points_history.id={record_id} neexistuje!")

        # Ověř FK pokud je v datech
        if "customer_id" in data:
            if not self._check_id_exists("customer", data["customer_id"]):
                raise ValueError(f"customer_id={data['customer_id']} neexistuje!")
        return super().update(record_id, data)

    def delete(self, record_id: int):
        if not self._check_id_exists(self.table_name, record_id):
            raise ValueError(f"points_history.id={record_id} neexistuje!")
        return super().delete(record_id)
