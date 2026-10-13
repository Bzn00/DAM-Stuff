import tkinter as tk
from tkinter import ttk
import json

root = tk.Tk()


frameIntroducirDatos = tk.Frame(root)

frameTabla = tk.Frame(root)

etiquetaNuevoCoche = tk.Label(frameIntroducirDatos, text="Nuevo coche")
etiqeutaMarca = tk.Label(frameIntroducirDatos, text="Marca: ")
etiquetaModelo = tk.Label(frameIntroducirDatos, text="Modelo: ")
etiqeutaAño = tk.Label(frameIntroducirDatos, text="Año: ")
campoTextoMarca = tk.Entry(frameIntroducirDatos)
campoTextoModelo = tk.Entry(frameIntroducirDatos)
campoEditarAño = ttk.Spinbox(frameIntroducirDatos, from_=2000, to=2026)
tablaCoches = ttk.Treeview(frameTabla, columns=("Marca", "Modelo", "Año"), show="headings")
tablaCoches.heading("Marca", text="Marca")
tablaCoches.heading("Modelo", text="Modelo")
tablaCoches.heading("Año", text="Año")

def añadirCoche():
    datos = [campoTextoMarca.get(), campoTextoModelo.get(), campoEditarAño.get()]
    tablaCoches.insert("", tk.END, values=datos)

botonAñadir = tk.Button(frameIntroducirDatos, text="Añadir", command=añadirCoche)
frameIntroducirDatos.grid(column=0, row=0)
etiquetaNuevoCoche.grid(padx=100, column=0, row=0)
etiqeutaMarca.grid(padx=0, pady=0, column=1, row=1)
etiquetaModelo.grid(padx=0, pady=0, column=1, row=2)
etiqeutaAño.grid(padx=0, pady=0, column=1, row=3)
campoTextoMarca.grid(padx=0, pady=0, column=2, row=1)
campoTextoModelo.grid(padx=0, pady=0, column=2, row=2)
campoEditarAño.grid(padx=0, pady=0, column=2, row=3)
botonAñadir.grid(padx=100, pady=0, column=3, row=3)
frameTabla.grid(row=4, pady=200, column=0, padx=20)
tablaCoches.grid(padx=0, pady=0, column=0, row=0)
root.geometry("800x600")
root.mainloop()