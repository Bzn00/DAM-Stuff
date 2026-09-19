import tkinter as Tk

ventana = Tk.Tk()
texto = Tk.StringVar()
entrada = Tk.Entry(ventana, textvariable=texto)
boton = Tk.Button(text="Nigga")
entrada.pack()
boton.pack()
palabraObtenida = texto.get()
ventana.geometry("1000x600")

ventana.mainloop()