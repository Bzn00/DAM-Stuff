import tkinter as tk
from tkinter import messagebox

root = tk.Tk()



campoTexto = tk.Entry()
textoAEditar = tk.Label(text="HOLA MUNDO")


def cambiarEtiqueta():
    if campoTexto == "":
        messagebox.showerror(title="Error", message="Introduce un texto para cambiarlo")
    else:
        textoAEditar.configure(text=campoTexto.get())

boton = tk.Button(text="Cambiar texto", command=cambiarEtiqueta)

root.geometry("800x600")

campoTexto.pack()
boton.pack()
textoAEditar.pack()

root.mainloop()