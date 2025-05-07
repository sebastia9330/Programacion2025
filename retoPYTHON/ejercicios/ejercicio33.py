#Ejercicio 33
#Crea un programa que cuente cuántas vocales hay en una cadena ingresada por el usuario.


cadena = input("Ingrese una frase: ").lower()

vocales = ["a","e","i","o","u"]
fin_vocales = []

for caracter in cadena:
    for i in vocales:
        if(caracter == i):
            fin_vocales.append(i)
            

print(f"Las vocales de la frase {cadena} son {fin_vocales}")


#version mejorada
# Ejercicio 33 mejorado
cadena = input("Ingrese una frase: ").lower()

vocales = ["a", "e", "i", "o", "u","á", "é", "´í", "ó", "ú"]
fin_vocales = []

for caracter in cadena:
    if caracter in vocales:
        fin_vocales.append(caracter)

print(f"Las vocales de la frase son: {fin_vocales}")
print(f"Cantidad de vocales: {len(fin_vocales)}")
