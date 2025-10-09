import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo lable")

etiqueta = tk.Label(ventana, text="Hola, soy un label")
#etiqueta.config(text="Nuevo texto")
etiqueta.config(fg="blue", bg="yellow", font=("Arial", 64, "bold"))
etiqueta.pack()

ventana.mainloop()