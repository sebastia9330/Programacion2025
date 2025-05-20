#Ejercicio 53
#Usa comprensión de listas para generar una lista de los cuadrados de los números del 1 al 10.

lista = [i+1 for i in range(10)]
listaCuadrada = [numero**2 for numero in lista]

print(listaCuadrada)

#Mejora
listaCuadrada = [i**2 for i in range(1, 11)]
print(listaCuadrada)
