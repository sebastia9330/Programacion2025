#Ejercicio 18
#Solicita una frase e imprime su longitud


cadena = input("Digita una cadena de la cual quieres medir su longitud: ")

print(f"La longitud de la cadena es de: {len(cadena)} caracteres")


#Ejercicio mejorado
cadena = input("Digita una cadena de la cual quieres medir su longitud: ")

longitud_total = len(cadena)
espacios = cadena.count(" ")
letras_sin_espacio = longitud_total - espacios

print(f"La longitud total es: {longitud_total} caracteres")
print(f"Espacios: {espacios}")
print(f"Letras (sin espacios): {letras_sin_espacio}")