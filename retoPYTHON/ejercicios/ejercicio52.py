#Ejercicio 52
#Solicita al usuario una lista de palabras y muestra solo las que tengan más de 5 letras. usando compresion de listas

lista = [input(f"Digita la palbra numero {i + 1}: ") for i in range(5)]

def conteo(lista):
    nuevaLista = []
    for i in lista:
        if len(i) > 5:
            nuevaLista.append(i)
    print(nuevaLista)


conteo(lista)

#Mejora
# Crear la lista de palabras
lista = [input(f"Digita la palabra número {i + 1}: ") for i in range(5)]

# Usar comprensión de listas para filtrar palabras con más de 5 letras
palabras_largas = [palabra for palabra in lista if len(palabra) > 5]

print("Palabras con más de 5 letras:", palabras_largas)

