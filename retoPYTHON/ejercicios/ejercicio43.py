#Ejercicio 43
#Crea una función que reciba un número y devuelva True si es par y False si es impar.


try:
    numero = int(input("Digita un numero y descubre si el numero es par o impar: "))

    def numParOImpar(num):
        if num % 2 == 0:
            return True
        else:
            return False
        

    resultado = numParOImpar(numero)
    print(resultado)
except(ValueError):
    print("Error Digita un numero, vuelve a intentarlo")


#mejora en codigo
def es_par(num):
    return num % 2 == 0  # Esta expresión ya retorna True o False directamente

try:
    numero = int(input("Digita un número para saber si es par o impar: "))
    print(es_par(numero))
except ValueError:
    print("Error: digita un número válido.")
