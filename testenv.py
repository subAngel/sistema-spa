import tkinter as tk

root = tk.Tk()
#Asignar un color al fondo de root (De preferencia un color que no utilices)
root['bg'] = 'grey'
#Configurar el color que va a ser transparente, debe ser el mismo que el color del fondo de root
root.attributes('-transparentcolor', 'grey')

#Todos los componentes que tengan el color de fondo igual al que configuraste como transparente van a ser transparentes
lbl = tk.Label(text='Soy transparente!', font='Helvetica 36 bold', bg='green', fg='grey')
btn = tk.Button(text='Botón', font='Helvetica 36', bg='grey', fg='blue')
canvas = tk.Canvas(bg='grey')

lbl.pack()
canvas.pack()
btn.pack()

root.mainloop()
