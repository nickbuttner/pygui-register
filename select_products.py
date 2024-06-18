def selectProduct(cursor):
    cursor.execute("select * from products")
    result = cursor.fetchall()

    for prod in result:
        print(prod)

    return result