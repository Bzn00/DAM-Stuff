import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()
etiquetaNombre = tk.Label(text="Nombre")
campoTextoNombre = tk.Entry()
etiquetaApellido = tk.Label(text="Apellido")
campoTextoApellido = tk.Entry()
etiquetaCurso = tk.Label(text="Curso")
campoTextoCurso = tk.Entry()
etiquetaMarcarSiPromociona = tk.Label(text="Marcar si promociona")
campoBooleanPromociona = tk.Checkbutton()

tablaValores = ttk.Treeview(ventana, columns=("Nombre", "Apellido", "Curso", "Marcar si promociona"))
tablaValores.heading("Nombre", text="Nombre", anchor="w")
tablaValores.heading("Apellido", text="Apellido", anchor="w")
tablaValores.heading("Curso", text="Curso", anchor="w")
tablaValores.heading("Marcar si promociona", text="¿Promociona?", anchor="w")

ventana.title("Tabla alumnos")

ventana.geometry("1200x800")

etiquetaNombre.grid(padx=100, pady=10, column=1)
campoTextoNombre.grid(padx=100, pady=0, column=1)
etiquetaApellido.grid(padx=100, pady=10, column=1)
campoTextoApellido.grid(padx=100, pady=0, column=1)
etiquetaCurso.grid(padx=100, pady=10, column=1)
campoTextoCurso.grid(padx=100, pady=0, column=1)
etiquetaMarcarSiPromociona.grid(padx=100, pady=10, column=1)
campoBooleanPromociona.grid(padx=100, pady=0, column=1)

tablaValores.grid(padx=200, pady=0, column=2)

ventana.mainloop()