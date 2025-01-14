import mysql.connector
import json

class DatabaseSingleton:
    """
    Singleton pro práci s MySQL databází.
    Načítá konfiguraci z config.json (host, port, user, password, database).
    Poskytuje metody:
      - connect()
      - get_connection()
      - close()
      - get_table_columns(table_name)
    které využívá GenericMapper.
    """

    _instance = None  # Sdílená instance (singleton)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            cls._instance._init_config()
            cls._instance._connection = None
        return cls._instance

    def _init_config(self):
        """Načtení konfigurace z config.json"""
        with open("./Database_ORM/config.json","r") as f:
            config = json.load(f)
            db_conf = config["database"]

        self.host = db_conf.get("host", "localhost")
        self.port = db_conf.get("port", 3306)
        self.user = db_conf.get("user", "root")
        self.password = db_conf.get("password", "")
        self.database = db_conf.get("database", "")

    def connect(self):
        """Otevře připojení, pokud ještě není otevřené."""
        if self._connection is None or not self._connection.is_connected():
            self._connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )

    def get_connection(self):
        """Vrací aktivní připojení. Pokud není aktivní, znovu se připojí."""
        if self._connection is None or not self._connection.is_connected():
            self.connect()
        return self._connection

    def close(self):
        """Uzavře připojení k databázi."""
        if self._connection and self._connection.is_connected():
            self._connection.close()
            self._connection = None

    def get_table_columns(self, table_name: str):
        """
        Vykoná DESCRIBE table_name a vrátí list tuple (col_name, col_type).
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(f"DESCRIBE {table_name}")
        columns = []
        for col_name, col_type, _, _, _, _ in cursor.fetchall():
            columns.append((col_name, col_type))
        cursor.close()
        return columns