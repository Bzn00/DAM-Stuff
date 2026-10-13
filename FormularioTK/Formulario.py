import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

    



ventana = tk.Tk()

def salir():
    ventana.destroy()


ventana.geometry("1200x600")
campoTextoTitulo = tk.Label(ventana, text="Rellena los siguientes campos", font=("Malignant", 24)).grid(padx=33, pady=50, sticky='ne', column=0)

campoTextoNombreCompleto = tk.Label(text="Nombre completo", font=("Arial", 10)).grid(padx=100, sticky='nw', column=0)
rellenarNombre = tk.Entry(ventana)
rellenarNombre.grid(padx=90, pady=5, sticky='nw', column=0)

campoTextoEmail = tk.Label(ventana, text="E-mail", font=("Arial", 10)).grid(padx=100, pady=5, sticky='nw', column=0)
rellenarEmail = tk.Entry(ventana)
rellenarEmail.grid(padx=90, sticky='nw', column=0, pady=5)

etiquetaAsunto = tk.Label(ventana, text="Asunto", font=("Arial", 10)).grid(padx=100, pady=5, sticky='nw', column=0)
campoEntradaAsunto = tk.Entry(ventana)
campoEntradaAsunto.grid(padx=90, pady=5, sticky='nw', column=0)

tablaNombresEmail = ttk.Treeview(ventana, columns=("Nombre", "E-Mail", "Asunto"))

def insertarDatos():
    nombre = rellenarNombre.get()
    email = rellenarEmail.get()
    asunto = campoEntradaAsunto.get()
    tablaNombresEmail.insert("", "end", values=(nombre, email, asunto))
    rellenarNombre.delete(0, tk.END)
    rellenarEmail.delete(0, tk.END)
    campoEntradaAsunto.delete(0, tk.END)

botonInsertar = tk.Button(ventana, text="Insertar datos", command=insertarDatos).grid(padx=90, pady=35, sticky='nw', column=0, row=6)

botonSalir = tk.Button(ventana, text="Salir", command=salir).grid(padx=90, pady=65, sticky='nw', column=0, row=6)

tablaNombresEmail.heading("Nombre", text="Nombre")
tablaNombresEmail.heading("E-Mail", text="E-Mail")
tablaNombresEmail.heading("Asunto", text="Asunto")
tablaNombresEmail.grid(padx=0, pady=0, column=1, row=6)


ventana.mainloop()
