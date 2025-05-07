#Ejercicio 34
#Solicita un número entero y determina si es primo.

try:
    numero = int(input("Ingresa un numero para validar: "))
    esPrimo = 0

    for i in range(numero):
        i += 1
        if(numero % i == 0):
            esPrimo += 1
            
    if(esPrimo <= 2):
        print(f"el numero {numero} es primo")
    else:
        print(f"el numero {numero} no es primo")
except(ValueError):
    print("Número mal digitado, intentalo de nuevo")


#version mejorada
import math

try:
    numero = int(input("Ingresa un número para validar: "))
    
    if numero <= 1:
        print(f"El número {numero} no es primo")
    else:
        esPrimo = True
        for i in range(2, int(math.sqrt(numero)) + 1):
            if numero % i == 0:
                esPrimo = False
                break

        if esPrimo:
            print(f"El número {numero} es primo")
        else:
            print(f"El número {numero} no es primo")

except ValueError:
    print("Número mal digitado, inténtalo de nuevo")
