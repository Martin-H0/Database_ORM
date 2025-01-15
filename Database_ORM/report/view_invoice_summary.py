# report/view_invoice_summary.py
from database.generic_mapper import GenericMapper

class ViewInvoiceSummaryMapper(GenericMapper):
    def __init__(self):    # self, db
        super().__init__("view_invoice_summary")  # db, "customer"