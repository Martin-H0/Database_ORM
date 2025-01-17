# interface/reservation_room_interface.py
from src.Reservation_Room.reservation_room_commander import ReservationRoomCommander
import aplication_task
# from interface import MainInterface2
class ReservationRoomInterface:
    def __init__(self):
        self.isrunning = True

        self.reservation_room_commander = ReservationRoomCommander()

        self.commands = {
            "help": self.menu_input,
            "exit": self.exit,
            "create": self.reservation_room_commander.create_reservation_room,
            "read": self.reservation_room_commander.read_reservation_room,
            "update": self.reservation_room_commander.update_reservation_room,
            "delete": self.reservation_room_commander.delete_reservation_room,     
        }


    def exit(self):
        self.isrunning = False

    def menu_input(self):
        print("create:   Create reservation_room")
        print("read:     Read reservation_room")
        print("update:   Update reservation_room")
        print("delete:   Delete reservation_room")
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

