#Ejercicio 68
#Dadas dos listas, crea un set con los elementos comunes a ambas.

lista1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista2 = [1,16,2,17,3,18,4,19,5,20,6,21,7,22,8]

comunes = set(lista1) & set(lista2)

print(comunes)
