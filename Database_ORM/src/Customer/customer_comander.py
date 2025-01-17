import csv
import os
from database.generic_mapper import GenericMapper
import get_safe_value
import aplication_task
from models.customer import CustomerMapper


class CustomerCommander:
    """Manages CRUD operations for customers using CustomerMapper."""

    def __init__(self):
        self.customer_mapper = CustomerMapper()

    def create_customer(self):
        """Creates a new customer with user input validation."""
        aplication_task.print_title("CREATE CUSTOMER")
        print("\n Enter details for the new customer:")

        # Name validation
        while True:
            name = input("Name: ").strip()
            if get_safe_value.StringCheck(name, 100):
                break
            print("❌ Invalid name. Please enter a valid name (max 100 characters, no special characters).")

        # Email validation
        while True:
            email = input("E-mail: ").strip()
            if "@" in email and "." in email:
                break
            print("❌ Invalid email format. Please enter a valid email (include @ and .).")

        # Phone validation
        while True:
            phone = input("Phone: ").strip()
            if get_safe_value.NumberCheck(phone, 30, negative=False):
                break
            print("❌ Invalid phone number. Please enter numbers only (max 30 characters).")

        # VIP status
        is_vip = input("Is VIP? (yes/no): ").strip().lower() == "yes"

        # Loyalty points validation
        while True:
            loyalty_points = input("Loyalty points: ").strip()
            if get_safe_value.NumberCheck(loyalty_points, negative=False):
                loyalty_points = float(loyalty_points)
                break
            print("❌ Invalid input. Loyalty points must be a positive number.")

        # Create customer
        new_cust_id = self.customer_mapper.create({
            "name": name,
            "email": email,
            "phone": phone,
            "is_vip": is_vip,
            "loyalty_points": loyalty_points
        })

        print(f"✅ [CREATE] Customer created with ID={new_cust_id}")

    def read_customer(self):
        """Reads a customer by ID."""
        aplication_task.print_title("READ CUSTOMER")

        while True:
            cust_id = input("Enter Customer ID: ").strip()
            if get_safe_value.NumberCheck(cust_id, negative=False):
                cust_id = int(cust_id)
                break
            print("❌ Invalid input. Customer ID must be a positive number.")

        cust_data = self.customer_mapper.read(cust_id)
        if cust_data:
            print(f"✅ [READ] Customer ID {cust_id}: {cust_data}")
        else:
            print(f"❌ No customer found with ID {cust_id}")

    def update_customer(self):
        """Updates an existing customer's phone and loyalty points."""
        aplication_task.print_title("UPDATE CUSTOMER")

        while True:
            cust_id = input("Enter Customer ID to update: ").strip()
            if get_safe_value.NumberCheck(cust_id, negative=False):
                cust_id = int(cust_id)
                break
            print("❌ Invalid input. Customer ID must be a positive number.")

        # Phone update
        while True:
            phone = input("New phone number: ").strip()
            if get_safe_value.NumberCheck(phone, 30, negative=False):
                break
            print("❌ Invalid phone number. Please enter numbers only (max 30 characters).")

        # Loyalty points update
        while True:
            loyalty_points = input("New loyalty points: ").strip()
            if get_safe_value.NumberCheck(loyalty_points, negative=False):
                loyalty_points = float(loyalty_points)
                break
            print("❌ Invalid input. Loyalty points must be a positive number.")

        updated_rows = self.customer_mapper.update(cust_id, {
            "phone": phone,
            "loyalty_points": loyalty_points
        })

        if updated_rows:
            print(f"✅ [UPDATE] Customer ID {cust_id} updated successfully.")
        else:
            print(f"❌ No customer found with ID {cust_id}")

    def delete_customer(self):
        """Deletes a customer by ID."""
        aplication_task.print_title("DELETE CUSTOMER")

        while True:
            cust_id = input("Enter Customer ID to delete: ").strip()
            if get_safe_value.NumberCheck(cust_id, negative=False):
                cust_id = int(cust_id)
                break
            print("❌ Invalid input. Customer ID must be a positive number.")

        deleted_rows = self.customer_mapper.delete(cust_id)
        if deleted_rows:
            print(f"✅ [DELETE] Customer ID {cust_id} deleted successfully.")
        else:
            print(f"❌ No customer found with ID {cust_id}")

    def load_customers_from_file(self):
        """Loads customers from a CSV file with validation."""
        aplication_task.print_title("LOAD CUSTOMERS FROM FILE")
        aplication_task.print_line("create customers.csv,   path: Database_ORM/src/Customer/customers.csv" )
        aplication_task.print_line("csv form:  name,email,phone,is_vip,loyalty_points")
        aplication_task.print_line("Example:   John Doe,john@example.com,123456789,true,50.0")

        file_path = "./Database_ORM/src/Customer/customers.csv"
        if not os.path.exists(file_path):
            print("❌ Error: customers.csv file not found.")
            return

        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            count = 0
            skipped = 0

            for row in reader:
                name = row["name"].strip()
                email = row["email"].strip()
                phone = row["phone"].strip()
                is_vip = row["is_vip"].strip().lower() == "true"
                loyalty_points = row["loyalty_points"].strip()

                # Validate data
                if not get_safe_value.StringCheck(name, 100):
                    print(f"⚠️ Skipping invalid name: {name}")
                    skipped += 1
                    continue

                if "@" not in email or "." not in email:
                    print(f"⚠️ Skipping invalid email: {email}")
                    skipped += 1
                    continue

                if not get_safe_value.NumberCheck(phone, 30, negative=False):
                    print(f"⚠️ Skipping invalid phone number: {phone}")
                    skipped += 1
                    continue

                if not get_safe_value.NumberCheck(loyalty_points, negative=False):
                    print(f"⚠️ Skipping invalid loyalty points: {loyalty_points}")
                    skipped += 1
                    continue

                # Convert values
                loyalty_points = float(loyalty_points)

                # Create customer
                new_cust_id = self.customer_mapper.create({
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "is_vip": is_vip,
                    "loyalty_points": loyalty_points
                })
                count += 1

        print(f"✅ [LOAD] {count} customers loaded from file. ⚠️ {skipped} entries skipped due to errors.")
























# # import  csv
# import random,  datetime, decimal, threading, email
# import json
# from database.generic_mapper import GenericMapper
# import get_safe_value
# import aplication_task
# from models.customer import CustomerMapper
# import logging

# class CustomerCommander:
#     """Spravuje CRUD operace pro customer pomocí CustomerMapperu."""

#     def __init__(self):
#         self.customer_mapper = CustomerMapper()

#     def create_customer(self):
#         """Creates a new customer based on user input with validation."""
#         aplication_task.print_title("CREATE CUSTOMER")
#         aplication_task.print_line("\nEnter details for the new customer:")

#         # Validate name (only letters and numbers, max length 50)
#         while True:
#             name = input("Name: ").strip()
#             if get_safe_value.StringCheck(name, lenght=50):
#                 break
#             print("❌ Invalid input. Name can only contain letters and numbers (max 50 characters).")

#         # Validate email (basic format check)
#         while True:
#             email = input("E-mail: ").strip()
#             if "@" in email and "." in email and len(email) < 100:
#                 break
#             print("❌ Invalid input. Enter a valid email address.")

#         # Validate phone number (only numbers, max length 15)
#         while True:
#             phone = input("Phone: ").strip()
#             if get_safe_value.NumberCheck(phone, lenght=15, negative=False):
#                 break
#             print("❌ Invalid input. Phone number can only contain digits (max 15 characters).")

#         # Validate VIP status (yes/no)
#         while True:
#             is_vip = input("Is VIP? (yes/no): ").strip().lower()
#             if get_safe_value.BoolCheck(is_vip, "yes", "no"):
#                 is_vip = is_vip == "yes"
#                 break
#             print("❌ Invalid input. Enter 'yes' or 'no'.")

#         # Validate loyalty points (must be a positive number)
#         while True:
#             loyalty_points = input("Loyalty points: ").strip()
#             if get_safe_value.NumberCheck(loyalty_points, negative=False):
#                 loyalty_points = float(loyalty_points)
#                 break
#             print("❌ Invalid input. Loyalty points must be a positive number.")

#         # Create customer
#         new_cust_id = self.customer_mapper.create({
#             "name": name,
#             "email": email,
#             "phone": phone,
#             "is_vip": is_vip,
#             "loyalty_points": loyalty_points
#         })

#         print(f"✅ [CREATE] Customer created with ID={new_cust_id}")

#     def read_customer(self):
#         """Načte a zobrazí customer podle ID."""
#         aplication_task.print_title("READ CUSTOMER")

#         try:
#             cust_id = int(input("\n Enter customer ID: "))
#             cust_data = self.customer_mapper.read(cust_id)

#             if cust_data:
#                 print(f"📌 [READ] Customer data: {cust_data}")
#             else:
#                 print("❌ No customer found with this ID.")
#         except ValueError:
#             print("⚠️ Error: ID must be a number.")

#     def update_customer(self):
#         """Aktualizuje zákazníka podle ID."""
#         aplication_task.print_title("UPDATE CUSTOMER")
        
#         try:
#             cust_id = int(input("\n Enter customer ID to update: "))
#             phone = input("New phone number (leave blank to keep current): ")
#             loyalty_points = input("New loyalty points (leave blank to keep current): ")

#             update_data = {}
#             if phone:
#                 update_data["phone"] = phone
#             if loyalty_points:
#                 update_data["loyalty_points"] = float(loyalty_points)

#             if update_data:
#                 updated_rows = self.customer_mapper.update(cust_id, update_data)
#                 print(f"✅ [UPDATE] Updated records: {updated_rows}")
#             else:
#                 print("⚠️ No changes were provided.")
#         except ValueError:
#             print("⚠️ Error: ID and loyalty points must be numbers.")

#     def delete_customer(self):
#         """Odstraní zákazníka podle ID."""
#         aplication_task.print_title("DELETE CUSTOMER")
#         try:
#             cust_id = int(input("\n Enter customer ID to delete: "))
#             del_rows = self.customer_mapper.delete(cust_id)

#             if del_rows:
#                 print(f"✅ [DELETE] Customer with ID {cust_id} has been deleted.")
#             else:
#                 print("❌ No customer found with this ID.")
#         except ValueError:
#             print("⚠️ Error: ID must be a number.")


















# def create_customer():
#     customer_mapper = CustomerMapper()   
#     name = input("Zadejte jméno: ")
#     email = input("Zadejte e-mail: ")
#     phone = input("Zadejte telefonní číslo: ")
#     is_vip = input("Je VIP? (ano/ne): ").strip().lower() == "ano"
#     loyalty_points = float(input("Zadejte počet věrnostních bodů: "))

#     new_cust_id = customer_mapper.create({
#         "name": name,
#         "email": email,
#         "phone": phone,
#         "is_vip": is_vip,
#         "loyalty_points": loyalty_points
#     })

#     print(f"[CREATE] Zákazník vytvořen s ID={new_cust_id}")


# def read_customer(customer_mapper):
#     cust_id = int(input("Zadejte ID zákazníka k načtení: "))
#     cust_data = customer_mapper.read(cust_id)
#     print("[READ] Načtený zákazník:", cust_data)


# def update_customer(customer_mapper):
#     cust_id = int(input("Zadejte ID zákazníka k aktualizaci: "))
#     phone = input("Zadejte nové telefonní číslo: ")
#     loyalty_points = float(input("Zadejte nový počet věrnostních bodů: "))

#     updated_rows = customer_mapper.update(cust_id, {
#         "phone": phone,
#         "loyalty_points": loyalty_points
#     })

#     print("[UPDATE] Počet aktualizovaných záznamů:", updated_rows)


# def delete_customer(customer_mapper):
#     cust_id = int(input("Zadejte ID zákazníka k odstranění: "))
#     del_rows = customer_mapper.delete(cust_id)
#     print("[DELETE] Počet smazaných záznamů:", del_rows)













# class CustomerCommander:
    
#     def __init__(self):
#         # self.model_command = model_command
#         self.generic_mapper = GenericMapper(self)

#     def CreateCustomer(customer_mapper):
#         aplication_task.print_title("CreateCustomer")
#         name = input("Enter customer name: ")
#         try:
#             if(not get_safe_value.StringCheck(name)):
#                 raise ValueError("Invalid name")
#         except:
#             raise ValueError("Couldn't parse name")
#         Uemail = input("Enter customer email: ")
#         try:
#              email.Email(Uemail)
#         except:
#             raise ValueError("Couldn't parse email")
#         phone = input("Enter customer phone: ")
#         try:
#             if(not get_safe_value.NumberCheck(phone)):
#                 raise ValueError("Invalid phone, phone mus be numbers")
#         except:
#             raise ValueError("Couldn't parse phone")
        
#         try:
#             new_cust_id = customer_mapper.create({
#             "name": name,
#             "email": email,
#             "phone": phone,
#             "is_vip": False,
#             "loyalty_points": 0.0
#             })
#             aplication_task.print_line(f"[CREATE] Customer with id={new_cust_id}")
#         except:
#             raise ValueError("Couldn't Create new customer")





#     def ReadCustomer(customer_mapper):
#         read_id = input("Enter customer phone: ")
#         try:
#             if(not get_safe_value.NumberCheck(read_id)):
#                 raise ValueError("Invalid phone, read_id mus be number")
#         except:
#             raise ValueError("Couldn't parse phone")
#         aplication_task.print_title("ReadCustomer")

#         cust_data = customer_mapper.read(read_id)
#         print("[READ] Loaded customer:", cust_data)

#     def UpdateCustomer(customer_mapper):
#         aplication_task.print_title("UpdateCustomer")
#     def DeleteCustomer(customer_mapper):
#         aplication_task.print_title("DeleteCustomer")
#     def LoadCustomer(customer_mapper):
#         aplication_task.print_title("LoadFromFileCustomer")