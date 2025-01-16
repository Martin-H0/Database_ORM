# interface/reservation_room_interface.py
from src.Reservation_Room.reservation_room_commander import ReservationRoomCommander
import aplication_task
# from interface import MainInterface2
class ReservationRoomInterface:
    def __init__(self):
        self.isrunning = True

        self.commands = {}
        self.commands["help"] = self.menu_input
        self.commands["exit"] = self.exit
        # self.commands["create"] = ReservationRoomCommander().CreateReservationRoom
        # self.commands["read"] = ReservationRoomCommander().ReadReservationRoom
        # self.commands["update"] = ReservationRoomCommander().UpdateReservationRoom
        # self.commands["delete"] = ReservationRoomCommander().DeleteReservationRoom
        # self.commands["fromfile"] = ReservationRoomCommander().LoadReservationRoom


    def exit(self):
        self.isrunning = False

    def menu_input(self):
        print("create:   Create reservation_room")
        print("read:     Read reservation_room")
        print("update:   Update reservation_room")
        print("delete:   Delete reservation_room")
        print("fromfile: Load reservation_room from file")
        print("exit:     Back to Main Menu")

    def run(self):
        self.isrunning = True
        aplication_task.print_title("ReservationRoom")
        self.menu_input()
        while self.isrunning:
            try:
                cmd = input("reservation_room: ")
                if cmd in self.commands:
                    self.commands[cmd]()
                else:
                    print("Unknown command")
            except EOFError:
                self.isrunning = False
            except Exception as error:
                print("Error:", error)
        print("EXIT")

