#Ejercicio Diario 1: Calculadora Simple
#Escribe un programa que funcione como una calculadora simple.

#Requisitos:
#Solicita al usuario que ingrese:
#Dos números (pueden ser enteros o decimales).
#Una operación matemática: suma (+), resta (-), multiplicación (*) o división (/).
#Realiza la operación seleccionada e imprime el resultado.

operacion = input("Digita el simbolo de la operacion que quieres ejecutar: ")
numero1 = int(input("Digita el numeri 1: "))
numero2 = int(input("Digita el numero 2: "))
if (operacion == "+"):
    resultado = numero1 + numero2
    print(f'El resultado de la suma es: {resultado}')
elif(operacion == "-"):
    resultado = numero1 - numero2
    print(f'El resultado de la resta es: {resultado}')
elif(operacion == "*"):
    resultado = numero1 * numero2
    print(f'El resultado de la Multiplicacion es: {resultado}')
elif(operacion == "/"):
    resultado = numero1 / numero2
    print(f'El resultado de la division es: {resultado}')
else:
    print("operacion invalida")

