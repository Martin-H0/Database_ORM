from database.generic_mapper import GenericMapper
from models.reservation_room import ReservationRoomMapper
import get_safe_value
import aplication_task


class ReservationRoomCommander:

    reservation_room_mapper = ReservationRoomMapper()
    
    def __init__(self):
        # self.model_command = model_command
        self.generic_mapper = GenericMapper(self)

    def CreateReservationRoom(self):
        aplication_task.print_title("CreateReservationRoom")
    def ReadReservationRoom(self):
        aplication_task.print_title("ReadReservationRoom")
    def UpdateReservationRoom(self):
        aplication_task.print_title("UpdateReservationRoom")
    def DeleteReservationRoom(self):
        aplication_task.print_title("DeleteReservationRoom")
    def LoadReservationRoom(self):
        aplication_task.print_title("LoadFromFileReservationRoom")