import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
root = tk.Tk()



root.geometry("800x600")

columnas = ["Nombre", "Calificacion", "Genero"]
tabla = ttk.Treeview(columns=(columnas), show="headings")

def eliminarFila():
    seleccion = tabla.selection()
    tabla.delete(seleccion)


botonEliminar = tk.Button(text="Eliminar", command=eliminarFila)

tabla.heading("Nombre", text=columnas[0])
tabla.heading("Calificacion", text=columnas[1])
tabla.heading("Genero", text=columnas[2])

with open("C:\\Users\\PC GAMER\\Documents\\VSCode\\PracticaInsertarDatosJSON\\animes.json", "r", encoding="UTF-8") as file:
    datos = json.load(file)

for animes in datos:
    valores = list(animes.values())
    tabla.insert("", "end", values=valores)

tabla.grid(row=1, column=1, pady=100, padx=100)

botonEliminar.grid(row=2, column=1)

root.mainloop()