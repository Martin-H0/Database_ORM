# database/procedure_mapper.py
from database_singleton import DatabaseSingleton
from database_singleton import* 

class ProcedureMapper:
    def __init__(self):
        pass

    def call_transfer_points(self, from_id, to_id, amount):
        """Calls the proc_transfer_points stored procedure."""
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        cursor.execute("CALL proc_transfer_points(%s, %s, %s)", (from_id, to_id, amount))
        conn.commit()
        DatabaseSingleton.close_conn()

    def call_calculate_total_reservation_cost(self, reservation_id):
        """Calls the proc_calculate_total_reservation_cost stored procedure."""
        conn = DatabaseSingleton()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("CALL proc_calculate_total_reservation_cost(%s)", (reservation_id,))
        result = cursor.fetchone()
        DatabaseSingleton.close_conn()
        return result['total_cost'] if result else None
    

    def call_add_payment(self, reservation_id, amount, method, add_points):
        """Calls the proc_add_payment stored procedure."""
        conn = DatabaseSingleton()
        cursor = conn.cursor(dictionary=True)
        result = None
        try:
            cursor.execute("START TRANSACTION;")
            cursor.execute(
                "CALL proc_add_payment(%s, %s, %s, %s)",
                (reservation_id, amount, method, add_points),
            )
            # Process all result sets to avoid sync issues
            while cursor.nextset():
                pass
            # Fetch the result if there is a valid row
            if cursor.with_rows:
                result = cursor.fetchone()
            cursor.execute("COMMIT;")
        except Exception as e:
            cursor.execute("ROLLBACK;")
            print(f"Error during transaction: {e}")
        finally:
            cursor.close()  # Ensure cursor is closed
            DatabaseSingleton.close_conn()
        # return result['new_payment_id'] if result else None














    # def call_add_payment(self, reservation_id, amount, method, add_points):
    #     """Calls the proc_add_payment stored procedure."""
    #     conn = DatabaseSingleton()
    #     cursor = conn.cursor(dictionary=True)
    #     result = None
    #     try:
    #         cursor.execute("START TRANSACTION;")
    #         cursor.execute(
    #             "CALL proc_add_payment(%s, %s, %s, %s)",
    #             (reservation_id, amount, method, add_points),
    #         )
    #         # Process all result sets to avoid sync issues
    #         while cursor.nextset():
    #             pass
    #         # Fetch the result if there is a valid row
    #         if cursor.with_rows:
    #             result = cursor.fetchone()
    #         cursor.execute("COMMIT;")
    #     except Exception as e:
    #         cursor.execute("ROLLBACK;")
    #         print(f"Error during transaction: {e}")
    #     finally:
    #         cursor.close()  # Ensure cursor is closed
    #         DatabaseSingleton.close_conn()
    #     return result['new_payment_id'] if result else None

    




    

    # def call_add_payment(self, reservation_id, amount, method, add_points):
    #     """Calls the proc_add_payment stored procedure."""
    #     conn = DatabaseSingleton()
    #     cursor = conn.cursor()
    #     try:
    #         cursor.execute("START TRANSACTION;")
    #         cursor.execute("CALL proc_add_payment(%s, %s, %s, %s)", (reservation_id, amount, method, add_points))
    #     except Exception as e:
    #         print(e)
    #         cursor.execute("ROLLBACK;")
    #     else:
    #         cursor.execute("COMMIT;")
    #     finally:
    #         result = cursor.fetchone()
    #         DatabaseSingleton.close_conn()
    #     return result['new_payment_id'] if result else None
    