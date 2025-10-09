import time
import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo label")

etiqueta = tk.Label(ventana, text="Hola soy un label")
etiqueta.pack()

def actualizar_hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    ventana.after(1000, actualizar_hora)

actualizar_hora()

ventana.mainloop()