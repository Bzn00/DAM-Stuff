import tkinter as tk
from tkinter import font

ventana = tk.Tk()



ventana.title("Cambiar propiedades etiqueta")
ventana.geometry("800x600")


fuente = font.Font(family="Segoe UI", size=25, weight="bold")


label = tk.Label(ventana, text="Pasa el raton y cambia el estilo", width=35, anchor="center")
label.grid(row=0, column=0, columnspan=3, pady=12)


def cambiarColorForeGround():
    label.config(fg="blue")

def cambiarColorBackGround():
    label.config(bg="white")

def cambiarFuente():
    label.config(font=fuente)

def reset():
    label.config(text="Pasa el raton y cambia el estilo", fg="black", bg=ventana.cget("bg"), font=("Segoe UI", 11))

btn_fg = tk.Button(ventana, text="Texto azul", command=cambiarColorForeGround)
btn_bg = tk.Button(ventana, text="Fondo claro", command=cambiarColorBackGround)
btn_font = tk.Button(ventana, text="Fuente bold", command=cambiarFuente)
btn_reset = tk.Button(ventana, text="Reset", command=reset)


btn_fg.grid(row=1, column=0, padx=5, pady=8)
btn_bg.grid(row=1, column=1, padx=5, pady=8)
btn_font.grid(row=1, column=2, padx=5, pady=8)
btn_reset.grid(row=2, column=0, columnspan=3, pady=8)

def entrar(_):
    label.config(text="Dentro de la etiqueta!", underline=0)

def salir(_):
    label.config(text="Pasa el raton para cambiar estilo", underline=-1)

label.bind("<Enter>", entrar)
label.bind("<Escape>", salir)

ventana.mainloop()