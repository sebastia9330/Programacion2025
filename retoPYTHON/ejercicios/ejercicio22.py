#ejercicio 22
#Pide la edad de una persona y determina si puede votar (mayor o igual a 18 años).


nombre = input("Digita tu nombre completo: ")
edad = int(input("Digita tu edad: "))

if(edad >= 18):
    print(f"{nombre} Eres mayor de edad, puedes votar")
else:
    print(f"{nombre} No eres mayor de edad, No puedes votar")