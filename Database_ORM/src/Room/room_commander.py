from database.generic_mapper import GenericMapper
from models.room import RoomMapper
import get_safe_value
import aplication_task


class RoomCommander:

    room_mapper = RoomMapper()
    
    def __init__(self):
        # self.model_command = model_command
        self.generic_mapper = GenericMapper(self)

    def CreateRoom(self):
        aplication_task.print_title("CreateRoom")
    def ReadRoom(self):
        aplication_task.print_title("ReadRoom")
    def UpdateRoom(self):
        aplication_task.print_title("UpdateRoom")
    def DeleteRoom(self):
        aplication_task.print_title("DeleteRoom")
    def LoadRoom(self):
        aplication_task.print_title("LoadFromFileRoom")