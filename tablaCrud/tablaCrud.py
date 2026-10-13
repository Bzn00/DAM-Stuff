import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

ventanaPrincipal = tk.Tk()
frame = tk.Frame(ventanaPrincipal, bg="lightgray")
tablaDatos = ttk.Treeview(frame, columns=("Nombre", "Edad", "Anime fav"))

tablaDatos.heading("Nombre", text="Nombre")
tablaDatos.heading("Edad", text="Edad")
tablaDatos.heading("Anime fav", text="Anime fav")



etiquetaNombre = tk.Label(ventanaPrincipal, text="Nombre")
etiquetaEdad = tk.Label(ventanaPrincipal, text="Edad")
etiquetaAnimeFav = tk.Label(ventanaPrincipal ,text="Anime Favorito")

campoTextoNombre = tk.Entry(ventanaPrincipal)
campoTextoEdad = tk.Entry(ventanaPrincipal)
campoTextoAnimeFavorito = tk.Entry(ventanaPrincipal)

def insertarDatos():
    nombre = campoTextoNombre.get()
    edad = campoTextoEdad.get()
    animeFav = campoTextoAnimeFavorito.get()

    tablaDatos.insert("", "end", values=( nombre, edad, animeFav))

    campoTextoNombre.delete(0, tk.END)
    campoTextoEdad.delete(0, tk.END)
    campoTextoAnimeFavorito.delete(0, tk.END)

def eliminarDatos():
    seleccion = tablaDatos.selection()
    opcion = messagebox.askyesno(message="¿Quieres eliminar este registro de la tabla?")
    if not seleccion:
        messagebox.showerror(title="Error", message="Elige un elemento para borrar")
    if opcion:
        tablaDatos.delete(seleccion)
    else:
        messagebox.showinfo(message="No se eliminara ningun registro")

def eliminarTodo():
    opcion = messagebox.askyesno(message="¿Quieres borrar toda la tabla?")
    if opcion:
        for elementos in tablaDatos.get_children():
            tablaDatos.delete(elementos)
    else:
        messagebox.showinfo(message="No se ha eliminado ningun elemento")

def cargarDatos():
    opcion = messagebox.askyesno(message="¿Desea cargar los datos?")
    if opcion:
        with open("C:\\Users\\PC GAMER\\Documents\\VSCode\\tablaCrud\\datos.json", "r", encoding="utf-8") as file:
            datos = json.load(file)
        for animes in datos:
            valores = list(animes.values())
            tablaDatos.insert("", "end", values=valores)
    else:
        messagebox.showinfo(message="Se ha elegido no cargar los datos")


botonIntroducir = tk.Button(text="Insertar", command=insertarDatos)
botonEliminar = tk.Button(text="Eliminar", command=eliminarDatos)
botonEliminarTodo = tk.Button(text="Eliminar Todo", command=eliminarTodo)
botonCargarDatos = tk.Button(text="Cargar datos", command=cargarDatos)

frame.grid(column=1, padx=200, pady=20)
tablaDatos.pack(padx=10, pady=10)

etiquetaNombre.grid(column=0, padx=0, pady=10, row=1)
etiquetaEdad.grid(column=0, padx=0, pady=10, row=2)
etiquetaAnimeFav.grid(column=0, padx=0, pady=10, row=3)

campoTextoNombre.grid(column=1, padx=0, pady=10, row=1)
campoTextoEdad.grid(column=1, padx=0, pady=10, row=2)
campoTextoAnimeFavorito.grid(column=1, padx=0, pady=10, row=3)

botonIntroducir.grid(column=1, row=4)
botonEliminar.grid(column=1, row=5)
botonEliminarTodo.grid(column=1, row=6)
botonCargarDatos.grid(column=1, row=7)

with open("C:\\Users\\PC GAMER\\Documents\\VSCode\\tablaCrud\\datos.json", "r", encoding="utf-8") as file:
    datos = json.load(file)

for animes in datos:
    valores = list(animes.values())
    tablaDatos.insert("", "end", values=valores)


ventanaPrincipal.geometry("1200x800")
ventanaPrincipal.mainloop()