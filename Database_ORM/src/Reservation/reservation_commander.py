from database.generic_mapper import GenericMapper
from models.reservation import ReservationMapper
import get_safe_value
import aplication_task

class ReservationCommander:
    """Handles CRUD operations for reservations using ReservationMapper."""

    def __init__(self):
        self.reservation_mapper = ReservationMapper()

    def create_reservation(self):
        """Creates a new reservation based on user input with validation."""

        aplication_task.print_title("CREATE RESERVATION")
        aplication_task.print_line("\nEnter details for the new reservation:")

        # Validate customer ID (must be a positive number)
        while True:
            customer_id = input("Customer ID: ").strip()
            if get_safe_value.NumberCheck(customer_id, negative=False):
                customer_id = int(customer_id)
                break
            print("❌ Invalid input. Customer ID must be a positive number.")

        # Validate check-in date (must be a valid date)


        while True:
            check_in = input("Check-in date (YYYY-MM-DD): ").strip()
            if get_safe_value.DateCheck(check_in):
                break
            print("❌ Invalid input. Please enter a valid date in format YYYY-MM-DD.")

        # Validate check-out date (must be a valid date and after check-in)
        while True:
            check_out = input("Check-out date (YYYY-MM-DD): ").strip()
            if get_safe_value.DateCheck(check_out) and check_out > check_in:
                break
            print("❌ Invalid input. Check-out date must be later than check-in date and in format YYYY-MM-DD.")

        # Create reservation
        new_reservation_id = self.reservation_mapper.create({
            "customer_id": customer_id,
            "check_in": f"'{check_in}'",
            "check_out": f"'{check_out}'"
        })

        print(f"✅ [CREATE] Reservation created with ID={new_reservation_id}")

    def read_reservation(self):
        """Reads and displays reservation details."""
        aplication_task.print_title("READ RESERVATION")

        # Validate reservation ID input
        while True:
            reservation_id = input("Enter Reservation ID: ").strip()
            if get_safe_value.NumberCheck(reservation_id, negative=False):
                reservation_id = int(reservation_id)
                break

            print("❌ Invalid input. Reservation ID must be a positive number.")

        reservation_data = self.reservation_mapper.read(reservation_id)
        if reservation_data:
            print(f"✅ [READ] Reservation Details: {reservation_data}")
        else:
            print(f"❌ No reservation found with ID {reservation_id}")

    def update_reservation(self):
        """Updates an existing reservation based on user input."""
        aplication_task.print_title("UPDATE RESERVATION")

        # Validate reservation ID input
        while True:
            reservation_id = input("Enter Reservation ID to update: ").strip()
            if get_safe_value.NumberCheck(reservation_id, negative=False):
                reservation_id = int(reservation_id)
                break
            print("❌ Invalid input. Reservation ID must be a positive number.")

        # Check if reservation exists
        existing_reservation = self.reservation_mapper.read(reservation_id)
        if not existing_reservation:
            print(f"❌ No reservation found with ID {reservation_id}")
            return

        # Get updated values with validation
        print("Enter new values (leave blank to keep existing):")

        customer_id = input(f"Customer ID [{existing_reservation['customer_id']}]: ").strip()
        if customer_id and not get_safe_value.NumberCheck(customer_id, negative=False):
            print("❌ Invalid input. Keeping old value.")
            customer_id = existing_reservation['customer_id']

        else:
            customer_id = int(customer_id) if customer_id else existing_reservation['customer_id']

        check_in = input(f"Check-in date [{existing_reservation['check_in']}]: ").strip()

        if check_in and not get_safe_value.DateCheck(check_in):
            print("❌ Invalid input. Keeping old value.")
            check_in = existing_reservation['check_in']

        check_out = input(f"Check-out date [{existing_reservation['check_out']}]: ").strip()

        if check_out and (not get_safe_value.DateCheck(check_out) or check_out <= check_in):
            print("❌ Invalid input. Keeping old value.")
            check_out = existing_reservation['check_out']

        # Update reservation
        updated_rows = self.reservation_mapper.update(reservation_id, {
            "customer_id": customer_id,
            "check_in": f"'{check_in}'",
            "check_out": f"'{check_out}'"
        })

        if updated_rows:
            print(f"✅ [UPDATE] Reservation ID {reservation_id} updated successfully.")
        else:
            print(f"❌ [UPDATE] Failed to update reservation ID {reservation_id}.")

    def delete_reservation(self):
        """Deletes a reservation based on user input."""
        aplication_task.print_title("DELETE RESERVATION")

        # Validate reservation ID input
        while True:
            reservation_id = input("Enter Reservation ID to delete: ").strip()
            if get_safe_value.NumberCheck(reservation_id, negative=False):
                reservation_id = int(reservation_id)
                break
            print("❌ Invalid input. Reservation ID must be a positive number.")

        # Check if reservation exists
        existing_reservation = self.reservation_mapper.read(reservation_id)
        if not existing_reservation:
            print(f"❌ No reservation found with ID {reservation_id}")
            return

        # Confirm deletion
        confirm = input(f"Are you sure you want to delete reservation ID {reservation_id}? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("❌ Deletion cancelled.")
            return

        # Delete reservation
        deleted_rows = self.reservation_mapper.delete(reservation_id)

        if deleted_rows:
            print(f"✅ [DELETE] Reservation ID {reservation_id} deleted successfully.")
        else:
            print(f"❌ [DELETE] Failed to delete reservation ID {reservation_id}.")
