#Ejercicio 36
#Crea una función que reciba un número y devuelva su cuadrado.


def numeroCuadrado(numero):
    print(numero ** 2)
    return numero


numeroCuadrado(int(input("Digita un numero y conoce su cuadrado: ")))

#version mejorada
def numero_cuadrado(numero):
    return numero ** 2

# Solicita número al usuario
numero = int(input("Digita un número y conoce su cuadrado: "))
resultado = numero_cuadrado(numero)

# Presenta el resultado
print(f"El cuadrado de {numero} es: {resultado}")
