from database.generic_mapper import GenericMapper

class ViewReservationDetailsMapper(GenericMapper):
    def __init__(self):    # self, db
        super().__init__("view_reservation_details")  # db, "customer"