import tkinter as tk
from tkinter import filedialog

def abrirArchivo():
    filepath = filedialog.askopenfilename(filetypes=[('Archivo de texto', '*.txt'), ('Todos los archivos', '*.*')])
    if filepath:
        with open(filepath, 'r') as fileobj:
            contenido = fileobj.read()
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.INSERT, contenido)

ventana = tk.Tk()
ventana.title("Editor de texto")

text_widget = tk.Text(ventana, wrap='word')
text_widget.pack(expand=True, fill='both')

abrirbutton = tk.Button(ventana, text="Abrir Archivo", command=abrirArchivo)
abrirbutton.pack()

ventana.mainloop()