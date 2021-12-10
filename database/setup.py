
import sqlite3
from sqlite3 import Error
from .connection import create_connection

def read_file(path):
    """
    function for read file
    """
    with open (path, 'r') as sql_file:
        return sql_file.read()
    

def create_table():
    """
    This function create the table
    """
    conn = create_connection()

    path = "database/sql/tables.sql"
    sql = read_file(path)

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Entre en TRY")
        return True
    
    except Error as e:
         print(f"Error in funtion create_tables  {str(e)}")
         return False
    finally:
        if conn:
            cur.close()
            conn.close()
