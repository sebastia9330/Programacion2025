#ejercicio 15
#Intercambia el valor de dos variables


variable1 = input("Digita el valor de la variable 1: ")
variable2 = input("Digita el valor de la variable 2: ")


temporal = variable1
variable1 = variable2
variable2 = temporal

print(f"Este es el valor de la variable 1 despues del cambio: {variable1}")
print(f"Este es el valor de la variable 2 despues del cambio: {variable2}")