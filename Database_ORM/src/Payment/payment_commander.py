from database.generic_mapper import GenericMapper
from models.payment import PaymentMapper
import get_safe_value
import aplication_task
from database.procedure_mapper import ProcedureMapper


class PaymentCommander:
    
    def __init__(self):
        # self.model_command = model_command
        self.payment_mapper = PaymentMapper()
        self.procedure_mapper = ProcedureMapper()

    def create_payment(self):
        """Creates a payment and updates loyalty points if applicable."""
        aplication_task.print_title("CREATE PAYMENT")
        aplication_task.print_line("\nEnter details for the new payment:")

        # Validate customer_id (must be a number)
        while True:
            customer_id = input("Customer ID: ")
            if get_safe_value.NumberCheck(customer_id, lenght=10, negative=False):
                customer_id = int(customer_id)
                break
            print("❌ Invalid input. Customer ID must be a positive number.")

        # Validate money (must be a positive number)
        while True:
            money = input("Money to pay: ")
            if get_safe_value.NumberCheck(money, negative=False):
                money = float(money)
                break
            print("❌ Invalid input. Money must be a positive number.")

        # Validate payment method (must be one of the allowed values)
        valid_methods = ["CARD", "CASH", "BANK_TRANSFER"]
        while True:
            method = input("Payment method (CARD, CASH, BANK_TRANSFER): ").strip().upper()
            if get_safe_value.EnumCheck(method, valid_methods):
                break
            print(f"❌ Invalid input. Payment method must be one of {valid_methods}.")

        # Validate bonus (must be yes/no)
        while True:
            bonus = input("Points? (yes/no): ").strip().lower()
            if get_safe_value.BoolCheck(bonus, "yes", "no"):
                bonus = bonus == "yes"
                break
            print("❌ Invalid input. Enter 'yes' or 'no'.")

        # Call stored procedure to add payment
        self.procedure_mapper.call_add_payment(customer_id, money, method, bonus)
        print("✅ Payment successfully created!")



    def read_payment(self):
        """Načte a zobrazí payment podle ID."""
        aplication_task.print_title("READ PAYMENT")

        try:
            cust_id = int(input("\n Enter payment ID: "))
            cust_data = self.payment_mapper.read(cust_id)

            if cust_data:
                print(f"📌 [READ] Payment data: {cust_data}")
            else:
                print("❌ No payment found with this ID.")
        except ValueError:
            print("⚠️ Error: ID must be a number.")
