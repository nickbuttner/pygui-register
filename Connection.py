import mysql.connector

class Connection:
    def open(self):
        conn = mysql.connector.connect(user='root', password='segredo', host='localhost', database='loja_ap2_2', auth_plugin='mysql_native_password')
        return conn

    def fechar(self, conn):
        conn.close()