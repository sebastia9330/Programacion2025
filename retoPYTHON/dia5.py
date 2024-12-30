#Ejercicio Diario 5: Clasificar Temperaturas
#Crea un programa que:

#Solicite al usuario una lista de temperaturas separadas por comas (e.g., 25,30,35,28,40).
#Clasifique las temperaturas en tres categorías:
#Altas: mayores o iguales a 30.
#Medias: entre 20 y 29 (inclusive).
#Bajas: menores a 20.
#Imprima cuántas temperaturas pertenecen a cada categoría.



temperaturas = []

cantidad = int(input("cuantas temperaturas quieres registrar: "))

for i in range(cantidad):
    temp = int(input(f"Ingresa la temperatura {i+1}: "))
    temperaturas.append(temp)
total = len(temperaturas)

mayor = []
medio = []
bajo = []

for j in temperaturas:
    if j >= 30:
        mayor.append(j)
    elif j >= 20 and j <= 29:
        medio.append(j)
    elif j < 20:
        bajo.append(j)


mayor1 = len(mayor)
medias = len(medio)
bajas = len(bajo)

print(f"altas: {mayor1}")
print(f"Medias: {medias}")
print(f"Bajas: {bajas}")


#Correccioón y mejora
cantidad = int(input("¿Cuántas temperaturas quieres registrar? "))
altas = medias = bajas = 0  # Inicialización de contadores

for i in range(cantidad):
    try:
        temp = float(input(f"Ingresa la temperatura {i + 1}: "))
        if temp >= 30:
            altas += 1
        elif temp >= 20:
            medias += 1
        else:
            bajas += 1
    except ValueError:
        print("Por favor, ingresa un número válido.")
        break

# Resultados finales
print(f"Temperaturas altas: {altas}")
print(f"Temperaturas medias: {medias}")
print(f"Temperaturas bajas: {bajas}")
