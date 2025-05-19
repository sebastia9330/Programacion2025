#Ejercicio 49
#Crea una función que reciba un número entero y devuelva una lista con todos los números primos menores a él.

def esPrimo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    
    return True

def imprimirPrimos(limite):
    lista = []
    for numero in range(2, limite + 1):
        if esPrimo(numero):
            lista.append(numero)
    print(f"Los numero menores que son primos de {limite} son {lista}")

try:
    numero = int(input("Digita un numero que desees conocer sus menores primos: "))

    imprimirPrimos(numero)
except(ValueError):
    print("Error digita un numero valido")