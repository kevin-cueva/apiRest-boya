import sqlite3
from sqlite3 import Error

def create_connection():
    """
    create conecction to the darabase
    """
    conn = None
    try:
        conn = sqlite3.connect("database/table_data.db") #crea la base de datos
        print("SE CREO LA CONEXION\n")
    except Error as e:
        print("Error connenting to database")
    
    return conn

