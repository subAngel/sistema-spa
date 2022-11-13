from re import T
from tkinter import *
from Database.database import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import ctypes


# * COLORES
color1 = "#FAF7F0"
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
        self.img = ImageTk.PhotoImage(Image.open('relax1.png').resize((150,150),Image.ANTIALIAS))
        lblImagen = Label(self.frame, background=background ,image=self.img).place(
            x=100, y=30, width=300, height=150)
        lblImagen = Label(self.frame, background=background ,image=self.img).place(
            x=1000, y=30, width=300, height=150)

    def DrawButtons(self):
        self.imgT = ImageTk.PhotoImage(Image.open('terapeuta.png').resize((100,100),Image.ANTIALIAS))
        self.imgP = ImageTk.PhotoImage(Image.open('paciente.png').resize((100,100),Image.ANTIALIAS))
        self.imgC = ImageTk.PhotoImage(Image.open('cita.png').resize((100,100),Image.ANTIALIAS))
        self.btn_terapeuta = Button(self.frame, font=(font_family, 15), foreground=foreground, background=color3,  text="Ingresar", borderwidth=2, relief="flat", cursor="hand1",
        overrelief="raise", image=self.imgT, command=lambda: self.moduloTerapeuta()).place(x=200, y=420, width=200, height=250)

        self.btn_paciente = Button(self.frame, font=('Segoe UI', 15), foreground=foreground, background=color3, text="Ingresar", borderwidth=2, relief="flat", cursor="hand1",
        overrelief="raise", image=self.imgP, command=lambda: self.Option(2)).place(x=600, y=420, width=200, height=250)

        self.btn_cita = Button(self.frame, font=(font_family, 15), foreground=foreground, background=color3, text="Ingresar", borderwidth=2, relief="flat", cursor="hand1",
        overrelief="raise", image=self.imgC, command=lambda: self.Option(3)).place(x=1000, y=420, width=200, height=250)

    def Option(self,op):
        if op==1:
            self.frame.destroy()


        elif op==2:
            messagebox.showerror(
                message="Falta por ponerla", title="Error")
        elif op==3:
            messagebox.showerror(
                message="Falta por hacerla xd", title="Error")

    def moduloTerapeuta(self):
        self.popT= Toplevel(self.frame)
        self.popT.title("Terapeuta")
        #popT.attributes('-topmost',True)
        self.popT.state('zoomed')
        ancho = self.frame.winfo_screenwidth()
        alto = self.frame.winfo_screenheight()
        self.frame.geometry("{}x{}".format(ancho, alto))

        self.DrawLabelT(self.popT)
        self.DrawEntryT(self.popT)
        self.DrawButtonsT(self.popT)
        self.DrawListT(self.popT)
        self.popT.config(background=background)
        # self.popT.geometry("3000x800")

    def DrawLabelT(self,popT):
        self.lbl_registrarP = Label(popT, foreground=foreground, font=(
            font_family, 30), background=background, text="Terapeuta").place(x=650, y=10)
        self.lbl_idt = Label(popT, foreground=foreground, font=(font_family,
            12), background=background, text="Id Terapeuta").place(x=25, y=70)
        self.lbl_name = Label(popT, foreground=foreground, font=(font_family,
            12), background=background, text="Nombre").place(x=320, y=70)
        self.lbl_ape = Label(popT, foreground=foreground, font=(font_family,
            12), background=background, text="Apellidos").place(x=600, y=70)
        self.lbl_turno = Label(popT, foreground=foreground, font=(font_family,
            12), background=background, text="Turno").place(x=25, y=150)
        self.lbl_sueldo = Label(popT, foreground=foreground, font=(font_family,
            12), background=background, text="Sueldo").place(x=320, y=150)
        self.lbl_especialidad = Label(popT, foreground=foreground, font=(font_family,
            12), background=background, text="Especialidad").place(x=600, y=150)
        self.lbl_cedula = Label(popT, foreground=foreground, font=(font_family,
            12), background=background, text="Cedula").place(x=25, y=240)

    def DrawEntryT(self,popT):

        self.idter = StringVar()
        self.nombreT = StringVar()
        self.apellidosT = StringVar()
        self.turnoT = StringVar()
        self.sueldoT = StringVar()
        self.especialidadT = StringVar()
        self.cedulaT = StringVar()

        self.b_idter = Entry(popT, font=('Arial', 12), relief="flat", background="#E7E7E7",
                             textvariable=self.idter).place(x=140, y=70, height=25, width=150)
        self.b_nombre = Entry(popT, font=('Arial', 12), relief="flat", background="#E7E7E7",
                              textvariable=self.nombreT).place(x=400, y=70, height=25, width=150)
        self.b_apellidos = Entry(popT, font=('Arial', 12), relief="flat", background="#E7E7E7",
                                 textvariable=self.apellidosT).place(x=720, y=70, height=25, width=150)
        self.b_turno = Entry(popT, font=('Arial', 12), relief="flat", background="#E7E7E7",
                             textvariable=self.turnoT).place(x=140, y=150, height=25, width=150)
        self.b_sueldo = Entry(popT, font=('Arial', 12), relief="flat", background="#E7E7E7",
                              textvariable=self.sueldoT).place(x=400, y=150, height=25, width=150)
        self.b_especialidad = Entry(popT, font=('Arial', 12), relief="flat", background="#E7E7E7",
                                    textvariable=self.especialidadT).place(x=720, y=150, height=25, width=150)
        self.b_cedula = Entry(popT, font=('Arial', 12), relief="flat", background="#E7E7E7",
                              textvariable=self.cedulaT).place(x=140, y=240, height=25, width=150)
    def DrawButtonsT(self,popT):
        self.btn_confirm = Button(popT, foreground="white", text="Guardar", borderwidth=2, relief="flat", cursor="hand1",
                                  overrelief="raise", background="#0051C8", command=lambda: self.confirmProcessT(popT)).place(x=750, y=640, width=90)
        self.btn_cancel = Button(popT, text="Cancelar", foreground="white", borderwidth=2, relief="flat", cursor="hand1",
                                 overrelief="raise", background="#E81123", command=lambda: self.canceProcessT()).place(x=850, y=640, width=90)
        self.btn_home = Button(popT, font=(font_family, 15), foreground="white", text="Regresar", borderwidth=2, relief="flat", cursor="hand1",
                               overrelief="raise", background="#0051C8", command=lambda: self.homT(popT)).place(x=950, y=640, width=90)
    def DrawListT(self,popT):
        self.list_elemtsT = ttk.Treeview(popT, columns=(
            1, 2, 3, 4, 5, 6, 7), show="headings", height="8")

        # --- STYLE ---
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="#0051C8",
                        relief="flat", foreground="white")
        style.map("Treeview", background=[
                  ('selected', 'yellow')], foreground=[('selected', 'black')])

        # --- Event---
        self.list_elemtsT.bind("<Double 1>", self.getRowT)
        # ---- end ---

        self.list_elemtsT.heading(1, text="IdTerapeuta")
        self.list_elemtsT.heading(2, text="Nombre")
        self.list_elemtsT.heading(3, text="Apellidos")
        self.list_elemtsT.heading(4, text="Turno")
        self.list_elemtsT.heading(5, text="Sueldo")
        self.list_elemtsT.heading(6, text="Especialidad")
        self.list_elemtsT.heading(7, text="Cedula")

        self.list_elemtsT.column(1, anchor=CENTER)
        self.list_elemtsT.column(2, anchor=CENTER)
        self.list_elemtsT.column(3, anchor=CENTER)
        self.list_elemtsT.column(4, anchor=CENTER)
        self.list_elemtsT.column(5, anchor=CENTER)
        self.list_elemtsT.column(6, anchor=CENTER)
        self.list_elemtsT.column(7, anchor=CENTER)

        # -- FILL LIST--
        d = Data()
        self.rows = d.returnAllElements()
        for i in self.rows:
            print(i)
            self.list_elemtsT.insert('', 'end', values=i)
        # ----- end -----

        self.list_elemtsT.place(x=10, y=400)

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
        self.idter.set("")
        self.nombreT.set("")
        self.apellidosT.set("")
        self.turnoT.set("")
        self.sueldoT.set("")
        self.especialidadT.set("")
        self.cedulaT.set("")

    def confirmProcessT(self,popT):
        # if self.nombre.get() != "":#self.idter.get() != None and self.nombre.get() != "" and self.apellidos.get() != "" and self.turno.get() != "" and self.sueldo.get() != None and self.especialidad.get() != "" and self.cedula.get() != "":
        d = Data()
        arr = [self.idter.get(), self.nombreT.get(), self.apellidosT.get(), self.turnoT.get(
        ), self.sueldoT.get(), self.especialidadT.get(), self.cedulaT.get()]
        d.InsertItems(arr)
        # messagebox.showinfo(
        #     title="Alerta", message="Se inserto correctamente!")
        self.ClearListT()
        self.DrawListT(popT)
        self.ClearEntryT()

    def homT(self,popT):
        popT.destroy()
