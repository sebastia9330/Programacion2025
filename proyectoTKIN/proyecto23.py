import tkinter as tk

ventana = tk.Tk()
texto = tk.Text(ventana)

scrollbarver = tk.Scrollbar(ventana)
scrollbarver.pack(side="right", fill="y")

scrollbarver.config(command=texto.yview)
texto.config(yscrollcommand=scrollbarver.set)
texto.pack(side="left", fill="both", expand=True)


scrollbarhor = tk.Scrollbar(ventana, orient=tk.HORIZONTAL)
scrollbarhor.pack(side="bottom", fill="x")

ventana.mainloop()
