#Ejercicio 48
#Define una variable global y otra local con el mismo nombre. Muestra el valor de ambas dentro y fuera de una función.

# Variable global
mensaje = "Soy una variable GLOBAL"

def mostrar_mensaje():
    # Variable local con el mismo nombre
    mensaje = "Soy una variable LOCAL"
    print("Dentro de la función:", mensaje)

# Llamamos la función
mostrar_mensaje()

# Fuera de la función
print("Fuera de la función:", mensaje)
