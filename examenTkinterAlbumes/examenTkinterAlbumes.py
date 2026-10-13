import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

root = tk.Tk()


campoNombreArtista = tk.Entry()
campoTituloAlbum = tk.Entry()
campoAñoAlbum = tk.Spinbox(from_=1900, to=2030)



def salirVentana(evt):
    opcion = messagebox.askyesno(message="¿Quieres salir?")
    if opcion == messagebox.askyesno.YES:
        root.destroy()
    else:
        messagebox.showinfo(message="Se ha elegido no salir")

root.geometry("1600x600")
root.title("Tabla Albumes")

columnas = ["Artista", "Titulo album", "Año"]

etiquetaTitulo = tk.Label(text="Tabla albumes", font="Impact")
etiquetaNombreArtista = tk.Label(text="Artista", font="Terminal")
etiquetaTituloAlbum = tk.Label(text="Titulo Album", font="Terminal")
etiquetaAñoAlbum = tk.Label(text="Año", font="Terminal")

root.bind("<Escape>", func=salirVentana)

def insertarDatos():
    artista = campoNombreArtista.get()
    titulo = campoTituloAlbum.get()
    año = campoAñoAlbum.get()
    if artista == "" or titulo == "" or año == "":
        messagebox.showinfo(message="Error, no puede haber ningun campo vacio")
    else:
        tablaDatos.insert("", "end", values=(artista, titulo, año))
        campoNombreArtista.delete(0, tk.END)
        campoTituloAlbum.delete(0, tk.END)
        campoAñoAlbum.delete(0, tk.END)

    
def borrarCampo():
    seleccion = tablaDatos.selection()
    if seleccion:
        tablaDatos.delete(seleccion)
    else:
        messagebox.showerror(title="Error", message="Error, selecciona un elemento para eliminarlo")


botonInsertar = tk.Button(text="Insertar datos", command=insertarDatos)
botonBorrar = tk.Button(text="Borrar elemento", command=borrarCampo)


tablaDatos = ttk.Treeview(columns=(columnas), show="headings")



tablaDatos.heading("Artista", text="Artista")
tablaDatos.heading("Titulo album", text="Titulo album")
tablaDatos.heading("Año", text="Año")
etiquetaTitulo.grid(padx=50, pady=10, column=0, row=0)
etiquetaNombreArtista.grid(padx=0, pady=10, column=1, row=1)
etiquetaTituloAlbum.grid(padx=0, pady=10, column=1, row=2)
etiquetaAñoAlbum.grid(padx=0, pady=10, column=1, row=3)
botonInsertar.grid(padx=100, pady=10, column=3, row=2)
botonBorrar.grid(padx=100, pady=10, column=3, row=3)
campoNombreArtista.grid(padx=0, pady=10, column=2, row=1)
campoTituloAlbum.grid(padx=0, pady=10, column=2, row=2)
campoAñoAlbum.grid(padx=0, pady=10, column=2, row=3)
tablaDatos.grid(column=4, row=2)

with open("C:\\Users\\PC GAMER\\Documents\\VSCode\\examenTkinterAlbumes\\albumes.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    for album in datos:
        tablaDatos.insert("",
                            "end",
                             values=(album["artista"],
                                    album["nombre"], 
                                    str(album["año"])
                                ),
                            )

root.mainloop()