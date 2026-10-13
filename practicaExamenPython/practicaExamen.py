import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
    

root = tk.Tk()
titulo = tk.Label(text="Gestor de tareas python", font=("Segoe UI", 25, "bold"))

tituloTarea = tk.Label(text="Tarea", font=("Arial", 10, "bold"))
campoTextoTarea = tk.Entry()

nombreUsuario = tk.Label(text="Usuario", font=("Arial", 10, "bold"))
campoTextoUsuario = tk.Entry()

tiempoEstimado = tk.Label(text="Tiempo estimado (min)", font=("Arial", 10, "bold"))
campoTextoTiempoEstimado = tk.Entry()


tablaDatos = ttk.Treeview(root, columns=("Tarea", "Usuario", "Tiempo estimado"), show="headings")
tablaDatos.heading("Tarea", text="Tarea", anchor="w")
tablaDatos.heading("Usuario", text="Usuario", anchor="w")
tablaDatos.heading("Tiempo estimado", text="Tiempo Estimado", anchor="w")

root.title("Gestor de tareas")

def enviarDatosTabla():
    
    campoTextoUsuario.get()
    campoTextoTiempoEstimado.get()
    campoTextoTarea.get()
    if campoTextoUsuario.get() == "" or campoTextoTiempoEstimado.get() == "" or campoTextoTarea.get() == "":
        messagebox.showerror(title="Error", icon="error", message="Error, debes introducir datos en todos los campos de la tabla")
    else:
        datos = [
            (campoTextoTarea.get(), campoTextoUsuario.get(), campoTextoTiempoEstimado.get()),
        ]


    tablaDatos.insert("", "end", values=datos[0])

    
    campoTextoUsuario.delete(0, tk.END)
    campoTextoTiempoEstimado.delete(0, tk.END)
    campoTextoTarea.delete(0, tk.END)


def eliminarFila():
    seleccion = tablaDatos.selection()
    tablaDatos.delete(seleccion)

def eliminarTodo():
    confirmacion = messagebox.askyesno(title="Confirmar", message="¿Quieres borrar toda la tabla?")
    if confirmacion is True:
       for fila in tablaDatos.get_children():
           tablaDatos.delete(fila)
    else:
        messagebox.showinfo(message="Has elegido no borrar la tabla")
        


botonEnviar = tk.Button(text="Enviar", command=enviarDatosTabla)
botonBorrarFila = tk.Button(text="Eliminar Seleccionado", command=eliminarFila)
botonEliminarTabla = tk.Button(text="Borrar tabla", command=eliminarTodo)
root.geometry("1200x675")
titulo.grid(column=1, padx=100, pady=10)
tituloTarea.grid(column=1, padx=12, pady=10)
campoTextoTarea.grid(column=1, padx=12, pady=1)
nombreUsuario.grid(column=1, padx=12, pady=10)
campoTextoUsuario.grid(column=1, padx=12, pady=1)
tiempoEstimado.grid(column=1, padx=12, pady=10)
campoTextoTiempoEstimado.grid(column=1, padx=12, pady=1)
botonEnviar.grid(column=1, padx=12, pady=10)
botonBorrarFila.grid(column=1, padx=12, pady=14)
botonEliminarTabla.grid(column=1, padx=12, pady=18)
tablaDatos.grid(sticky="nsew", column=2)

root.mainloop()