#Ejercicio 19
#Accede a un carácter específico de una cadena


cadena = input("Digita una cadena: ")
caracter = int(input("Digita un numero de caracter al que quiera ver en la cadena, recuerda que el primer caracter el el numero 0: "))

resum = cadena[caracter]

if(caracter >= len(cadena)):
    print("el numero del caracter ex mayor que la logintud de la cadena")
else:
    print(f"El caracter número {caracter} de la cadena {cadena} es: {resum}")
