#Ejercicio 16
#Muestra el tipo de dato de varias variables

numero =  int(input("Digita un dato tipo número: "))
texto = input("digita un dato tipo texto: ")
decimal = float(input("Digita un tipo de dato decimal: "))
respuesta = bool(input("Digita un dato tipo boleano: "))


print(f"El tipo de dato es: {type(numero)}")
print(f"El tipo de dato es: {type(texto)}")
print(f"El tipo de dato es: {type(decimal)}")
print(f"El tipo de dato es: {type(respuesta)}")


#version corregida
# Ejercicio 16
# Muestra el tipo de dato de varias variables

numero = int(input("Digita un dato tipo número: "))
texto = input("Digita un dato tipo texto: ")
decimal = float(input("Digita un tipo de dato decimal: "))
respuesta = input("Digita un dato tipo booleano (True/False): ")
respuesta = respuesta.lower() == "true"

print(f"El tipo de dato de 'numero' es: {type(numero)}")
print(f"El tipo de dato de 'texto' es: {type(texto)}")
print(f"El tipo de dato de 'decimal' es: {type(decimal)}")
print(f"El tipo de dato de 'respuesta' es: {type(respuesta)}")
