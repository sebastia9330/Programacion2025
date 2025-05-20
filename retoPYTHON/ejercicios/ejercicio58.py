#Ejercicio 58
#Genera una lista de tuplas (número, cuadrado) para los números del 1 al 10 usando comprensión de listas.

listaTuplaCuadrada = [(i, i**2) for i in range(1, 11)]

print(listaTuplaCuadrada)

#Mejoras
#cubo
lista_tuplas = [(i, i**2, i**3) for i in range(1, 11)]
print(lista_tuplas)

#mensaje amigable
for numero, cuadrado in listaTuplaCuadrada:
    print(f"El cuadrado de {numero} es {cuadrado}")
