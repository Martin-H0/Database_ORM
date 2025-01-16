from database.generic_mapper import GenericMapper
from models.reservation import ReservationMapper
import get_safe_value
import aplication_task


class ReservationCommander:

    reservation_mapper = ReservationMapper()
    
    def __init__(self):
        # self.model_command = model_command
        self.generic_mapper = GenericMapper(self)

    def CreateReservation(self):
        aplication_task.print_title("CreateReservation")
    def ReadReservation(self):
        aplication_task.print_title("ReadReservation")
    def UpdateReservation(self):
        aplication_task.print_title("UpdateReservation")
    def DeleteReservation(self):
        aplication_task.print_title("DeleteReservation")
    def LoadReservation(self):
        aplication_task.print_title("LoadFromFileReservation")