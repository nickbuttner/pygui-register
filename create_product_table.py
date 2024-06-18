from Connection import Connection 

connection = Connection()
conn = connection.open()

if conn.is_connected():
    cursor = conn.cursor()

    query = "create table produtos (" 
    query += " id int not null primary key auto_increment,  " 
    query += " name varchar(50),  " 
    query += " price double,       " 
    query += " quantity double) "
    cursor.execute(query)

    cursor.close()
    conn.close()

else:
    print("nao conectado")

