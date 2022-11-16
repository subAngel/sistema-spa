import ctypes
from re import T
from tkinter import *
from tkinter import messagebox, ttk

from PIL import Image, ImageTk

from Database.database import *

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
                               overrelief="raise", image=self.imgC, command=lambda: self.Option(3)).place(x=1000, y=420, width=200, height=250)

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

    def homT(self, popT):
        popT.destroy()


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

                self.btn_nuevo_p.config(state=NORMAL)
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
<<<<<<< HEAD

=======
        
                
        self.tabla_pacientes.bind("<<TreeviewSelect>>", seleccionar)
        
>>>>>>> 574785e26b808fda1b100cb8ba72425a422528a2
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
            font_family, 12), cursor="hand1", overrelief="raise", background="#b3ffae", command=lambda: self.generar_cita(mp))
        self.btn_generar_cita.grid(column=3, row=8)

    def vaciar_tabla_cliente(self):
        filas = self.tabla_pacientes.get_children()
        for fila in filas:
            self.tabla_pacientes.delete(fila)

    def llenar_tabla_cliente(self):
        self.vaciar_tabla_cliente()
        d = Data()
        self.filas = d.returnAllElementsC()
        print(self.filas)
        for fila in self.filas:
            id = fila[0]
            self.tabla_pacientes.insert("", END, id, text=id, values=fila)

    def nuevo_cliente(self, mp):
        print("hola")
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
<<<<<<< HEAD
=======
        
    def getID(id):
        return id
>>>>>>> 574785e26b808fda1b100cb8ba72425a422528a2

    def eliminar_cliente(self, popT):
        id = self.tabla_pacientes.selection()[0]
        db = Data()
        if id:
            db.DeleteC(int(id))
            self.tabla_pacientes.delete(id)
            self.lbl_messagess.config(
                text="Paciente eliminado", fg="#d2b440", bg=background)
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
        print("idcc ", id)
        db = Data()
        db.actualizar_paciente(arr, id)
        self.lbl_messagess.config(
            text="Paciente modificado correctamente", fg="green")
        self.llenar_tabla_cliente()
        print("hii")
        self.limpiar_campos_cliente()
        self.btn_nuevo_p.config(state=NORMAL)
        self.btn_eliminar_p.config(state=NORMAL)
        self.btn_modificar_p.config(state=NORMAL)
        print("-----------------------------------")


         

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

    def generar_cita(self, padre):
        self.padre = Toplevel(self.frame)
        self.padre.title("Generar Cita")
        ancho = self.frame.winfo_screenwidth()
        alto = self.frame.winfo_screenheight()
        self.padre.geometry("{}x{}".format(740, 650))
        self.marcoCita = LabelFrame(self.padre, text="Formulario de Cliente")

        self.marcoCita.place(x=50, y=50, width=500, height=400)

        self.marcoCita.config(background=background)

    def homT(self, popT):
        popT.destroy()
# **
