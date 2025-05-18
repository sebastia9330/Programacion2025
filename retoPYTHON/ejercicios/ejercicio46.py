#Ejercicio 46
#Escribe una función que calcule el factorial de un número (usa recursión).

def factorial(num):
    if num < 0:
        print(f"El numero {num} es negativo, no trabajo con numeros negativos")
    if num == 0 or num == 1:
        return  1
    else:
        resultado = num*factorial(num-1)
        return resultado


try:
    numero = int(input("Digita un numero al que desees conocer su factorial: "))
    print(f"El factorial de {numero} es {factorial(numero)}")
except(ValueError):
    print("No se pueden usar letras para el factorial, intenta solo con numeros positivos")