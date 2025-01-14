# main.py

from database_singleton import DatabaseSingleton

# Import mapperů
from models.customer import CustomerMapper
from models.points_history import PointsHistoryMapper
from models.room import RoomMapper
from models.reservation import ReservationMapper
from models.payment import PaymentMapper
from models.reservation_room import ReservationRoomMapper

def main():
    # 1) Vytvoříme (resp. získáme) instanci DB singletonu
    db = DatabaseSingleton()
    db.connect()  # Otevře spojení

    # 2) Vytvoříme mappery
    customer_mapper = CustomerMapper(db)
    ph_mapper = PointsHistoryMapper(db)
    room_mapper = RoomMapper(db)
    reservation_mapper = ReservationMapper(db)
    payment_mapper = PaymentMapper(db)
    resroom_mapper = ReservationRoomMapper(db)

    # 3) Ukázka CRUD (např. na customer)
    new_cust_id = customer_mapper.create({
        "name": "Jane Doe",
        "email": "jane@example.com",
        "phone": "789654",
        "is_vip": True,
        "loyalty_points": 50.0
    })
    print(f"[CREATE] Customer with id={new_cust_id}")


    # # 4) READ
    # cust_data = customer_mapper.read(new_cust_id)
    # print("[READ] Loaded customer:", cust_data)

    # # 5) UPDATE
    # updated_rows = customer_mapper.update(new_cust_id, {
    #     "phone": "000111222",
    #     "loyalty_points": 99.9
    # })
    # print("[UPDATE] Updated rows (customer):", updated_rows)





    # 6) DELETE (pokud chcete vyzkoušet)
    # del_rows = customer_mapper.delete(new_cust_id)
    # print("[DELETE] Deleted rows (customer):", del_rows)

    # 7) Vyzkoušíme cizí klíč (např. points_history) => customer_id musí existovat
    # ph_id = ph_mapper.create({
    #     "customer_id": new_cust_id,
    #     "ammount": 30.0,
    #     "description": "Bonus"
    # })
    # print("Inserted points_history id:", ph_id)

    # Nakonec zavřeme spojení
    db.close()

if __name__ == "__main__":
    main()
