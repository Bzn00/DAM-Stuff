import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()


ventana.geometry("1050x550")
ventana.title("Gestor de videojuegos")

etiquetaTitulo = tk.Label(text="Titulo")
etiquetaTitulo.grid(padx=115, pady=20, row=1, column=0)

etiquetaGenero = tk.Label(text="Genero")
etiquetaGenero.grid(padx=115, pady=20, row=2, column=0)

etiquetaPlataforma = tk.Label(text="Plataforma")
etiquetaPlataforma.grid(padx=10, pady=20, row=3, column=0)

etiquetaNota = tk.Label(text="Nota")
etiquetaNota.grid(padx=115, pady=20, row=4, column=0)

frame = tk.Frame(ventana)
frame.grid(padx=100, pady=100)

tabla = ttk.Treeview(columns=("Titulo", "Genero", "Plataforma", "Nota"), show="headings")
tabla.grid(row=0, column=0)

tabla.heading("Titulo", text="Titulo")
tabla.heading("Genero", text="Genero")
tabla.heading("Plataforma", text="Plataforma")
tabla.heading("Nota", text="Nota")

campoTitulo = tk.Entry()
campoTitulo.grid(padx=10, row=1, column=1)
campoGenero = tk.Entry()
campoGenero.grid(padx=10, row=2, column=1)
campoPlataforma = tk.Entry()
campoPlataforma.grid(padx=10, row=3, column=1)
campoNota = tk.Entry()
campoNota.grid(padx=10, row=4, column=1)


def insertarDatos():
    titulo = campoTitulo.get()
    genero = campoGenero.get()
    plataforma = campoPlataforma.get()
    nota = campoNota.get()

    if titulo or genero or plataforma or nota:
        tabla.insert("", tk.END, values=(titulo, genero, plataforma, nota))
        campoTitulo.delete(0, tk.END)
        campoGenero.delete(0, tk.END)
        campoPlataforma.delete(0, tk.END)
        campoNota.delete(0, tk.END)

    

botonInsertarDatos = tk.Button(ventana, text="Insertar datos", command=insertarDatos)
botonInsertarDatos.grid(padx=20, pady=20, column=2, row=5)


ventana.mainloop()


