# models/customer.py
from database.generic_mapper import GenericMapper

class CustomerMapper(GenericMapper):
    def __init__(self, db):
        super().__init__(db, "customer")
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















# from database.generic_mapper import GenericMapper

# class CustomerMapper(GenericMapper):
#     def __init__(self, db):
#         super().__init__(db, "customer")






# from table_row import TableRow

# class Costumer(TableRow):
#     def __init__(self, name: str, email: str, phone: str, is_vip: bool, loyalty_points: float, id: int = None):
#         """
#         Reprezentuje záznam v tabulce 'costumer'.

#         :param name: Jméno zákazníka.
#         :param email: Email zákazníka.
#         :param phone: Telefon zákazníka.
#         :param is_vip: Flag zda je zákazník VIP.
#         :param loyalty_points: Body věrnostního programu.
#         :param id: ID zákazníka (id volitelné databáze sama doplní).
#         """
#         data = {
#             'id': id,     """nezaddávat necha na DS"""
#             'name': name,
#             'email': email,
#             'phone': phone,
#             'is_vip': is_vip,
#             'loyalty_points': loyalty_points
#         }
#         super().__init__('costumer', data)
