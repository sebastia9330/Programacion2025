import tkinter as tk
from tkinter import filedialog

ventana = tk.Tk()
ventana.withdraw()
#seleccionar archivos
filepath = tk.filedialog.askopenfilenames()

print(filepath)

#leer archivo
fileobj = filedialog.askopenfile(mode='r')
if fileobj:
    print(fileobj.read())
    fileobj.close()

ventana.mainloop()