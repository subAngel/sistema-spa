from cProfile import label
from email.mime import image
import tkinter
from tkinter import*
from tkinter import messagebox
import pymysgql

pantalla = Tk()
pantalla.geometry('300x380')
pantalla.title("Welcome")
pantalla.iconbitmap('logo-spa.ico')

image = PhotoImage(file="logo-spa.gif")
image = image.subsample(2, 2)
label = Label(image=image)
label.pack()

Label(text="Acceso al sistema", bg='lightSteelBlue1', fg="white", width='300', height='3', font=("Hasklug NF", 15)).pack()



pantalla.mainloop()
