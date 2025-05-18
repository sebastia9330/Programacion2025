#Ejercicio 47
#Crea una función login que reciba un usuario y una contraseña y verifique si coinciden con valores predefinidos.

def seguridad(usuario, contraseña):
    if usuario == "Sebastian9":
        print("Usuario Correcto")
    elif usuario != "Sebastian9":
        print("Usuario incorrecto")
    if contraseña == "Contraseña123":
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")

seguridad("juan","jajajaja")
seguridad("Sebastian9","Contraseña123")


#Mejora
def login(usuario, contraseña):
    usuario_correcto = "Sebastian9"
    contraseña_correcta = "Contraseña123"

    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        return "✅ Acceso permitido"
    else:
        return "❌ Usuario o contraseña incorrectos"

# Pruebas
print(login("juan", "jajajaja"))            # Incorrecto
print(login("Sebastian9", "Contraseña123")) # Correcto
