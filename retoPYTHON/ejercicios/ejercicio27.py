#Ejercicio 27
#Solicita una contraseña al usuario y valida si coincide con una clave predefinida.


contraseña1 = input("Digita la contraseña: ")

contraseña2 = input("Confirma tu contraseña: ")

if(contraseña1 == contraseña2):
    print(f"las contraseñas coinciden")
else:
    print(F"{contraseña2} esta contraseña es incorrecta, corrigela")
    