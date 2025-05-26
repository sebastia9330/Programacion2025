#Ejercicio 62
#Solicita al usuario ingresar 5 pares clave-valor y guárdalos en un diccionario. Luego, 
# muestra el diccionario completo.

personas = []

for i in range(5):
    nombre = input(f"Digita el nombre de la persona {i + 1}: ")
    edad = int(input(f"Digita la edad de la persona {i + 1}: "))
    
    personas.append({"Nombre": nombre, "Edad": edad})

print(personas)

#Segunda opcion
personas = {}

for i in range(5):
    nombre = input(f"Digita el nombre de la persona {i + 1}: ")
    edad = int(input(f"Digita la edad de la persona {i + 1}: "))
    personas[nombre] = edad

print(personas)


#quien es mayor
mayor = max(personas, key=personas.get)
print(f"La persona mayor es {mayor} con {personas[mayor]} años.")
