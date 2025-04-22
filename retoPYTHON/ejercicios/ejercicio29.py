#Ejercicio 29
#Pide un número entero y muestra todos los números desde 1 hasta ese número usando un bucle.

lista = []
try:
    numero = int(input("Digita un numero y veras los numeros que lo preceden: "))

    for i in range(1, numero):    
        lista.append(i)

    print(f"Los números anteriores a {numero} son: ")
    print(lista)
except ValueError:
    print("Pro favor, Digita un valor valido")