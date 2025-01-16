# interface/Points_History/points_history_interface.py
from src.Points_History.points_history_commander import PointsHistoryCommander
import aplication_task
# from interface import MainInterface
class PointsHistoryInterface:
    def __init__(self):
        self.isrunning = True

        self.commands = {}
        self.commands["help"] = self.menu_input
        self.commands["exit"] = self.exit
        # self.commands["create"] = PointsHistoryCommander().CreatePointsHistory
        # self.commands["read"] = PointsHistoryCommander().ReadPointsHistory
        # self.commands["update"] = PointsHistoryCommander().UpdatePointsHistory
        # self.commands["delete"] = PointsHistoryCommander().DeletePointsHistory
        # self.commands["fromfile"] = PointsHistoryCommander().LoadPointsHistory


    def exit(self):
        self.isrunning = False

    def menu_input(self):
        print("create:   Create points_history")
        print("read:     Read points_history")
        print("update:   Update points_history")
        print("delete:   Delete points_history")
        print("fromfile: Load points_history from file")
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

        



    



    
    