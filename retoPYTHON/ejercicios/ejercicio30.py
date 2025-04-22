#Ejercicio 30
#Muestra la tabla de multiplicar de un número dado por el usuario, usando un bucle for.

try:
    numero = int(input("Digita el numero del que quieres ver su tabla de multiplicar: "))

    for i in range(11):
        resu = i * numero
        print(f"{i} X {numero} = {resu}")
except ValueError:
    print("Por favor, Digita un valor valido")