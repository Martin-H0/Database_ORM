# models/customer.py
from database.generic_mapper import GenericMapper

class CustomerMapper(GenericMapper):
    def __init__(self):    # self, db
        super().__init__("customer")  # db, "customer"
        # Nemáme cizí klíče, jen PK = id

    def update(self, record_id: int, data: dict):
        # Ověřit, zda záznam existuje
        if not self._check_id_exists(self.table_name, record_id):
            raise ValueError(f"Záznam customer.id={record_id} neexistuje!")
        return super().update(record_id, data)

    def delete(self, record_id: int):
        if not self._check_id_exists(self.table_name, record_id):
            raise ValueError(f"Záznam customer.id={record_id} neexistuje!")
        return super().delete(record_id)

