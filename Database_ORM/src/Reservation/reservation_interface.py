# interface/Reservation/reservation_interface.py
from src.Reservation.reservation_commander import ReservationCommander
import aplication_task
# from interface import MainInterface
class ReservationInterface:
    def __init__(self):
        self.isrunning = True

        self.commands = {}
        self.commands["help"] = self.menu_input
        self.commands["exit"] = self.exit
        # self.commands["create"] = ReservationCommander().CreateReservation
        # self.commands["read"] = ReservationCommander().ReadReservation
        # self.commands["update"] = ReservationCommander().UpdateReservation
        # self.commands["delete"] = ReservationCommander().DeleteReservation
        # self.commands["fromfile"] = ReservationCommander().LoadReservation


    def exit(self):
        self.isrunning = False

    def menu_input(self):
        print("create:   Create reservation")
        print("read:     Read reservation")
        print("update:   Update reservation")
        print("delete:   Delete reservation")
        print("fromfile: Load reservation from file")
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
