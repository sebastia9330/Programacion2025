#Ejercicio 31
#Solicita una lista de números al usuario (separados por coma) y muestra solo los números pares.

lista = []
pares = []

seguir = "SI"
while(seguir == "SI"):
    numero = int(input("Digita la secuencia de numeros: "))
    seguir = input("Quieres seguir digitando numeros: si o no: ").upper()
    lista.append(numero)

for i in range(len(lista)):
    if(lista[i] % 2 == 0):
        pares.append(lista[i])

print(f"los numeros pares de la secuencia son: {pares}")