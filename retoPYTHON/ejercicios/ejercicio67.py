#Ejercicio 67
#Crea un set con 5 elementos ingresados por el usuario y muestra cuántos elementos únicos hay.

conjunto = set()


for i in range(5):
    valores = input(f"Digita el valor {i+1} para agregar al set de valores: ")
    conjunto.add(valores)

print(conjunto)
print(f"Hay {len(conjunto)} elementos unicos")


#dando al usuario opcion de salir
conjunto = set()

while True:
    valor = input("Digita un valor (o escribe 'salir' para terminar): ")
    if valor.lower() == 'salir':
        break
    conjunto.add(valor)

print(conjunto)
print(f"Hay {len(conjunto)} elementos únicos.")


#mostrando elementos ignorados
conjunto = set()
duplicados = 0

for i in range(5):
    valor = input(f"Digita el valor {i+1}: ")
    if valor in conjunto:
        duplicados += 1
    conjunto.add(valor)

print(conjunto)
print(f"Hay {len(conjunto)} elementos únicos y se ignoraron {duplicados} duplicados.")
