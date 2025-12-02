import tkinter as tk
from tkinter import filedialog

#Funciones
def nuevoArchivo():
    areaDeTexto.delete(1.0, tk.END)

def abrirArchivo():
    global rutaArchivo
    rutaArchivo = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"),
                                                                                    ("Archivos Python", "*.py"),
                                                                                    ("Todos los archivos", "*.*")])
    
    with open(rutaArchivo, "r", encoding="utf-8") as file:
        areaDeTexto.insert(tk.INSERT, file.read())


def guardarArchivo():
    global rutaArchivo
    if rutaArchivo:
        try:
            with open(rutaArchivo, "w", encoding="utf-8") as file:
                file.write(areaDeTexto.get(1.0, tk.END))
        except:
            print("No se puede guardar el archivo")

def guardarComo():
    nuevaRuta = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"),
                                                                                    ("Archivos Python", "*.py"),
                                                                                    ("Todos los archivos", "*.*")])
    
    if nuevaRuta:
        with open(nuevaRuta, "w", encoding="utf-8") as file:
            file.write(areaDeTexto.get(1.0, tk.END))

def Copiar():
    areaDeTexto.event_generate(("<<Copy>>"))

def Pegar():
    areaDeTexto.event_generate(("<<Paste>>"))

def Cortar():
    areaDeTexto.event_generate(("<<Cut>>"))


ventana = tk.Tk()
ventana.title("Bloc de notas")
ventana.geometry("800x400")
rutaArchivo = ""


menu = tk.Menu(ventana)
ventana.config(menu=menu)

archivo = tk.Menu(menu)
menu.add_cascade(labe="Archivo", menu=archivo)

edicion = tk.Menu(menu)
menu.add_cascade(labe="Edición", menu=edicion)

areaDeTexto = tk.Text(ventana)
areaDeTexto.pack(fill=tk.BOTH, expand=True)

archivo.add_command(label="Nuevo", command=nuevoArchivo)
archivo.add_command(label="Abrir", command=abrirArchivo)
archivo.add_command(label="Guardar", command=guardarArchivo)
archivo.add_command(label="Guardar Como", command=guardarComo)

edicion.add_command(label="Copiar", command=Copiar)
edicion.add_command(label="Pegar", command=Pegar)
edicion.add_command(label="Cortar", command=Cortar)


ventana.mainloop()