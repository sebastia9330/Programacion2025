#Ejercicio Diario 7: Registro de Calificaciones
#Crea un programa que:

#1. Solicite al usuario los nombres de 3 estudiantes.
#2. Para cada estudiante, solicite 3 calificaciones.
#3. Almacene los datos en un diccionario, donde la clave sea el nombre del estudiante y el valor sea una lista de sus calificaciones.
#4. Calcule e imprima:
    #- El promedio de calificaciones de cada estudiante.
    #- El promedio general de todas las calificaciones.

estudiantes = []
notas = []

#cantidad_estudiantes = int(input("¿Cuanto estudiantes deseas registrar? "))

for i  in range(3):
    estudiante = input(f"Digita el nombre del estudiante {i + 1}: ")
    estudiantes.append(estudiante)

    notas_estudiante = []

    nota = input(f"Digita la lista de notas separada por comas del estudiante {estudiante} para terminar oprime enter ")
    for n in nota.split(','):
        notas_estudiante.append(float(n))

    notas.append(notas_estudiante)



registro = dict(zip(estudiantes, notas))
print(registro)

for clave, valor in registro.items():
    promedioIndividual = sum(valor)
    print(f"{clave}: {promedioIndividual/ len(notas_estudiante)}")

promedioG = 0
totalNotas = 0

for j in notas:
    promedioG += sum(j)
    totalNotas += len(j)

print(f"Promedio General {promedioG / totalNotas}")

#Corrección

# Crear un diccionario para almacenar los datos
registro = {}

# Recolección de datos
for i in range(3):
    estudiante = input(f"Digita el nombre del estudiante {i + 1}: ")

    try:
        # Ingresar las notas separadas por comas y convertirlas a una lista de floats
        notas = list(map(float, input(f"Digita la lista de notas separada por comas para {estudiante}: ").split(',')))
        registro[estudiante] = notas
    except ValueError:
        print("Por favor, ingresa solo números separados por comas.")
        exit()

# Mostrar el registro completo
print("\nRegistro de estudiantes y notas:")
for estudiante, notas in registro.items():
    print(f"{estudiante}: {notas}")

# Calcular promedios individuales
print("\nPromedios individuales:")
for estudiante, notas in registro.items():
    promedio_individual = sum(notas) / len(notas)
    print(f"{estudiante}: {promedio_individual:.2f}")

# Calcular promedio general
total_notas = sum(len(notas) for notas in registro.values())
promedio_general = sum(sum(notas) for notas in registro.values()) / total_notas
print(f"\nPromedio general: {promedio_general:.2f}")
