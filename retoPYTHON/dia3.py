#Ejercicio Diario 3: Promedio de Calificaciones
#Crea un programa que permita al usuario calcular el promedio de un grupo de calificaciones.

#Requisitos:
#1. Usa una lista para almacenar las calificaciones.
#2. Solicita al usuario cuántas calificaciones quiere ingresar.
#3. Usa un bucle para capturar cada calificación y almacenarla en la lista.
#4. Calcula e imprime el promedio de las calificaciones.




calificaciones = int(input("¿Cuantas calificaciones quieres ingresar? "))
grupo = []
contador = 0
while(calificaciones > contador):
    contador += 1
    calificacion = float(input(f"ingresa la calificacion {contador}: "))
    grupo.append(calificacion)


for cuenta in grupo:
    cuenta += cuenta


print(f"El promedio de las calificaciones es: {cuenta/calificaciones}")


#Corrección
calificaciones = int(input("¿Cuántas calificaciones quieres ingresar? "))
grupo = []  # Lista para almacenar las calificaciones

# Recopilar las calificaciones
for i in range(calificaciones):
    calificacion = float(input(f"Ingresa la calificación {i + 1}: "))
    grupo.append(calificacion)

# Calcular el promedio
suma = sum(grupo)
promedio = suma / calificaciones

print(f"El promedio de las calificaciones es: {promedio:.2f}")
