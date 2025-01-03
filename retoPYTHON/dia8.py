#Ejercicio Diario 8: Sistema de Gestión de Inventarios
#Problema:
#Eres responsable de un inventario en una tienda. Crea un programa que:

#1. Inicialice un inventario con al menos 2 categorías y 2 productos por categoría.
#2. Permita al usuario:
    #- Consultar productos en una categoría específica.
    #- Agregar un nuevo producto a una categoría.
    #- Consultar el producto más caro de una categoría.
#3. Use listas y diccionarios para organizar los datos.

inventario = {
    "dulces": [
        {"nombre": "Chocolate", "precio": 800},
        {"nombre": "Caramelo", "precio": 500},
        {"nombre": "Helado", "precio": 1800}
    ],
    "mercado": [
        {"nombre": "Leche", "precio": 5000},
        {"nombre": "Pan", "precio": 500},
        {"nombre": "Huevos", "precio": 600},
        {"nombre": "Harina", "precio": 2500}
    ],
    "bebidas": [
        {"nombre": "Coca-Cola", "precio": 3500},
        {"nombre": "Jugo de Naranja", "precio": 2000},
        {"nombre": "Cerveza", "precio": 4000},
        {"nombre": "Agua", "precio": 1000}
    ],
    "snacks": [
        {"nombre": "Papas Fritas", "precio": 2500},
        {"nombre": "Galletas", "precio": 1500},
        {"nombre": "Maní Salado", "precio": 1200},
        {"nombre": "Barra de Granola", "precio": 1800}
    ]
}

eleccion = int(input("¿Qué deseas hacer? 1. Consultar productos, 2. Agregar producto, 3. Consultar producto más caro: "))


if(eleccion == 1):
#consultar una categoria
    categoria = int(input("Digita el numero de la categoria que quieres consultar: 0 = dulces, 1 = mercado, 2 = bebidad, 3 = snacks: "))

    if(categoria == 0):
        print(inventario["dulces"])
    elif(categoria == 1):
        print(inventario["mercado"])
    elif(categoria == 2):
        print(inventario["bebidas"])
    elif(categoria == 3):
        print(inventario["snacks"])

elif(eleccion == 2):
#Agregar un nuevo producto
    nuevo = int(input("Digita el numero de la categoria en la que quieres agragar un producto: 0 = dulces, 1 = mercado, 2 = bebidad, 3 = snacks: "))
    columnas = ["nombre", "precio"]
    valores = []
    nombre = input("Digita el nombre del producto: ")
    precio = int(input("Digita el precio del producto: "))

    valores.append(nombre)
    valores.append(precio)

    nuevoProducto = dict(zip(columnas, valores))

    if(nuevo == 0):
        inventario["dulces"].append(nuevoProducto)
        print(inventario["dulces"])
    elif(nuevo == 1):
        inventario["mercado"].append(nuevoProducto)
        print(inventario["mercado"])
    elif(nuevo == 2):
        inventario["bebidas"].append(nuevoProducto)
        print(inventario["bebidas"])
    elif(nuevo == 3):
        inventario["snacks"].append(nuevoProducto)
        print(inventario["snacks"])

elif(eleccion == 3):
    categriaMayor = int(input("Digita el numero de la categoria que quieres consultar: 0 = dulces, 1 = mercado, 2 = bebidad, 3 = snacks: "))

    
    if(categriaMayor == 0):
        for categ, items in inventario.items():
            if(categ == "dulces"):
                print(f"Categoria : {categ}")

                precio_mayor = 0;
                producto_mas_caro = ""

                for item in items:
                    print(f"- {item['nombre']}: ${item['precio']}")

                    if item['precio'] > precio_mayor:
                        precio_mayor = item['precio']
                        producto_mas_caro = item['nombre']
    elif(categriaMayor == 1):
        for categ, items in inventario.items():
            if(categ == "mercado"):
                print(f"Categoria : {categ}")

                precio_mayor = 0;
                producto_mas_caro = ""

                for item in items:
                    print(f"- {item['nombre']}: ${item['precio']}")

                    if item['precio'] > precio_mayor:
                        precio_mayor = item['precio']
                        producto_mas_caro = item['nombre']
    elif(categriaMayor == 2):
        for categ, items in inventario.items():
            if(categ == "bebidas"):
                print(f"Categoria : {categ}")

                precio_mayor = 0;
                producto_mas_caro = ""

                for item in items:
                    print(f"- {item['nombre']}: ${item['precio']}")

                    if item['precio'] > precio_mayor:
                        precio_mayor = item['precio']
                        producto_mas_caro = item['nombre']
    elif(categriaMayor == 3):
        for categ, items in inventario.items():
            if(categ == "snacks"):
                print(f"Categoria : {categ}")

                precio_mayor = 0;
                producto_mas_caro = ""

                for item in items:
                    print(f"- {item['nombre']}: ${item['precio']}")

                    if item['precio'] > precio_mayor:
                        precio_mayor = item['precio']
                        producto_mas_caro = item['nombre']

    print(f"El precio mas caro es: {precio_mayor} y pertenece al producto: {producto_mas_caro}")


#Corrección
inventario = {
    "dulces": [
        {"nombre": "Chocolate", "precio": 800},
        {"nombre": "Caramelo", "precio": 500},
        {"nombre": "Helado", "precio": 1800}
    ],
    "mercado": [
        {"nombre": "Leche", "precio": 5000},
        {"nombre": "Pan", "precio": 500},
        {"nombre": "Huevos", "precio": 600},
        {"nombre": "Harina", "precio": 2500}
    ],
    "bebidas": [
        {"nombre": "Coca-Cola", "precio": 3500},
        {"nombre": "Jugo de Naranja", "precio": 2000},
        {"nombre": "Cerveza", "precio": 4000},
        {"nombre": "Agua", "precio": 1000}
    ],
    "snacks": [
        {"nombre": "Papas Fritas", "precio": 2500},
        {"nombre": "Galletas", "precio": 1500},
        {"nombre": "Maní Salado", "precio": 1200},
        {"nombre": "Barra de Granola", "precio": 1800}
    ]
}

def consultar_categoria(categoria):
    """Consulta los productos de una categoría."""
    if categoria in inventario:
        print(f"Productos en la categoría '{categoria}':")
        for item in inventario[categoria]:
            print(f"- {item['nombre']}: ${item['precio']}")
    else:
        print("Categoría no encontrada.")

def agregar_producto(categoria):
    """Agrega un producto a una categoría."""
    if categoria in inventario:
        nombre = input("Nombre del producto: ")
        try:
            precio = int(input("Precio del producto: "))
            inventario[categoria].append({"nombre": nombre, "precio": precio})
            print(f"Producto agregado exitosamente a la categoría '{categoria}'.")
        except ValueError:
            print("El precio debe ser un número.")
    else:
        print("Categoría no encontrada.")

def producto_mas_caro(categoria):
    """Encuentra el producto más caro en una categoría."""
    if categoria in inventario:
        productos = inventario[categoria]
        if productos:
            mas_caro = max(productos, key=lambda x: x['precio'])
            print(f"El producto más caro en '{categoria}' es '{mas_caro['nombre']}' con un precio de ${mas_caro['precio']}.")
        else:
            print(f"No hay productos en la categoría '{categoria}'.")
    else:
        print("Categoría no encontrada.")

# Menú principal
while True:
    print("\nOpciones disponibles:")
    print("1. Consultar productos")
    print("2. Agregar producto")
    print("3. Consultar producto más caro")
    print("4. Salir")
    
    try:
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            categoria = input("Ingresa la categoría: ").lower()
            consultar_categoria(categoria)
        elif opcion == 2:
            categoria = input("Ingresa la categoría: ").lower()
            agregar_producto(categoria)
        elif opcion == 3:
            categoria = input("Ingresa la categoría: ").lower()
            producto_mas_caro(categoria)
        elif opcion == 4:
            print("¡Gracias por usar el sistema de inventario!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
