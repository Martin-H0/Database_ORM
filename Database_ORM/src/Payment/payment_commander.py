from database.generic_mapper import GenericMapper
from models.payment import PaymentMapper
import get_safe_value
import aplication_task


class PaymentCommander:

    payment_mapper = PaymentMapper()
    
    def __init__(self):
        # self.model_command = model_command
        self.generic_mapper = GenericMapper(self)

    def CreatePayment(self):
        aplication_task.print_title("CreatePayment")
    def ReadPayment(self):
        aplication_task.print_title("ReadPayment")
    def UpdatePayment(self):
        aplication_task.print_title("UpdatePayment")
    def DeletePayment(self):
        aplication_task.print_title("DeletePayment")
    def LoadPayment(self):
        aplication_task.print_title("LoadFromFilePayment")