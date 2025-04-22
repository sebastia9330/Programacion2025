#Ejercicio 26
#Pide un número al usuario y determina si es par o impar.

try:
    numero = int(input("Digita un número y valida si es par o impar: "))

    if(numero % 2 == 0):
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")
except ValueError:
    print("El numero digitado no es valido")