#ejercicio 20
#Redondea un número decimal

import math

decimal = float(input("digita un numero decimal: "))

print(f"El redondeo al numero mas cercano es: {round(decimal)}")
print(f"El redondeo hacia arriba es: {math.ceil(decimal)}")
print(f"El redondeo hacia abajo es: {math.floor(decimal)} ")