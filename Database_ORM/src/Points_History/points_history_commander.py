from database.generic_mapper import GenericMapper
from models.points_history import PointsHistoryMapper
import get_safe_value
import aplication_task

class PointsHistoryCommander:
    """Handles reading of points history using PointsHistoryMapper."""

    def __init__(self):
        self.points_history_mapper = PointsHistoryMapper()

    def read_points_history(self):
        """Reads and displays points history for a specific customer."""
        aplication_task.print_title("READ POINTS HISTORY")

        # Validate customer ID input
        while True:
            customer_id =  ("Enter Customer ID: ").strip()
            if get_safe_value.NumberCheck(customer_id, negative=False):
                customer_id = int(customer_id)
                break
            print("❌ Invalid input. Customer ID must be a positive number.")

        # Fetch points history
        points_data = self.points_history_mapper.read(customer_id)
        if points_data:
            print(f"✅ [READ] Points History for Customer ID {customer_id}:")
            for record in points_data:
                print(f"- ID: {record['id']}, Amount: {record['ammount']}, Description: {record['description']}")
        else:
            print(f"❌ No points history found for Customer ID {customer_id}")
