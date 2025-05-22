#Ejercicio 61
#Crea un diccionario donde las claves sean nombres de personas y los valores sus edades. Luego, 
#imprime la edad de una persona consultando por su nombre.

personas = [
    {
        "nombre": "Sebastian",
        "edad": 30
    },
    {
        "nombre": "Dilza",
        "edad": 30
    },
    {
        "nombre": "Samuel",
        "edad": 10
    }
]



def buscarnombre(nombre):
    for valor in personas:
        if valor["nombre"].upper() == nombre.upper():
            print(f"la edad de {valor['nombre']} es {valor['edad']}")
        else:
            print("Nombre no encontrado.")
            break


nombre = input("Digita el nombre de la persona que quieres consultar: ")
buscarnombre(nombre)

#mejora para agregar personas
nueva_edad = int(input("Nombre no encontrado. Ingresa la edad para registrarlo: "))
personas.append({"nombre": nombre, "edad": nueva_edad})
print(f"{nombre} ha sido agregado al registro.")

print(personas)