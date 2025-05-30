#Ejercicio 65
#Recorre un diccionario e imprime cada clave junto con su valor.


frutas = {
    "mora":  100,
    "uvas":  200,
    "fresas":  300,
    "manzana":  400,
    "lulo": 500,
    "naranja": 600
}

for fruta, valor in frutas.items():
    print(f"la fruta {fruta} cuesta {valor} pesos")


#imprimir en orden alfabetico
for fruta in sorted(frutas):
    print(f"La fruta {fruta} cuesta {frutas[fruta]} pesos")


#impresion en forma de tabla
print("Fruta".ljust(10), "| Precio")
print("-" * 20)
for fruta, precio in frutas.items():
    print(fruta.ljust(10), "|", f"{precio} pesos")

#valor total
total = sum(frutas.values())
print(f"\nEl total del valor de todas las frutas es: {total} pesos")
