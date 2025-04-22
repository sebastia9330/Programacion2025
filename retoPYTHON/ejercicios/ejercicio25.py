#Ejercicio 25
#Escribe un programa que determine si un año es bisiesto.

try:
    año = int(input("Digita un año para validar si es bisiesto o no: "))

    if (año % 4 == 0) and (año % 100 != 0 or año % 400 == 0):
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")
except ValueError:
    print("Año no valido, mal digitado")