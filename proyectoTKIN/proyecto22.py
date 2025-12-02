import tkinter as tk

def iniciarArrastre(event):
    global objetoSeleccionado
    objetoSeleccionado = canvas.find_closest(event.x, event.y)

def terminaArrastre(event):
    global objetoSeleccionado
    if objetoSeleccionado:
        x, y = event.x, event.y
        canvas.move(objetoSeleccionado, x - canvas.coords(objetoSeleccionado)[0], y - canvas.coords(objetoSeleccionado)[1])
        objetoSeleccionado = None

ventana = tk.Tk()
canvas = tk.Canvas(ventana, width=500, height=500, bg="blue")
canvas.pack()

objetoSeleccionado = None

rectangulo = canvas.create_rectangle(50,50,150,100, fill="green", outline="black", tags="rectangulo")
canvas.create_oval(200, 50, 300, 150, fill="gray", outline="red", width=2)


canvas.tag_bind("rectangulo", "<ButtonPress-1>", iniciarArrastre)
canvas.tag_bind("rectangulo", "<ButtonRelease-1>", terminaArrastre)

ventana.mainloop()
