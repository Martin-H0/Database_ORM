# interface/Room/room_interface.py
from src.Room.room_commander import RoomCommander
import aplication_task
#
class RoomInterface:
    def __init__(self):
        self.isrunning = True

        self.commands = {}
        self.commands["help"] = self.menu_input
        self.commands["exit"] = self.exit
        # self.commands["create"] = RoomCommander().CreateRoom
        # self.commands["read"] = RoomCommander().ReadRoom
        # self.commands["update"] = RoomCommander().UpdateRoom
        # self.commands["delete"] = RoomCommander().DeleteRoom
        # self.commands["fromfile"] = RoomCommander().LoadRoom


    def exit(self):
        self.isrunning = False

    def menu_input(self):
        print("create:   Create room")
        print("read:     Read room")
        print("update:   Update room")
        print("delete:   Delete room")
        print("fromfile: Load room from file")
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