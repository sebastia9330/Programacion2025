#Ejercicio37
#Define una función que reciba dos números y retorne su suma.

def funcionSuma(numero1, numero2):
    return numero1 + numero2


try:
    numero1 = int(input("Digita el numero 1: "))
    numero2 = int(input("Digita el numero 2: "))

    resultado = funcionSuma(numero1,numero2)

    print(f"El resultado de la suma entre {numero1} y {numero2} es {resultado}")
except(ValueError):
    print("Valor erroneo, intentalo de nuevo")