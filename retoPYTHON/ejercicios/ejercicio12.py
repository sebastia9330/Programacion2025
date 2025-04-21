#Ejercicio 12
#Convierte una cadena en entero y viceversa

cadenaNum = int(input("Digita la cadena que deseas convertir en numero, recuerda debe ser un numero: "))
cadenaText = str(cadenaNum)

print(f"Te presento la cadena en formato numero {cadenaNum} y en formato texto {cadenaText}")

#forma mas completa para resolver el ejercicio
texto_input = input("Digita un número en formato de texto: ")

if texto_input.isdigit():
    numero = int(texto_input)
    texto_convertido = str(numero)
    print(f"Número: {numero} | Texto: {texto_convertido}")
else:
    print("Error: Solo puedes convertir cadenas que representen números.")
