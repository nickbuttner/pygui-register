from Connection import Connection 
from ProductForm import ProductForm
from Product import Product

connection = Connection()
conn = connection.open()

form = ProductForm()
product = form.show()

if conn.is_connected():
    print("Conectado!")

    cursor = conn.cursor()
    query = "INSERT INTO produtos (nome, preco, quantidade) VALUES ("
    query += " '" +product.name+"' , " +str(product.price) + " , " + str(product.quantity) + " )"

    cursor.execute(query)
    conn.commit()
    conn.close()
