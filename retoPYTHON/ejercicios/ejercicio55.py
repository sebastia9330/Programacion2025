#Ejercicio 55
#Crea una lista de números del 1 al 20 y usa comprensión de listas para generar una lista de los múltiplos de 3.

lista = [i for i in range(1,21) if i % 3 == 0]

print(lista)

lista2 = [(i, i**2) for i in range(1, 21) if i % 3 == 0]

print(lista2)