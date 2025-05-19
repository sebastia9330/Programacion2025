#Ejercicio 51
#Crea una lista con 10 números ingresados por el usuario y muestra la lista invertida. usa compresion de listas


lista = []
for i in range(1,11):
    numero = int(input("Digita los numeros que quieres ingresar en la lista: "))
    lista.append(numero)
    print(lista[::-1])

#mejora
try:
    lista = [int(input(f"Digita el número {i + 1}: ")) for i in range(10)]
    lista_invertida = lista[::-1]
    print(f"Lista original: {lista}")
    print(f"Lista invertida: {lista_invertida}")
except ValueError:
    print("Por favor, ingresa solo números válidos.")