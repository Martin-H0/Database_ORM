# src/Report/costumer_interface.py
# from src.Report.report_comander import ReportCommander # ReadReport, CreateReport, UpdateReport, DeleteReport, LoadReport
from src.Report.report_commander import RoomCommander
import aplication_task
# from interface import MainInterface
class ReportInterface:
    def __init__(self):
        self.isrunning = True

        self.report_commander = RoomCommander()

        self.commands = {
            "help": self.menu_input,
            "exit": self.exit,
            "customer_point": self.report_commander.view_CP,
            "invoice_sum": self.report_commander.view_IS,
            "res_detail": self.report_commander.view_RM,
        }
        # self.commands["help"] = self.menu_input
        # self.commands["exit"] = self.exit
        # self.commands["create"] = create_report()
        # self.commands["read"] = report_mapper.read_c
        # self.commands["update"] = ReportCommander().UpdateReport
        # self.commands["delete"] = ReportCommander().DeleteReport
        # self.commands["fromfile"] = ReportCommander().LoadReport


    def exit(self):
        self.isrunning = False

    def menu_input(self):
        print("customer_point:   View Customer points")
        print("invoice_sum:      View Sumay ")
        print("res_detail:       View reservation detail")
        print("exit:             Back to Main Menu")

    def run(self):
        self.isrunning = True
        aplication_task.print_title("Report")
        self.menu_input()
        while self.isrunning:
            try:
                cmd = input("report: ")
                if cmd in self.commands:
                    self.commands[cmd]()
                else:
                    print("Unknown command")
            except EOFError:
                self.isrunning = False
            except Exception as error:
                print("Error:", error)
        print("EXIT")

        



    



    
    