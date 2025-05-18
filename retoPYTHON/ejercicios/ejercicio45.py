#Ejercicio 45
#Crea una función que reciba el nombre y la edad de una persona y devuelva un saludo personalizado.

def saludo(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años de edad")



nombre = input("Digita tu nombre: ")
edad = int(input("Digita tu edad: "))

saludo(nombre,edad)

#mejora
def saludo(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años de edad")

try:
    nombre = input("Digita tu nombre: ")
    edad = int(input("Digita tu edad: "))
    saludo(nombre, edad)
except ValueError:
    print("Por favor, digita una edad válida (número entero).")
