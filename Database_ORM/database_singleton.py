import mysql.connector
import json

class DatabaseSingleton:
    conn = None

    def __new__(cls):
        if not cls.conn:
            cls.new_conn()
        return cls.conn
    
    @classmethod
    def new_conn(cls):
        connection = mysql.connector.connect(
        host=cls.readconfig("host"),
        port=cls.readconfig("port"),
        user=cls.readconfig("user"),
        password=cls.readconfig("password"),
        database=cls.readconfig("database"),
        )
        cls.conn = connection
    
    @classmethod
    def close_conn(cls):
        if(cls.conn):
            cls.conn.close()
            cls.conn = None

    @classmethod
    def readconfig(cls,key):
        with open("./Database_ORM/config.json","r") as f:
            config = json.load(f)
            return config["database"][key]
    
    



conn = DatabaseSingleton.new_conn()
DatabaseSingleton.close_conn()
print("Konec")