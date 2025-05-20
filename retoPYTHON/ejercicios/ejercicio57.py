#Ejercicio 57
#Dada una lista de números, crea una nueva lista que contenga True si el número es par y False si es impar.

import random

numeros = [random.randint(1, 100) for _ in range(100)]
print(numeros)

validacionNumeros = [numero % 2 == 0 for numero in numeros]

print(validacionNumeros)

#Mejoras
#unir las dos listas
resultado = list(zip(numeros, validacionNumeros))
print(resultado)

#filtro de pares
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

#conteo de pares/impares
cantidad_pares = validacionNumeros.count(True)
cantidad_impares = validacionNumeros.count(False)
print(f"Pares: {cantidad_pares}, Impares: {cantidad_impares}")
