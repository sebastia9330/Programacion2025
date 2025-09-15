import string
import random

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)



def generarContraseñas(longitud):
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#$*+-/<=>?@'
    contraseña = ""
    for i in range(longitud):
        contraseña += random.choice(caracteres)
    return contraseña


longitud = int(input("Cuantos caracteres deseas que tenga la contraseña: "))
nuevaContraseña = generarContraseñas(longitud)
print(f"la contraseña sugerida es: {nuevaContraseña}")