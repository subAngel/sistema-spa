import pymysql
import os
from dotenv import load_dotenv
load_dotenv()


class Data:

    def __init__(self):
        self.conn = pymysql.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            db=os.getenv("DB_NAME")
        )

        self.cursor = self.conn.cursor()

    def InsertItems(self, element):
        # our element contend the name, age and the carreer of the student
        # in position 0, 1, 2
        sql = "insert into terapeuta(nombre,apellidos,turno,sueldo,especialidad,cedula) values('{}', '{}','{}', '{}', '{}','{}')".format(
            element[0], element[1], element[2], element[3], element[4], element[5])
        # execute the query
        self.cursor.execute(sql)
        self.conn.commit()  # guardamos 
        
    def InsertItemsC(self, element):
        # our element contend the name, age and the carreer of the student
        # in position 0, 1, 2
        sql1 = "insert into paciente(nombre,apellidos,email,descuento,condicion_salud) values('{}', '{}', '{}','{}', '{}')".format(
            element[0], element[1], element[2], element[3], element[4])
        # execute the query
        self.cursor.execute(sql1)
        self.conn.commit()  # guardamos cambios

    def ReturnOneItem(self, ref):
        # we have ref like name of the element
        sql = "select * from terapeuta where nombre = '{}'".format(ref)
        self.cursor.execute(sql)
        # return the element or nil
        return self.cursor.fetchone()


    def ReturnOneItemC(self, ref):
        # we have ref like name of the element
        sql = "select * from paciente where nombre = '{}'".format(ref)
        self.cursor.execute(sql)
        # return the element or nil
        return self.cursor.fetchone()

    def returnAllElements(self):
        sql = "select * from terapeuta"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def returnAllElementsC(self):
        sql = "select * from paciente"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    

    def Delete(self, ref):
        sql = "delete from terapeuta where id_terapeuta = '{}'".format(ref)
        self.cursor.execute(sql)
        self.conn.commit()

    def DeleteC(self, ref):
        sql = "delete from paciente where id_paciente = '{}'".format(ref)
        self.cursor.execute(sql)
        self.conn.commit() 


    def UpdateItem(self, element, ref):
        # element contains the values and ref is the name of the item that we want change

        sql = "update terapeuta set nombre = '{}',apellidos = '{}', turno='{}', sueldo ='{}', especialidad='{}', cedula='{}'  where id_terapeuta = '{}'".format(
            element[0], element[1], element[2], element[3], element[4], element[5], ref)
        # execute the query
        self.cursor.execute(sql)
        self.conn.commit()  # guardamos cambios

    
    def UpdateItemC(self, element, ref):
        # element contains the values and ref is the name of the item that we want change

        sql = "update paciente set  nombre = '{}',apellidos = '{}', email='{}', descuento ='{}', condicion_salud='{}'  where id_paciente = '{}'".format(
            element[0], element[1], element[2], element[3], element[4], ref)
        # execute the query
        self.cursor.execute(sql)
        self.conn.commit()  # guardamos cambios 
    

    def checkuser(self, user, passw):
        sql = "select password from user where user='"+user+"'and password='"+passw+"'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
        #     us = self.cursor.fetchall()
        #     return 1
        # else:
        #     return 0

        # for i in us:
        # 	print(i)


'''
d = Data()
users = d.returnAllElements()
for i in users:
	print(i)
'''
