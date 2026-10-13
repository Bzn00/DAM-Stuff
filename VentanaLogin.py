import tkinter as tk

ventana = tk.Tk()

etiquetaNombre = tk.Label(ventana, text="Nombre de Usuario")
etiquetaContraseña = tk.Label(ventana, text="Contraseña")

campoTextoNombre = tk.Entry(ventana)
campoTextoContraseña = tk.Entry(ventana, show="*")


def login():
    if campoTextoNombre.get() == "Daniel" and campoTextoContraseña.get() == "Bleach99":
        ventana.destroy()

        ventana2 = tk.Tk()
        ventana2.geometry("600x300")

        etiqueta2 = tk.Label(
            ventana2,
            text="Inicio de sesión exitoso :D"
        )
        etiqueta2.pack(pady=100)

        ventana2.mainloop()

    else:
        ventana.destroy()


botonLogin = tk.Button(
    ventana,
    text="Login",
    command=login
)

ventana.geometry("800x400")

etiquetaNombre.pack(pady=5)
campoTextoNombre.pack(pady=10)

etiquetaContraseña.pack(pady=15)
campoTextoContraseña.pack(pady=20)

botonLogin.pack()

ventana.mainloop()
