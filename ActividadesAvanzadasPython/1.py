import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



ventanaPrincipal = tk.Tk()
ventanaPrincipal.geometry("1200x600")
ventanaPrincipal.title("Gestor de tareas")




etiquetaPresentacion = tk.Label(ventanaPrincipal, text="Gestor de tareas", font="Impact")
etiquetaNombreTarea = tk.Label(ventanaPrincipal, text="Nombre de la tarea")
campoTarea = tk.Entry(ventanaPrincipal)
etiquetaTiempoEstimado = tk.Label(ventanaPrincipal, text="Tiempo estimado (min)")
campoTiempoEstimado = tk.Entry(ventanaPrincipal)
listaTareas = ttk.Treeview(ventanaPrincipal, columns=("Tarea", "Tiempo"), show="headings")
listaTareas.heading("Tarea", text="Tarea")
listaTareas.heading("Tiempo", text="Tiempo estimado(min)")


def salir():
    ventanaPrincipal.destroy()

def añadirTarea():
    tarea = campoTarea.get()
    tiempo = campoTiempoEstimado.get()
    if tarea != "" or tiempo != "":
        listaTareas.insert("", "end", values=(tarea, tiempo))
    else:
        messagebox.showerror(title="Error", message="Error el campo \"tarea\" o \"tiempo estimado\" esta vacio")


def borrarSeleccionado(seleccion):
    if seleccion:
        listaTareas.delete(*seleccion)

def borrarTodo():
    listaTareas.delete()

frameBotones = tk.Frame(ventanaPrincipal)
botonInsertar = tk.Button(frameBotones, text="Insertar Tarea", command=añadirTarea)
botonSalir = tk.Button(ventanaPrincipal, text="Salir", command=salir)
botonBorrarSeleccion = tk.Button(frameBotones, text="Borrar Seleccion", command=lambda: borrarSeleccionado(listaTareas.selection()))
botonBorrarTodo = tk.Button(frameBotones, text="Borrar todo", command=borrarTodo)

etiquetaPresentacion.grid(row=0, padx=550, pady=10, column=0)

etiquetaNombreTarea.grid(padx=1, pady=2, column=0, row=1)
campoTarea.grid(padx=1, pady=1,  column=0, row=2)

etiquetaTiempoEstimado.grid(padx=1, pady=10, column=0, row=3)
campoTiempoEstimado.grid(padx=1, pady=1, column=0, row=4)

botonInsertar.grid(padx=5, column=0, row=0)
botonBorrarSeleccion.grid(padx=5, column=1, row=0)
botonBorrarTodo.grid(padx=5, column=2, row=0)

frameBotones.grid(row=5, column=0, pady=10)

listaTareas.grid(padx=1, pady=40, column=0, row=6)

botonSalir.grid(padx=0, pady=30, column=0, row=7)

ventanaPrincipal.mainloop()
