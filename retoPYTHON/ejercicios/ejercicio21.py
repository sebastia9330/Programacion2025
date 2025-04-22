#Ejercicio 21
#Solicita un número al usuario y determina si es positivo, negativo o cero.


numero = int(input("Digita el numero que deseas verificar: "))

if(numero > 0):
    print(f"El número {numero} es positivo")
elif(numero == 0):
    print(f"El número {numero} es cero")
else:
    print(f"El número {numero} es negativo")