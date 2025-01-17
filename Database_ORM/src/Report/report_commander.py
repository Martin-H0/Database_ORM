import csv
import os
from database.generic_mapper import GenericMapper
from report.view_customer_points import ViewCustomerPointsMapper
from report.view_invoice_summary import ViewInvoiceSummaryMapper
from report.view_reservation_details import ViewReservationDetailsMapper
import get_safe_value
import aplication_task

class RoomCommander:
    """Handles CRUD operations for rooms using RoomMapper."""

    def __init__(self):
        self.view_customer_points = ViewCustomerPointsMapper()
        self.view_invoice_summary = ViewInvoiceSummaryMapper()
        self.view_reservation_details = ViewReservationDetailsMapper()

    def view_CP(self):
        aplication_task.print_title("VIEW COSTUMER POINTS")
        cust_data = self.view_customer_points.read_all()
        for e in cust_data:
            aplication_task.print_line(e)

    def view_IS(self):
        aplication_task.print_title("VIEW SUMMARY MAPPER")
        cust_data = self.view_invoice_summary.read_all()
        for e in cust_data:
            print (e)

    def view_RM(self):
        aplication_task.print_title("VIEW RESERVATION DETAILS")
        cust_data = self.view_reservation_details.read_all()
        for e in cust_data:
            print (e)

