import tkinter as tk
from tkinter import ttk
import json

ventana = tk.Tk()
ventana.geometry("825x600")
ventana.title("Tabla albumes")
columnas = ["Nombre", "Grupo", "Año"]
titulo = tk.Label(text="Tabla albumes cargados JSON")
    

tabla = ttk.Treeview(columns=(columnas), show="headings")

tabla.heading("Nombre", text="Nombre")
tabla.heading("Grupo", text="Grupo")
tabla.heading("Año", text="Año lanzamiento")

with open("C:\\Users\\PC GAMER\\Documents\\VSCode\\insertarDatosJsonTkinter\\Albumes\\albumes.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    for album in datos:
        tabla.insert("", "end", values=(album["nombre"], album["grupo"], str(album["año"])))

titulo.grid(padx=100, pady=10)
tabla.grid(padx=10, pady=100)
ventana.mainloop()