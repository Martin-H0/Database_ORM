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











# class GenericMapper:
#     def __init__(self, db, table_name: str):
#         """
#         db: instanci třídy Database
#         table_name: název tabulky (např. 'customer')
#         """
#         self.db = db
#         self.table_name = table_name
#         self.columns_info = []  # Bude obsahovat list tuple (col_name, col_type)
#         self.fetch_columns()

#     def fetch_columns(self):
#         """
#         Načte si metadata o sloupcích pomocí DESCRIBE
#         a uloží do self.columns_info.
#         """
#         self.columns_info = self.db.get_table_columns(self.table_name)

#     def _mysql_type_to_python(self, mysql_type: str):
#         """
#         Převede název MySQL typu (např. 'varchar(100)', 'int(11)', 'date')
#         na odpovídající Python typ. Zde to pojmeme velmi jednoduše a hrubě.
#         """
#         mysql_type_lower = mysql_type.lower()

#         if 'int' in mysql_type_lower:
#             return int
#         elif 'float' in mysql_type_lower or 'double' in mysql_type_lower or 'decimal' in mysql_type_lower:
#             return float
#         elif 'char' in mysql_type_lower or 'text' in mysql_type_lower:
#             return str
#         elif 'date' in mysql_type_lower or 'time' in mysql_type_lower or 'datetime' in mysql_type_lower:
#             return datetime  # Můžeme pak ukládat jako string nebo datetime
#         elif 'bit' in mysql_type_lower:
#             return bool
#         elif 'enum' in mysql_type_lower:
#             # Enum vrátíme také jako str, bude obsahovat jednu z hodnot definovaných v DB
#             return str
#         else:
#             return str

#     def _python_value_to_sql(self, py_value, py_type):
#         """
#         Převede hodnotu z Pythonu do stringu, který lze vložit do SQL dotazu.
#         Zároveň se postará o ošetření typů (např. string do uvozovek).
        
#         V reálné aplikaci doporučuji používat parametrizované dotazy
#         (např. cursor.execute(sql, params)) místo skládání řetězců!
#         """
#         if py_value is None:
#             return "NULL"
#         elif py_type == str or py_type == datetime:
#             return f"'{py_value}'"
#         elif py_type == bool:
#             return "1" if py_value else "0"
#         else:
#             return str(py_value)

#     def create(self, data: dict):
#         """
#         Vytvoří nový záznam (INSERT).
#         data: dictionary {col_name: value, ...}.
#         """
#         col_names = []
#         col_values = []

#         for col_name, col_type in self.columns_info:
#             # Vynecháme sloupec id, pokud je AUTO_INCREMENT
#             #if col_name.lower() == 'id':
#             #   continue

#             if col_name in data:
#                 py_type = self._mysql_type_to_python(col_type)
#                 value_sql_str = self._python_value_to_sql(data[col_name], py_type)
#                 col_names.append(col_name)
#                 col_values.append(value_sql_str)
        
#         # Vytvoříme SQL
#         sql = f"INSERT INTO {self.table_name} ({', '.join(col_names)}) VALUES ({', '.join(col_values)})"
        
#         conn = self.db.get_connection()
#         cursor = conn.cursor()
#         cursor.execute(sql)
#         conn.commit()
#         new_id = cursor.lastrowid
#         cursor.close()
#         return new_id

#     def read(self, record_id: int):
#         """
#         Načte záznam podle primárního klíče (id).
#         """
#         sql = f"SELECT * FROM {self.table_name} WHERE id = %s"
#         conn = self.db.get_connection()
#         cursor = conn.cursor(dictionary=True)
#         cursor.execute(sql, (record_id,))
#         result = cursor.fetchone()
#         cursor.close()
#         return result

#     def update(self, record_id: int, data: dict):
#         """
#         Aktualizuje záznam s daným id (UPDATE).
#         data: dictionary {col_name: value, ...}.
#         """
#         set_parts = []
#         for col_name, col_type in self.columns_info:
#             if col_name.lower() == 'id':
#                 continue

#             if col_name in data:
#                 py_type = self._mysql_type_to_python(col_type)
#                 value_sql_str = self._python_value_to_sql(data[col_name], py_type)
#                 set_parts.append(f"{col_name} = {value_sql_str}")

#         set_clause = ", ".join(set_parts)
#         sql = f"UPDATE {self.table_name} SET {set_clause} WHERE id = %s"

#         conn = self.db.get_connection()
#         cursor = conn.cursor()
#         cursor.execute(sql, (record_id,))
#         conn.commit()
#         affected_rows = cursor.rowcount
#         cursor.close()
#         return affected_rows

#     def delete(self, record_id: int):
#         """
#         Smaže záznam s daným id (DELETE).
#         """
#         sql = f"DELETE FROM {self.table_name} WHERE id = %s"
#         conn = self.db.get_connection()
#         cursor = conn.cursor()
#         cursor.execute(sql, (record_id,))
#         conn.commit()
#         affected_rows = cursor.rowcount
#         cursor.close()
#         return affected_rows
#         #se asi po pro4 prost2 nemu6u m9t DAO pro v3echno u6 bz to bzlo tak 20x hotov0 a je3t2 yase p93 s eng klavesnic9 do 5iti