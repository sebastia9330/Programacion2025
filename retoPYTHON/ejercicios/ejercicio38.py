#Ejercicio 38
#Escribe una función que reciba una lista de números y devuelva la suma de todos.

try:
    numero = 1
    lista = []
    while numero != 0:
        numero = int(input("Digita un numero para la lista de numeros a sumar, digita 0 para parar: "))
        if numero != 0:
            lista.append(numero)
    print(lista)


    def sumaLista(lista):
        resultado = sum(lista)
        return resultado

    def mayorLista(lista):
        mayor = max(lista)
        return mayor

    resultado = sumaLista(lista)
    mayor = mayorLista(lista)


    print(f"La suma de todos los números es: {resultado}")
    print(f"El numero mayor de la lista es: {mayor}")
except(ValueError):
    print("numero mal digitado, sigue intentandoo")