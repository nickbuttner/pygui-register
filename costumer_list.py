from Connection import Connection
from select_costumers import select_costumers

def costumer_list():
    connection = Connection()
    conn = connection.open()

    if conn.is_connected():
        cursor = conn.cursor()

        result = select_costumers(cursor)
        cursor.close()
        conn.close()
        return result     

costumer_list()