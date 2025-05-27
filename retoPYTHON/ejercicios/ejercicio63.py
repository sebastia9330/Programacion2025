#Ejercicio 63
#Dado un diccionario de productos y precios, permite al usuario consultar el precio ingresando el nombre del producto.

productos = {
    "manzana": 500,
    "uvas": 100,
    "fresas": 300,
    "moras": 400,
    "feijobas": 700
}

print("Productos disponibles:", ", ".join(productos.keys()))
producto = input("Digita el nombre de un producto y conoce su precio: ").lower()



if producto in productos:
    print(f"El producto {producto} tiene el precio de {productos[producto]} pesos")
else:
    print(f"El producto {producto} no existe")


#mejora de multiples busquedas
while True:
    producto = input("Escribe el producto (o 'salir' para terminar): ").lower()
    if producto == "salir":
        break
    elif producto in productos:
        print(f"El producto {producto} vale {productos[producto]} pesos.")
    else:
        print("Ese producto no está en la lista.")


