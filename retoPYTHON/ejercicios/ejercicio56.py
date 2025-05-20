#Ejercicio 56
#Pide al usuario 5 notas y guárdalas en una lista. Luego, muestra la nota mayor, menor y el promedio.

try:
    notas = [float(input(f"Digita la nota numero {i + 1}: ")) for i in range(5)]

    print(f"La Nota mayor es {max(notas)}")
    print(f"La Nota menor es {min(notas)}")
    print(f"El promedio es {(sum(notas))/len(notas):.2f}")
except(ValueError):
    print("Digita solo numeros como notas, vuelve a intentar")