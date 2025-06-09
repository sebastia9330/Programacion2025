#Conversor de Temperatura


try:
    temperatura = float(input("Digita la temperatura: "))
except(ValueError):
    print("Temperatura mmal digitada, intentalo de nuevo")    
print("Unidades de conversion Celsius = C, Fahrenheit = F, Kelvin = K")
unidadInicial = input("Digita la unidad inicial: ").upper()
unidadDestino = input("Digita la unidad de destino: ").upper()

if unidadInicial == "C" and unidadDestino == "F": #CELSIUS A Fahrenheit
    resultado = (temperatura * 1.8) + 32
    print(f"la conversion de {temperatura} grados Celsius, da como resultado {resultado:.2f} grados Fahrenheit")
elif unidadInicial == "C" and unidadDestino == "K": #CELSIUS A LEKVIN
    resultado = (temperatura + 273.15)
    print(f"la conversion de {temperatura} grados Celsius, da como resultado {resultado:.2f} grados Kelvin")
elif unidadInicial == "F" and unidadDestino == "C": #FAHRENHEIT A CELSIUS
    resultado = (temperatura - 32) * 0.55
    print(f"la conversion de {temperatura} grados Fahrenheit, da como resultado {resultado:.2f} grados Celsius")
elif unidadInicial == "F" and unidadDestino == "K": #FAHRENHEIT A KELVIN
    resultado = (((temperatura - 32) * 0.55) + 273.15)
    print(f"la conversion de {temperatura} grados Fahrenheit, da como resultado {resultado:.2f} grados Kelvin")
elif unidadInicial == "K" and unidadDestino == "F": #KELVIN A FAHRENHEIT
    resultado = (((temperatura - 273.15) * 1.8) + 32)
    print(f"la conversion de {temperatura} grados Kelvin, da como resultado {resultado:.2f} grados Fahrenheit")
elif unidadInicial == "K" and unidadDestino == "C": #KELVIN A CELSIUS
    resultado = temperatura - 273.15
    print(f"la conversion de {temperatura} grados Kelvin, da como resultado {resultado:.2f} grados Celsius")
else:
    print("Valor fuera de las opciones existentes, Celsius = C, Fahrenheit = F, Kelvin = K ")    
