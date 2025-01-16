import random, csv
import random, datetime, decimal, threading, email
import json
from database.generic_mapper import GenericMapper
from models.customer import CustomerMapper
import get_safe_value
import aplication_task

class CustomerCommander:
    customer_mapper = CustomerMapper()
    def __init__(self):
        # self.model_command = model_command
        self.generic_mapper = GenericMapper(self)

    def CreateCustomer(self):
        aplication_task.print_title("CreateCustomer")
        name = input("Enter customer name: ")
        try:
            if(not get_safe_value.StringCheck(name)):
                raise ValueError("Invalid name")
        except:
            raise ValueError("Couldn't parse name")
        Uemail = input("Enter customer email: ")
        try:
             email.Email(Uemail)
        except:
            raise ValueError("Couldn't parse email")
        phone = input("Enter customer phone: ")
        try:
            if(not get_safe_value.NumberCheck(phone)):
                raise ValueError("Invalid phone, phone mus be numbers")
        except:
            raise ValueError("Couldn't parse phone")
        
        try:
            new_cust_id = CustomerCommander.customer_mapper.create({
            "name": name,
            "email": email,
            "phone": phone,
            "is_vip": False,
            "loyalty_points": 0.0
            })
            aplication_task.print_line(f"[CREATE] Customer with id={new_cust_id}")
        except:
            raise ValueError("Couldn't Create new customer")





    def ReadCustomer(self):
        aplication_task.print_title("ReadCustomer")
    def UpdateCustomer(self):
        aplication_task.print_title("UpdateCustomer")
    def DeleteCustomer(self):
        aplication_task.print_title("DeleteCustomer")
    def LoadCustomer(self):
        aplication_task.print_title("LoadFromFileCustomer")