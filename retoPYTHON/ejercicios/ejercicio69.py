#Ejercicio 69
#Usa un set para eliminar los elementos duplicados de una lista ingresada por el usuario.


lista = []

while True:
    valores = input("Digita valores y mira solo los valores unicos: ").upper()
    if valores == "SALIR":
        break
    lista.append(valores)
    print("Digita 'Salir' para terminar" )

conjunto = set(lista)
print(f"lista original {lista}")
print(f"lista de solo elementos unicos {conjunto}")