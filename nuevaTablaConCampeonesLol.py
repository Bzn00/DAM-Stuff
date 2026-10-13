import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

root = tk.Tk()
# Funciones
def insertarDatos():
    nombre = campoTextoNombre.get()
    rol = campoTextoRol.get()
    daño = campoTextoTipoDaño.get()
    vida = campoTextoVida.get()

    if campoTextoNombre.get() == "" or campoTextoRol.get() == "" or campoTextoTipoDaño.get() == "" or campoTextoVida.get() == "":
        messagebox.showwarning(title="Error", message="Intrdouce valores para adjuntarlos a la tabla")
    else: 
        tablaCampeones.insert("", "end", values=(nombre, rol, daño, vida))
        campoTextoNombre.delete(0, tk.END)
        campoTextoRol.delete(0, tk.END)
        campoTextoTipoDaño.delete(0, tk.END)
        campoTextoVida.delete(0, tk.END)
    
def eliminarSeleccion():
    seleccion = tablaCampeones.selection()
    if not seleccion:
        messagebox.showinfo(title="Error",message="Selecciona un campo para eliminarlo")
    else:
        tablaCampeones.delete(seleccion)

def eliminarTodo():
    entrada = messagebox.askyesno(title="Confirmacion", message="¿Desea eliminar la tabla?")
    if entrada:
        messagebox.showinfo(title="Eliminar", message="Eliminando tabla..")
        tablaCampeones.delete(*tablaCampeones.get_children())
    else:
        messagebox.showinfo(title="Elegiste no eliminar la tabla", message="No se eliminara nada")


def salirVentana(evt):
    mensaje = messagebox.askyesno(message="¿Quieres salir?")
    if mensaje: 
        root.destroy()


def editarCampos(evt):
   seleccion = tablaCampeones.selection()
   if not seleccion:
       return

   item_id = seleccion[0]
   valores_actuales = tablaCampeones.item(item_id, "values")

   ventanaModal = tk.Toplevel(root)
   ventanaModal.geometry("400x300")
   ventanaModal.grab_set()
   ventanaModal.transient(root)
   tk.Label(ventanaModal, text="Nombre").pack(pady=5)
   entry_nombre = tk.Entry(ventanaModal)
   entry_nombre.pack(pady=5)
   entry_nombre.insert(0, valores_actuales[0])
   entry_nombre.focus_set()  # Foco en el primer cuadro (requisito de examen)
   botonEditar = tk.Button(ventanaModal, text="Editar")
   botonEditar.pack(pady=15)

# Crear elementos

root.geometry("1250x800")
titulo = tk.Label(root, text="Campeones Lol", font=("Impact"))
etiquetaNombre = tk.Label(root, text="Nombre")
etiquetaRol = tk.Label(root, text="Rol")
etiquetaTipoDaño = tk.Label(root, text="Tipo Daño")
etiquetaVida = tk.Label(root, text="Vida")
    

campoTextoNombre = tk.Entry(root)
campoTextoRol = tk.Entry(root)
campoTextoTipoDaño = tk.Entry(root)
campoTextoVida = tk.Entry(root)

root.bind("<Escape>", salirVentana)

botonInsertarDatos = tk.Button(text="Insertar", command=insertarDatos)
botonEliminarSeleccion = tk.Button(text="Eliminar", command=eliminarSeleccion)
botonEliminarDatos = tk.Button(text="Eliminar todo", command=eliminarTodo)
botonEditarDatos = tk.Button(text="Editar", command=editarCampos)
frame = tk.Frame(root)
tablaCampeones = ttk.Treeview(frame, columns=("Nombre", "Rol", "Tipo daño", "Vida"), show="headings")
tablaCampeones.heading("Nombre", text="Nombre")
tablaCampeones.heading("Rol", text="Rol")
tablaCampeones.heading("Tipo daño", text="Tipo de daño")
tablaCampeones.heading("Vida", text="Vida")

tablaCampeones.bind("<Double-1>", editarCampos)

# Posicionar elementos
titulo.grid(row=0, column=2, padx=10)
etiquetaNombre.grid(row=1 ,column=0, padx=100) 
etiquetaRol.grid(row=1, column=1, padx=100)  
etiquetaTipoDaño.grid(row=1, column=2, padx=100)
etiquetaVida.grid(row=1, column=3, padx=100)

campoTextoNombre.grid(row=2, column=0, padx=100)
campoTextoRol.grid(row=2, column=1, padx=100)
campoTextoTipoDaño.grid(row=2, column=2, padx=100)
campoTextoVida.grid(row=2, column=3, padx=100)

botonInsertarDatos.grid(row=3, column=2, pady=50)
botonEliminarSeleccion.grid(row=3, column=1, pady=50, padx=20)
botonEliminarDatos.grid(row=3, column=0, padx=20, pady=50)
botonEditarDatos.grid(row=3, column=3, padx=20, pady=50)
frame.grid(row=4, column=0, columnspan=4)


#Insertar datos json
with open("C:\\Users\\PC GAMER\\Documents\\VSCode\\nuevaTablaConCampeonesLol.json", "r", encoding="UTF-8") as file:
    datos = json.load(file)

for campeones in datos:
    valores = list(campeones.values())
    tablaCampeones.insert("", "end", values=valores)
tablaCampeones.pack(fill="both", expand=True)
root.mainloop()