import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'admin'
DB_NAME = 'namastebd'
DB_PORT = '3306'

conexion = mysql.connector.connect( user=DB_USER,
                                    password=DB_PASS,
                                    host = DB_HOST,
                                    database = DB_NAME,
                                    port=DB_PORT)

print(conexion)
