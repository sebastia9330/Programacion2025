def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    return a / b

#El usuario solicita la operacion
while True:
    try:
        operacion = int(input("Selecciona la operacion que deseas: \n (1)suma \n (2)Resta \n (3)Multiplicación \n (4)División \n"))
        if(operacion > 0 and operacion < 5):
            break
    except:
        print("Ingresa una opcion valida")

numero1 = float(input("Digita el numero 1: "))
numero2 = float(input("Digita el numero 2: "))

if operacion == 1:
    resultado = suma(numero1, numero2)
elif operacion == 2:
    resultado = resta(numero1, numero2)
elif operacion == 3:
    resultado = multiplicacion(numero1, numero2)
elif operacion == 4:
    resultado = division(numero1, numero2)
else:
    resultado = "Operacion no valida"
    print("Operacion no valida")

print(resultado)