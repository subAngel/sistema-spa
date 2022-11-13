from re import T
from tkinter import *
from Database.database import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import ctypes


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
        # self.lbl_usuario = Label(self.frame, foreground="white", font=(
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
                                   overrelief="raise", image=self.imgP, command=lambda: self.Option(2)).place(x=600, y=420, width=200, height=250)

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

    def DrawComponents(self, popT):
        self.nombreT = StringVar()
        self.apellidosT = StringVar()
        self.turnoT = StringVar()
        self.sueldoT = StringVar()
        self.especialidadT = StringVar()
        self.cedulaT = StringVar()

        def seleccionar(event):
            id = self.list_elemtsT.selection()[0]
            if id:
                self.nombreT.set(self.list_elemtsT.item(id, "values")[1])
                self.apellidosT.set(self.list_elemtsT.item(id, "values")[2])
                self.turnoT.set(self.list_elemtsT.item(id, "values")[3])
                self.sueldoT.set(self.list_elemtsT.item(id, "values")[4])
                self.especialidadT.set(self.list_elemtsT.item(id, "values")[5])
                self.cedulaT.set(self.list_elemtsT.item(id, "values")[6])
                self.btn_nuevo_tera.config(state=DISABLED)
                self.btn_modificar_tera.config(state=NORMAL)
                self.btn_eliminar_tera.config(state=NORMAL)

        def limpiar_campos():
            self.ClearEntryT()
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
            column=0, row=4, columnspan=7, padx=100, pady=80)
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
        # self.btn_modificar_tera = Button(popT, font=(font_family, 13), foreground="#222",
        #                                  text="EDITAR", borderwidth=2, relief="flat", cursor="hand1", overrelief="raise",
        #                                  background="#B1AFFF", command=lambda: self.modificar_terapeuta(popT))
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
        ), self.sueldoT.get(), self.especialidadT.get(), self.cedulaT.get()]
        d.InsertItems(arr)
        self.llenar_tabla_terapeuta()
        self.lbl_messages.config(
            text="Registro correcto", fg="green", bg=background)
        self.ClearEntryT()

    def eliminar_terapeuta(self, popT):
        id = self.list_elemtsT.selection()[0]
        db = Data()
        if id:
            db.Delete(int(id))
            self.list_elemtsT.delete(id)
            self.lbl_messages.config(
                text="Terapeuta eliminado", fg="#d2b440", bg=background)
            self.ClearEntryT()
            self.btn_nuevo_tera.config(state=NORMAL)
            self.btn_eliminar_tera.config(state=DISABLED)
            self.btn_modificar_tera.config(state=DISABLED)
        else:
            self.lbl_messages.config(
                text="Seleccione un registro", fg="#eb6736", bg=background)

    def modificar_terapeuta(self):
        arr = [self.nombreT.get(), self.apellidosT.get(), self.combo_turno.get(
        ), self.sueldoT.get(), self.especialidadT.get(), self.cedulaT.get()]
        id = self.list_elemtsT.selection()[0]
        db = Data()
        db.UpdateItem(arr, int(id))
        self.lbl_messages.config(
            text="Terapeuta modificado correctamente", fg="green")
        self.llenar_tabla_terapeuta()
        self.ClearEntryT()
        self.btn_nuevo_tera.config(state=NORMAL)
        self.btn_eliminar_tera.config(state=DISABLED)
        self.btn_modificar_tera.config(state=DISABLED)

    def getRowT(self, event):
        idterap = StringVar()
        nomT = StringVar()
        apeT = StringVar()
        tuT = StringVar()
        suT = StringVar()
        esT = StringVar()
        ceT = StringVar()

        rowName = self.list_elemtsT.identify_row(event.y)
        item = self.list_elemtsT.item(self.list_elemtsT.focus())
        idtt = item['values'][0]
        nt = item['values'][1]
        at = item['values'][2]
        tt = item['values'][3]
        st = item['values'][4]
        et = item['values'][5]
        ct = item['values'][6]

        idterap.set(idtt)
        nomT.set(nt)
        apeT.set(at)
        tuT.set(tt)
        suT.set(st)
        esT.set(et)
        ceT.set(ct)
        popTE = Toplevel(self.popT)
        popTE.geometry("400x200")
        lbl_n = Entry(popTE, textvariable=idterap,
                      state=DISABLED).place(x=40, y=40)
        lbl_e = Entry(popTE, textvariable=nomT).place(x=40, y=80)
        lbl_c = Entry(popTE, textvariable=apeT).place(x=40, y=120)
        lbl_t = Entry(popTE, textvariable=tuT).place(x=40, y=160)
        lbl_s = Entry(popTE, textvariable=suT).place(x=40, y=200)
        lbl_e = Entry(popTE, textvariable=esT).place(x=40, y=240)
        lbl_ce = Entry(popTE, textvariable=ceT).place(x=40, y=280)
        btn_change = Button(popTE, text="Actualizar", relief="flat", background="#00CE54", foreground="white", command=lambda: self.editarT(
            idtt, idterap.get(), nomT.get(), apeT.get(), tuT.get(), suT.get(), esT.get(), ceT.get(), popTE)).place(x=180, y=160, width=90)
        btn_delete = Button(popTE, text="Eliminar", relief="flat", background="red", foreground="white",
                            command=lambda: self.eliminarT(idtt, popTE)).place(x=290, y=160, width=90)

    def eliminarT(self, idtt, popTE):
        d = Data()
        print(idtt)
        d.Delete(idtt)
        popTE.destroy()
        # messagebox.showinfo(title="Eliminacion",
        #                     message="Se ha borrado con exito")
        self.ClearListT()
        self.DrawListT(self.popT)
        self.ClearEntryT()

    def editarT(self, idtt, idterap, nom, ape, tu, su, es, ce, popTE):
        arr = [idterap, nom, ape, tu, su, es, ce]
        d = Data()
        d.UpdateItem(arr, idtt)
        popTE.destroy()
        # messagebox.showinfo(title="Actualizacion",
        #                     message="Se han actualizado los datos")
        self.ClearListT()
        self.DrawListT(self.popT)
        self.ClearEntryT()

    def ClearListT(self):
        self.list_elemtsT.delete(*self.list_elemtsT.get_children())

    def canceProcessT(self):
        self.ClearEntry()

    def ClearEntryT(self):
        # self.idter.set("")
        self.nombreT.set("")
        self.apellidosT.set("")
        self.combo_turno.set("")
        self.sueldoT.set("")
        self.especialidadT.set("")
        self.cedulaT.set("")

    def homT(self, popT):
        popT.destroy()
