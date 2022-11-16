from tkinter import *
from Home.home import *
from Database.database2 import *
from tkinter import messagebox
from PIL import ImageTk, Image


class Login:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("Bienvenido al sistema")
        self.frame.config(background="#000000")
        self.frame.geometry("500x500+400+100")
        self.frame.resizable(0, 0)
        self.DrawEntry()
        self.DrawButtons()
        self.DrawLabel()
        # self.DrawList()
        self.DrawImage()
        self.frame.mainloop()

    def DrawLabel(self):
        self.lbl_usuario = Label(self.frame, foreground="white", font=(
            'Times', 30), background="#000000", text="Bienvenido al sistema").place(x=100, y=210)
        self.lbl_usuario = Label(self.frame, foreground="white", font=(
            8), background="#000000", text="Usuario").place(x=230, y=260)
        self.lbl_usuario = Label(self.frame, foreground="white", font=(
            8), background="#000000", text="Contraseña").place(x=220, y=340)

    def DrawEntry(self):
        self.user = StringVar()
        self.password = StringVar()

        self.c_user = Entry(self.frame, validate="key", font=('Times', 12), relief="flat", background="#E7E7E7",
                            textvariable=self.user).place(x=160, y=290, height=25, width=200)
        self.c_password = Entry(self.frame, show="*", font=('Times', 12), relief="flat", background="#E7E7E7",
                                textvariable=self.password).place(x=160, y=370, height=25, width=200)

    def DrawImage(self):
        self.img = ImageTk.PhotoImage(Image.open('prueba.jpg'))
        lblImagen = Label(self.frame, image=self.img).place(
            x=100, y=30, width=300, height=150)

    def validate_number(text):
        return text.isdecimal()

    def DrawButtons(self):
        self.btn_login = Button(self.frame, font=('Times', 15), foreground="white", text="Ingresar", borderwidth=2, relief="flat", cursor="hand1",
                                overrelief="raise", background="#0051C8", command=lambda: self.check()).place(x=200, y=420, width=100)

    def check(self):
        d = Data()

        res = d.checkuser(self.user.get(), self.password.get())
        if res:
            # messagebox.showinfo(message="Bienvenid@", title="Bienvenid@")
            self.frame.destroy()
            Home()
        else:
            messagebox.showerror(
                message="Credenciales incorrectas", title="Error")
