from Connection import Connection
from CustomerForm import CustomerForm
from Customer import Customer

connection = Connection()
conn = connection.open()

form = CustomerForm()
customer = form.show()

if conn.is_connected():
    print("Connectado!")

    cursor = conn.cursor()
    query = "INSERT INTO customers (name, email_accept, gender, age) VALUES ("
    query += " '" +customer.name+"' , " +str(customer.email_accept) + " , '" + customer.gender + "' , " + str(customer.age) + " )"
    cursor.execute(query)
    conn.commit()
    conn.close()
