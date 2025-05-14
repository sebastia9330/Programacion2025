#Ejercicio 40
#Define una función que reciba una lista de números y devuelva el mayor.

try:
    lista = []
    numero = 1
    while numero != 0:
        numero = int(input("Digita un numero, si no quieres ingresar mas numeros digita el numero 0 :"))
        lista.append(numero)
        if numero == 0:
            lista.pop()
        
    def numeroMayor(lista):
        return max(lista)

    numeroMay = numeroMayor(lista)
    print(f"el numero mayor de la lista de numeros es {numeroMay}")
except(ValueError):
    print("Error al digitar un numero, vuelve a intentar")