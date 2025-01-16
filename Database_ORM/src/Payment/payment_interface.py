# src/Payment/payment_interface.py

from src.Payment.payment_commander import PaymentCommander
import aplication_task

class PaymentInterface:
    def __init__(self):
        self.isrunning = True

        self.commands = {}
        self.commands["help"] = self.menu_input
        self.commands["exit"] = self.exit
        # self.commands["create"] = PaymentCommander().CreatePayment
        # self.commands["read"] = PaymentCommander().ReadPayment
        # self.commands["update"] = PaymentCommander().UpdatePayment
        # self.commands["delete"] = PaymentCommander().DeletePayment
        # self.commands["fromfile"] = PaymentCommander().LoadPayment


    def exit(self):
        self.isrunning = False

    def menu_input(self):
        print("create:   Create payment")
        print("read:     Read payment")
        print("update:   Update payment")
        print("delete:   Delete payment")
        print("fromfile: Load payment from file")
        print("exit:     Back to Main Menu")

    def run(self):
        self.isrunning = True
        aplication_task.print_title("Payment")
        self.menu_input()
        while self.isrunning:
            try:
                cmd = input("payment: ")
                if cmd in self.commands:
                    self.commands[cmd]()
                else:
                    print("Unknown command")
            except EOFError:
                self.isrunning = False
            except Exception as error:
                print("Error:", error)
        print("EXIT")