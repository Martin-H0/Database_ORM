from database.generic_mapper import GenericMapper
from models.reservation_room import ReservationRoomMapper
import get_safe_value
import aplication_task

class ReservationRoomCommander:
    """Handles CRUD operations for reservation_room using ReservationRoomMapper."""

    def __init__(self):
        self.reservation_room_mapper = ReservationRoomMapper()

    def create_reservation_room(self):
        """Creates a new reservation-room relationship."""
        aplication_task.print_title("CREATE RESERVATION ROOM")

        # Validate reservation_id
        while True:
            reservation_id = input("Enter Reservation ID: ").strip()
            if get_safe_value.NumberCheck(reservation_id, negative=False):
                reservation_id = int(reservation_id)
                break
            print("❌ Invalid input. Reservation ID must be a positive number.")

        # Validate room_id
        while True:
            room_id = input("Enter Room ID: ").strip()
            if get_safe_value.NumberCheck(room_id, negative=False):
                room_id = int(room_id)
                break
            print("❌ Invalid input. Room ID must be a positive number.")

        # Validate price_applied
        while True:
            price_applied = input("Enter Applied Price: ").strip()
            if get_safe_value.NumberCheck(price_applied, negative=False):
                price_applied = float(price_applied)
                break
            print("❌ Invalid input. Price must be a positive number.")

        # Insert data
        new_res_room_id = self.reservation_room_mapper.create({
            "reservation_id": reservation_id,
            "room_id": room_id,
            "price_applied": price_applied
        })

        print(f"✅ [CREATE] Reservation-Room entry created with ID={new_res_room_id}")

    def read_reservation_room(self):
        """Reads all reservation-room relationships for a given reservation."""
        aplication_task.print_title("READ RESERVATION ROOM")

        # Validate reservation_id
        while True:
            reservation_id = input("Enter Reservation ID: ").strip()
            if get_safe_value.NumberCheck(reservation_id, negative=False):
                reservation_id = int(reservation_id)
                break
            print("❌ Invalid input. Reservation ID must be a positive number.")

        # Fetch records
        res_rooms = self.reservation_room_mapper.read(reservation_id)

        # Debugging: Print type of res_rooms
        print(f"DEBUG: Type of res_rooms = {type(res_rooms)}")
        print(f"DEBUG: Value of res_rooms = {res_rooms}")

        # Handle possible errors in return data
        if isinstance(res_rooms, dict):  
            # Pokud vrací jen jeden záznam jako slovník, obalíme ho do seznamu
            res_rooms = [res_rooms]
        
        if isinstance(res_rooms, list) and res_rooms:
            print(f"✅ [READ] Rooms for Reservation ID {reservation_id}:")
            for record in res_rooms:
                print(f"- ID: {record.get('id')}, Room ID: {record.get('room_id')}, Price: {record.get('price_applied')}")
        else:
            print(f"❌ No rooms found for Reservation ID {reservation_id}")

    def update_reservation_room(self):
        """Updates the applied price for a reservation-room entry."""
        aplication_task.print_title("UPDATE RESERVATION ROOM")

        # Validate entry ID
        while True:
            entry_id = input("Enter Reservation-Room Entry ID: ").strip()
            if get_safe_value.NumberCheck(entry_id, negative=False):
                entry_id = int(entry_id)
                break
            print("❌ Invalid input. Entry ID must be a positive number.")

        # Validate new price
        while True:
            new_price = input("Enter New Applied Price: ").strip()
            if get_safe_value.NumberCheck(new_price, negative=False):
                new_price = float(new_price)
                break
            print("❌ Invalid input. Price must be a positive number.")

        # Update the entry
        updated_rows = self.reservation_room_mapper.update(entry_id, {
            "price_applied": new_price
        })

        if updated_rows > 0:
            print(f"✅ [UPDATE] Updated {updated_rows} rows for Entry ID {entry_id}")
        else:
            print(f"❌ No entry found with ID {entry_id}")

    def delete_reservation_room(self):
        """Deletes a reservation-room entry."""
        aplication_task.print_title("DELETE RESERVATION ROOM")

        # Validate entry ID
        while True:
            entry_id = input("Enter Reservation-Room Entry ID to Delete: ").strip()
            if get_safe_value.NumberCheck(entry_id, negative=False):
                entry_id = int(entry_id)
                break
            print("❌ Invalid input. Entry ID must be a positive number.")

        # Delete entry
        deleted_rows = self.reservation_room_mapper.delete(entry_id)

        if deleted_rows > 0:
            print(f"✅ [DELETE] Deleted {deleted_rows} row(s) with Entry ID {entry_id}")
        else:
            print(f"❌ No entry found with ID {entry_id}")
