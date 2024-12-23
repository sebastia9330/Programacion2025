#Ejercicio Diario 4: Calculadora Modular
#Crea un programa que utilice funciones para implementar una calculadora. Debe incluir las operaciones de:

#Suma
#Resta
#Multiplicación
#División

#Requisitos:
#1. Define una función para cada operación.
#2. Solicita al usuario dos números y elige la operación que desea realizar.
#3. Usa una función principal para coordinar el flujo del programa.
#4. Asegúrate de manejar el caso de división entre cero.


def calculadora():
    operacion = input("Selecciona la operación: suma, resta, multiplicación, división: ")
    numero1 = int(input("Ingresa el primer número: "))
    numero2 = int(input("Ingresa el segundo número: "))

    def suma(a,b):
        return a + b
    
    def resta(a,b):
        return a - b
    
    def multiplicacion(a,b):
        return a * b
    
    def division(a,b):
        if(a == 0 or b == 0):
            print("numeros no validos")
        else:
            return a/b

    if(operacion == "suma"):
        resultado = suma(numero1,numero2)
        print(resultado)
    elif(operacion == "resta"):
        resultado = resta(numero1,numero2)
        print(resultado)
    elif(operacion == "multiplicacion"):
        resultado = multiplicacion(numero1,numero2)
        print(resultado)
    elif(operacion == "division"):
        resultado = division(numero1,numero2)
        print(resultado)


calculadora()


#CORRECCION
def calculadora():
    def suma(a, b):
        return a + b

    def resta(a, b):
        return a - b

    def multiplicacion(a, b):
        return a * b

    def division(a, b):
        if b == 0:
            return "Error: División entre cero no permitida"
        return a / b

    try:
        operacion = input("Selecciona la operación: suma, resta, multiplicación, división: ").lower()
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))

        if operacion == "suma":
            resultado = suma(numero1, numero2)
        elif operacion == "resta":
            resultado = resta(numero1, numero2)
        elif operacion == "multiplicación":
            resultado = multiplicacion(numero1, numero2)
        elif operacion == "división":
            resultado = division(numero1, numero2)
        else:
            print("Operación no válida. Intenta nuevamente.")
            return

        print(f"El resultado de la {operacion} es: {resultado}")

    except ValueError:
        print("Por favor, ingresa números válidos.")

calculadora()
