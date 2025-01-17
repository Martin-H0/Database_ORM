# src/Customer/costumer_interface.py
# from src.Customer.customer_comander import CustomerCommander # ReadCustomer, CreateCustomer, UpdateCustomer, DeleteCustomer, LoadCustomer
from src.Customer.customer_comander import  CustomerCommander
import aplication_task
# from interface import MainInterface
class CustomerInterface:
    def __init__(self):
        self.isrunning = True

        self.customer_commander = CustomerCommander()

        self.commands = {
            "help": self.menu_input,
            "exit": self.exit,
            "create": self.customer_commander.create_customer,
            "read": self.customer_commander.read_customer,
            "update": self.customer_commander.update_customer,
            "delete": self.customer_commander.delete_customer,
            "fromfile": self.customer_commander.load_customers_from_file,
        }
        # self.commands["help"] = self.menu_input
        # self.commands["exit"] = self.exit
        # self.commands["create"] = create_customer()
        # self.commands["read"] = customer_mapper.read_c
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

        



    



    
    