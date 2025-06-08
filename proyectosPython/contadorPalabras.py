#Crear un programa que reciba un texto del usuario, cuente cuántas veces aparece cada palabra y muestre los resultados.

import string

texto = input("Digita las palabras que desees: ")
print(texto)

texto_limpio = texto.translate(str.maketrans('', '', string.punctuation))


palabras = texto_limpio.lower().split()
print(palabras)

contador = {}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

print( "\nConteo de Palabras: ")
for palabra in sorted(contador):
    print(f"{palabra}: {contador[palabra]}")