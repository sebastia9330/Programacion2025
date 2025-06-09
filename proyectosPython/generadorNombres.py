import random

prefijos = ["Zor", "Val", "El", "Mor", "Thal", "Kael","Drav","Syl","Vor","Luth"]
sufijos = ["ion", "mar", "dor", "eth", "azar","mir","gorn","hael","vek","dros"]

try:
    cantidad = int(input("Digita la cantidad de nombres que quieres crear: "))


    for i in range(cantidad):
        nombre = random.choice(prefijos) + random.choice(sufijos)
        print(f"El nombre numero {i + 1} es : {nombre}")
except(ValueError):
    print("Error de cantidad, intentalo de nuevo")