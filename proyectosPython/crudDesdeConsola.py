
usuarios = []
id_actual = 1

def mostrar_menu():
    print("\n=== GESTOR DE USUARIOS ===")
    print("1. Crear Usuario")
    print("2. Listar Usuarios")
    print("3. Actualizar Usuario")
    print("4. Eliminar Usuario")
    print("5. Salir")
    return input("seleccione una opcion")

def crear_usuario():
    global id_actual
    nombre = input("Nombre: ")
    email = input("Email: ")
    edad = input("Edad: ")

    usuario = {
        "id": id_actual,
        "nombre": nombre,
        "email": email,
        "edad": edad
    }
    usuarios.append(usuario)
    id_actual += 1
    print("✅ Usuario agregado con exito")

def lista_usuarios():
    if not usuarios:
        print("🟡 No hay usuarios")
        return
    for u in usuarios:
        print(f"ID: {u['id']} | Nombre: {u['nombre']} | Email: {u['email']} | Edad: {u['edad']}")


def actualizar_usuario():
    id_usuario = int(input("Ingrese el ID del usuario a actualizar: "))
    for u in usuarios:
        if u["id"] == id_usuario:
            nuevo_nombre = input(f"Nuevo Nombre: ({u['nombre']}): ") or u['nombre']
            nuevo_email = input(f"Nuevo Email ({u['email']}): ") or u['email']
            nueva_edad = input(f"Nueva edad ({u['edad']}): ") or u['edad']

            u["nombre"] = nuevo_nombre
            u["email"] = nuevo_email
            u["edad"] = nueva_edad
            print("✅ Usuario Actualizado")
            return
    print("❌ usuario no encontrado")

crear_usuario()
lista_usuarios()
actualizar_usuario()
lista_usuarios()