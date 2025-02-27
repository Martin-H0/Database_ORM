# main.py
import random, datetime, decimal, threading, email
import aplication_task
import get_safe_value


from database_singleton import DatabaseSingleton
from models.customer import CustomerMapper
from models.points_history import PointsHistoryMapper
from models.room import RoomMapper
from models.reservation import ReservationMapper
from models.payment import PaymentMapper
from models.reservation_room import ReservationRoomMapper
from report.view_customer_points import ViewCustomerPointsMapper
from report.view_reservation_details import ViewReservationDetailsMapper
from report.view_invoice_summary import ViewInvoiceSummaryMapper
from database.procedure_mapper import ProcedureMapper

from interface import  Interface
import logging
# from src.utils import setup_logging, readconfiglogging


if __name__ == "__main__":

    # setup_logging()
    # logging.ERROR("funguj")
    i = Interface()
    i.run()



# def main():
#     # 1) Vytvoříme (resp. získáme) instanci DB singletonu
#     # db = DatabaseSingleton()
#     # db.connect()  # Otevře spojení

#     # 2) Vytvoříme mappery
    






# ph_mapper = PointsHistoryMapper()
# room_mapper = RoomMapper()
# reservation_mapper = ReservationMapper()
# payment_mapper = PaymentMapper()
# resroom_mapper = ReservationRoomMapper()

# view_cospoint_mapper = ViewCustomerPointsMapper()
# view_resdetail_mapper = ViewReservationDetailsMapper()
# view_invsum_mapper = ViewInvoiceSummaryMapper()

# cust_data = view_cospoint_mapper.read_all()
# for e in cust_data:
#     print (e)
# cust_data = view_invsum_mapper.read_all()
# for e in cust_data:
#     print (e)
# cust_data = view_resdetail_mapper.read_all()
# for e in cust_data:
#     print (e)


# procedure_maper = ProcedureMapper()
# customer_mapper = CustomerMapper()    #
# name = input("Zadejte jméno: ")
# email = input("Zadejte e-mail: ")
# phone = input("Zadejte telefonní číslo: ")
# is_vip = input("Je VIP? (ano/ne): ").strip().lower() == "ano"
# loyalty_points = float(input("Zadejte počet věrnostních bodů: "))

# new_cust_id = customer_mapper.create({
#     "name": name,
#     "email": email,
#     "phone": phone,
#     "is_vip": is_vip,
#     "loyalty_points": loyalty_points
# })

# print(f"[CREATE] Zákazník vytvořen s ID={new_cust_id}")



    # 4) READ
    # cust_data = view_cospoint_mapper.read_all()
    # for e in cust_data:
    #     print (e)
    # cust_data = view_invsum_mapper.read_all()
    # for e in cust_data:
    #     print (e)
    # cust_data = view_resdetail_mapper.read_all()
    # for e in cust_data:
    #     print (e)

#     # # CALL p5evede od customera 1 100 bodu customerovi 2
#     # procedure_maper.call_transfer_points(1, 2, 100)

#     # # CALL Calculate total price  (input = id costumer)
#     # total_cost = procedure_maper.call_calculate_total_reservation_cost(4)
#     # print(f"Total cost: {total_cost}")

#     # # CALL add payment  costumer id = 4, castka 2500, metoda CARD, body TRUE
#     # procedure_maper.call_add_payment(4, 2500.0, 'CARD', False)




    # 3) Ukázka CRUD (např. na customer)
    # new_cust_id = customer_mapper.create({
    #     "name": "Jane Doe",
    #     "email": "jane@example.com",
    #     "phone": "789654",
    #     "is_vip": True,
    #     "loyalty_points": 50.0
    # })
    # print(f"[CREATE] Customer with id={new_cust_id}")


    # 4) READ
# cust_data = customer_mapper.read(50)
# print("[READ] Loaded customer:", cust_data)

    # # 5) UPDATE
    # updated_rows = customer_mapper.update(new_cust_id, {
    #     "phone": "000111222",
    #     "loyalty_points": 99.9
    # })
    # print("[UPDATE] Updated rows (customer):", updated_rows)

#     # cust_data = customer_mapper.read(new_cust_id)
#     # print("[READ] Loaded customer:", cust_data)

    # # 6) DELETE (pokud chcete vyzkoušet)
    # del_rows = customer_mapper.delete(new_cust_id)
    # print("[DELETE] Deleted rows (customer):", del_rows)

#     # 7) Vyzkoušíme cizí klíč (např. points_history) => customer_id musí existovat
#     # ph_id = ph_mapper.create({
#     #     "customer_id": new_cust_id,
#     #     "ammount": 30.0,
#     #     "description": "Bonus"
#     # })
#     # print("Inserted points_history id:", ph_id)

#     # Nakonec zavřeme spojení
#     # db.close()

# if __name__ == "__main__":
#     main()
