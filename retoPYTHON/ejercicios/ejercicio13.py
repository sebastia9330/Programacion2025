#Ejercicio 13
#Calcula el área de un círculo a partir del radio

radio = float(input("Digita el radio del circulo: "))

area = 3.1416 * radio ** 2

print(f"El areá del circulo con un radio de {radio} es: {area}")


#Usando la libreria math

import math
area = math.pi * radio ** 2
print(f"El areá del circulo con un radio de {radio} es: {area:.2f}")