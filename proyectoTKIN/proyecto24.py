import tkinter as tk
from tkcalendar import Calendar, DateEntry

ventana = tk.Tk()
cal = Calendar(ventana, selectmode='day', locale='es_ES', year=2025, mounth=11, day=1, date_pattern='dd-mm-y')

cal.pack()

def imprimirFecha(date):
    print(date)


cal.bind('<<CalendarSelected>>', lambda x: imprimirFecha(cal.get_date()))

dataEntry = DateEntry(ventana, selectmode='day', locale='es_ES', year=2025, mounth=11, day=1, date_pattern='dd-mm-y')

dataEntry.pack()

ventana.mainloop()
