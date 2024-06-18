from Connection import Connection
from show_products import show_products

def product_list():
    connection = Connection()
    conn = connection.open()

    if conn.is_connected():
        cursor = conn.cursor()

        result = show_products(cursor)
        cursor.close()
        conn.close()
        return result 

product_list()