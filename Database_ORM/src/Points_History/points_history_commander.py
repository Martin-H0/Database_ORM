from database.generic_mapper import GenericMapper
from models.points_history import PointsHistoryMapper
import get_safe_value
import aplication_task


class PointsHistoryCommander:

    points_history_mapper = PointsHistoryMapper()
    
    def __init__(self):
        # self.model_command = model_command
        self.generic_mapper = GenericMapper(self)

    def CreatePointsHistory(self):
        aplication_task.print_title("CreatePointsHistory")
    def ReadPointsHistory(self):
        aplication_task.print_title("ReadPointsHistory")
    def UpdatePointsHistory(self):
        aplication_task.print_title("UpdatePointsHistory")
    def DeletePointsHistory(self):
        aplication_task.print_title("DeletePointsHistory")
    def LoadPointsHistory(self):
        aplication_task.print_title("LoadFromFilePointsHistory")