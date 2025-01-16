import random, csv
import random, datetime, decimal, threading
import json
from database.generic_mapper import GenericMapper
from models.customer import CustomerMapper
from get_safe_value import*
import aplication_task

class CustomerComander:
    

    
    def __init__(self, model_command):
        self.model_command = model_command
        self.generic_mapper = GenericMapper(self)

    def print_line(self, mesage="default_mesage"):
        print(mesage)


    def CreateCustomer(self):
        aplication_task.print_title("CreateCustomer")
        name = input("Enter customer name: ")
        try:
            name = decimal.Decimal(name)
        except:
            raise ValueError("Couldn't parse name as a decimal")
    def ReadCustomer(self):
        aplication_task.print_title("ReadCustomer")
    def UpdateCustomer(self):
        aplication_task.print_title("UpdateCustomer")
    def DeleteCustomer(self):
        aplication_task.print_title("DeleteCustomer")
    def LoadCustomer(self):
        aplication_task.print_title("LoadFromFileCustomer")