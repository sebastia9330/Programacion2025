#Ejercicio42
#Escribe una función que cuente cuántas veces aparece una letra en una frase.


palabra = input("Digita la palabra: ")

def contadorLetra(palabra):
    letra = input("Digita la letra que deseas ver cuantas veces aparece: ")
    contador = 0
    for letrai in palabra:
        if(letra == letrai):
            contador += 1

    print(f"La letra {letra} aparece {contador} veces dentro de la palabra o frase {palabra}")
    return contador
        


resultado = contadorLetra(palabra)
print(resultado)


#Mejoras
def contar_letra(frase, letra):
    contador = 0
    for caracter in frase:
        if caracter.lower() == letra.lower():  # insensible a mayúsculas
            contador += 1
    return contador


frase = input("Digita la frase o palabra: ")
letra = input("Digita la letra que deseas contar: ")

resultado = contar_letra(frase, letra)
print(f"La letra '{letra}' aparece {resultado} veces en la frase: '{frase}'")
