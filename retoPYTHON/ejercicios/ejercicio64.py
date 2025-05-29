#Ejercicio 64
#Agrega una nueva entrada a un diccionario ya creado y muestra el resultado.

dulceria = {
    "mora":  100,
    "uvas":  200,
    "fresas":  300,
    "manzana":  400,
}

fruta = input("Escribe el nombre de la fruta o dulce que quieres agregar: ").lower()

precio = int(input("Digita el valor: "))

dulceria[fruta] = precio

print(dulceria)

#mejora por si hay frutas repetidas
if fruta in dulceria:
    confirmar = input(f"{fruta} ya existe con precio {dulceria[fruta]}. ¿Deseas actualizarlo? (s/n): ")
    if confirmar.lower() != "s":
        print("No se actualizó el valor.")
    else:
        dulceria[fruta] = precio
else:
    dulceria[fruta] = precio


#errores de usuari
try:
    precio = int(input("Digita el valor: "))
except ValueError:
    print("Debes ingresar un número válido.")
    exit()
