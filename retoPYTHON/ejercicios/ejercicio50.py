#Ejercicio 50
#Define una función que determine si un año es bisiesto (reutiliza la lógica del ejercicio 25).

def añoBisiesto(añob):
    if (añob % 4 == 0) and (añob % 100 != 0 or añob % 400 == 0):
        return True
    else: 
        return False
    

try:
    año = int(input("Digita un año y conoce si es bisiesto o no: "))

    resultado = añoBisiesto(año)
    if resultado:
        print(f"El año {año} es bisiesto")
    else: 
        print(f"El año {año} no es es bisiesto")
except(ValueError):
    print("Error digita un año valido")