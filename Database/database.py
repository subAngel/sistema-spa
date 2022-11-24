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
        sql = "insert into terapeuta(nombre,apellidos,turno,sueldo,especialidad,cedula) values('{}', '{}','{}', {}, '{}','{}')".format(
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

        sql = "update terapeuta set nombre = '{}',apellidos = '{}', turno='{}', sueldo ={}, especialidad='{}', cedula='{}'  where id_terapeuta = {}".format(
            element[0], element[1], element[2], element[3], element[4], element[5], ref)
        # execute the query
        self.cursor.execute(sql)
        self.conn.commit()  # guardamos cambios

    def actualizar_terapeuta(self, args, id):
        try:
            sql = "update terapeuta set nombre = '{}',apellidos = '{}', turno='{}', sueldo={}, especialidad='{}', cedula='{}'  where id_terapeuta = {};".format(
                args[0], args[1], args[2], args[3], args[4], args[5], id)
            print(args, id)
            self.cursor.execute(sql)
            self.conn.commit()
            # return True
        except:
            # return False
            print("exception")

    def actualizar_paciente(self, args, id):
        try:
            sql = "update paciente set nombre = '{}',apellidos = '{}', email='{}', descuento={}, condicion_salud='{}'  where id_paciente = {};".format(
                args[0], args[1], args[2], args[3], args[4], id)
            print(args, id)
            self.cursor.execute(sql)
            self.conn.commit()
            # return True
        except:
            # return False
            print("exception")

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

    def return_list_terapeutas(self):
        sql = "select id_terapeuta, concat_ws(' ', nombre, apellidos) as terapeuta from terapeuta"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def return_list_pacientes(self):
        sql = "select id_paciente, concat_ws(' ', nombre, apellidos) as paciente from paciente"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def return_list_servicios(self):
        sql = "select id_servicios, nombre from servicios"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # regresar el descuento de un paciente
    def return_descuento_paciente(self, id):
        sql = 'select descuento from paciente where id_paciente={}'.format(id)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # regresar el monto del servicio
    def return_monto_servicio(self, id):
        sql = "select monto from servicios where id_servicios={}".format(id)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # obtener las consultas
    def return_consultas(self):
        sql = "select * from paciente_terapeuta"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def return_consulta(self, id):
        sql = "select c.id_p_t, concat_ws(' ', p.nombre, p.apellidos) as paciente, concat_ws(' ', t.nombre, t.apellidos) as terapeuta , s.nombre as servicio ,c.total from paciente_terapeuta c inner join paciente p on c.id_paciente = p.id_paciente inner join terapeuta t on c.id_terapeuta = t.id_terapeuta inner join servicios s on c.id_servicio = s.id_servicios where c.id_p_t = {}".format(id)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # Retornar los nombres
    def return_inner_join_consulta(self):
        sql = "select c.id_p_t, concat_ws(' ', p.nombre, p.apellidos) as paciente, concat_ws(' ', t.nombre, t.apellidos) as terapeuta , s.nombre as servicio ,c.total from paciente_terapeuta c inner join paciente p on c.id_paciente = p.id_paciente inner join terapeuta t on c.id_terapeuta = t.id_terapeuta inner join servicios s on c.id_servicio = s.id_servicios"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def return_descripcion_servicio(self, id):
        sql = "select descripcion from servicios where id_servicios= {}".format(
            id)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # insertar consulta
    def insertar_consulta(self, values):
        sql = "insert into paciente_terapeuta (id_paciente, id_terapeuta, id_servicio, total) values ({},{},{},{})".format(
            values[0], values[1], values[2], values[3])
        self.cursor.execute(sql)
        self.conn.commit()


    def return_reserva(self):
        sql = "select * from reserva"
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    

    def insertar_reserva(self, values):
        fecha="'"+values[1]+"'"
        sql = "insert into reserva (pk_paciente, fecha, status_pago) values ({},{},{})".format(
            values[0], fecha, values[2])
        self.cursor.execute(sql)
        self.conn.commit()
        
        
    # regresar el correo de un paciente
    def return_amil_paciente(self, id):
        sql = 'select email from paciente where id_paciente={}'.format(id)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

