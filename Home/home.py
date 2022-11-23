import ctypes
from re import T
from tkinter import *
from tkinter import messagebox, ttk
from Database.database import *

from PIL import Image, ImageTk


# * COLORES
color1 = "#FAF7F0"
input_color = "#fff"
background = "#FAF7F0"
foreground = "#333"
color2 = "#CDFCF6"
color3 = "#BCCEF8"
color4 = "#98A8F8"

# * variables globales
font_family = 'Segoe UI'


class Home:

    def __init__(self):

        # instanciar la clase
        self.frame = Tk()
        self.frame.title("Home")
        self.frame.config(background=color1)
        ancho = self.frame.winfo_screenwidth()
        alto = self.frame.winfo_screenheight()
        self.frame.geometry("{}x{}".format(ancho, alto))
        self.frame.state('zoomed')

        # self.frame.attributes('-zoomed', True)
        self.DrawButtons()
        self.DrawLabel()
        self.DrawImage()
        self.frame.mainloop()
        # self.loadImage()

    def DrawLabel(self):
        self.lbl_titulo = Label(self.frame, foreground=foreground, font=(
            font_family, 40), background=background, text="Bienvenido al sistema").place(x=450, y=20)
        self.lbl_opcion = Label(self.frame, foreground=foreground, font=(
            font_family, 30), background=background, text="Seleccione una opción").place(x=500, y=100)
        self.lbl_terapeuta = Label(self.frame, foreground=foreground, font=(
            font_family, 30), background=background, text="Agregar terapeuta").place(x=150, y=350)
        self.lbl_opcion = Label(self.frame, foreground=foreground, font=(
            font_family, 30), background=background, text="Agregar paciente").place(x=560, y=350)
        self.lbl_opcion = Label(self.frame, foreground=foreground, font=(
            font_family, 30), background=background, text="Generar consulta").place(x=980, y=350)
        self.lbl_opcion = Label(self.frame, foreground=foreground, font=(
            font_family, 100), background=background, text=". . .").place(x=600, y=150)
        # self.lbl_usuario = Label(self.frame, foreground="white", font=(
        #     8), background="#000000", text="Usuario").place(x=230, y=260)
        # self.lbl_usuario = Label(self.frame, foreground="white", font=(git
        #     8), background="#000000", text="Contraseña").place(x=220, y=340)

    def DrawImage(self):
        self.img = ImageTk.PhotoImage(Image.open(
            'relax1.png').resize((150, 150), Image.ANTIALIAS))
        lblImagen = Label(self.frame, background=background, image=self.img).place(
            x=100, y=30, width=300, height=150)
        lblImagen = Label(self.frame, background=background, image=self.img).place(
            x=1000, y=30, width=300, height=150)

    def DrawButtons(self):
        self.imgT = ImageTk.PhotoImage(Image.open(
            'terapeuta.png').resize((100, 100), Image.ANTIALIAS))
        self.imgP = ImageTk.PhotoImage(Image.open(
            'paciente.png').resize((100, 100), Image.ANTIALIAS))
        self.imgC = ImageTk.PhotoImage(Image.open(
            'cita.png').resize((100, 100), Image.ANTIALIAS))
        self.btn_terapeuta = Button(self.frame, font=(font_family, 15), foreground=foreground, background=color3,  text="Ingresar", borderwidth=2, relief="flat", cursor="hand1",
                                    overrelief="raise", image=self.imgT, command=lambda: self.moduloTerapeuta()).place(x=200, y=420, width=200, height=250)

        self.btn_paciente = Button(self.frame, font=('Segoe UI', 15), foreground=foreground, background=color3, text="Ingresar", borderwidth=2, relief="flat", cursor="hand1",
                                   overrelief="raise", image=self.imgP, command=lambda: self.moduloPaciente()).place(x=600, y=420, width=200, height=250)

        self.btn_cita = Button(self.frame, font=(font_family, 15), foreground=foreground, background=color3, text="Ingresar", borderwidth=2, relief="flat", cursor="hand1",
                               overrelief="raise", image=self.imgC, command=lambda: self.modulo_consulta()).place(x=1000, y=420, width=200, height=250)

    def Option(self, op):
        if op == 1:
            self.frame.destroy()

        elif op == 2:
            messagebox.showerror(
                message="Falta por ponerla", title="Error")
        elif op == 3:
            messagebox.showerror(
                message="Falta por hacerla xd", title="Error")

    def moduloTerapeuta(self):
        self.popT = Toplevel(self.frame)
        self.popT.title("Terapeuta")
        # popT.attributes('-topmost',True)
        self.popT.state('zoomed')
        ancho = self.frame.winfo_screenwidth()
        alto = self.frame.winfo_screenheight()
        self.frame.geometry("{}x{}".format(ancho, alto))
        self.marco = LabelFrame(self.popT, text="Formulario de terapeuta")

        self.marco.place(x=300, y=80, width=1000, height=alto-150)
        self.DrawComponents(self.marco)
        # self.DrawButtonsT(self.marco)
        # self.DrawEntryT(self.marco)
        # self.DrawListT(self.marco)
        self.marco.config(background=background)
        # self.popT.geometry("3000x800")

    def moduloPaciente(self):
        self.popP = Toplevel(self.frame)
        self.popP.title("Cliente")
        # popT.attributes('-topmost',True)
        self.popP.state('zoomed')
        ancho = self.frame.winfo_screenwidth()
        alto = self.frame.winfo_screenheight()
        self.frame.geometry("{}x{}".format(ancho, alto))
        self.marcoP = LabelFrame(self.popP, text="Formulario de Cliente")

        self.marcoP.place(x=300, y=80, width=1000, height=alto-150)
        self.components_paciente(self.marcoP)
        # self.DrawButtonsT(self.marco)
        # self.DrawEntryT(self.marco)
        # self.DrawListT(self.marco)
        self.marcoP.config(background=background)
        # self.popT.geometry("3000x800")

    def DrawComponents(self, popT):
        self.nombreT = StringVar()
        self.apellidosT = StringVar()
        self.turnoT = StringVar()
        self.sueldoT = StringVar()
        self.especialidadT = StringVar()
        self.cedulaT = StringVar()

        def seleccionar(event):
            try:
                id = self.list_elemtsT.selection()[0]
                if id:
                    self.nombreT.set(self.list_elemtsT.item(id, "values")[1])
                    self.apellidosT.set(
                        self.list_elemtsT.item(id, "values")[2])
                    self.turnoT.set(self.list_elemtsT.item(id, "values")[3])
                    self.sueldoT.set(self.list_elemtsT.item(id, "values")[4])
                    self.especialidadT.set(
                        self.list_elemtsT.item(id, "values")[5])
                    self.cedulaT.set(self.list_elemtsT.item(id, "values")[6])
                    self.btn_nuevo_tera.config(state=DISABLED)
                    self.btn_modificar_tera.config(state=NORMAL)
                    self.btn_eliminar_tera.config(state=NORMAL)
            except:
                print("Warning seleccionar()")

        def limpiar_campos():
            self.limpiar_campos_terapeuta()
            self.btn_nuevo_tera.config(state=NORMAL)
            self.btn_modificar_tera.config(state=DISABLED)
            self.btn_eliminar_tera.config(state=DISABLED)

        # * ____________________________________TITULO__________________________________
        self.lbl_registrarP = Label(popT, foreground=foreground, font=(
            font_family, 30), background=background, text="Terapeuta").grid(column=0, row=0)

        self.limpiar = Button(popT, font=(font_family, 11), foreground="#222",
                              text="LIMPIAR FORMULARIO", borderwidth=2, relief="flat", cursor="hand1", overrelief="raise",
                              background=background, command=lambda: limpiar_campos())
        self.limpiar.grid(column=3, row=0)

        # * -----------------------------------FILA 1------------------------------------
        self.lbl_name = Label(popT, foreground=foreground, font=(font_family,
                                                                 12), background=background, text="Nombre").grid(column=0, row=1, pady=20, padx=100)
        self.b_nombre = Entry(popT, font=(font_family, 12), relief="flat",
                              background=input_color, foreground=foreground, textvariable=self.nombreT)
        self.b_nombre.grid(column=1, row=1)

        self.lbl_ape = Label(popT, foreground=foreground, font=(font_family,
                                                                12), background=background, text="Apellidos").grid(column=2, row=1)
        self.b_apellidos = Entry(popT, font=(font_family, 12), relief="flat", background=input_color, foreground=foreground,
                                 textvariable=self.apellidosT)
        self.b_apellidos.grid(column=3, row=1)

        # * ----------------------FILA 2 turno , sueldo ---------------------------

        self.lbl_turno = Label(popT, foreground=foreground, font=(font_family,
                                                                  12), background=background, text="Turno").grid(column=0, row=2, pady=20, padx=100)
        self.combo_turno = ttk.Combobox(
            popT, values=["Vespertino", "Matutino"], textvariable=self.turnoT)
        self.combo_turno.grid(column=1, row=2)

        self.lbl_sueldo = Label(popT, foreground=foreground, font=(font_family,
                                                                   12), background=background, text="Sueldo").grid(column=2, row=2)
        self.b_sueldo = Entry(popT, font=(font_family, 12), relief="flat", background=input_color, foreground=foreground,
                              textvariable=self.sueldoT)
        self.b_sueldo.grid(column=3, row=2)

        # * ----------------------FILA 3 especialidad, cedula ---------------------------

        self.lbl_especialidad = Label(popT, foreground=foreground, font=(font_family,
                                                                         12), background=background, text="Especialidad").grid(column=0, row=3, pady=20, padx=100)
        self.b_especialidad = Entry(popT, font=(font_family, 12), relief="flat", background=input_color, foreground=foreground,
                                    textvariable=self.especialidadT)
        self.b_especialidad.grid(column=1, row=3)

        self.lbl_cedula = Label(popT, foreground=foreground, font=(font_family,
                                                                   12), background=background, text="Cedula").grid(column=2, row=3)
        self.b_cedula = Entry(popT, font=(font_family, 12), relief="flat", background=input_color, foreground=foreground,
                              textvariable=self.cedulaT)
        self.b_cedula.grid(column=3, row=3)

        # * -------------------------------FILA 3 tabla---------------------------------
        # self.table_container
        self.list_elemtsT = ttk.Treeview(popT, columns=(
            1, 2, 3, 4, 5, 6, 7), show="headings", height="8")

        # --- STYLE ---
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", background=color4,
                        relief="flat", foreground=foreground)
        style.map("Treeview", background=[
                  ('selected', '#FBFACD')], foreground=[('selected', 'black')])

        # --- Event---
        self.list_elemtsT.bind("<<TreeviewSelect>>", seleccionar)
        # ---- end ---
        self.list_elemtsT.grid(
            column=0, row=4, columnspan=7, padx=100, pady=20)
        self.list_elemtsT["columns"] = (
            "ID", "NOMBRE", "APELLIDOS", "TURNO", "SUELDO", "ESPECIALIDAD", "CEDULA")
        self.list_elemtsT.column("#0", anchor=CENTER, stretch=NO)
        self.list_elemtsT.column("ID", anchor=CENTER, width=50)
        self.list_elemtsT.column("NOMBRE", anchor=CENTER, width=130)
        self.list_elemtsT.column("APELLIDOS", anchor=CENTER, width=150)
        self.list_elemtsT.column("TURNO", anchor=CENTER, width=100)
        self.list_elemtsT.column("SUELDO", anchor=CENTER, width=80)
        self.list_elemtsT.column("ESPECIALIDAD", anchor=CENTER, width=100)
        self.list_elemtsT.column("CEDULA", anchor=CENTER, width=100)
        self.list_elemtsT.heading("#0", text="")
        self.list_elemtsT.heading("ID", text="ID", anchor=CENTER)
        self.list_elemtsT.heading("NOMBRE", text="NOMBRE", anchor=CENTER)
        self.list_elemtsT.heading("APELLIDOS", text="APELLIDOS", anchor=CENTER)
        self.list_elemtsT.heading("TURNO", text="TURNO", anchor=CENTER)
        self.list_elemtsT.heading("SUELDO", text="SUELDO", anchor=CENTER)
        self.list_elemtsT.heading(
            "ESPECIALIDAD", text="ESPECIALIDAD", anchor=CENTER)
        self.list_elemtsT.heading("CEDULA", text="CEDULA", anchor=CENTER)
        # -- FILL LIST--

        self.llenar_tabla_terapeuta()

        # *---------------------------------- botones--------------------------------
        self.lbl_messages = Label(popT, text=".", fg="green")
        self.lbl_messages.grid(column=0, row=5)

        self.btn_nuevo_tera = Button(popT, foreground="#222", text="AGREGAR", font=(font_family, 13),
                                     borderwidth=2, relief="flat", cursor="hand1", overrelief="raise",
                                     background="#B3FFAE", command=lambda: self.nuevo_terapeuta(popT))
        self.btn_nuevo_tera.grid(column=1, row=5)

        self.btn_eliminar_tera = Button(popT, text="ELIMINAR", foreground="white", font=(font_family, 13),
                                        borderwidth=2, relief="flat", cursor="hand1", overrelief="raise",
                                        background="#E97777", command=lambda: self.eliminar_terapeuta(popT))
        self.btn_eliminar_tera.grid(column=2, row=5)

        self.btn_modificar_tera = Button(popT, text="MODIFICAR", foreground="white", font=(font_family, 13),
                                         borderwidth=2, relief="flat", cursor="hand1", overrelief="raise",
                                         background="#B1AFFF", command=lambda: self.modificar_terapeuta(popT))
        self.btn_modificar_tera.grid(column=3, row=5)

    # * MODIFICACIONES ANGEL
    def vaciar_tabla_terapeuta(self):
        filas = self.list_elemtsT.get_children()
        for fila in filas:
            self.list_elemtsT.delete(fila)

    def llenar_tabla_terapeuta(self):
        self.vaciar_tabla_terapeuta()
        d = Data()
        self.filas = d.returnAllElements()
        for fila in self.filas:
            id = fila[0]
            self.list_elemtsT.insert("", END, id, text=id, values=fila)

    def nuevo_terapeuta(self, popT):
        d = Data()
        arr = [self.nombreT.get(), self.apellidosT.get(), self.combo_turno.get(
        ), int(self.sueldoT.get()), self.especialidadT.get(), self.cedulaT.get()]
        d.InsertItems(arr)
        self.llenar_tabla_terapeuta()
        self.lbl_messages.config(
            text="Registro correcto", fg="green", bg=background)
        self.limpiar_campos_terapeuta()

    def getID(id):
        return id

    def eliminar_terapeuta(self, popT):
        id = self.list_elemtsT.selection()[0]
        db = Data()
        if id:
            db.Delete(int(id))
            self.list_elemtsT.delete(id)
            self.lbl_messages.config(
                text="Terapeuta eliminado", fg="#d2b440", bg=background)
            self.limpiar_campos_terapeuta()
            self.btn_nuevo_tera.config(state=NORMAL)
            self.btn_eliminar_tera.config(state=DISABLED)
            self.btn_modificar_tera.config(state=DISABLED)
        else:
            self.lbl_messages.config(
                text="Seleccione un registro", fg="#eb6736", bg=background)

    def modificar_terapeuta(self, marco):
        arr = [self.nombreT.get(), self.apellidosT.get(), self.combo_turno.get(
        ), int(self.sueldoT.get()), self.especialidadT.get(), self.cedulaT.get()]
        id = int(self.list_elemtsT.selection()[0])
        db = Data()
        db.actualizar_terapeuta(arr, id)
        self.lbl_messages.config(
            text="Terapeuta modificado correctamente", fg="green")
        self.llenar_tabla_terapeuta()
        self.limpiar_campos_terapeuta()
        self.btn_nuevo_tera.config(state=NORMAL)
        self.btn_eliminar_tera.config(state=DISABLED)
        self.btn_modificar_tera.config(state=DISABLED)
        print("-----------------------------------")

    def limpiar_campos_terapeuta(self):
        # self.idter.set("")
        self.nombreT.set("")
        self.apellidosT.set("")
        self.combo_turno.set("")
        self.sueldoT.set("")
        self.especialidadT.set("")
        self.cedulaT.set("")

    def ClearListT(self):
        self.list_elemtsT.delete(*self.list_elemtsT.get_children())


# ********************* MODULO PACIENTE **********************

    def components_paciente(self, mp):
        self.nombre_paciente = StringVar()
        self.apellidos_paciente = StringVar()
        self.email = StringVar()
        self.descuento = IntVar()
        self.condicion_fisica = StringVar()

        def seleccionar(event):
            id = self.tabla_pacientes.selection()[0]
            if id:
                self.nombre_paciente.set(
                    self.tabla_pacientes.item(id, "values")[1])
                self.apellidos_paciente.set(
                    self.tabla_pacientes.item(id, "values")[2])
                self.email.set(self.tabla_pacientes.item(id, "values")[3])
                self.descuento.set(self.tabla_pacientes.item(id, "values")[4])
                self.condicion_fisica.set(
                    self.tabla_pacientes.item(id, "values")[5])

                self.btn_nuevo_p.config(state=DISABLED)
                self.btn_modificar_p.config(state=NORMAL)
                self.btn_eliminar_p.config(state=NORMAL)

        # * ----------------------TITULO ------------------
        self.lbl_titulo_paciente = Label(mp, foreground=foreground, font=(
            font_family, 30), background=background, text="Paciente").grid(column=0, row=0, padx=170, columnspan=4)

        # * --------------------- CAMPOS -------------------
        self.lbl_nombre_p = Label(mp, foreground=foreground, font=(
            font_family, 12), background=background, text="Nombre").grid(column=0, row=1, padx=140)

        self.txt_nombre_p = Entry(mp, font=(
            font_family, 12), relief='flat', background=input_color, foreground=foreground, textvariable=self.nombre_paciente)
        self.txt_nombre_p.grid(column=1, row=1)

        self.lbl_apellidos_p = Label(mp, foreground=foreground, font=(
            font_family, 12), background=background, text="Apellidos").grid(column=2, row=1)
        self.txt_apellidos_p = Entry(mp, font=(
            font_family, 12), relief='flat', background=input_color, foreground=foreground, textvariable=self.apellidos_paciente)
        self.txt_apellidos_p.grid(column=3, row=1)

        self.lbl_email_p = Label(mp, foreground=foreground, font=(
            font_family, 12), background=background, text="Correo").grid(column=0, row=2, padx=140)
        self.txt_correo_p = Entry(mp, font=(
            font_family, 12), relief='flat', background=input_color, foreground=foreground, textvariable=self.email)
        self.txt_correo_p.grid(column=1, row=2)

        self.lbl_descuento_p = Label(mp, foreground=foreground, font=(
            font_family, 12), background=background, text="Descuento").grid(column=2, row=2)

        self.txt_descuento_p = Entry(mp, font=(
            font_family, 12), relief='flat', background=input_color, foreground=foreground, textvariable=self.descuento)
        self.txt_descuento_p.grid(column=3, row=2)

       # self.lbl_condicion_p = Label(mp, foreground=foreground, font=(
        #    font_family, 12), relief="flat", text="Condición médica", background=background).grid(column=0, row=3, columnspan=4, padx=140)

        # self.txt_condicion_p = Text(mp, font=(
        #   font_family, 12), background=input_color, foreground=foreground, height=3, width=45)
        # self.txt_condicion_p.grid(
        #   column=0, row=4, columnspan=4, rowspan=2, padx=140)
        # self.txt_condicion_p=Entry(self.txt_condicion_p)

        self.lbl_condicion_p = Label(mp, foreground=foreground, font=(
            font_family, 12), background=background, text="Condicion").grid(column=0, row=3)

        self.txt_condicion_p = Entry(mp, font=(
            font_family, 12), relief='flat', background=input_color, foreground=foreground, textvariable=self.condicion_fisica, width=40)
        self.txt_condicion_p.grid(column=1, row=3, columnspan=3)

        # self.lbl_message_p = Label(mp, fg=foreground, font=(
        #     font_family, 12), text="", background=background).grid(column=0, row=5, columnspan=4)
        # * ------------------------------ TABLA --------------------------
        self.tabla_pacientes = ttk.Treeview(mp)

        self.tabla_pacientes.bind("<<TreeviewSelect>>", seleccionar)

        self.tabla_pacientes.grid(
            column=0, row=6, columnspan=5, pady=10, padx=160)
        self.tabla_pacientes['columns'] = (
            "ID", "NOMBRE", "APELLIDOS", "EMAIL", "DESCUENTO", "CONDICION")
        self.tabla_pacientes.column("#0", width=0, stretch=NO)
        self.tabla_pacientes.column("ID", width=40, anchor=CENTER)
        self.tabla_pacientes.column("NOMBRE", width=100, anchor=CENTER)
        self.tabla_pacientes.column("APELLIDOS", width=100, anchor=CENTER)
        self.tabla_pacientes.column("EMAIL", width=200, anchor=CENTER)
        self.tabla_pacientes.column("DESCUENTO", width=40, anchor=CENTER)
        self.tabla_pacientes.column("CONDICION", width=100, anchor=CENTER)

        self.tabla_pacientes.heading("#0", text="")
        self.tabla_pacientes.heading("ID", text="ID")
        self.tabla_pacientes.heading("NOMBRE", text="NOMBRE")
        self.tabla_pacientes.heading("APELLIDOS", text="APELLIDOS")
        self.tabla_pacientes.heading("EMAIL", text="EMAIL")
        self.tabla_pacientes.heading("DESCUENTO", text="DESCUENTO")
        self.tabla_pacientes.heading("CONDICION", text="CONDICION")

        self.llenar_tabla_cliente()

        # TODO llenar tabla de pacientes

        # * --------------------- botones ---------------------------------
        self.lbl_messagess = Label(mp, text=".", fg="green")
        self.lbl_messagess.grid(column=0, row=5)
# --------------------------------------------------------------------------------------------------------------------------

        self.btn_nuevo_p = Button(mp, foreground=foreground, text="NUEVO", font=(
            font_family, 12), cursor="hand1", overrelief="raise", background="#B3FFAE", command=lambda: self.nuevo_cliente(mp))

        self.btn_nuevo_p.grid(column=1, row=7)

        self.btn_eliminar_p = Button(mp, foreground=foreground, text="ELIMINAR", font=(
            font_family, 12), cursor="hand1", overrelief="raise", background="#b3ffae", command=lambda: self.eliminar_cliente(mp))
        self.btn_eliminar_p.grid(column=2, row=7)

        self.btn_modificar_p = Button(mp, foreground=foreground, text="MODIFICAR", font=(
            font_family, 12), cursor="hand1", overrelief="raise", background="#b3ffae", command=lambda: self.modificar_cliente(mp))
        self.btn_modificar_p.grid(column=3, row=7)

        self.btn_generar_cita = Button(mp, foreground=foreground, text="Generar Cita", font=(
            font_family, 12), cursor="hand1", overrelief="raise", background="#b3ffae", command=self.modulo_reserva)
        self.btn_generar_cita.grid(column=3, row=8)

    def vaciar_tabla_cliente(self):
        filas = self.tabla_pacientes.get_children()
        for fila in filas:
            self.tabla_pacientes.delete(fila)

    def llenar_tabla_cliente(self):
        self.vaciar_tabla_cliente()
        d = Data()
        self.filas = d.returnAllElementsC()
        # print(self.filas)
        for fila in self.filas:
            id = fila[0]
            self.tabla_pacientes.insert("", END, id, text=id, values=fila)

    def nuevo_cliente(self, mp):
        d = Data()
        arr = [self.nombre_paciente.get(), self.apellidos_paciente.get(), self.email.get(
        ), self.descuento.get(), self.condicion_fisica.get()]

        print("hii ", self.nombre_paciente.get())
        d.InsertItemsC(arr)
        self.limpiar_campos_cliente()
        print("se guardo")
        self.lbl_messagess.config(
            text="Registro correcto", fg="green", bg=background)
        self.llenar_tabla_cliente()
        self.limpiar_campos_cliente()

    def eliminar_cliente(self, popT):
        id = self.tabla_pacientes.selection()[0]
        db = Data()
        if id:
            db.DeleteC(int(id))
            self.tabla_pacientes.delete(id)
            self.lbl_messagess.config(
                text="Cliente eliminado", fg="#d2b440", bg=background)
            self.limpiar_campos_cliente()
            self.btn_nuevo_p.config(state=NORMAL)
            self.btn_eliminar_p.config(state=NORMAL)
            self.btn_modificar_p.config(state=NORMAL)
        else:
            self.lbl_messagess.config(
                text="Seleccione un registro", fg="#eb6736", bg=background)

    def modificar_cliente(self, marco):

        arr = [self.nombre_paciente.get(), self.apellidos_paciente.get(), self.email.get(
        ), int(self.descuento.get()), self.condicion_fisica.get()]

        id = int(self.tabla_pacientes.selection()[0])
        # print("idcc ", id)
        db = Data()
        db.actualizar_paciente(arr, id)
        self.lbl_messagess.config(
            text="Paciente modificado correctamente", fg="green")
        self.llenar_tabla_cliente()
        # print("hii")
        self.limpiar_campos_cliente()
        self.btn_nuevo_p.config(state=NORMAL)
        self.btn_eliminar_p.config(state=NORMAL)
        self.btn_modificar_p.config(state=NORMAL)
        # print("-----------------------------------")

    def eliminarT(self, idtt, popTE):
        d = Data()
        # print(idtt)
        d.DeleteC(idtt)
        popTE.destroy()
        # messagebox.showinfo(title="Eliminacion",
        #                     message="Se ha borrado con exito")
        self.ClearListT()
        self.DrawListT(self.popT)
        self.limpiar_campos_cliente()

    def editarT(self, idtt, idterap, nom, ape, tu, su, es, ce, popTE):
        arr = [idterap, nom, ape, tu, su, es, ce]
        d = Data()
        d.UpdateItem(arr, idtt)
        popTE.destroy()
        # messagebox.showinfo(title="Actualizacion",
        #                     message="Se han actualizado los datos")
        self.ClearListT()
        self.DrawListT(self.popT)
        self.limpiar_campos_cliente()

    def ClearListT(self):
        self.list_elemtsT.delete(*self.list_elemtsT.get_children())

    def limpiar_campos_cliente(self):
        # self.idter.set("")
        self.nombre_paciente.set("")
        self.apellidos_paciente.set("")
        self.email.set("")
        self.descuento.set("")
        self.condicion_fisica.set("")


# TODO -------------------------------------------------------MODULO CITA----------------------------------------------


    def modulo_consulta(self):
        self.frame_consulta = Toplevel(self.frame)
        self.frame_consulta.title("Generar Cita")
        self.frame_consulta.state("zoomed")
        self.marcoReserva = LabelFrame(
            self.frame_consulta, text="Generar una reserva")

        self.marcoReserva.place(x=(290+142), y=100, width=630, height=660)
        self.marcoReserva.config(background=background)
        self.components_consulta(self.marcoReserva)
        # self.components_reserva(self.marcoReserva)

    def components_consulta(self, mr):
        # ? @mc es el marco reserva

        self.titulo_consulta = Label(mr, foreground=foreground, font=(
            font_family, 22), background=background, text="consulta").grid(column=0, row=0, columnspan=2, padx=30)

        self.tabla_terapeuta_consulta = ttk.Treeview(mr)
        # self.tabla_terapeuta_consulta.bind
        self.tabla_terapeuta_consulta.grid(column=0, row=1, padx=10)
        self.tabla_terapeuta_consulta['columns'] = ("ID", "TERAPEUTA")
        self.tabla_terapeuta_consulta.column("#0", width=0, stretch=NO)
        self.tabla_terapeuta_consulta.column("ID", width=30, anchor=CENTER)
        self.tabla_terapeuta_consulta.column(
            "TERAPEUTA", width=140, anchor=CENTER)
        self.tabla_terapeuta_consulta.heading("#0", text="")
        self.tabla_terapeuta_consulta.heading("ID", text="ID")
        self.tabla_terapeuta_consulta.heading("TERAPEUTA", text="TERAPEUTA")

        # * ----------------------tabla pacientes
        self.tabla_pacientes_consulta = ttk.Treeview(mr)
        self.tabla_pacientes_consulta.grid(column=1, row=1, padx=10)
        self.tabla_pacientes_consulta['columns'] = ("ID", "PACIENTE")
        self.tabla_pacientes_consulta.column("#0", width=0, stretch=NO)
        self.tabla_pacientes_consulta.column("ID", width=30, anchor=CENTER)
        self.tabla_pacientes_consulta.column(
            "PACIENTE", width=140, anchor=CENTER)
        self.tabla_pacientes_consulta.heading("#0", text="")
        self.tabla_pacientes_consulta.heading("ID", text="ID")
        self.tabla_pacientes_consulta.heading("PACIENTE", text="PACIENTE")

        # * ---------------------tabla servicios
        self.tabla_servicios_consulta = ttk.Treeview(mr)
        self.tabla_servicios_consulta.grid(column=2, row=1, padx=10)
        self.tabla_servicios_consulta['columns'] = ("ID", "SERVICIO")
        self.tabla_servicios_consulta.column("#0", width=0, stretch=NO)
        self.tabla_servicios_consulta.column("ID", width=30, anchor=CENTER)
        self.tabla_servicios_consulta.column(
            "SERVICIO", width=100, anchor=CENTER)
        self.tabla_servicios_consulta.heading("#0", text="")
        self.tabla_servicios_consulta.heading("ID", text="ID")
        self.tabla_servicios_consulta.heading("SERVICIO", text="SERVICIO")

        self.tabla_consulta = ttk.Treeview(mr)
        self.tabla_consulta.grid(
            column=0, row=2, columnspan=3, pady=30, padx=40)
        self.tabla_consulta['columns'] = (
            "ID", "PACIENTE", "TERAPEUTA", "SERVICIO", "MONTO")
        self.tabla_consulta.column("#0", width=0, stretch=NO)
        self.tabla_consulta.column("ID", width=40)
        self.tabla_consulta.column("PACIENTE", width=150)
        self.tabla_consulta.column("TERAPEUTA", width=100)
        self.tabla_consulta.column("SERVICIO", width=100)
        self.tabla_consulta.column("MONTO", width=100)
        self.tabla_consulta.heading("#0", text="")
        self.tabla_consulta.heading("ID", text="ID")
        self.tabla_consulta.heading("PACIENTE", text="PACIENTE")
        self.tabla_consulta.heading("TERAPEUTA", text="TERAPEUTA")
        self.tabla_consulta.heading("SERVICIO", text="SERVICIO")
        self.tabla_consulta.heading("MONTO", text="MONTO $")

        # * ---
        self.btn_generar_total = Button(mr, text="Insertar consulta", foreground=foreground, background=input_color, font=(
            font_family, 18), command=self.generar_consulta)
        self.btn_generar_total.grid(column=0, row=3, pady=20)

        self.llenar_tablas_consulta()

        # self.label_fecha = Label(mr, foreground=foreground, background=background, font=(
        #     font_family, 12)).grid(column=1, row=1)
        # self.combo_year_consulta = ttk.Combobox(
        #     self, state="readonly", values=['2022', '2023', '2024', 2025], width=10).grid(column=2, row=1)
        # self.combo_month_consulta = ttk.Combobox(mr, state="readonly", values=[
        #     "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], width=10).grid(column=3, row=1)
        # self.combo_day_consulta = ttk.Combobox(mr, state="readonly", values=[
        #     "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "21", "23", "24", "25", "26", "27", "28", "29", "30", "31"], width=10).grid(column=4, row=1)

    def vaciar_tabla_consulta(self):
        filas_tera = self.tabla_terapeuta_consulta.get_children()
        for fila in filas_tera:
            self.tabla_terapeuta_consulta.delete(fila)
        filas_pac = self.tabla_pacientes_consulta.get_children()
        for fila in filas_pac:
            self.tabla_pacientes_consulta.delete(fila)
        fila_ser = self.tabla_servicios_consulta.get_children()
        for fila in fila_ser:
            self.tabla_servicios_consulta.delete(fila)
        fila_consulta = self.tabla_consulta.get_children()
        for fila in fila_consulta:
            self.tabla_consulta.delete(fila)

    def llenar_tablas_consulta(self):
        self.vaciar_tabla_consulta()
        db = Data()
        self.filas_tera = db.return_list_terapeutas()
        for fila in self.filas_tera:
            id = fila[0]
            self.tabla_terapeuta_consulta.insert(
                "", END, id, text=id, values=fila)

        self.filas_pac = db.return_list_pacientes()
        for fila in self.filas_pac:
            id = fila[0]
            self.tabla_pacientes_consulta.insert(
                "", END, id, text=id, values=fila)

        self.filas_serv = db.return_list_servicios()
        for fila in self.filas_serv:
            id = fila[0]
            self.tabla_servicios_consulta.insert(
                "", END, id, text=id, values=fila)

        # self.filas_consulta = db.return_consultas()
        self.filas_consulta = db.return_inner_join_consulta()
        for fila in self.filas_consulta:
            id = fila[0]
            self.tabla_consulta.insert("", END, id, text=id, values=fila)

    def generar_consulta(self):
        id_paciente = self.tabla_pacientes_consulta.selection()[0]
        id_terapeuta = self.tabla_terapeuta_consulta.selection()[0]
        id_servicio = self.tabla_servicios_consulta.selection()[0]
        db = Data()
        descuento = int(db.return_descuento_paciente(id_paciente)[0])
        precio_servicio = int(db.return_monto_servicio(id_servicio)[0])
        total_consulta = precio_servicio - precio_servicio * (descuento/100)
        round(total_consulta)

        valores = (int(id_paciente), int(id_terapeuta),
                   int(id_servicio), round(total_consulta))
        db.insertar_consulta(valores)
        self.llenar_tablas_consulta()



    



#modulo reserva-----------------------------------------------------------------------------------------
          

    def modulo_reserva(self):
        self.frame_reserva = Toplevel(self.frame)
        self.frame_reserva.title("Generar cita")
        self.frame_reserva.state("zoomed")
        self.marcoReserva = LabelFrame(
            self.frame_reserva, text="Generar una cita")
        # x=(290+142)
        self.marcoReserva.place(x=(250), y=70, width=950, height=660)
        self.marcoReserva.config(background=background)
        self.components_reserva(self.marcoReserva)
        # self.components_reserva(self.marcoReserva)

    def components_reserva(self, mr):
        # ? @mc es el marco reserva
        self.diaa = StringVar()
        self.mes = StringVar()
        self.anio = StringVar()
        self.hora1 = StringVar()
        self.timee = StringVar()
        #self.hora2 = StringVar()
        self.min1 = StringVar()
        #self.min2 = StringVar()
        self.seg1 = StringVar()
        #self.seg2 = StringVar()
        self.statu = StringVar()
        self.titulo_reserva = Label(mr, foreground=foreground, font=(
            font_family, 22), background=background, text="Reserva").grid(column=0, row=0, columnspan=2, padx=30)

        

        # * ----------------------tabla pacientes

        
        self.tabla_pacientes_reserva = ttk.Treeview(mr)
        self.tabla_pacientes_reserva.grid(column=0, row=1, padx=10)
        self.tabla_pacientes_reserva['columns'] = ("ID", "PACIENTE")
        self.tabla_pacientes_reserva.column("#0", width=0, stretch=NO)
        self.tabla_pacientes_reserva.column("ID", width=30, anchor=CENTER)
        self.tabla_pacientes_reserva.column(
            "PACIENTE", width=140, anchor=CENTER)
        self.tabla_pacientes_reserva.heading("#0", text="")
        self.tabla_pacientes_reserva.heading("ID", text="ID")
        self.tabla_pacientes_reserva.heading("PACIENTE", text="PACIENTE")

        

        self.tabla_reserva = ttk.Treeview(mr)
        self.tabla_reserva.grid(
            column=0, row=2, columnspan=2, pady=30, padx=10)
        self.tabla_reserva['columns'] = ("PACIENTE", "FECHA","ESTATUS")
        self.tabla_reserva.column("#0", width=0, stretch=NO)
        # self.tabla_reserva.column("ID", width=40)
        self.tabla_reserva.column("PACIENTE", width=100)
    
        self.tabla_reserva.column("FECHA", width=100)
        self.tabla_reserva.column("ESTATUS", width=100)
    
        self.tabla_reserva.heading("#0", text="")
        # self.tabla_reserva.heading("ID", text="ID")
        self.tabla_reserva.heading("PACIENTE", text="PACIENTE")
        self.tabla_reserva.heading("FECHA", text="FECHA")
        self.tabla_reserva.heading("ESTATUS", text="ESTATUS")

        self.an= Label(mr, foreground=foreground, font=(
            font_family, 12), background=background, text="año").place(x=250, y=120)
        self.lmes= Label(mr, foreground=foreground, font=(
            font_family, 12), background=background, text="mes").place(x=390, y=120)
        self.ldi= Label(mr, foreground=foreground, font=(
            font_family, 12), background=background, text="dia").place(x=540, y=120)
        self.lhor= Label(mr, foreground=foreground, font=(
            font_family, 12), background=background, text="hora").place(x=660, y=120)
        self.lmin= Label(mr, foreground=foreground, font=(
            font_family, 12), background=background, text="min").place(x=830, y=120)
        self.lsta= Label(mr, foreground=foreground, font=(
            font_family, 12), background=background, text="Estatus").place(x=370, y=380)
            # .grid(column=1, row=0)

        self.anioo = ttk.Combobox(
            mr, state="readonly",values=["2022", "2023"], textvariable=self.anio)
        self.anioo.grid(column=1, row=1)

        self.mess = ttk.Combobox(
            mr, state="readonly",values=["01", "02","03","04", "05","06","07", "08","09","10", "11","12"], textvariable=self.mes)
        self.mess.grid(column=2, row=1)

        self.diia = ttk.Combobox(
            mr, state="readonly",values=["01", "02","03","04", "05","06","07", "08","09","10", "11","12","13","14","15",
            "16", "17","18","19", "20","21","22", "23","24","25","26","27","28","29","30","31"], textvariable=self.diaa)
        self.diia.grid(column=3, row=1)

        self.horaa = ttk.Combobox(
            mr, state="readonly",values=["00","01", "02","03","04", "05","06","07", "08","09","10", "11","12","13","14",
            "15","16","17","18","19","20","21","22","23"], textvariable=self.hora1)
        self.horaa.grid(column=4, row=1)

        self.minu = ttk.Combobox(
            mr, state="readonly",values=["00","01", "02","03","04", "05","06","07", "08","09","10", "11","12","13","14",
            "15","16","17","18","19","20","21","22","23","24","25", "26","27","28", "29","30","31", "32","33","34", "35","36","37","38",
            "39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"], textvariable=self.min1)
        self.minu.grid(column=5, row=1)

        self.statusp = ttk.Combobox(
            mr, state="readonly",values=["Pagado","No pagado"], textvariable=self.statu)
        self.statusp.grid(column=2, row=2)

        
        
        
         
       # self.tabla_servicios_consulta = ttk.Treeview(mr)
        #self.tabla_servicios_consulta.grid(column=2, row=1, padx=10)
        #self.tabla_servicios_consulta['columns'] = ("ID", "SERVICIO")
        #self.tabla_servicios_consulta.column("#0", width=0, stretch=NO)
        #self.tabla_servicios_consulta.column("ID", width=30, anchor=CENTER)
        #self.tabla_servicios_consulta.column(
        #    "SERVICIO", width=100, anchor=CENTER)
        #self.tabla_servicios_consulta.heading("#0", text="")
        #self.tabla_servicios_consulta.heading("ID", text="ID")
        #self.tabla_servicios_consulta.heading("SERVICIO", text="SERVICIO")

        

        # * ---
        self.btn_generar_total = Button(mr, text="Insertar consulta", foreground=foreground, background=input_color, font=(
            font_family, 18),  command=self.generar_reserva)
        self.btn_generar_total.grid(column=0, row=3, pady=20)

        self.llenar_tablas_reserva()
        self.llenar_tablaCit()

    def vaciar_tabla_reserva(self):     
        filas_pac = self.tabla_pacientes_reserva.get_children()
        for fila in filas_pac:
            self.tabla_pacientes_reserva.delete(fila)
        
        # fila_reserva = self.tabla_reserva.get_children()
        # for fila in fila_reserva:
        #     self.tabla_reserva.delete(fila)  comentado hoy xd
    def vaciar_tablaCit(self):     
        filas_pac = self.tabla_reserva.get_children()
        for fila in filas_pac:
            self.tabla_reserva.delete(fila)
    
    def llenar_tablas_reserva(self):
        self.vaciar_tabla_reserva()
        db = Data()
        self.filas_pac = db.return_list_pacientes()
        for fila in self.filas_pac:
            id = fila[0]
            self.tabla_pacientes_reserva.insert(
                "", END, id, text=id, values=fila)
        print("cargue bien xd")

        
   
    def generar_reserva(self):
        id_paciente = self.tabla_pacientes_reserva.selection()[0]
        print(id_paciente)
        #id_terapeuta = self.tabla_terapeuta_consulta.selection()[0]
        #id_servicio = self.tabla_servicios_consulta.selection()[0]
        db = Data()
        #descuento = int(db.return_descuento_paciente(id_paciente)[0])
        #precio_servicio = int(db.return_monto_servicio(id_servicio)[0])
        #total_consulta = precio_servicio - precio_servicio * (descuento/100)
        #round(total_consulta)

        self.timee=self.anioo.get()+"-"+self.mess.get()+"-"+self.diia.get()+" "+self.horaa.get()+":"+self.minu.get()+":"+"00"
        print("tiempo ", self.timee)
        estatus = 1 if self.statusp.get()=="Pagado" else 0
        valoresr = (int(id_paciente),"2022-12-31 15:30:21",estatus)
        print(valoresr)
        db.insertar_reserva(valoresr)
        self.llenar_tablaCit()
        #self.llenar_tablas_reserva() 

    def llenar_tablaCit(self):
        self.vaciar_tablaCit()
        db = Data()
        self.filas_pac = db.return_list_pacientes()
        self.filas_cit=db.return_reserva()
        for fila in self.filas_cit:
            id = fila[0]
            idP=fila[1]
            for fila2 in self.filas_pac:
                if(idP==fila2[0]):
                    self.tabla_reserva.insert(
                    "", END, id, text=id, values=[fila2[1],fila[2],"Pagado"if fila[3]==1 else "No pagado"])
        


        print("Jelou")
