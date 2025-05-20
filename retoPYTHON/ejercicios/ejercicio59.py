#Ejercicio 59
#Solicita al usuario una lista de palabras y muestra otra lista con esas palabras en mayúsculas.

palabras = [input(f"Digita la palabra numero {i + 1}: ") for i in range(10)]

palabrasUpper = [palabra.upper() for palabra in palabras]

print(palabrasUpper)

#Mejoras
#mostrar antes y despues
for original, mayuscula in zip(palabras, palabrasUpper):
    print(f"{original} → {mayuscula}")


#orden alfabetico
palabrasUpper.sort()
print("Palabras en mayúscula ordenadas:", palabrasUpper)
