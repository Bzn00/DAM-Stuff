import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
root = tk.Tk()
root.geometry("1050x550")
root.title("Gestion Alumnos")

# Creamos etiquetas
labelTitulo = tk.Label(text="Gestion de alumnos", font="Arial")
labelNombre = tk.Label(text="Nombre", font="Arial")
labelApellido = tk.Label(text="Apellido", font="Arial")
labelCurso = tk.Label(text="Curso", font="Arial")
labelNota = tk.Label(text="Nota", font="Arial")

# Creamos campos de entrada, etc
campoTextoNombre = tk.Entry()
campoTextoApellido = tk.Entry()
desplegableCurso = ttk.Combobox(values=("1º SMR", "2º SMR", "1º DAM", "2º DAM"))
campoTextoNota = tk.Entry()
frameTabla = tk.Frame(root)
frameBotones = tk.Frame(root)

# Funciones para la tabla
contadorID = 1
def añadirAlumno():
    global contadorID
    nombre = campoTextoNombre.get()
    apellido = campoTextoApellido.get()
    curso = desplegableCurso.get()
    nota = campoTextoNota.get()

    tablaAlumnos.insert("", "end", values=(contadorID, nombre, apellido, curso, nota))
    contadorID+=1
    campoTextoNombre.delete(0, tk.END)
    campoTextoApellido.delete(0, tk.END)
    desplegableCurso.set("")
    campoTextoNota.delete(0, tk.END)



# Creamos botones
botonAñadir = tk.Button(frameBotones, text="Añadir", command=añadirAlumno)
botonModificar = tk.Button(frameBotones, text="Modificar")


def eliminarSeleccionado():
    seleccion = tablaAlumnos.selection()
    if seleccion:
        tablaAlumnos.delete(seleccion[0])


botonEliminar = tk.Button(frameBotones, text="Eliminar", command=eliminarSeleccionado)

#Creamos la tabla
columnas = ("ID", "Nombre", "Apellidos", "Curso", "Nota")
tablaAlumnos = ttk.Treeview(frameTabla, columns=columnas, show="headings")
for columna in columnas:
    tablaAlumnos.heading(columna, text=columna)

def limpiarAlumnos():
    valor = messagebox.askyesno(title="Borrar", message="¿Eliminar tabla?")
    if valor == True:
        messagebox.showinfo(title="Si", message="Se ha elegido eliminar la tabla")
        for elemento in tablaAlumnos.get_children():
            tablaAlumnos.delete(elemento)
    else:
        messagebox.showinfo(title="No", message="Se ha elegido no eliminar la tabla")

botonLimpiar = tk.Button(frameBotones, text="Limpiar", command=limpiarAlumnos)
# Colocamos Etiquetas
labelTitulo.grid(padx=100, pady=10, column=1, row=0)
labelNombre.grid(padx=50, pady=5, column=0, row=1)
labelApellido.grid(padx=50, pady=5, column=0, row=2)
labelCurso.grid(padx=50, pady=5, column=0, row=3)
labelNota.grid(padx=50, pady=5, column=0, row=4)

# Colocamos Campos de texto, e.t.c.
campoTextoNombre.grid(padx=0, pady=5, column=1, row=1)
campoTextoApellido.grid(padx=0, pady=5, column=1, row=2)
desplegableCurso.grid(padx=0, pady=5, column=1, row=3)
campoTextoNota.grid(padx=0, pady=5, column=1, row=4)

# Colocamos Botones
frameBotones.grid(row=5, column=0, columnspan=5)
botonAñadir.grid(padx=50, row=0, column=0)
botonEliminar.grid(padx=50, row=0, column=1)
botonLimpiar.grid(padx=50, row=0, column=2)
botonModificar.grid(padx=50, row=0, column=3)
frameTabla.grid(row=7, column=0, columnspan=4, padx=20, pady=20)
tablaAlumnos.pack()

root.mainloop()