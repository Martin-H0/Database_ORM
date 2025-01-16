# src/Customer/costumer_interface.py
from src.Customer.customer_comander import CustomerCommander
import aplication_task
# from interface import MainInterface
class CustomerInterface:
    def __init__(self):
        self.isrunning = True

        self.commands = {}
        self.commands["help"] = self.menu_input
        self.commands["exit"] = self.exit
        # self.commands["create"] = CustomerCommander().CreateCustomer
        # self.commands["read"] = CustomerCommander().ReadCustomer
        # self.commands["update"] = CustomerCommander().UpdateCustomer
        # self.commands["delete"] = CustomerCommander().DeleteCustomer
        # self.commands["fromfile"] = CustomerCommander().LoadCustomer


    def exit(self):
        self.isrunning = False

    def menu_input(self):
        print("create:   Create customer")
        print("read:     Read customer")
        print("update:   Update customer")
        print("delete:   Delete customer")
        print("fromfile: Load customer from file")
        print("exit:     Back to Main Menu")

    def run(self):
        self.isrunning = True
        aplication_task.print_title("Customer")
        self.menu_input()
        while self.isrunning:
            try:
                cmd = input("customer: ")
                if cmd in self.commands:
                    self.commands[cmd]()
                else:
                    print("Unknown command")
            except EOFError:
                self.isrunning = False
            except Exception as error:
                print("Error:", error)
        print("EXIT")

        



    



    
    