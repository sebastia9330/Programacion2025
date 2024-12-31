#Ejercicio Diario 6: Análisis de Lista de Edades
#Crea un programa que:

#Solicite al usuario una lista de edades separadas por comas (e.g., 25,30,18,40,60).
#Analice y muestre:
#La edad promedio.
#La edad mínima.
#La edad máxima.
#El número de menores de 18 años.
#El número de mayores o iguales a 60 años.

edades_input = input("ingresa las edades separadas por comas ej: (18,19,20,21..) ")

edades = []
for e in edades_input.split(','):
    edades.append(int(e))

promedio = sum(edades)/ len(edades)
maximo = max(edades)
minimo = min(edades)
mayores18 = [i for i in edades if i > 18]
mayores60 = [j for j in edades if j >= 60]


print(f"las edades digitadas fueron: {edades}")
print(f"Promedio de edades: {promedio}")
print(f"Edad maxima: {maximo}")
print(f"Edad minima: {minimo}")
print(f"mayores de 18 años: {mayores18}")
print(f"mayores o iguales a 60 años: {mayores60}")

#Corrección
try:
    edades_input = input("Ingresa las edades separadas por comas (ej: 18,19,20,21): ")
    
    # Convertir entrada a una lista de enteros
    edades = [int(e.strip()) for e in edades_input.split(',')]
    
    # Cálculos
    promedio = sum(edades) / len(edades)
    maximo = max(edades)
    minimo = min(edades)
    menores_18 = sum(1 for i in edades if i < 18)
    mayores_60 = sum(1 for i in edades if i >= 60)
    
    # Resultados
    print(f"\nLas edades ingresadas fueron: {edades}")
    print(f"Promedio de edades: {promedio:.2f}")
    print(f"Edad máxima: {maximo}")
    print(f"Edad mínima: {minimo}")
    print(f"Menores de 18 años: {menores_18}")
    print(f"Mayores o iguales a 60 años: {mayores_60}")

except ValueError:
    print("Por favor, asegúrate de ingresar solo números separados por comas.")
