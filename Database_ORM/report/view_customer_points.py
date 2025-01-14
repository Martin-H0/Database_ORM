from database.generic_mapper import GenericMapper

class ViewCustomerPointsMapper(GenericMapper):
    def __init__(self):    # self, db
        super().__init__("view_customer_points")  # db, "customer"