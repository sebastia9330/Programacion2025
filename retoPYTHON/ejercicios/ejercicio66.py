#Ejercicio 66
#Dado un diccionario con nombres y notas, muestra la nota promedio de todos los estudiantes.

notas = {
    "Valentina" : 1.2,
    "Sebastián" : 2.3,
    "Camila" : 3.4,
    "Mateo" : 4.5,
    "Isabella" : 1.3,
    "Santiago" : 2.4,
    "Mariana" : 3.5,
    "Nicolás" : 4.4,
    "Gabriela" : 1.4,
    "Alejandro" : 2.5,
    "Daniela" : 3.6,
    "Tomás" : 4.3,
    "Luciana" : 1.5,
    "David" : 2.6,
    "Sara" : 3.7
}

print(notas)
nota = notas.values()
suma = sum(nota)
cantidad = len(notas.values())
promedio = suma/cantidad
print(f"El promedio de las notas es {promedio:.2f}")