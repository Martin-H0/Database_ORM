# database/generic_mapper.py
import re
from datetime import datetime
from database_singleton import* 

class GenericMapper:
    def __init__(self, table_name: str):
        """
        db: instance DatabaseSingleton
        table_name: např. 'customer', 'room', ...
        """
        # self.db = db
        self.table_name = table_name
        self.columns_info = []
        self.fetch_columns()
    
    def get_table_columns(self, table_name: str):
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        cursor.execute(f"DESCRIBE {table_name}")
        columns = []
        for i in cursor.fetchall():
            columns.append((i[0],i[1]))
        DatabaseSingleton.close_conn()
        return columns

    def fetch_columns(self):

        self.columns_info = self.get_table_columns(self.table_name)

    def _mysql_type_to_python(self, mysql_type: str):
        mysql_type_lower = mysql_type.lower()
        if 'int' in mysql_type_lower:
            return int
        elif ('float' in mysql_type_lower or 'double' in mysql_type_lower 
              or 'decimal' in mysql_type_lower):
            return float
        elif 'char' in mysql_type_lower or 'text' in mysql_type_lower:
            return str
        elif 'date' in mysql_type_lower or 'time' in mysql_type_lower or 'datetime' in mysql_type_lower:
            return datetime
        elif 'bit' in mysql_type_lower:
            return bool
        elif 'enum' in mysql_type_lower:
            return str
        else:
            return str

    def _python_value_to_sql(self, py_value, py_type):
        """
        Převede Python hodnotu do SQL řetězce (zjednodušeně).
        V reálu používejte raději parametrizované dotazy!
        """
        if py_value is None:
            return "NULL"

        # Příklad jednoduché "ochrany" proti drop table
        if py_type == str:
            if re.search(r"drop\s+table", py_value, re.IGNORECASE):
                raise ValueError("Nalezen potenciálně nebezpečný řetězec (DROP TABLE) ve vstupu!")
            return f"'{py_value}'"

        if py_type == bool:
            return "1" if py_value else "0"

        return str(py_value)

    def _check_id_exists(self, table_name: str, record_id: int) -> bool:
        """
        Ověří, zda v tabulce existuje záznam s daným ID.
        Vrací True/False.
        """
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE id = %s", (record_id,))
        (count,) = cursor.fetchone()
        DatabaseSingleton.close_conn()
        return (count > 0)

    def create(self, data: dict):
        """
        INSERT. Vrátí ID nového záznamu.
        """
        col_names = []
        col_values = []

        for col_name, col_type in self.columns_info:
            if col_name.lower() == 'id':
                continue
            if col_name in data:
                py_type = self._mysql_type_to_python(col_type)
                value_sql_str = self._python_value_to_sql(data[col_name], py_type)
                col_names.append(col_name)
                col_values.append(value_sql_str)

        sql = f"INSERT INTO {self.table_name} ({', '.join(col_names)}) VALUES ({', '.join(col_values)})"
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        new_id = cursor.lastrowid
        DatabaseSingleton.close_conn()
        return new_id

    def read(self, record_id: int):
        """
        SELECT * FROM table WHERE id = record_id.
        Pokud záznam neexistuje, vrátí None.
        """
        sql = f"SELECT * FROM {self.table_name} WHERE id = %s"
        conn = DatabaseSingleton()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, (record_id,))
        result = cursor.fetchone()
        DatabaseSingleton.close_conn()
        return result
    

    def read_all(self):
        """
        SELECT * FROM table.
        Pokud záznam neexistuje, vrátí None.
        """
        sql = f"SELECT * FROM {self.table_name}"
        conn = DatabaseSingleton()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql,)
        result = cursor.fetchall()
        DatabaseSingleton.close_conn()
        return result

    def update(self, record_id: int, data: dict):
        """
        UPDATE záznamu s daným id.
        Vrátí počet upravených řádků (0 nebo 1).
        """
        set_parts = []
        for col_name, col_type in self.columns_info:
            if col_name.lower() == 'id':
                continue
            if col_name in data:
                py_type = self._mysql_type_to_python(col_type)
                value_sql_str = self._python_value_to_sql(data[col_name], py_type)
                set_parts.append(f"{col_name} = {value_sql_str}")

        if not set_parts:
            return 0  # nic k update

        sql = f"UPDATE {self.table_name} SET {', '.join(set_parts)} WHERE id = %s"
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        cursor.execute(sql, (record_id,))
        conn.commit()
        affected_rows = cursor.rowcount
        DatabaseSingleton.close_conn()
        return affected_rows

    def delete(self, record_id: int):
        """
        DELETE záznamu s daným id.
        Vrátí počet smazaných řádků (0 nebo 1).
        """
        sql = f"DELETE FROM {self.table_name} WHERE id = %s"
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        cursor.execute(sql, (record_id,))
        conn.commit()
        affected_rows = cursor.rowcount
        DatabaseSingleton.close_conn()
        return affected_rows
