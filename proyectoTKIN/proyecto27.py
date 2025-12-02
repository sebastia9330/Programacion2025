import tkinter as tk

ventana = tk.Tk()

#variables
valorA = 0
valorB = 0
operacion = "sumar"
resultado = 0

#funciones
def sumar():
    global valorA
    global valorB
    return valorA+valorB

def restar():
    global valorA
    global valorB
    return valorA-valorB

def multiplicacion():
    global valorA
    global valorB
    return valorA*valorB

def divicion():
    global valorA
    global valorB
    return valorA/valorB

def borrar():
    global pantalla
    pantalla.delete(0, tk.END)
    

def agregarEnPantalla(valor):
    global pantalla
    pantalla.insert(tk.END, valor)

def operar(simbolo):
    global pantalla
    global valorA
    global operacion
    valorA = float(pantalla.get())
    print(valorA)
    pantalla.delete(0, tk.END)
    if simbolo == "/":
        operacion = "divicion"
    elif simbolo == "*":
        operacion = "multiplicacion"
    elif simbolo == "-":
        operacion = "restar"
    else:
        operacion = "sumar"
    print(operacion)

def resultadoIgual():
    global pantalla
    global valorA
    global valorB
    global resultado
    global operacion
    valorB = float(pantalla.get())
    print(valorB)
    pantalla.delete(0, tk.END)
    evaluacion = eval(operacion)
    resultado = evaluacion()
    pantalla.insert(tk.END, resultado)
    print(resultado)


#interfazgrafica

#pantalla
pantalla = tk.Entry(ventana, width=30, bd=7, justify="right")
pantalla.grid(row=0, column=0, columnspan=4, ipady=15)


#botones
siete = tk.Button(ventana, text="7", width=5, command=lambda: agregarEnPantalla(7))
siete.grid(row=1, column=0)
ocho = tk.Button(ventana, text="8", width=5, command=lambda: agregarEnPantalla(8))
ocho.grid(row=1, column=1)
nueve = tk.Button(ventana, text="9", width=5, command=lambda: agregarEnPantalla(9))
nueve.grid(row=1, column=2)
dividir = tk.Button(ventana, text="/", width=5, command=lambda: operar("/"))
dividir.grid(row=1, column=3)
cuatro = tk.Button(ventana, text="4", width=5, command=lambda: agregarEnPantalla(4))
cuatro.grid(row=2, column=0)
cinco = tk.Button(ventana, text="5", width=5, command=lambda: agregarEnPantalla(5))
cinco.grid(row=2, column=1)
seis = tk.Button(ventana, text="6", width=5, command=lambda: agregarEnPantalla(6))
seis.grid(row=2, column=2)
multiplicar = tk.Button(ventana, text="*", width=5, command=lambda: operar("*"))
multiplicar.grid(row=2, column=3)
uno = tk.Button(ventana, text="1", width=5, command=lambda: agregarEnPantalla(1))
uno.grid(row=3, column=0)
dos = tk.Button(ventana, text="2", width=5, command=lambda: agregarEnPantalla(2))
dos.grid(row=3, column=1)
tres = tk.Button(ventana, text="3", width=5, command=lambda: agregarEnPantalla(3))
tres.grid(row=3, column=2)
resta = tk.Button(ventana, text="-", width=5, command=lambda: operar("-"))
resta.grid(row=3, column=3)
punto = tk.Button(ventana, text=".", width=5, command=lambda: agregarEnPantalla("."))
punto.grid(row=4, column=0)
cero = tk.Button(ventana, text="0", width=5, command=lambda: agregarEnPantalla(0))
cero.grid(row=4, column=1)
igual = tk.Button(ventana, text="=", width=5, command=resultadoIgual)
igual.grid(row=4, column=2)
suma = tk.Button(ventana, text="+", width=5, command=lambda: operar("+"))
suma.grid(row=4, column=3)
borrardo = tk.Button(ventana, text="Borrar", width=30, command=lambda: borrar())
borrardo.grid(row=5, column=0, columnspan=4)

ventana.mainloop()