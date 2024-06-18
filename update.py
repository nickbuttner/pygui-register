from Connection import Connection
from show_products import show_products

connection = Connection()
conn = connection.open()

if conn.is_connected():
    cursor = conn.cursor()

    show_products()

    id = input("Informe o id do produto que voce quer editar: ")
    name = input("Digite o nome do produto: ")
    price = input("Preco do produto: ") 
    price = price.replace("," , ".")
    Product =  input("Quantidade do produto: ") 
    Product = Product.replace("," , ".")

    query = "UPDATE produtos SET "
    query += " name = '" + name + "' , "
    query += " price = " + price + " , " 
    query += " product = " + product + " "
    query += " WHERE id = " + id
    cursor.execute( query )
    conn.commit()

    show_products()

    cursor.close()
    conn.close()