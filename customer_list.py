from Connection import Connection
from select_customers import select_customers

def customer_list():
    connection = Connection()
    conn = connection.open()

    if conn.is_connected():
        cursor = conn.cursor()

        result = select_customers(cursor)
        cursor.close()
        conn.close()
        return result     

customer_list()