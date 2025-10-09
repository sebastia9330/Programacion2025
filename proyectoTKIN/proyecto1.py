import tkinter as tk

ventana = tk.Tk()

ventana.title("M primera ventana")
ventana.geometry("600x500")
ventana.minsize(300,400)
ventana.maxsize(500,800)
ventana.configure(bg="red")
ventana.resizable(False,False)
ventana.attributes("-alpha", 0.5)


boton = tk.Button(ventana, text="Presiona aqui")
boton.config(fg="yellow", bg="green", font=("Arial", 12))

boton.pack()

etiqueta = tk.Label(ventana, text="Hola mundoooooo")
etiqueta.pack()


def boton_presionado():
    etiqueta.config(text="Boton presionado")

boton.config(command=boton_presionado)


etiqueta2 = tk.Label(ventana, text="esto es un entry")
etiqueta2.pack()

entrada = tk.Entry(ventana)
boton.config(fg="red", bg="black", font=("Arial", 12))
entrada.pack()

entrada.insert(0, "Nombre")




def aplicar_texto():
    texto = entrada.get()
    etiqueta2.config(text=texto)

boton_aplicar = tk.Button(ventana, text="Aplicar texto", command=aplicar_texto)
boton_aplicar.pack()

ventana.mainloop()