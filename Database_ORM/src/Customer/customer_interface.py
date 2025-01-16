# src/Customer/costumer_interface.py
from src.Customer.customer_comander import CustomerComander
# from interface import MainInterface
class CustomerInterface:
    def __init__(self):
        self.isrunning = True

        self.commands = {}
        self.commands["exit"] = self.exit
        # self.commands["customer"] = CustomerInterface().run()
        # self.commands["room"] = bankinterface.BankInterface().start
        # self.commands["reservation"] = accountinterface.AccountInterface().start
        # self.commands["payment"] = transactioninterface.TransactionInterface().start

    def exit(self):
        self.isrunning = False
    def menu_input(self):
        print("help: Display this")
        print("exit: Exit")
        print("customer: Manage customers")
        print("room: Manage rooms")
        print("reservation: Manage reservations")
        print("payment: pay")
        print("transaction: Manage reservation_room")
        print("transaction: Manage LP points")

    def run(self):
        self.isrunning = True
        self.print_line()
        print("Welcome to ORM databse system")
        self.menu_input()
        while self.isrunning:
            try:
                cmd = input(": ")
                if cmd in self.commands:
                    self.commands[cmd]()
                else:
                    print("Unknown command")
            except EOFError:
                self.isrunning = False
            except Exception as error:
                print("Error:", error)
        print("EXIT")

        
    def print_line(self, symbol="="):
        """Slou69 pro v7pis odn2lovac9 48rz"""
        print(symbol * 60)

    



    
    