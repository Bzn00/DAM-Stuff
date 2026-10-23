import tkinter as tk


def focusIn(evt):
    if campoEscribirTarea.get() == placeholder_text:
        campoEscribirTarea.delete(0, tk.END)
        campoEscribirTarea.config(fg='black')

def on_focus_out(evt):
    if campoEscribirTarea.get() == "":
        campoEscribirTarea.insert(0, placeholder_text)
        campoEscribirTarea.config(fg='grey')


def añadirTarea():
    tarea = campoEscribirTarea.get()
    listaTareas.insert(tk.END, tarea)
    campoEscribirTarea.delete(0, tk.END)

def eliminarTarea():
    seleccion = listaTareas.selection()
    listaTareas.delete(seleccion)

def marcarHecha():
    seleccion = listaTareas.selecction()
    listaTareas.insert("✔ "+seleccion)

root = tk.Tk()
root.title("Gestor de tareas")
root.geometry("350x400")

placeholder_text= "Escribe la tarea.."

campoEscribirTarea = tk.Entry(root, fg='grey')
campoEscribirTarea.insert(0, placeholder_text)
botonAñadir = tk.Button(text="Añadir", command=añadirTarea)

listaTareas = tk.Listbox(width=40)

botonEliminar = tk.Button(text="Eliminiar", command=eliminarTarea)

botonMarcarHecha = tk.Button(text="Marcar como hecha", command=marcarHecha)

campoEscribirTarea.grid(padx=40, pady=30, row=0, column=0)
botonAñadir.grid(padx=20, pady=30, row=0, column=1)
botonMarcarHecha.grid(padx=20, pady=30, row=3 ,column=1)
campoEscribirTarea.bind("<FocusIn>", focusIn)
campoEscribirTarea.bind("<FocusOut>", on_focus_out)

listaTareas.grid(padx=20, pady=20, column=0, columnspan=2)
botonEliminar.grid(padx=20, pady=20)

root.mainloop()