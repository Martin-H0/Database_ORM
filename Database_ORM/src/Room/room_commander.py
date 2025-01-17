from database.generic_mapper import GenericMapper
from models.room import RoomMapper
import get_safe_value
import aplication_task

class RoomCommander:
    """Handles CRUD operations for rooms using RoomMapper."""

    def __init__(self):
        self.room_mapper = RoomMapper()

    def create_room(self):
        """Creates a new room based on user input with validation."""
        aplication_task.print_title("CREATE ROOM")
        aplication_task.print_line("\nEnter details for the new room:")

        # Validate room number (letters & numbers, max length 10)
        while True:
            room_number = input("Room Number: ").strip()
            if get_safe_value.StringCheck(room_number, lenght=10):
                break
            print("❌ Invalid input. Room number can only contain letters and numbers (max 10 characters).")

        # Validate capacity (only positive numbers)
        while True:
            capacity = input("Capacity: ").strip()
            if get_safe_value.NumberCheck(capacity, negative=False):
                capacity = int(capacity)
                break
            print("❌ Invalid input. Capacity must be a positive number.")

        # Validate price per night (only positive float numbers)
        while True:
            price_per_night = input("Price per night: ").strip()
            if get_safe_value.NumberCheck(price_per_night, negative=False):
                price_per_night = float(price_per_night)
                break
            print("❌ Invalid input. Price must be a positive number.")

        # Validate room type (only STANDARD, DELUXE, SUITE)
        valid_types = ["STANDARD", "DELUXE", "SUITE"]
        while True:
            room_type = input("Room Type (STANDARD, DELUXE, SUITE): ").strip().upper()
            if get_safe_value.EnumCheck(room_type, valid_types):
                break
            print(f"❌ Invalid input. Room type must be one of {valid_types}.")

        # Create room
        new_room_id = self.room_mapper.create({
            "room_number": room_number,
            "capacity": capacity,
            "price_per_night": price_per_night,
            "room_type": room_type
        })

        print(f"✅ [CREATE] Room created with ID={new_room_id}")

    def read_room(self):
        """Reads and displays room details."""
        aplication_task.print_title("READ ROOM")
        
        # Validate room ID input
        while True:
            room_id = input("Enter Room ID: ").strip()
            if get_safe_value.NumberCheck(room_id, negative=False):
                room_id = int(room_id)
                break
            print("❌ Invalid input. Room ID must be a positive number.")

        room_data = self.room_mapper.read(room_id)
        if room_data:
            print(f"✅ [READ] Room Details: {room_data}")
        else:
            print(f"❌ No room found with ID {room_id}")

    def update_room(self):
        """Updates an existing room based on user input."""
        aplication_task.print_title("UPDATE ROOM")

        # Validate room ID input
        while True:
            room_id = input("Enter Room ID to update: ").strip()
            if get_safe_value.NumberCheck(room_id, negative=False):
                room_id = int(room_id)
                break
            print("❌ Invalid input. Room ID must be a positive number.")

        # Check if room exists
        existing_room = self.room_mapper.read(room_id)
        if not existing_room:
            print(f"❌ No room found with ID {room_id}")
            return

        # Get updated values with validation
        print("Enter new values (leave blank to keep existing):")

        room_number = input(f"Room Number [{existing_room['room_number']}]: ").strip() or existing_room['room_number']
        if not get_safe_value.StringCheck(room_number, lenght=10):
            print("❌ Invalid input. Keeping old value.")
            room_number = existing_room['room_number']

        capacity = input(f"Capacity [{existing_room['capacity']}]: ").strip()
        if capacity and not get_safe_value.NumberCheck(capacity, negative=False):
            print("❌ Invalid input. Keeping old value.")
            capacity = existing_room['capacity']
        else:
            capacity = int(capacity) if capacity else existing_room['capacity']

        price_per_night = input(f"Price per night [{existing_room['price_per_night']}]: ").strip()
        if price_per_night and not get_safe_value.NumberCheck(price_per_night, negative=False):
            print("❌ Invalid input. Keeping old value.")
            price_per_night = existing_room['price_per_night']
        else:
            price_per_night = float(price_per_night) if price_per_night else existing_room['price_per_night']

        valid_types = ["STANDARD", "DELUXE", "SUITE"]
        room_type = input(f"Room Type [{existing_room['room_type']}]: ").strip().upper() or existing_room['room_type']
        if not get_safe_value.EnumCheck(room_type, valid_types):
            print("❌ Invalid input. Keeping old value.")
            room_type = existing_room['room_type']

        # Update room
        updated_rows = self.room_mapper.update(room_id, {
            "room_number": room_number,
            "capacity": capacity,
            "price_per_night": price_per_night,
            "room_type": room_type
        })

        if updated_rows:
            print(f"✅ [UPDATE] Room ID {room_id} updated successfully.")
        else:
            print(f"❌ [UPDATE] Failed to update room ID {room_id}.")

    def delete_room(self):
        """Deletes a room based on user input."""
        aplication_task.print_title("DELETE ROOM")

        # Validate room ID input
        while True:
            room_id = input("Enter Room ID to delete: ").strip()
            if get_safe_value.NumberCheck(room_id, negative=False):
                room_id = int(room_id)
                break
            print("❌ Invalid input. Room ID must be a positive number.")

        # Check if room exists
        existing_room = self.room_mapper.read(room_id)
        if not existing_room:
            print(f"❌ No room found with ID {room_id}")
            return

        # Confirm deletion
        confirm = input(f"Are you sure you want to delete room ID {room_id}? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("❌ Deletion cancelled.")
            return

        # Delete room
        deleted_rows = self.room_mapper.delete(room_id)

        if deleted_rows:
            print(f"✅ [DELETE] Room ID {room_id} deleted successfully.")
        else:
            print(f"❌ [DELETE] Failed to delete room ID {room_id}.")
