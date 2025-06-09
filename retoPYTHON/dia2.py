#Ejercicio Diario 2: Tabla de Multiplicar Interactiva
#Crea un programa que le pida al usuario un número y luego imprima la tabla de multiplicar de ese número, desde el 1 hasta el 10.

#Requisitos:
#Usa un bucle (for o while) para generar la tabla.
#Muestra el resultado en el formato:
#python
#
#3 x 1 = 3
#3 x 2 = 6
#...
#3 x 10 = 30
#Asegúrate de que el usuario pueda ingresar números enteros positivos.

numeroTabla = int(input("digita el numero del que deseas obtener la tabla de multiplicar "))

if(numeroTabla > 0):
    contador = 1
    while(contador <= 10):
        resultado = numeroTabla * contador
        print(f'{numeroTabla} X {contador} = {resultado}')
        contador += 1
else:
    print("El numero digitado es negativo")


#version mejorada
try:
    numero_tabla = int(input("Digita el número del que deseas obtener la tabla de multiplicar: "))

    if numero_tabla != 0:
        for contador in range(1, 11):
            resultado = numero_tabla * contador
            print(f'{numero_tabla} x {contador} = {resultado}')
    else:
        print("El número digitado es cero, su tabla sería cero en todos los valores.")
except ValueError:
    print("Por favor, ingresa un número válido.")
