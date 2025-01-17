# interface/Room/room_interface.py
from src.Room.room_commander import RoomCommander
import aplication_task
#
class RoomInterface:
    def __init__(self):
        self.isrunning = True

        self.room_commander = RoomCommander()

        self.commands = {
            "help": self.menu_input,
            "exit": self.exit,
            "create": self.room_commander.create_room,
            "read": self.room_commander.read_room,
            "update": self.room_commander.update_room,
            "delete": self.room_commander.delete_room,

        }
        # self.commands["fromfile"] = RoomCommander().LoadRoom


    def exit(self):
        self.isrunning = False

    def menu_input(self):
        print("create:   Create room")
        print("read:     Read room")
        print("update:   Update room")
        print("delete:   Delete room")
        # print("fromfile: Load room from file")
        print("exit:     Back to Main Menu")

    def run(self):
        self.isrunning = True
        aplication_task.print_title("Room")
        self.menu_input()
        while self.isrunning:
            try:
                cmd = input("room: ")
                if cmd in self.commands:
                    self.commands[cmd]()
                else:
                    print("Unknown command")
            except EOFError:
                self.isrunning = False
            except Exception as error:
                print("Error:", error)
        print("EXIT")