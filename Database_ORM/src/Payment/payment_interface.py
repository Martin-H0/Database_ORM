# src/Payment/payment_interface.py

from src.Payment.payment_commander import PaymentCommander
import aplication_task

class PaymentInterface:
    def __init__(self):
        self.isrunning = True

        self.payment_commander = PaymentCommander()

        self.commands = {
            "help": self.menu_input,
            "exit": self.exit,
            "create": self.payment_commander.create_payment,
            "read": self.payment_commander.read_payment,
            # "update": self.payment_commander.update_payment,
            # "delete": self.payment_commander.delete_payment,
        }



    def exit(self):
        self.isrunning = False

    def menu_input(self):
        print("create:   Create payment")
        print("read:     Read payment")
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