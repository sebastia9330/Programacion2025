#Ejercicio 28
#Crea un menú con cuatro opciones, elige una y realiza una acción diferente según la opción seleccionada.

print("Bienvenido a tu calculadora, elige una opcion entre 1 y 4")
print("elige 1 para sumar")
print("elige 2 para restar")
print("elige 3 para multiplicar")
print("elige 4 para dividir")

try:
    opcion = int(input("Digita la opcion que deseas: "))

    if(opcion == 1):
        print("Seleccionaste Suma")
        numero1 = int(input("Digita el número 1: "))
        numero2 = int(input("Digita el número 2: "))
        resultadoSuma = numero1 + numero2
        print(f"El resultado de la Suma entre {numero1} más {numero2} es: {resultadoSuma}")
    elif(opcion == 2):
        print("Seleccionaste Resta")
        numero1 = int(input("Digita el número 1: "))
        numero2 = int(input("Digita el número 2: "))
        resultadoResta = numero1 - numero2
        print(f"El resultado de la Resta entre {numero1} menos {numero2} es: {resultadoResta}")
    elif(opcion == 3):
        print("Seleccionaste Multiplicación")
        numero1 = int(input("Digita el número 1: "))
        numero2 = int(input("Digita el número 2: "))
        resultadoMultiplicacion = numero1 * numero2
        print(f"El resultado de la Multiplicacion entre {numero1} por {numero2} es: {resultadoMultiplicacion}")
    elif(opcion == 4):
        print("Seleccionaste Division")
        numero1 = int(input("Digita el número 1: "))
        numero2 = int(input("Digita el número 2: "))
        resultadoDivision = numero1 / numero2
        print(f"El resultado de la Division entre {numero1} dividido {numero2} es: {resultadoDivision:.2f}")
    else:
        print("Error el numero es mayor a 4")
except ValueError:
    print("Por favor, Digita un valor valido")