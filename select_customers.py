def select_customers(cursor):
    cursor.execute("select * from clientes")
    result = cursor.fetchall()

    for customer in result:
        print(customer)
    
    return result