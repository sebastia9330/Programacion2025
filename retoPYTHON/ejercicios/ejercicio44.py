#Ejercicio 44
#Define una función con un parámetro opcional. Si el parámetro no se pasa, que imprima "Parámetro no recibido".

def parametroOpci(param=None):
    if param is None:
        print("Parámetro no recibido")
    else:
        print(f"Parámetro recibido: {param}")


parametroOpci(1)