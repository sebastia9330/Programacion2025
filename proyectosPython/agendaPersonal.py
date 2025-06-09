#Proyecto de agenda personal


agenda = {}

print("Menu de agenda personal")
print("Agregar contacto = 1")
print("Buscar contacto = 2")
print("salir = 3")

try:
    opcion = int(input("Que deseas hacer el dia de hoy: "))
    while opcion != 3:
        if opcion == 1:
            print("Opcion 1")
            nombre = input("Digita el nombre del contacto: ")
            telefono = input("Digita el numero del contacto: ")
            agenda[nombre] = telefono
            print(agenda)
            print("Agregar contacto = 1")
            print("Buscar contacto = 2")
            opcion = int(input("Digita otra opcion, o 3 para salir: "))

        elif opcion == 2:
            print("Opcion 2")
            nombre = input("Digita el nombre del contacto que deseas ver: ")
            if nombre in agenda:
                print(f"Nombre: {nombre} Teléfono: {agenda[nombre]}")
            else:
                print("Ese contacto no está en la agenda.")
            print("Agregar contacto = 1")
            print("Buscar contacto = 2")
            opcion = int(input("Digita otra opcion, o 3 para salir: "))
        else:
            print("opcion mayor a las soportadas, recuerda: ")
            print("Agregar contacto = 1")
            print("Buscar contacto = 2")
            print("salir = 3")
            opcion = int(input("Digita una opcion correcta: "))



    print("Saliendo............")
except(ValueError):
    print("opcion no valida, intenta de nuevi")