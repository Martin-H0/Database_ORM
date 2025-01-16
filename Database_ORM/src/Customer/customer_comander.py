import random, csv
import random, datetime, decimal, threading
import json
from database.generic_mapper import GenericMapper
from models.customer import CustomerMapper

class CustomerComander:
    

    
    def __init__(self, model_command):
        self.model_command = model_command
        self.generic_mapper = GenericMapper(self)

    def print_title(self, title="default_title" , symbol="="):
        """Slou69 pro v7pis odn2lovac9 48rz"""
        print(symbol * 60)
        print(title)
        print(symbol * 60)
    def print_line(self, mesage="default_mesage"):
        print(mesage)


    def CreateCustomer(self):
        self.print_title("CreateCustomer")
        name = input("Amount to transfer: ")
        try:
            name = decimal.Decimal(name)
        except:
            raise ValueError("Couldn't parse name as a decimal")
    def ReadCustomer(self):
        self.print_title("ReadCustomer")
    def UpdateCustomer(self):
        self.print_title("UpdateCustomer")
    def DeleteCustomer(self):
        self.print_title("DeleteCustomer")
    def LoadCustomer(self):
        self.print_title("LoadFromFileCustomer")