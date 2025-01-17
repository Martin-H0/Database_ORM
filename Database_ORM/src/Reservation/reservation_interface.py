# interface/Reservation/reservation_interface.py
from src.Reservation.reservation_commander import ReservationCommander
import aplication_task
# from interface import MainInterface
class ReservationInterface:
    def __init__(self):
        self.isrunning = True

        self.reservation_commander = ReservationCommander()

        self.commands = {
            "help": self.menu_input,
            "exit": self.exit,
            "create": self.reservation_commander.create_reservation,
            "read": self.reservation_commander.read_reservation,
            "update": self.reservation_commander.update_reservation,
            "delete": self.reservation_commander.delete_reservation,

        }

    def exit(self):
        self.isrunning = False

    def menu_input(self):
        print("create:   Create reservation")
        print("read:     Read reservation")
        print("update:   Update reservation")
        print("delete:   Delete reservation")
        # print("fromfile: Load reservation from file")
        print("exit:     Back to Main Menu")

    def run(self):
        self.isrunning = True
        aplication_task.print_title("Reservation")
        self.menu_input()
        while self.isrunning:
            try:
                cmd = input("reservation: ")
                if cmd in self.commands:
                    self.commands[cmd]()
                else:
                    print("Unknown command")
            except EOFError:
                self.isrunning = False
            except Exception as error:
                print("Error:", error)
        print("EXIT")
