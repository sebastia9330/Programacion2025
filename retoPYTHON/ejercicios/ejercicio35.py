#Ejercicio 35
#"Simula un intento de inicio de sesión con un máximo de 3 intentos. Si el usuario ingresa 
#la contraseña correcta antes de los 3 intentos, mostrar ""Acceso permitido""."

usuario = input("Digita tu usario: ")
contraseña = input("Digita tu contraseña: ")

for i in range(3):
    confUsuario = input("Confirma tu usuario: ")
    confContraseña = input("Confirma tu Contraseña: ")
    if(confUsuario == usuario and confContraseña == contraseña):
        print("Usuario y contraseña correctos")
        break
    else:
        print("usuario y contraseña incorrectos")


#Estructura mejorada
usuario_correcto = "admin"
contraseña_correcta = "1234"

intentos = 0
max_intentos = 3

while intentos < max_intentos:
    usuario = input("Digita tu usuario: ")
    contraseña = input("Digita tu contraseña: ")

    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("Acceso permitido ✅")
        break
    else:
        intentos += 1
        print(f"Usuario o contraseña incorrectos. Intento {intentos} de {max_intentos}")

if intentos == max_intentos:
    print("Acceso denegado ❌. Límite de intentos alcanzado.")

