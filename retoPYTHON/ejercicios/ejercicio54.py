#Ejercicios 54
#Dada una lista de nombres, crea una nueva lista que contenga solo los nombres que comienzan con la letra "A".

nombres = ["Ana", "Luis", "Carlos", "María", "Pedro", "Laura", "José", "Elena", "Miguel", "Sofía",
        "Andrés", "Lucía", "Javier", "Camila", "Diego", "Valentina", "Raúl", "Carla", "Daniel", "Fernanda",
        "Marco", "Isabela", "Tomás", "Paula", "Hugo", "Gabriela", "Felipe", "Rosa", "Iván", "Clara", "aliria"]

listaA = [letra for letra in nombres if letra[0] == "a" or letra[0] == "A"]

print(listaA)

#Mejora
listaL = [nombre for nombre in nombres if nombre.lower().startswith("l")]

print(listaL)