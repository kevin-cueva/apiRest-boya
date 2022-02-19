import sqlite3
from sqlite3 import Error

from .connection import  create_connection

def insert_data(data):
    """"
    Funcion para insertar  datos (titulo, la fecha de creacion)
    """
    conn = create_connection()

    sql = f"""INSERT INTO table_data (temperatura, ph, created_date)
              VALUES(?, ?, ?)
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print ("CORRECTO")
        return cur.lastrowid #id del registro
    
    except Error as e:
        print(f"error at the insert_data() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()

def select_data_by_id(_id):
    """
    Trae una tarea con el parametro id 
    """
    conn = create_connection()
    sql = f"""SELECT * FROM table_data WHERE id={_id}"""

    try:
        conn.row_factory = sqlite3.Row #convierte la tupla en un objeto mas simple
        cur = conn.cursor()
        cur.execute(sql)
        data = dict(cur.fetchone())
        return data
    except Error as e:
        print(f"Errorn at select_task_by_id: {str(e)}")
        return False

    finally:
        if conn:
            cur.close()
            conn.close()   


def select_all_data():
    """
    Mustra todas las tareas
    """
    conn = create_connection() #Esta funcion crea la conexion
    sql = "SELECT * FROM table_data ORDER BY id DESC LIMIT 1"

    try:
        conn.row_factory = sqlite3.Row #conviertelo en una lista de objetos
        cur = conn.cursor()
        cur.execute(sql)
        data_rows = cur.fetchall()
        data = [dict(row) for row in data_rows] #Cada lista combiertela en diccionario
        return data
    except Error as e:
        print(f"Error at select_all_tasks {str(e)}")
    
    finally:
        if conn:
            cur.close()
            conn.close()

def select_vector_date():
    """
    Funcion que envia los ultimos 50 datos
    """
    conn = create_connection() #Esta funcion crea la conexion
    sql = "SELECT * FROM table_data ORDER BY id DESC LIMIT 50"

    try:
        conn.row_factory = sqlite3.Row #conviertelo en una lista de objetos
        cur = conn.cursor()
        cur.execute(sql)
        data_rows = cur.fetchall()
        data = [dict(row) for row in data_rows] #Cada lista combiertela en diccionario
        return data
    except Error as e:
        print(f"Error at select_all_tasks {str(e)}")
    
    finally:
        if conn:
            cur.close()
            conn.close()


