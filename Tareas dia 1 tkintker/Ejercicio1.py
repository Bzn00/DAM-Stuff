import tkinter as tk

clicks = 0

def contarClicks():
    global clicks
    clicks+=1
    etiqueta.config(text=f"Clicks: {clicks}")
    

root = tk.Tk()
boton = tk.Button(root, text="Click aqui", command=contarClicks)

etiqueta = tk.Label(root, text=f"Clicks: {clicks}")
root.title("Contador de clicks")


boton.pack(pady=20)
etiqueta.pack(pady=10)

root.geometry("300x200") 
root.mainloop()