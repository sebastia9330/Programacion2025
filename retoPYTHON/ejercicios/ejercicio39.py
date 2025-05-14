#ejercicio39
#Crea una función que verifique si una palabra es un palíndromo (se lee igual al derecho y al revés).



cadena = input("Digita una palabra y verifica si es un palindromo: ")
def palindromo(cadena):
    lista = []
    for caracter in cadena:
        lista.append(caracter)

    reverso = "".join(lista[::-1])

    if cadena == reverso:
        return print(f"La palabra {cadena} es un palindromo")
    else:
        return print(f"La palabra {cadena} no es un palindromo")

    

pali = palindromo(cadena)



