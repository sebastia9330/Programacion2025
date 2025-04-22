#Ejercicio 23
#Solicita tres números y muestra cuál es el mayor usando condicionales.


try:
    numero1 = int(input("digita el numero 1 para validar cual es mayor: "))
    numero2 = int(input("digita el numero 2 para validar cual es mayor: "))
    numero3 = int(input("digita el numero 3 para validar cual es mayor: "))

    if(numero1 > numero2 and numero1 > numero3):
        print(f"el número {numero1} es mayor que {numero2} y {numero3}")
    elif(numero2 > numero1 and numero2 > numero3):
        print(f"el número {numero2} es mayor que {numero1} y {numero3}")
    else:
        print(f"el número {numero3} es mayor que {numero1} y {numero2}")
except ValueError:
    print("Digita un valor numerico valido")