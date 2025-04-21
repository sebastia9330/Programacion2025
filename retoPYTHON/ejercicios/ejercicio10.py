#ejercicio 10
#Solicita dos números y muestra la suma, resta, multiplicación y división

numero1 = int(input("Digita el número 1: "))
numero2 = int(input("Digita el número 2: "))

resultadoSuma = numero1 + numero2
resultadoResta = numero1 - numero2
resultadoMultiplicacion = numero1 * numero2
resultadoDivision = numero1 / numero2

print(f"El resultado de la Suma entre {numero1} más {numero2} es: {resultadoSuma}")
print(f"El resultado de la Resta entre {numero1} menos {numero2} es: {resultadoResta}")
print(f"El resultado de la Multiplicacion entre {numero1} por {numero2} es: {resultadoMultiplicacion}")
print(f"El resultado de la Division entre {numero1} dividido {numero2} es: {resultadoDivision:.2f}")