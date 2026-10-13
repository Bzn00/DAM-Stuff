import tkinter as tk
from tkinter import messagebox

def on_destroy(event):
    widget = event.widget
    print(f"Se ha destruido el widget: {widget}")
    
    # Si el widget destruido es la ventana principal
    if widget == root:
        messagebox.showinfo("Adiós", "¡La ventana se ha cerrado!")

# ---------------------------
# Ventana principal
# ---------------------------
root = tk.Tk()
root.title("Ejemplo bind <Destroy>")
root.geometry("300x200")

# ---------------------------
# Widgets
# ---------------------------
label = tk.Label(root, text="Cierra la ventana para activar el evento.")
label.pack(pady=20)

btn = tk.Button(root, text="Cerrar ventana", command=root.destroy)
btn.pack(pady=10)

# ---------------------------
# Bind al evento <Destroy>
# ---------------------------
root.bind("<Destroy>", on_destroy)

root.mainloop()
