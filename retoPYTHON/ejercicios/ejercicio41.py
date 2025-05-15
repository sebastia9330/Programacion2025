#Ejercicio 41
#Crea una función que reciba una temperatura en Celsius y la convierta a Fahrenheit.

try:
    celsius = float(input("Digita una temperatura en grados celsius: "))

    def conversorDeTemperaturas(grados):
        fahrenheit = (grados * 1.8) + 32
        return fahrenheit


    gradosConv = conversorDeTemperaturas(celsius)

    print(f"{celsius} grados Celsius equivalen a {gradosConv} grados Fahrenheit")
except(ValueError):
    print("Digitaste la temperatura mal, intenta de nuevo")