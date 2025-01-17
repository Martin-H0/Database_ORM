# import  csv
import random,  datetime, decimal, threading, email
import json
from database.generic_mapper import GenericMapper
import get_safe_value
import aplication_task
# src/Customer/customer_commander.py
from models.customer import CustomerMapper

class CustomerCommander:
    """Spravuje CRUD operace pro customer pomocí CustomerMapperu."""

    def __init__(self):
        self.customer_mapper = CustomerMapper()

    def create_customer(self):
        """Vytvoří nového customer na základě vstupu od uživatele."""
        aplication_task.print_title("CREATE CUSTOMER")
        aplication_task.print_line("\n Enter details for the new customer::")
        name = input ("Name: ")
        email = input("E-mail: ")
        phone = input("Phone: ")
        is_vip = input("Is VIP? (yes/no): ").strip().lower() == "yes"
        loyalty_points = float(input("Loyalty points: "))

        new_cust_id = self.customer_mapper.create({
            "name": name,
            "email": email,
            "phone": phone,
            "is_vip": is_vip,
            "loyalty_points": loyalty_points
        })

        print(f"✅ [CREATE] Customer created with ID={new_cust_id}")

    def read_customer(self):
        """Načte a zobrazí customer podle ID."""
        aplication_task.print_title("READ CUSTOMER")

        try:
            cust_id = int(input("\n Enter customer ID: "))
            cust_data = self.customer_mapper.read(cust_id)

            if cust_data:
                print(f"📌 [READ] Customer data: {cust_data}")
            else:
                print("❌ No customer found with this ID.")
        except ValueError:
            print("⚠️ Error: ID must be a number.")

    def update_customer(self):
        """Aktualizuje zákazníka podle ID."""
        aplication_task.print_title("UPDATE CUSTOMER")
        
        try:
            cust_id = int(input("\n Enter customer ID to update: "))
            phone = input("New phone number (leave blank to keep current): ")
            loyalty_points = input("New loyalty points (leave blank to keep current): ")

            update_data = {}
            if phone:
                update_data["phone"] = phone
            if loyalty_points:
                update_data["loyalty_points"] = float(loyalty_points)

            if update_data:
                updated_rows = self.customer_mapper.update(cust_id, update_data)
                print(f"✅ [UPDATE] Updated records: {updated_rows}")
            else:
                print("⚠️ No changes were provided.")
        except ValueError:
            print("⚠️ Error: ID and loyalty points must be numbers.")

    def delete_customer(self):
        """Odstraní zákazníka podle ID."""
        aplication_task.print_title("DELETE CUSTOMER")
        try:
            cust_id = int(input("\n Enter customer ID to delete: "))
            del_rows = self.customer_mapper.delete(cust_id)

            if del_rows:
                print(f"✅ [DELETE] Customer with ID {cust_id} has been deleted.")
            else:
                print("❌ No customer found with this ID.")
        except ValueError:
            print("⚠️ Error: ID must be a number.")


















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