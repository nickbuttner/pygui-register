def select_customers(cursor):
    cursor.execute("select * from customers")
    result = cursor.fetchall()

    for customer in result:
        print(customer)
    
    return result