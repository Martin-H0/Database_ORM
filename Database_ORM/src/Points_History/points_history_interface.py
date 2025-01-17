# interface/Points_History/points_history_interface.py
from src.Points_History.points_history_commander import PointsHistoryCommander
import aplication_task
# from interface import MainInterface
class PointsHistoryInterface:
    def __init__(self):
        self.isrunning = True

        self.points_history_mapper = PointsHistoryCommander()

        self.commands = {
                        "help": self.menu_input,
            "exit": self.exit,
            "read": self.points_history_mapper.read_points_history,
        }


    def exit(self):
        self.isrunning = False

    def menu_input(self):
        print("read:     Read points_history")
        print("exit:     Back to Main Menu")

    def run(self):
        self.isrunning = True
        aplication_task.print_title("PointsHistory")
        self.menu_input()
        while self.isrunning:
            try:
                cmd = input("points_history: ")
                if cmd in self.commands:
                    self.commands[cmd]()
                else:
                    print("Unknown command")
            except EOFError:
                self.isrunning = False
            except Exception as error:
                print("Error:", error)
        print("EXIT")

        



    



    
    